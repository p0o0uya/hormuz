# Tank-fed fire suppression concept and cost estimate

Prepared **13 October 2026** for Hormuz Data Center, Ilam Province, Iran. Currency: **Iranian tomans (IRT); 10 IRR = 1 IRT**. Status: preliminary layout and budget for specialist quotation, **not an installation drawing**.

## Recommended system

For the repository's **4.5 m × 4 m (18 m²), four-rack room**, obtain a quotation for a **manufacturer-approved high-pressure water-mist pre-action system**: atmospheric water tank, matched fire pump, pre-action valve, pressure-rated pipework and automatic closed mist heads. Budget for protection both at the room ceiling and inside the roofed hot aisle. Use a matched system with documented approval for the actual data-center application, ceiling height, airflow and containment geometry. Domestic spray nozzles, irrigation pumps and a tank alone do not constitute this system.

The installed base allowance is **1,134,000,000 IRT before tax**. Low/base/high allowance scenarios are **685,500,000 / 1,134,000,000 / 2,004,000,000 IRT**. These are estimating scenarios, not verified Iranian market prices or binding quotes. All cost rows are unsourced allowances; manufacturer publications below support the concept, not prices. Obtain local written quotations before committing funds.

Marioff describes data-center water mist using a pump/tank arrangement and approved pre-action options. Its pre-action explanation describes dry standby piping, detection admitting water, and heat-operated closed heads controlling discharge. These support the proposed architecture, without certifying this room's layout. [Manufacturer data-center overview](https://www.marioff.com/en/industries/land/data-centers/), [pre-action operation](https://www.marioff.com/en/technology/system-types/pre-action/).

Request a conventional pre-action sprinkler alternative if the approved mist package cannot be supplied or maintained locally. It also uses piping, automatic heads and a water supply, but requires a separate hydraulic design and typically a different tank/pump budget. If the building has a proven compliant fire-water supply, quote connecting to it instead of duplicating storage and pumping. Clean-agent cylinders are another specialist option, but require a separate enclosure/agent design and are not the water-tank system budgeted here.

## Design basis and layout

Use the [airflow room plan](airflow-proposal.md) and [existing warning-system proposal](fire-monitoring-proposal.md). The room's **3.2 m height is an assumption**, not a measurement. Four assumed 600 × 1200 mm racks occupy x=1.05–3.45 m, y=1.60–2.80 m. The cold/front area is y=0–1.60 m; contained hot aisle is y=2.80–4.00 m. Room origin is the southwest corner, x east along 4.5 m and y north along 4 m.

The following tables contain the room layout and supply schematic. All positions are candidate areas for quotation, not installation coordinates.

| Room feature | Plan coordinates / arrangement |
| --- | --- |
| Orientation | North at top; southwest origin (0,0); x east and y north. Room 4.50 × 4.00 m; height assumed 3.20 m. |
| R1 | x=1.05–1.65 m, y=1.60–2.80 m |
| R2 | x=1.65–2.25 m, y=1.60–2.80 m |
| R3 | x=2.25–2.85 m, y=1.60–2.80 m |
| R4 | x=2.85–3.45 m, y=1.60–2.80 m |
| Rack fronts | Face south toward the cold aisle; keep escape and service routes clear. |
| Cold/front aisle | y=0–1.60 m |
| Contained hot aisle | Behind racks, y=2.80–4.00 m; H5–H6 beneath its roof. Coordinate heads with the return duct. |
| H1 / H2 | Ceiling candidates at (0.60,0.65) / (3.90,0.65) m |
| H3 / H4 | Ceiling candidates at (0.60,3.35) / (3.90,3.35) m |
| H5 / H6 | Containment candidates at (1.65,3.40) / (2.85,3.40) m |

| Supply / control stage | Connection and function |
| --- | --- |
| 1. Atmospheric tank | 3000 L nominal budget assumption; feeds the matched fire pump. Tank/pump are in an external service space. |
| 2. Matched fire pump and controller | Supplies the pre-action valve; duty and backup power determined by engineer. Include OEM-required filtration and water-quality preparation. |
| 3. Pre-action valve and supervision | Feeds OEM-approved pipework; single-interlock budget basis. |
| 4. Pressure-rated pipework | Feeds automatic closed heads; 35 m total budget quantity. Routing topology only; no bore or operating pressure specified. |
| 5. Closed heads | Six candidate heads: four ceiling and two beneath containment. Heat opens individual heads. No temperature rating or coverage radius specified. |
| Release controls | Compatible supervised controls receive detection, raise the alarm and release the valve. Control backup batteries and pump backup power are separate provisions. |

| Element | Quotation / layout basis | Final design requirement |
| --- | --- | --- |
| Tank and pump | Adjacent protected service space outside the rack room; 3000 L nominal tank as an illustrative allowance | Confirm available footprint, maintenance access, slab capacity, usable water volume, refill, water quality and freezing protection. A full 3000 L tank contains approximately 3 tonnes of water, plus its own weight. |
| Valve and controls | Accessible supervised assembly outside the protected room; short protected feeder to room | Exact valve, pressure ratings, detection interfaces, drains and release logic from the selected OEM package. |
| H1–H4 ceiling heads | Four candidate areas: (0.60,0.65), (3.90,0.65), (0.60,3.35), (3.90,3.35) m | Budget symbols, not drilling coordinates. Confirm wall spacing, rack/duct/tray obstructions and all coverage requirements. |
| H5–H6 hot-aisle heads | Two candidate areas inside containment: (1.65,3.40), (2.85,3.40) m, beneath its roof | The planned return duct occupies this area: revise head/duct locations together. Do not mount above the roof and assume protection below. More heads or a different layout may be required. |
| Pipework | 35 m total planning quantity including feeder, overhead branches, drops and routing reserve | No construction pipe bore specified. Engineer selects OEM-approved material, fittings, bore, support spacing and pressure rating after hydraulic calculation. The supply table represents topology only. |
| Detection | General room and contained-aisle detection coordinated with cooling airflow | Confirm listed compatibility with releasing controls. Aspirating detection may be needed; a new aspirating system is excluded from this estimate. |

Nozzle quantity cannot be established from floor area alone. The approval and installation manual must cover the actual room and aisle heights, obstructions, nozzle orientation/spacing, airflow and hazard. Survey any raised-floor or ceiling voids, combustible cabling and adjacent electrical/battery spaces separately. The budget covers only this rack room; it does not establish protection of the proposed UPS battery bank or the whole building.

## Supply and hydraulic sizing

The **six heads and 3000 L tank are costing assumptions**, not a proven suppression capacity. A supplier must identify the exact head model, K-factor, required minimum head pressure, maximum operating-head scenario, discharge duration and pump curve before equipment is ordered. Do not infer mist effectiveness from a nominal droplet size or calculate water demand from the facility's 50 kW electrical rating.

For budget sensitivity only, assume six simultaneous operating heads at **10 L/min each for 30 minutes**. Neither flow nor duration is a code requirement or a manufacturer's specification:

| Sizing step | Illustrative calculation / assumption | Result |
| --- | --- | ---: |
| Simultaneous heads | Budget example only | 6 |
| Flow per head | Budget example only | 10 L/min |
| Combined flow | 6 × 10 | 60 L/min |
| Discharge duration | Budget example only | 30 minutes |
| Discharge volume | 60 × 30 | 1800 L |
| Reserve | Assumed for example | 10% |
| Usable tank fraction | Assumed for example | 90% |
| Nominal volume example | 1800 × 1.10 / 0.90 | 2200 L |
| Rounded budget tank | Preliminary allowance | 3000 L nominal |

This example excludes separately required hose demand and other simultaneously protected zones; add them if applicable. Do not credit refill unless the engineer and authority accept its reliability. Reserve and usable fraction must be replaced with actual tank suction, freeboard and OEM requirements. If six heads instead require 15 L/min for 60 minutes, the same example gives **6600 L nominal**, requiring at least a **7000 L budget case** and revised tank, pump and installation pricing. A longer mandatory duration or greater operating area can increase this further.

At each operating head, use `q = K × sqrt(p)` with the manufacturer's consistent units. Calculate the remote-path pipe and fitting friction, filter and valve losses and elevation head; pump duty must deliver the complete simultaneous demand at the worst head's minimum pressure. Check maximum component pressure, transient effects, suction conditions, pump power and water delivery time. The engineer must also evaluate interlock-related delay. There is no pump pressure setpoint, head temperature or pipe diameter authorized by this concept.

Specify a documented power arrangement able to start and run the pump through a site mains failure. Battery backup for the alarm/releasing panel does **not** power the pump. The electrical allowance assumes suitable existing resilient power can be used; it does not buy a new generator, UPS, or a redundant pump set. The [50 kW UPS proposal](ups-proposal.md) is not evidence that spare capacity or motor-start capability exists. Quote those upgrades separately if required.

## Detection, release and building interfaces

The budget basis is **single-interlock pre-action with automatic closed heads**, subject to OEM and local acceptance. The DIY smoke-monitoring VM and Ethernet I/O in the warning-system proposal must not be used as suppression-release controls. Provide a compatible supervised releasing system, backed-up controls and a documented cause-and-effect schedule. Reuse existing detectors only when their compatibility and location are accepted by the suppression designer.

| Event | Intended behavior to be confirmed in the approved schedule |
| --- | --- |
| Normal | Valve closed; room piping dry as designed; tank level, valve position, power, control circuits and any supervisory air monitored. |
| Fire detection | Immediate local warning and existing cellular-call path; compatible release controls open the pre-action valve to fill pipes. Closed heads remain shut until heat activates them. Pump starts/maintains supply according to OEM logic. |
| Head opens after detection | Water discharges through the operated head; confirmed waterflow produces an alarm. Other closed heads remain shut. |
| Pipe/head damage without detection | Supervised pressure loss/fault as applicable; pre-action valve remains closed. Once detection releases the valve, a damaged pipe can discharge water: pre-action does not eliminate this risk. |
| Low tank level, power loss, closed valve or control fault | Local supervisory/trouble indication and operator escalation; handle as a protection impairment. Remote fault reporting needs a documented compatible interface. |
| Manual operation | Only the OEM-approved emergency release and maintenance controls; label and train operators. The existing evacuation call point is not automatically a suppression manual-release input. |

A double-interlock alternative admits water only after both detection and loss of supervisory air from an opened head; it has additional controls and delay considerations. Viking's technical description illustrates that distinction, not a selection of its sprinkler valve for this mist system. [Viking operation description, pages 1 and 4–5](https://www.vikinggroupinc.com/sites/default/files/migrated/F_052220.pdf).

Keep suppression independent of the LAN, monitoring VM and cellular network. Preserve immediate evacuation alarms and the [security door's fire release](security-proposal.md). Coordinate cooling, dampers and emergency electrical shutdown through the approved schedule; do not impose a generic fan stop or delayed release. Server UPS feeds can remain live after an ordinary mains disconnect. Mist can wet/damage electronics; agree emergency isolation, drainage and post-event recovery procedures. Any protection of batteries requires a separate hazard assessment.

## Cost table

All figures below are **unsourced planning allowances in IRT**, dated 13 October 2026. Quantities are preliminary. The tables in this file contain every low/base/high unit and extended price, scope note and calculated total. None of these numbers is a published Marioff or Viking price. An imported approved package may exceed the high scenario substantially.

### Low allowance: itemized costs

| ID | Part / service | Quantity | Low unit IRT | Low line IRT |
| --- | --- | ---: | ---: | ---: |
| S01 | Site survey, engineered drawings and hydraulic calculations | 1 lot | 25,000,000 | 25,000,000 |
| S02 | 3000 L nominal atmospheric water tank and level monitoring | 1 set | 35,000,000 | 35,000,000 |
| S03 | Matched high-pressure fire pump package with controller | 1 set | 250,000,000 | 250,000,000 |
| S04 | OEM-compatible pre-action valve assembly and supervised trim | 1 set | 65,000,000 | 65,000,000 |
| S05 | OEM-compatible automatic closed water-mist heads | 6 each | 8,000,000 | 48,000,000 |
| S06 | OEM-approved pressure-rated pipe or tubing | 35 m | 700,000 | 24,500,000 |
| S07 | Pressure-rated fittings, supports and penetration firestopping | 1 lot | 20,000,000 | 20,000,000 |
| S08 | OEM-required filtration and water-quality preparation | 1 set | 10,000,000 | 10,000,000 |
| S09 | Compatible releasing panel, batteries and supervised interfaces | 1 set | 35,000,000 | 35,000,000 |
| S10 | Compatible release detection and protected field cabling | 1 lot | 18,000,000 | 18,000,000 |
| S11 | Dry-pipe supervisory air package if required by OEM | 1 set | 15,000,000 | 15,000,000 |
| S12 | Test and drain assembly, flow and pressure supervision | 1 lot | 15,000,000 | 15,000,000 |
| S13 | Dedicated electrical feed and resilient pump power provision | 1 lot | 25,000,000 | 25,000,000 |
| S14 | Tank base, drainage route and leak detection | 1 lot | 15,000,000 | 15,000,000 |
| S15 | Specialist mechanical and electrical installation | 1 lot | 45,000,000 | 45,000,000 |
| S16 | Commissioning, acceptance, training and as-built documents | 1 lot | 20,000,000 | 20,000,000 |
| S17 | Local transport and handling | 1 lot | 10,000,000 | 10,000,000 |
| S18 | OEM-required spare heads, tools and initial service consumables | 1 lot | 10,000,000 | 10,000,000 |
| TOTAL | **Installed planning total before tax** | | | **685,500,000** |

### Base allowance: itemized costs

| ID | Part / service | Quantity | Base unit IRT | Base line IRT |
| --- | --- | ---: | ---: | ---: |
| S01 | Site survey, engineered drawings and hydraulic calculations | 1 lot | 40,000,000 | 40,000,000 |
| S02 | 3000 L nominal atmospheric water tank and level monitoring | 1 set | 55,000,000 | 55,000,000 |
| S03 | Matched high-pressure fire pump package with controller | 1 set | 400,000,000 | 400,000,000 |
| S04 | OEM-compatible pre-action valve assembly and supervised trim | 1 set | 100,000,000 | 100,000,000 |
| S05 | OEM-compatible automatic closed water-mist heads | 6 each | 14,000,000 | 84,000,000 |
| S06 | OEM-approved pressure-rated pipe or tubing | 35 m | 1,200,000 | 42,000,000 |
| S07 | Pressure-rated fittings, supports and penetration firestopping | 1 lot | 35,000,000 | 35,000,000 |
| S08 | OEM-required filtration and water-quality preparation | 1 set | 20,000,000 | 20,000,000 |
| S09 | Compatible releasing panel, batteries and supervised interfaces | 1 set | 60,000,000 | 60,000,000 |
| S10 | Compatible release detection and protected field cabling | 1 lot | 30,000,000 | 30,000,000 |
| S11 | Dry-pipe supervisory air package if required by OEM | 1 set | 25,000,000 | 25,000,000 |
| S12 | Test and drain assembly, flow and pressure supervision | 1 lot | 25,000,000 | 25,000,000 |
| S13 | Dedicated electrical feed and resilient pump power provision | 1 lot | 45,000,000 | 45,000,000 |
| S14 | Tank base, drainage route and leak detection | 1 lot | 25,000,000 | 25,000,000 |
| S15 | Specialist mechanical and electrical installation | 1 lot | 75,000,000 | 75,000,000 |
| S16 | Commissioning, acceptance, training and as-built documents | 1 lot | 35,000,000 | 35,000,000 |
| S17 | Local transport and handling | 1 lot | 20,000,000 | 20,000,000 |
| S18 | OEM-required spare heads, tools and initial service consumables | 1 lot | 18,000,000 | 18,000,000 |
| TOTAL | **Installed planning total before tax** | | | **1,134,000,000** |

### High allowance: itemized costs

| ID | Part / service | Quantity | High unit IRT | High line IRT |
| --- | --- | ---: | ---: | ---: |
| S01 | Site survey, engineered drawings and hydraulic calculations | 1 lot | 70,000,000 | 70,000,000 |
| S02 | 3000 L nominal atmospheric water tank and level monitoring | 1 set | 90,000,000 | 90,000,000 |
| S03 | Matched high-pressure fire pump package with controller | 1 set | 700,000,000 | 700,000,000 |
| S04 | OEM-compatible pre-action valve assembly and supervised trim | 1 set | 180,000,000 | 180,000,000 |
| S05 | OEM-compatible automatic closed water-mist heads | 6 each | 24,000,000 | 144,000,000 |
| S06 | OEM-approved pressure-rated pipe or tubing | 35 m | 2,000,000 | 70,000,000 |
| S07 | Pressure-rated fittings, supports and penetration firestopping | 1 lot | 60,000,000 | 60,000,000 |
| S08 | OEM-required filtration and water-quality preparation | 1 set | 40,000,000 | 40,000,000 |
| S09 | Compatible releasing panel, batteries and supervised interfaces | 1 set | 100,000,000 | 100,000,000 |
| S10 | Compatible release detection and protected field cabling | 1 lot | 55,000,000 | 55,000,000 |
| S11 | Dry-pipe supervisory air package if required by OEM | 1 set | 45,000,000 | 45,000,000 |
| S12 | Test and drain assembly, flow and pressure supervision | 1 lot | 45,000,000 | 45,000,000 |
| S13 | Dedicated electrical feed and resilient pump power provision | 1 lot | 90,000,000 | 90,000,000 |
| S14 | Tank base, drainage route and leak detection | 1 lot | 50,000,000 | 50,000,000 |
| S15 | Specialist mechanical and electrical installation | 1 lot | 130,000,000 | 130,000,000 |
| S16 | Commissioning, acceptance, training and as-built documents | 1 lot | 60,000,000 | 60,000,000 |
| S17 | Local transport and handling | 1 lot | 40,000,000 | 40,000,000 |
| S18 | OEM-required spare heads, tools and initial service consumables | 1 lot | 35,000,000 | 35,000,000 |
| TOTAL | **Installed planning total before tax** | | | **2,004,000,000** |

### Item scope and pricing basis

All S01–S18 entries are unsourced planning allowances, not supplier quotations.

| ID | Scope / pricing note |
| --- | --- |
| S01 | Includes manufacturer application and local authority review |
| S02 | Illustrative capacity only; OEM water quality and usable volume govern |
| S03 | OEM fire-protection package; duty and redundancy unconfirmed |
| S04 | Single-interlock budget basis; no generic solenoid substitution |
| S05 | Four ceiling and two containment candidate heads; final count by listing |
| S06 | Budget route allowance; material and bore from hydraulic design |
| S07 | No domestic compression fittings |
| S08 | Includes initial fill treatment allowance |
| S09 | Incremental suppression controls; DIY monitoring VM/I/O not used for release |
| S10 | Budget for two detection areas; reuse only with documented compatibility |
| S11 | Regulator and pressure supervision; deduct only if OEM permits omission |
| S12 | Remove overlaps with quoted valve/pump package |
| S13 | Assumes suitable existing backup source; excludes new generator or UPS |
| S14 | Assumes nearby approved drain and sound ground-level slab |
| S15 | Survey-dependent labor allowance |
| S16 | Includes safe test discharge and control testing |
| S17 | Excludes exceptional import/customs costs |
| S18 | Exact spare count and tools per OEM |

Each installed total is the sum of its itemized costs, with no contingency added. Totals exclude the existing warning-system budget and the exclusions listed below.

### Scenario totals

| Scenario | Installed total before tax IRT |
| --- | ---: |
| Low allowance | 685,500,000 |
| Base allowance | 1,134,000,000 |
| High allowance | 2,004,000,000 |

The scenario totals change every line's allowance together; they are not confidence intervals. Supplier package pricing may combine S03–S04, S08, S11–S12 and controls: remove overlaps before summing an actual quotation. S10 covers incremental release detection; the separately budgeted smoke detectors, Ethernet I/O, siren and voice API setup in the fire-monitoring proposal are not included again here.

**Excluded:** VAT/taxes, extraordinary shipping/customs/import charges, major structural work, tank room construction, new backup generator/UPS, redundant pumps, aspirating detection, additional protected rooms/voids, required upgrades to the building sprinkler supply and post-fire equipment replacement. Confirm applicable taxes on each quote rather than inventing a rate. Ring-fence an additional **30–70 million IRT per year as an unsourced service allowance**, outside the capital total, for scheduled specialist maintenance; replacement pumps, major repairs and consumables after discharge are extra.

## Procurement, installation and acceptance

1. **Survey and approval:** a qualified fire protection engineer and OEM-authorized installer measure the room, ducts, containment, voids, airflow, water/power availability and tank location. Confirm Iranian/local fire authority and insurer requirements, accepted standards/editions and whether water mist may satisfy the required building protection. NFPA 75 addresses fire protection of IT areas; NFPA 750 is the relevant water-mist framework, but a standard title is not proof of project compliance. [NFPA 75 scope](https://www.nfpa.org/codes-and-standards/nfpa-standard-development/75). Full standards and a manufacturer's installation manual have not been reviewed for this project.
2. **Obtain comparable quotes:** issue this single Markdown proposal, including its layout and cost tables, to qualified suppliers. Require exact model numbers, application approval/listing, local acceptance, manufacturer hydraulic calculations, final head count, pipe schedule, tank usable volume, pump curve, power redundancy, release logic, commissioning scope, taxes, delivery time, warranty and local spare/service availability. Reject a proposal consisting only of unspecified nozzles, a domestic pump and generic plumbing.
3. **Install the approved package:** specialist installs the tank/base, pump/valves, protected supply, approved tubing and supports, drain/test route and supervised control circuits. Flush to the OEM procedure before final head installation. Schedule work around live IT equipment and keep escape/service routes accessible. Allow roughly 4–7 specialist working days after equipment delivery and design approval, subject to survey; imported equipment lead time is unconfirmed. The owner coordinates access and procurement, rather than fabricating pressure or release components.
4. **Commission before service:** witness the checks below with the designer/installer and authority where required; obtain signed acceptance and operator training. Keep system impairments controlled during work, with locally agreed temporary protection.

| Acceptance check | Evidence required |
| --- | --- |
| Coverage and approvals | Approved as-built head layout including beneath containment; obstruction review and application listing/manual. |
| Hydraulic supply | Remote-path calculation, pump curve, measured flow/pressure at safe test outlet and recorded water delivery time meeting OEM/authority requirements. |
| Tank and water | Usable-volume/duration calculation; water-quality/filtration records; refill, low-level supervision and drain checks. |
| Pipe integrity | Flushing and prescribed pressure/leak test using the OEM's method; record pressure and duration. No improvised compressed-air proof testing. |
| Release logic | Detection-only and head/pressure-loss-only states demonstrated with approved safe simulations; correct interlock, pump start, waterflow alarm, reset and emergency-release operation. |
| Electrical and faults | Pump start/run on accepted backup source; control battery calculation/test; supervised valve/air/level/cable/power faults and restoration. |
| Interfaces and recovery | Local alarm/calls, door release and approved fan/power actions demonstrated; controlled discharge kept away from live racks; drainage and refill/reset procedure. |
| Handover | Model/serial inventory, drawings, hydraulic report, cause-and-effect schedule, signed test sheets, manuals, service contract and impairment procedure. |

Check panel normal state, water level, valve availability and pump readiness routinely; log faults and restore protection promptly. Have the authorized specialist set the inspection, testing, filter cleaning, water-quality and servicing schedule from the supplied manual and local requirements. Do not test discharge over live servers or alter head orifices, pump settings or release logic after handover.
