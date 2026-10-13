# Four-rack temperature and humidity monitoring proposal

Prepared for Hormuz Data Center on 13 October 2026. All financial totals are in Iranian tomans (IRT). Price checks are indicative, not supplier quotations.

## Recommendation and scope

Build **four Arduino Uno R3 nodes, one per rack, with three combined temperature/relative-humidity sensors per rack**: 12 installed sensing points. Connect each node by wired Ethernet to an existing local Linux VM that records readings and serves a Grafana dashboard. Send notifications through email, with an optional Iranian SMS gateway for escalation.

Allow **44,782,200 IRT for hardware and materials, including spares and 20% contingency**. One person with Arduino and Linux experience should allow **80–112 working hours**, usually **3–4 calendar weeks including installation and a 72-hour observation period**, after parts arrive. At an illustrative labor rate of 500,000 IRT/hour, the installed project is **84,782,200–100,782,200 IRT**, excluding recurring service costs.

“Moisture” is assumed to mean **air relative humidity (%RH)**. Humidity sensors do not detect water on the floor. Leak probes or sensing cable should be added separately if that is required. This proposal covers monitoring, logging, visualization and notifications; automatic cooling control is a separate project.

The estimate assumes four rack network ports, an existing Ethernet switch, UPS-backed rack outlets, an existing Linux VM, a backup destination, Internet connectivity and basic electronics tools. These prerequisites must be confirmed in the site survey.

## Sensor placement and controller choice

Use one SHT31-D module at each rack's lower, middle and upper **front air inlet**, approximately at the heights of the equipment intakes. Each module measures both temperature and humidity; separate pairs of devices are unnecessary. Keep sensors in ventilated holders, away from controller heat, direct contact with metal and exhaust air. Label them `R01-bottom`, `R01-middle`, `R01-top`, and similarly for the other racks.

This placement is an engineering recommendation to reveal vertical hot spots. Start with two points per rack if cost is the priority, then add the third. A fourth point at the rear can measure exhaust temperature, but must have separate thresholds and labels; it must not be averaged into inlet alarms.

SHT31 is a suitable starting choice because it provides factory-calibrated digital readings and typical humidity accuracy of ±2%RH. Use a conservative planning temperature accuracy of approximately ±0.3°C and confirm the exact purchased variant against its datasheet. Installation and module quality can increase practical measurement error. [Sensirion SHT31 product specifications](https://sensirion.com/products/catalog/SHT31-DIS-B), [Sensirion SHT3x datasheet](https://sensirion.com/media/documents/213E6A3B/63A5A569/Datasheet_SHT3x_DIS.pdf).

An **Uno is sufficient for sampling and sending three sensor readings**, provided storage, heavy filtering, HTTPS and the user interface run on the VM. Its 2 KB SRAM makes it unsuitable for hosting this complete application. By “Duo,” this proposal assumes **Arduino Due**: it provides more memory and processing capacity, but operates with 3.3 V logic and still needs a network interface. It brings little benefit for three slow sensors per rack. Verify all module voltage compatibility if an existing Due kit is used. [Arduino Uno specifications](https://docs.arduino.cc/hardware/uno-rev3/), [Arduino Due datasheet](https://docs-content.arduino.cc/resources/datasheets/A000062-datasheet.pdf).

One central Uno is possible on a bench, but would require long sensor wiring between racks and create a common failure point. Four local nodes make rack expansion and replacement easier.

## Architecture and wiring

```mermaid
flowchart LR
    S[Three SHT31 sensors per rack] --> M[I2C multiplexer]
    M --> U[Arduino Uno per rack]
    U --> E[W5500 Ethernet module]
    E --> L[Monitoring VLAN / switch]
    L --> B[Local MQTT broker]
    B --> C[Collector: validation and filtering]
    C --> P[(PostgreSQL: readings and events)]
    P --> G[Grafana browser dashboard and alerts]
    G --> N[Email / optional SMS webhook]
    V[Operator through VPN and HTTPS] --> G
```

Repeat the rack hardware four times; the local VM hosts the common software. The W5500 provides Ethernet and TCP/IP over SPI. Select a complete module with RJ45, magnetics and an onboard regulator suitable for a 5 V supply; the chip itself requires 3.3 V. Do not try to power its roughly 128 mA module load from the Uno's limited 3.3 V output. [WIZnet W5500 documentation](https://docs.wiznet.io/Product/Chip/Ethernet/W5500), [ECA W5500 module](https://eshop.eca.ir/ماژول-شبکه-و-wifi/10821-ماژول-شبکه-w5500-دارای-ارتباط-spi.html).

Per rack:

1. Connect Uno A4/SDA and A5/SCL to a TCA9548A multiplexer, with a common ground and voltage-compatible supply/pull-ups. Connect the three sensors individually to channels 0, 1 and 2. Enable only one channel at a time, so identical sensor addresses do not collide. SHT31 offers addresses 0x44 and 0x45; three devices need the multiplexer. For the two-sensor economy option, buy modules exposing the address-select pin and set those two addresses. [Sensirion address specification](https://sensirion.com/media/documents/213E6A3B/63A5A569/Datasheet_SHT3x_DIS.pdf), [Adafruit multiplexer operation](https://www.adafruit.com/product/2717).
2. Connect the W5500 to Uno SPI: D11/MOSI, D12/MISO, D13/SCK and D10/chip select. Wire reset as required by the actual module and verify its supply pins before applying power. Configure unique MAC addresses and reserved IP addresses.
3. Mount the controller near the middle of the rack. Aim for sensor branches no longer than about 1 m, use SDA/ground and SCL/ground pairs, start at 100 kHz, and check pull-up resistance and waveform quality using the actual harness. **A multiplexer solves address conflicts; it does not make I2C a long-distance bus.**
4. If a branch is unreliable, shorten it or use a qualified I2C extender/additional local node. Longer rack runs should use an industrial RS-485 sensor design. Those changes require a revised parts budget and schedule.
5. Feed each node through its USB power input from a regulated 5 V adapter on the rack UPS. Use soldered assembly, strain relief, labeled connectors and enclosed electronics for installation; breadboards are for the bench prototype.

## Measurement, filtering and recording

The following are proposed implementation settings, to be adjusted during commissioning:

- Sample all sensors every **10 seconds** using a timed, nonblocking loop. Check sensor CRC, reject failed/nonfinite readings and physically impossible values, and report quality flags. A failed read must never be converted to zero or a previous value presented as current.
- Send raw readings and status to `hormuz/racks/R01/telemetry` and equivalent rack topics. Include node ID, position, boot/session ID, sequence number, uptime, temperature, %RH and firmware version. Use fixed-size buffers on the Uno. Ordinary MQTT QoS 0 telemetry is adequate for this baseline if sequence gaps are recorded; it does not guarantee delivery.
- The collector timestamps reception in UTC with an NTP-synchronized VM clock. Preserve uptime and sequence numbers to detect delay/restarts. Store raw valid readings, invalid-read events and the filtered values. Expose freshness explicitly; do not retain telemetry as though it were a fresh measurement after restart.
- For each sensor independently, compute a median of the latest **three valid 10-second samples**, then an exponential moving average with `alpha = 0.3`. Reset the filter after a prolonged gap rather than smoothing old data into a new session. Save the processing version and any calibration offsets. Filtering removes noise; it cannot correct a biased sensor.
- Use smoothed values for trends and ordinary warning rules. Use valid raw readings for a faster critical rule, so smoothing cannot hide a sharp temperature rise. Do not reject a valid rapid rise merely because it is large.
- Preserve 10-second raw/filtered readings for **30 days**, and 5-minute minimum/maximum/mean/count aggregates for **12 months**. Preserve alert events for at least a year. The raw stream is about **3,110,400 sensor records per 30 days** for 12 points. Start the VM with 2 vCPU, 4 GB RAM and 40 GB disk, then measure actual storage usage during the pilot. Back up daily to another system and test a restore.

Use Mosquitto for MQTT, a small Python collector, PostgreSQL for storage and Grafana OSS for the interface. Grafana has a built-in PostgreSQL data source and notification integrations including email, Telegram and webhooks. An Iranian SMS API would be connected through a small webhook adapter; it requires a provider account and delivery testing. [Grafana PostgreSQL support](https://grafana.com/docs/grafana/latest/datasources/postgres/), [Grafana notification contact points](https://grafana.com/docs/grafana/latest/alerting/fundamentals/notifications/contact-points/).

## Online interface and notifications

Provide four rack overview cards showing maximum inlet temperature, humidity range, worst sensor status and last update. Include per-position readings, temperature/humidity histories, alert history and CSV export through the dashboard. Provide viewer and administrator access, with configurable thresholds and maintenance silences.

These are **initial commissioning examples**, not equipment operating limits or a claim of standards compliance. Set final limits from the installed server manufacturers' requirements and the site's agreed operating policy.

| Condition | Initial example | Proposed behavior |
| --- | --- | --- |
| Warm inlet | Filtered temperature >27°C for 2 minutes | Email warning |
| Critical inlet | Valid raw temperature >32°C twice consecutively | Urgent email and optional SMS |
| Humidity outside operating policy | Filtered RH <30% or >65% for 5 minutes | Warning |
| Sensor failure | Three consecutive invalid reads | Sensor fault notification |
| Missing node/sensor | No fresh valid reading for 60 seconds | Offline/stale notification |
| Recovery | Temperature below trigger minus 2°C; humidity back inside limits by 3 percentage points, for 5 minutes | Recovery notification |

Evaluate rules every 10 seconds. With two raw samples plus evaluation/delivery, target critical notification within **45 seconds of the measured threshold crossing**, excluding the sensor's physical response and external provider delays. Group notifications by rack; repeat unresolved critical alerts every 15 minutes and warnings every hour. Record firing, delivery failure and recovery events. Add an operator response procedure and an external heartbeat check for the monitoring VM, since a failed VM cannot report its own failure.

Keep the broker on an isolated monitoring VLAN with per-node credentials and topic permissions. Uno-to-broker traffic is unencrypted within that restricted network; do not expose that listener to the Internet. Use VPN and HTTPS for remote dashboard access. Store notification credentials on the VM. Mosquitto supports authentication and access-control configurations. [Mosquitto authentication documentation](https://mosquitto.org/documentation/authentication-methods/).

During an **Internet outage**, local sampling, storage, dashboard and alert evaluation continue; external notifications may fail and need retry/expiry handling. During a **rack LAN or VM outage**, the baseline has no durable storage on the Uno, so readings can be lost. Record gaps explicitly. If lossless outage recording is required, add SD storage and RTC to every node, sequence-based replay and duplicate suppression, or choose a controller with more memory. Historical replay must not trigger fresh critical notifications. This option is not included in the baseline budget.

## Financial estimate

Use **1 USD = 270,000 IRT**, exactly as requested. Iranian rial prices are divided by **10** to obtain IRT. Local Persian product pages below were opened during research; their prices were higher than the older search summaries, so the opened page prices are used. Availability is the displayed status, not a reservation. No quantity discounts are assumed.

| Item | Quantity | Source price per unit | Unit IRT | Line IRT | Basis |
| --- | ---: | ---: | ---: | ---: | --- |
| Uno R3 CH340 | 5 | 7,740,000 IRR | 774,000 | 3,870,000 | [ECA, in stock](https://eshop.eca.ir/بردهای-خانواده-آردوینو-arduino/3975-برد-آردوینو-arduino-uno-ch340.html); 4 installed + 1 spare |
| SHT31-D module | 14 | 6,200,000 IRR | 620,000 | 8,680,000 | [ECA, in stock](https://eshop.eca.ir/ماژول-دما-و-رطوبت/5330-ماژول-سنسور-دما-و-رطوبت-sht31-d.html); 12 installed + 2 spares |
| W5500 Ethernet module | 4 | 10,200,000 IRR | 1,020,000 | 4,080,000 | [ECA, in stock](https://eshop.eca.ir/ماژول-شبکه-و-wifi/10821-ماژول-شبکه-w5500-دارای-ارتباط-spi.html) |
| TCA9548A multiplexer | 4 | $6.95 | 1,876,500 | 7,506,000 | [Adafruit USD fallback](https://www.adafruit.com/product/2717); no verifiable Persian price found |
| 5 V USB adapter, CY-0530 rated 3 A | 4 | 9,500,000 IRR | 950,000 | 3,800,000 | [ECA, in stock](https://eshop.eca.ir/آداپتور/10738-آداپتور-5-ولت-3a-با-خروجی-usb-مدل-cy-0530.html); verify voltage and actual load performance |
| USB power/programming cables | 5 | $0.75 allowance | 202,500 | 1,012,500 | Planning allowance, not a supplier price |
| Controller enclosures | 4 | $2.00 allowance | 540,000 | 2,160,000 | Planning allowance |
| Perfboard, terminals, headers, protection and decoupling | 4 sets | $1.50 allowance | 405,000 | 1,620,000 | Planning allowance |
| Sensor harnesses, ventilated mounts, ties and labels | 4 sets | $2.00 allowance | 540,000 | 2,160,000 | Planning allowance; short branches |
| Ethernet patch cables | 4 | $1.50 allowance | 405,000 | 1,620,000 | Planning allowance; existing switch ports |
| Domestic shipping | 1 | $3.00 allowance | 810,000 | 810,000 | Planning allowance |
| **Materials subtotal** | | | | **37,318,500** | |
| **Contingency: 20% of materials** | | | | **7,463,700** | Price movement and small omissions |
| **Hardware/materials budget** | | | | **44,782,200** | Approximately **44.8 million IRT** |

The USD multiplexer price is a product-price fallback, not a delivered Iranian quote. International freight, import fees and local reseller markup are excluded; the domestic shipping line does not cover them. Prefer a locally sourced compatible multiplexer after getting a firm quote. The contingency may not cover importing four branded boards. All unquoted ancillary rows are explicit budgeting assumptions converted from USD, rather than researched market prices. Tax treatment is whatever the displayed local retail price includes; additional checkout taxes are not separately estimated.

For a lower starting cost, install **two sensors per rack**, keep the same two spare sensors and spare Uno, and omit the multiplexers. With address-selectable modules and otherwise identical allowances, the budget becomes **32,799,000 IRT including contingency**. It sacrifices middle-height coverage. Four points per rack add four sensors and produce a minimum budget of **47,758,200 IRT including contingency**; longer rear wiring or additional mounts may increase it.

### Labor, recurring costs and prerequisites

The illustrative labor rate is **500,000 IRT/hour**, an assumption for comparing the project cost, not a researched Iranian wage or contractor quote. At 80–112 hours, labor costs **40,000,000–56,000,000 IRT**. If you perform the work yourself, cash expenditure can be limited to materials and service charges, but your time remains the same.

| Scenario | One-time IRT |
| --- | ---: |
| Recommended hardware, existing infrastructure, self-built | 44,782,200 |
| Recommended hardware plus illustrative paid labor | 84,782,200–100,782,200 |
| Economy hardware, existing infrastructure, self-built | 32,799,000 |

The baseline uses existing infrastructure and the OSS software editions; there is no new software license purchase. For recurring budgeting, reserve **$2/month = 540,000 IRT/month** for backup storage and **$2/month = 540,000 IRT/month** for email/SMS usage: together **1,080,000 IRT/month**, or **12,960,000 IRT/year**. These are allowances, not provider tariffs; SMS usage, sender registration and API access require a quote. Existing backup/email services could reduce this incremental cost.

Allow **2–4 hours/month** for checks, updates, restore exercises and inspecting probes: **1–2 million IRT/month** at the illustrative labor rate. First-year hardware plus service allowances is **57,742,200 IRT** for a self-build; adding setup and maintenance labor gives **109,742,200–137,742,200 IRT**. Electricity and the opportunity cost of the existing VM are excluded.

If prerequisites are absent, provisional USD allowances are: a small Linux host with storage and power supply **$100 = 27,000,000 IRT**, a suitable switch **$30 = 8,100,000 IRT**, and basic tools **$30 = 8,100,000 IRT**. These are unquoted placeholders, outside the baseline. Obtain local specifications and prices before replacing them with purchase decisions. UPS capacity, independent outage notification hardware, leak detection, certified calibration, new Internet service and durable node logging are also outside the baseline and must be scoped separately if needed.

## Procedure and one-person schedule

| Step | Work and completion evidence | Hands-on hours |
| --- | --- | ---: |
| 1. Site survey and design | Map intake points, measure cable runs, confirm ports/UPS/VM, set retention and notification recipients; produce a wiring plan and final shopping list | 6–8 |
| 2. One-rack bench prototype | Buy/test one Uno, three probes, mux and Ethernet module; verify power and actual cable harness, compare probes side by side | 10–14 |
| 3. Firmware | Implement timed reads, CRC/status, channel selection, unique IDs, sequence/boot tracking, network reconnect and watchdog; inspect SRAM/flash usage | 18–24 |
| 4. Backend and records | Configure broker access, collector, schema, filters, retention, backups and automatic service restart; confirm correct timestamps and gap handling | 14–20 |
| 5. Interface and alerts | Build rack views/history/export, thresholds, stale/fault rules, email and notification templates; test from the intended remote access path | 10–14 |
| 6. Build and installation | Assemble/enclose four nodes, label harnesses, install sensor holders and rack network/power connections | 10–14 |
| 7. Commissioning | Run failure and threshold tests, observe for 72 hours, tune settings and compare sensors with a trusted reference | 8–12 |
| 8. Handover | Save firmware/configuration, inventory, operating procedure, restore instructions and replacement instructions | 4–6 |
| **Total** | | **80–112** |

At eight productive hours/day this is **10–14 working days**. Plan roughly **3–4 calendar weeks after parts arrive** to allow sequencing, rack access and a 72-hour unattended soak; the soak is elapsed time, with its active checks counted above. Procurement may add **1–2 weeks or longer**, especially for the USD fallback part. At about four hours/day, expect **5–7 weeks**. A beginner should allow approximately **160–220 hours**, often **6–8 full-time calendar weeks plus procurement**.

Start with one rack and establish the full sensor-to-notification path before assembling the remaining three. Use the pilot to decide whether two or three inlet points are sufficient and whether the short I2C harness is dependable.

### Commissioning acceptance criteria

- All 12 installed positions report every 10 seconds, with correct rack/position mapping and clear stale/fault status. Compare probes side by side and against a trusted reference after stabilization; investigate differences greater than roughly 0.5°C or 3 percentage points RH, accounting for reference uncertainty. This is a functional comparison, not certified calibration.
- A controlled sensor stimulus or injected test data produces warning, critical and recovery events. Verify actual email receipt and, if enabled, SMS receipt; a dashboard event alone does not demonstrate delivery.
- Unplug a probe and a rack Ethernet cable separately. Confirm fault/stale notification and that old readings are not shown as current. Reconnect and verify recovery and recorded gaps.
- Disconnect Internet while keeping the LAN running. Confirm local recording continues and failed notification attempts are visible. Reboot the node and VM separately; confirm automatic restart, boot identification and correct timestamps.
- Verify a threshold spike remains visible in raw records and exercises the critical path. Test hysteresis, maintenance silence and repeat suppression so one incident does not generate an alert storm.
- Complete a 72-hour run with no unexplained resets or gaps, export a history slice, and restore a backup into a separate database. Record all findings before operational handover.

Keep the wiring map, purchased module variants, firmware versions and notification settings with the project. Inspect connectors and dust periodically, compare probes every six months and after suspected drift, and retest alerts after changing software or service credentials.

## Alternative connections: G10 server serial, USB and other peripherals

**Yes: a monitoring VM on your own server can collect sensor readings through physical serial or USB devices assigned by the hypervisor.** A rented remote VPS cannot directly access your rack's physical ports; it needs a local collector or network gateway that forwards readings. The exact server model, hypervisor and guest OS must be confirmed before writing configuration instructions.

If “G10” means an HPE ProLiant Gen10, check the installed hardware rather than assuming every model has a COM port. For example, HPE lists the rear serial port on the DL380 Gen10 as optional and lists rear USB ports. This does not establish the configuration of your particular server. [HPE DL380 Gen10 rear-panel guide](https://support.hpe.com/hpesc/public/docDisplay?docId=a00018787en_us&page=GUID-94403017-2038-4EEE-B43A-F40ABC05B1DF.html).

| Connection | Hardware path | VM collection method | Suitability for these four racks |
| --- | --- | --- | --- |
| Arduino USB serial | Local SHT31 sensors → Uno → USB data cable → server | Assign each USB device to the VM; collector reads its serial stream | Simplest Arduino pilot when rack-to-server cable runs are short; four rack nodes mean four USB devices |
| Server RS-232 COM port | Sensors → Arduino/controller → RS-232 transceiver → server COM port | Map the physical host serial device to a guest serial port | Possible, but typically a point-to-point connection to one controller; not a direct connection for 12 bare sensors |
| Native USB temperature/RH module | USB sensor module → server or powered USB hub | USB passthrough plus manufacturer SDK or documented protocol | Can eliminate Arduino; verify continuous live readings and Linux support before choosing a device |
| RS-485 / Modbus RTU | Addressed industrial temperature/RH transmitters → daisy-chain bus → isolated USB-to-RS-485 adapter | Pass the adapter to the VM and poll each sensor's registers | Worth considering for longer cable runs and many sensing points; separate sensor power is usually required |
| Ethernet environmental gateway or sensors | Sensor inputs → network gateway → monitoring VLAN | VM polls a documented API, Modbus TCP or SNMP, or receives MQTT where supported | Avoids physical-port passthrough and allows the VM to move between hosts; protocol support depends on the product |
| Compatible PDU/UPS environmental input | Matching vendor probes → management module → LAN | Read the documented management API/SNMP interface | Useful if existing equipment already supports ambient temperature/RH probes; verify compatibility and sensor count |

### Using an Uno over USB

The Uno's existing USB interface can carry serial measurements; a separate Ethernet module is unnecessary for this alternative. The official Uno has a USB-to-serial bridge, while the budget CH340 clone uses its own bridge/driver. Program each node to send one structured record per sensor, with rack ID, position, temperature, RH, quality status, sequence and boot ID. The VM's collector reads these records and feeds the same database, filtering and notification pipeline described above. [Arduino USB serial example](https://docs.arduino.cc/tutorials/uno-rev3/AnalogReadSerial), [Arduino USB-to-serial documentation](https://support.arduino.cc/hc/en-us/articles/4408887452434-Flash-the-USB-to-serial-firmware-for-UNO-Rev3-and-earlier-and-Mega-boards).

Use USB **data** cables, and a powered hub if port count or available power requires it. Keep passive cable runs short and qualify the actual cables/hub during the prototype; use suitable active extenders or change to RS-485/Ethernet for longer runs. Do not run a single long I2C cable from the server across all racks. Mount the Arduino near its sensor branches as in the baseline design.

In a Linux guest, a bridge may appear as `/dev/ttyUSB0` or `/dev/ttyACM0`, depending on hardware and driver. Do not rely on enumeration numbers remaining constant. Prefer device serial numbers where available; otherwise map physical USB port paths and verify the rack ID in each incoming record. Identical low-cost adapters may lack unique USB serial numbers. The collector needs permission to access the device and must reconnect after unplugging, node reset or host/VM reboot. Opening an Uno serial connection can reset the board, so the collector must tolerate startup messages and a new boot ID.

### Using the physical serial port

The server's conventional COM interface is **RS-232**, while the Uno's D0/RX and D1/TX pins use **5 V TTL UART**. They require a suitable transceiver, such as a MAX232-based interface, with correctly wired transmit, receive and ground. Select straight-through or null-modem wiring based on the endpoints' documented pinouts. Do not wire the COM port directly to the Uno pins or to an SHT31 sensor. The SHT31 uses I2C and still needs a controller to translate its readings into serial records. [TI MAX232 interface specification](https://www.ti.com/product/MAX232).

One RS-232 port does not directly provide a multi-drop sensor bus. For several rack controllers, use independent serial ports, a controller that aggregates their readings, or an RS-485 design. An RS-485 adapter is a distinct peripheral, not an ordinary RS-232 cable. For example, ATEN documents a USB-to-RS-422/485 adapter; a purchased temperature/RH transmitter must additionally have a documented register map and configurable bus address. Follow the actual devices' instructions for supply, topology, termination and biasing. [ATEN USB-to-RS-485 adapter](https://www.aten.com/eu/en/products/usb-peripherals/usb-converters/uc485/).

### What RS-485 means: comparison with Ethernet

**RS-485 is an electrical communication standard, not a sensor or an Ethernet interface.** A temperature/humidity sensor can include an RS-485 interface to send its measurements. A common two-wire implementation communicates over a twisted signal pair, usually labeled A and B, with reference/ground and power connections as required by the equipment. Several compatible devices can share the bus. [Texas Instruments RS-485 explanation](https://www.ti.com/video/6107769508001).

RS-485 itself does not assign MAC addresses, IP addresses or device IDs. **Modbus RTU** is one protocol commonly used over RS-485: each sensor has a configured numeric address, such as 1, 2 or 3, and the collector asks each address for its measurements in turn. That number is a Modbus address, not an Ethernet MAC address. Other protocols can also use RS-485. [libmodbus RTU addressing documentation](https://libmodbus.org/reference/modbus_set_slave/).

| Feature | RS-485 sensor using Modbus RTU | Ethernet sensor or gateway using IP |
| --- | --- | --- |
| Typical connection | A/B signal terminals; separate supply and reference as specified | Ethernet port connected to a network switch |
| Device identification | Configured Modbus address; no Ethernet MAC/IP needed for this interface | MAC address for the Ethernet interface and an IP configuration |
| Several sensors | Share a properly wired bus with different Modbus addresses | Usually connect separately to a switch, or through a gateway |
| Connection to the monitoring VM | USB-to-RS-485 adapter passed into the VM, or a network-to-RS-485 gateway | VM reaches the device through the LAN |
| Arduino needed? | Not for a complete Modbus temperature/RH transmitter with a documented register map | Not for a complete network sensor/gateway with a supported API |

Example for the RS-485 alternative: **temperature/RH probes with addresses 1–12 → shared RS-485 bus → USB-to-RS-485 adapter → local monitoring VM**. The probe power supply is additional to the signal wiring. An Ethernet-to-RS-485 gateway is another option: the gateway has a network MAC/IP, while its attached RS-485 probes retain their Modbus addresses.

Some RS-485 products use an RJ45-shaped connector or Cat5 cable, but that does not make them Ethernet devices. Check the documented interface and pinout before connecting them to a network switch. Procurement should request a **temperature and relative-humidity transmitter with RS-485, Modbus RTU, configurable address and a published register map**, rather than a bare RS-485 converter.

### Native USB sensors exist

One documented example is **Yoctopuce Yocto-Meteo-V2-C**, a USB-C module measuring temperature, relative humidity and pressure, with a Python API. Its manufacturer describes it as a component requiring an enclosure. It demonstrates that Arduino-free USB sensing is possible; Iranian availability and pricing have not been verified for this alternative. A USB connector alone does not prove live acquisition support: some products only use USB for power or downloading historical logs. [Yoctopuce module and API manual](https://www.yoctopuce.com/EN/products/yocto-meteo-v2-c/doc/MTEOMK2C.usermanual.html).

### VM setup and verification procedure

1. Identify the server model, installed physical ports, hypervisor and VM placement. Check whether a host console or another service already owns the serial port.
2. Test one sensor/controller on a separate bench computer first. Establish its driver, serial settings or SDK, record format and unique identity.
3. Assign that USB device or physical serial port to the monitoring VM using the hypervisor's supported mechanism. For KVM/libvirt, documented mechanisms include USB `hostdev` assignment and a serial device backed by a host character-device path. This is not an automatic privilege available to every VPS tenant. [libvirt device assignment documentation](https://libvirt.org/formatdomain.html).
4. Run one collector service with device access permissions. Preserve raw records, processing timestamps, node IDs and sequence gaps, and route them into the existing recording/alerting pipeline.
5. Test unplug/replug, host reboot, VM reboot and stale-data notifications. A device assigned to one VM should have a single reader; coordinate any host-side collector accordingly.
6. Document that physical-port assignment ties collection to that host. Host migration or failover requires reattaching the hardware, forwarding readings from a separate collector, or selecting network-connected acquisition.

For this project, **pilot one Uno connected by USB to a local monitoring VM** if the racks are near the server. If rack distances or VM mobility make USB awkward, retain the Ethernet baseline or price industrial Modbus RTU probes and an isolated RS-485 interface. Keep acquisition outside the hypervisor host where practical, using either a dedicated VM or a separate gateway.

The earlier Ethernet budget remains the baseline. Switching four Uno nodes to USB removes four W5500 modules: **4,080,000 IRT of listed materials**, or **4,896,000 IRT including the associated 20% contingency**, before adding any USB hub, extension cables or revised power arrangements. A native-USB or RS-485 sensor design requires a new itemized quote and must not be assumed to cost the same as bare SHT31 modules.

## ELFI / Fidar EtherSense FTA3070-21: model and price research

**Research date: 13 October 2026. Result: the exact model is verified, but no public unit price in IRT, IRR or USD was found.** Fidar Electronics lists FTA3070-21 as a network temperature/relative-humidity sensor. Its product page directs purchasers to the sales team instead of displaying a price. Exact-model Persian and English price searches, including targeted searches of Torob and Emalls, did not produce a verifiable priced offer. Prices for unrelated products sharing the shorter `FTA3070` code are excluded. [Exact manufacturer product page](https://fidarelectronics.com/سنسور-دما-رطوبت-تحت-شبکه/), [Manufacturer purchasing information](https://fidarelectronics.com/از-کجا-بخریم؟/).

| Price question | Finding |
| --- | --- |
| Exact model | ELFI / Fidar Electronics EtherSense **FTA3070-21** |
| Published Iranian price | Not found; supplier quotation required |
| Published USD price | Not found; no actual dollar price available to convert |
| Confirmed unit cost in IRT | **Unknown**, not zero and not a planning allowance |
| Manufacturer sales telephone | **021-91308515** |
| Manufacturer email | **info@fidarelectronics.com** |

The telephone is published on the product/purchasing pages; the email is published on the [manufacturer homepage](https://fidarelectronics.com/). A written quote should specify unit price, currency, quantity discount, tax, delivery, included power supply/accessories and warranty. Request prices for **8 units** (two positions per rack), **12 units** (three positions per rack), and **14 units** (12 installed plus two spares). No purchase request or message to the manufacturer was sent during this research.

### Fit with the monitoring VM

The manufacturer describes Ethernet connectivity with DHCP/static IP and SNMP, HTTP and HTTPS support. The model's manual identifies a PoE Ethernet input, an adapter input and SNMP alarm configuration. **This is an Ethernet device alternative, rather than the RS-485 design discussed above.** The proposed connection is: **FTA3070-21 devices → monitoring LAN switch → collector in the monitoring VM → database/dashboard**. Arduino and serial/USB passthrough are unnecessary for that network acquisition path. [FTA3070-21 English manual](https://fidarelectronics.com/wp-content/uploads/2025/07/FTA3070-21-User-Manual-EN.pdf).

Obtain the exact SNMP MIB/OIDs, measurement scale and supported polling interval before configuring the collector. Also confirm sensor accuracy, calibration evidence, sensing-point count per unit, external-probe support and the required PoE standard/power budget. The public product page contains different temperature ranges in its overview and specification table, so final measurement and environmental limits need confirmation in the supplier's current datasheet. The manual also needs supplier clarification on the permissible combination of adapter power and Ethernet/PoE connections. Do not assume that four units provide 12 independent sensing points or that a generic 48 V injector is compatible.

### Conversion and quote-based sensor subtotal

Use **unit IRT = quoted unit USD × 270,000** when the quote is in dollars. If the quote is in Iranian rials, use **unit IRT = quoted unit IRR ÷ 10**. If it is already in tomans, no conversion is needed. Let **U** be the quoted unit price in USD and **T** the quoted unit price in IRT:

| Deployment | Units | Sensor subtotal from an IRT quote | Sensor subtotal from a USD quote, converted to IRT |
| --- | ---: | ---: | ---: |
| Two sensing positions per rack | 8 | 8 × T | 2,160,000 × U |
| Three sensing positions per rack | 12 | 12 × T | 3,240,000 × U |
| Three positions per rack plus two spare units | 14 | 14 × T | 3,780,000 × U |

These are conversion formulas, **not sensor prices or supplier quotations**. Quantities assume one sensing position per unit and must be revised if the confirmed product supports multiple remote probes. A complete FTA3070-21 system estimate must also include the required Ethernet/PoE ports or approved power supplies, cabling, mounting, taxes/delivery and integration labor. Its final cost cannot yet be calculated or compared reliably with the earlier **44,782,200 IRT Arduino materials budget**.
