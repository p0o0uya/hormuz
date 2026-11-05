# Hormuz source brief

This repository note preserves the context used for the first presentation draft. It is a project reference, not a claim of permanent assistant memory. Prepared 5 November 2026.

## Authoritative narrative

Use [Hormuz-Cost-Effective-Draft-02.docx](../assets/park/Hormuz-Cost-Effective-Draft-02.docx), with its [PDF counterpart](../assets/park/Hormuz-Cost-Effective-Draft-02.pdf), as the primary source for this presentation. Draft 01 and Jamali-17-05-1405 are earlier context; do not merge their differing scopes or model lists into the current pilot. The current application is for Ilam University's incubator. The presentation is in Persian to match that application.

Hormuz proposes a small, cost-effective data center in Ilam: selectively build maintainable components, validate prototypes, start with one equipped rack, and expand as customers justify purchases. Services are VPS, dedicated servers, colocation, and Internet telephony installation/support. The first customer segments are local software firms, shops, service offices and organizations needing remote-work infrastructure. Three initial customers are a target, not signed contracts.

The README describes Hormuz as operated by Rayka Dan Trade & Technology Company, established in 2025. The application leaves legal-registration fields unresolved. The presentation therefore does not make a new assertion about registration or completed operating capability.

## Design facts and unresolved bases

- Room basis: 4.5 × 4 m, 18 m², four 42U racks. Layouts are provisional; access, door, ceiling and real rack sizes require survey. Auxiliary space for batteries, cooling and a tank is separate and unconfirmed.
- The latest application uses **50 kW total facility load**, including IT and auxiliaries. This is not 50 kW proven IT capacity. The reported three-phase 220 V supply needs phase-to-phase/phase-to-neutral clarification.
- Airflow study: **20 kW IT example**, approximately 7,200 m³/h cold supply. Cooling-production equipment is excluded. The experimental radiator is a heat exchanger, not a source of cold.
- Backup ambition: **two hours**. The available commercial UPS estimate covers **50 kW UPS output and 15 minutes**, with provisional stationary-battery quantities. It is a distinct sizing case and must be reconciled with the total facility ceiling. It does not price or demonstrate two-hour backup.
- Automotive batteries are an experimental candidate, not an approved final selection. Solar is outside the initial budget.
- Monitoring: three inlet heights per rack, 12 installed temperature/RH points, local nodes and a VM. Prove a one-rack prototype first.
- Graphite/epoxy flooring and raw-media filters need qualification; do not describe them as certified or already proven.
- Smoke: start with two relay-output detectors; a third is conditional. Local siren operation must survive VM loss. Suppression uses independent controls and specialist design, not a VM release command. The water-mist study is a costing concept, not construction documentation.
- Security basis: four cameras and entrance control with emergency exit behavior tested.
- Existing equipment: two G10 servers plus some boards, sensors and fans. Inventory, health, exact models and usable capacity are unverified; deduct matched inventory from purchases.

## Financial baseline

All amounts below are **million Iranian tomans**, not rials. These are the 13 October 2026 estimate basis in Draft 02, not current supplier quotations or a verified current exchange rate. The application uses a historical scenario of 270,000 tomans/USD. The deck deliberately uses the application's amounts without presenting new market guidance.

| Group | Exact application subtotal |
| --- | ---: |
| Rack monitoring | 37.3185 |
| Rod earthing | 192.115 |
| Airflow and filtration | 319.58 |
| Antistatic floor | 43.5 |
| CCTV and entrance control | 259.576 |
| Smoke detection | 25.5473 |
| Tank-fed suppression | 1134 |
| Seven groups without UPS | **2011.6368** |
| Commercial 15-minute UPS reference | **10020** |
| Eight-group comparison | **12031.6368** |

These application figures exclude contingency. Some technical studies separately show totals with 20% contingency; do not mix those with the application subtotals. Rod, ring and plate earthing are alternatives. Shared cables, network and earth items must be counted once. Deduct existing inventory after verification. Cooling production, racks and server completion, premises, supply upgrades, tax and working capital remain outside this comparison. No full pilot capital request or full-project total has been established.

Monthly sales scenarios, not commitments:

| Scenario | Recurring | New installations | Gross sales | Assumed cash running cost | Cash surplus / deficit |
| --- | ---: | ---: | ---: | ---: | ---: |
| Target | 122 | 16 | 138 | 100 | +38 |
| Weak | 67 | 8 | 75 | 100 | -25 |

Without new installations, target recurring cash surplus is 22. These are not net profit; depreciation, tax, financing and major battery replacement are excluded. Running cost assumes founder activity and part-time support, not five full-time employees. The target 40 VPS at 4 GB each needs 160 GB guest RAM plus host/telephony overhead; usable hardware resources must be confirmed. One G10 is allocated to VPS/telephony, the other to dedicated rental; colocation capacity is separate.

The 24-month weak scenario assumes 600 cash deficit, fixed estimate-date prices, full purchase of priced groups, and 20 shutdown cost. Assumed recovery is about 599.49 without UPS or 4106.49 with the 15-minute reference. Illustrative loss is about 2032.15 or 8545.15 respectively. These are scenario assumptions, exclude unpriced purchases and do not guarantee resale. Do not imply a validated rapid payback.

## Execution and support

Sequence: survey/quotes/customer conversations → prototypes → base infrastructure → first-rack integrated acceptance and 72-hour loaded observation → initial services/three-customer target → adjust prices and expand. No fixed calendar is established. Material curing, soil and procurement can change timing.

Team according to application: Pouya Jamali, MSc mechatronics, infrastructure/software; Ali Shokri, BSc mechanical engineering, supply, mechanical/electrical safety and sales support. Personal credentials are application statements, not independently verified. Specialist electrical/fire design and acceptance remain necessary.

Requested incubator support: workspace with capacity for five people, shared measuring equipment, electrical/material laboratory access, academic guidance, pilot-customer introductions, contract and finance support. Connecting support to measurable milestone outputs is a presentation proposal, not an approved agreement.

## Supporting technical sources

All eight are under [assets/park](../assets/park/): [monitoring](../assets/park/rack-monitoring-proposal.md), [earthing](../assets/park/earthing-proposal.md), [airflow](../assets/park/airflow-proposal.md), [UPS](../assets/park/ups-proposal.md), [floor](../assets/park/antistatic-floor-proposal.md), [security](../assets/park/security-proposal.md), [smoke](../assets/park/fire-monitoring-proposal.md), [suppression](../assets/park/fire-suppression-proposal.md). They are proposals and estimates, not evidence of equipment purchased, tests passed, standards certification or service availability.
