# DIY graphite-filled epoxy floor: formulation, quantities, costs and installation

Prepared 13 October 2026 for Hormuz. This single document contains the design, research, recipes, material estimates, cost tables and implementation procedure. Design basis: **18 m² (4.5 × 4 m), existing sound mosaic, four racks removed during work**, as in the [airflow proposal](airflow-proposal.md). Currency: **Iranian tomans (IRT); 10 rials = 1 toman**.

## Design decision

**Make the conductive layers ourselves from unfilled epoxy resin, its matched room-temperature hardener, and ordinary fine graphite powder.** Purchase no proprietary ESD epoxy, conductive primer or grounding kit. Use ordinary epoxy as the bonding primer; make a graphite-rich collector coat over copper tape and a graphite-filled wearing coat above it.

The starting design is **40 wt% graphite in a 0.25 mm collector coat, followed by 35 wt% graphite in a 1.0 mm wearing coat**. These percentages refer to the total mixed mass including resin, hardener and graphite. They are proposed trial formulations, not a laboratory-verified recipe for our materials. Test 30%, 35% and 40% first; use the lowest loading that repeatedly passes the electrical and mechanical criteria. The room budget uses 35% for the wearing coat and 40% for the collector coat, conditional on those trials passing. The practical outcome is a black or dark gray opaque floor that hides the mosaic.

The papers establish that ordinary graphite can make epoxy conductive. They do not establish that every resin/graphite mixture produces an acceptable floor. Our qualification work addresses that gap; it is part of making the material, not a requirement to buy a branded replacement. If a batch fails, adjust and retest it before coating the room.

## Research and what it supports

| Primary source | Relevant evidence | Consequence for this design |
| --- | --- | --- |
| [Reis et al., COBEM 2013, full paper](https://www.abcm.org.br/anais/cobem/2013/PDF/646.pdf) | Used DGEBA epoxy, aliphatic amine hardener and ordinary natural graphite of approximately 105 μm. Table 1 reports room-temperature volume resistivity of 2.7 × 10⁵ Ω·cm at 30 wt%, 4.5 × 10⁴ Ω·cm at 40 wt%, and 1.6 × 10³ Ω·cm at 50 wt%. Graphite was dispersed into resin before hardener addition. | Ordinary graphite is a viable low-cost starting filler. Screen 30–40%; avoid jumping to extreme loading merely for greater conductivity. These were cast specimens, not walking-tested floors. |
| [Darabut et al., Materials Research Bulletin 183 (2025), article 113186](https://doi.org/10.1016/j.materresbull.2024.113186) | The accessible abstract reports electrical percolation thresholds of 2.8–8.5 vol% for different graphite fillers, with lower thresholds for thermally expanded graphite. Full text was not available in this review. | Filler grade and structure matter. A threshold reported for one graphite cannot be transferred to our ordinary powder. |
| [Kanapitsas et al., APS March Meeting 2009, abstract](https://meetings-archive.aps.org/mar/2009/s1/6/) | Expanded graphite showed a preliminary 3–5 wt% threshold after prolonged acetone sonication and thermal processing. | This low loading is not a recipe for ordinary graphite stirred into floor epoxy. We do not budget sonication, solvents or heated floor cure. |
| [WEST SYSTEM 423 technical sheet](https://www.westsystem.com/app/uploads/2022/12/423-Graphite-Powder-Technical-Data-Sheet.pdf) | Recommends 10% graphite by volume for low-friction/scuff-resistant marine coatings; the sheet does not establish an ESD floor rating. | Do not confuse a lubricating graphite additive recipe with a qualified ESD formulation; evaluate slip resistance. |
| [EOS/ESD Association: basic control procedures](https://www.esda.org/esd-overview/esd-fundamentals/part-3-basic-esd-control-procedures-and-materials/) | Personnel-grounding qualification requires person/footwear/floor resistance <10⁹ Ω and walking body voltage <100 V. | Measure both; powder content or a resistance reading alone cannot establish personnel ESD performance. |
| [EOS/ESD Association: footwear and flooring](https://www.esda.org/news/understanding-footwear-and-flooring-in-esd-control/) | Footwear contact and cleaning residues affect performance of the combined system. | Use actual operator footwear and actual cleaning practice in the trials. |

**Engineering inference, not a measured result:** for a uniform isotropic 1 mm film, sheet resistance is approximately `volume resistivity / thickness in cm`. The 30% and 40% results above would imply about **2.7 MΩ/square** and **0.45 MΩ/square**, respectively. This supports investigating these mixtures, but cannot predict our finished floor's resistance to ground: flake alignment, a resin-rich surface, copper contact, dispersion and probe geometry change the result. Volume resistivity, sheet resistance and floor-to-ground resistance are different quantities. The collector thicknesses, 35% midpoint, density assumptions and installation details below are our proposed design, not specifications reproduced from the papers.

## Raw materials and layer build-up

| Component | What to obtain / make | Purpose |
| --- | --- | --- |
| Epoxy part A | Low-viscosity, unfilled DGEBA-based epoxy suitable for room-temperature coating; published viscosity, cure, adhesion and abrasion data | Binder; ordinary flooring/coating grade rather than decorative deep-pour resin |
| Hardener part B | Matched amine hardener supplied for A, with a stated **weight** mixing ratio and working time | Cure; never substitute an unknown amine or adjust dosage for graphite |
| Graphite | Dry, fine flake powder, provisionally ≤45 μm and ≥99% carbon, consistent lot, no oil/wax treatment | Conductive network; finer grade than the cited 105 μm study, so our trials are essential |
| Bonding primer | The unfilled A+B binder, if its adhesion trial succeeds on prepared mosaic | Bond/seal substrate; no conductive function needed below collectors |
| Repair mortar | A+B with clean dry graded quartz, trial its workable filler ratio | Fill static cracks and grout recesses; ordinary nonconductive repair is below the conductive layers |
| Collector coat | A+B plus graphite at screened 40 wt% | Distributes charge to tape; target 0.25 mm cured thickness |
| Wearing coat | A+B plus graphite at screened 35 wt% | Conductive through-thickness and walking surface; target 1.0 mm cured thickness |
| Copper collectors | Thin copper tape/foil with mechanically continuous joints | Gather charge beneath collector coat |
| Grounding points | Fabricated copper contact plates, secure fasteners, lugs and protected accessible connections | Two independently wired connections to existing common bonding bar |

Do not buy coarse metallurgical coke, pencil dust, activated carbon or an unspecified black powder as a substitute. Do not add quartz, pigment, talc, solvent, water or a nonconductive clear coat to the conductive recipes. Quartz is only budgeted for repairs. Any later additive requires a fresh trial. The surface may be more slippery than ordinary epoxy and must pass the slip assessment before use.

```text
Walking surface: 35 wt% graphite + epoxy, 1.0 mm trial design
Collector layer: 40 wt% graphite + epoxy, 0.25 mm trial design
Copper tape + mechanically secured copper terminal plates
Unfilled epoxy bonding primer, approximately 0.30 kg/m²
Repaired, ground, sound and dry mosaic / underlying slab
```

## Exact batch recipes

Let `w = graphite fraction of total mixed mass`, `E = mass of resin A + hardener B`, and `G = graphite mass`:

```text
G = E × w / (1 − w)
Total mixed mass = E / (1 − w)
If the binder ratio by weight is A:B = 100:h:
A = E × 100 / (100 + h)
B = E × h / (100 + h)
```

**Use the selected binder's actual ratio.** The 100:40 ratio in the following table is only a worked example, not a universal formulation. We buy a matched A+B binder; we do not synthesize resin or choose hardener stoichiometry ourselves.

| Graphite fraction of total | Graphite per 1,000 g A+B | A for a 500 g total batch, example 100:40 | B for that batch | Graphite for that batch |
| --- | ---: | ---: | ---: | ---: |
| 0% control | 0 g | 357.14 g | 142.86 g | 0 g |
| 30% candidate | 428.57 g | 250.00 g | 100.00 g | 150.00 g |
| 35% candidate | 538.46 g | 232.14 g | 92.86 g | 175.00 g |
| 40% candidate | 666.67 g | 214.29 g | 85.71 g | 200.00 g |

Thus **35% does not mean adding 350 g graphite to 1 kg binder**; that would give only 25.93% graphite. For a 1 kg total production batch at 35% and example 100:40, use **464.29 g A + 185.71 g B + 350 g graphite**. At 40%, use **428.57 g A + 171.43 g B + 400 g graphite**.

### Mixing method

1. Work in a ventilated preparation area away from electronics. Use closed containers, extraction suitable for the material, gloves, goggles and respiratory protection selected from the powder and epoxy safety sheets. Avoid dispersed conductive dust; do not dry-sweep it or blow it with compressed air.
2. Weigh A, B and graphite separately. Use a scale resolving 0.1 g for trials and suitably accurate scales for production. Record lots, quantities, temperature and batch identification.
3. Add graphite gradually into **A only**, wetting it under the liquid surface. Use a small dispersing head or suitable mixer with controlled speed; scrape the vessel and mix until no dry clumps remain. About 10–15 minutes is a starting trial procedure, adjusted for equipment and viscosity. Keep temperature within the binder's instructions and record it; do not overheat it to obtain flow.
4. Let entrained air settle or vacuum-degas before B if equipment is available. Reject a mixture that cannot wet the powder or be spread evenly without thinning. Change binder viscosity or filler grade and repeat trials; do not improvise solvent dilution.
5. Add the correct B mass, mix for the binder's prescribed time while scraping sides/bottom, transfer to a clean vessel and remix. The working-time clock begins with B addition. Graphite contributes no hardener demand in this calculation.
6. Spread immediately using the tool and thickness qualified on panels. Use a spike roller only if the trial shows it removes bubbles without damaging the film. Start production at 0.5–1 kg total per batch; increase only after timing a successful application. Never leave a large reactive mass in a bucket or return mixed material to stock.

## Qualification before the room

Make **three independently mixed batches at each 30%, 35% and 40%**, plus an unfilled control. Use 100 g total mixed mass per screening batch (scale the 500 g recipes by 0.20), including a 100 g unfilled control. Small coupons check cure and dispersion; an approximately 1 m² mosaic mock-up checks the selected complete stack, including tape, collector, surface and grounding. Reserve **2.5 kg A+B and 1.5 kg graphite** for the first trial round and pilot. Additional rounds require additional material. Use the same powder, resin, mixing equipment, thickness and cure conditions planned for the room.

| Check | Method and project decision |
| --- | --- |
| Cure / workability | Follow the binder's full-cure time at measured temperature. No tack, soft patches, dry clumps or voids. Must spread at thickness without solvent. Do not use an arbitrary branded product's cure schedule. |
| Mosaic adhesion | Pull-off testing, provisionally ≥1.5 MPa with no unacceptable coating/mosaic debonding; identify weak substrate or tile bedding. Repeat after preparation changes. This is a project criterion, not a result from the papers. |
| Through-thickness contact | Test surface to embedded collector as well as lateral surface resistance. A conductive molded core can still have an insulating surface skin. Do not qualify panels using sanded faces when the installed surface will be unsanded. |
| Collector layer | On the connected pilot, seek resistance to ground ≤10⁷ Ω at representative positions before applying the wearing layer. This is an intermediate project goal, not a standard limit. |
| Final floor resistance | Preferred project range **10⁶–10⁸ Ω** to ground and point-to-point, for operating margin. All points must remain <10⁹ Ω; investigate results below 10⁶ Ω with the electrical/ESD specialist rather than assuming greater conductivity is always better. |
| Person/footwear/floor | Resistance <10⁹ Ω and walking voltage <100 V with actual footwear, using STM97.1/97.2 or applicable IEC equivalents. A multimeter cannot perform this qualification. |
| Climate / repeatability | Use intended temperature range and lowest expected RH, with controlled conditioning documented by the testing provider. Require passing results from all three independent batches, not just one point near percolation. |
| Wear and shedding | On the fully cured pilot, roll a representative loaded caster repeatedly, assess indentation/chipping and rub/clean the surface. Reject visible conductive dust or black transfer to shoes/cleaning cloths. Specify lab abrasion testing if service loads cannot be represented by this trial. Recheck electrical results after wear and cleaning. |
| Slip / operational suitability | Assess under expected dry and cleaning conditions using an appropriate slip-test method and local criterion. Reject unacceptable low-friction behavior; a texture adjustment needs complete electrical and wear retesting. |

Select the lowest graphite fraction that passes **all** checks reliably. If 30% is unstable, use the passing 35% or 40% mixture. If all fail electrically, investigate dispersion, surface skin and filler grade; screen 45% only as a new experiment and recheck mechanical properties. If powder sheds or the film becomes brittle, reduce loading or change binder/grade and repeat. A graphite-rich brittle coating is unsuitable for a datacenter even if its electrical reading is good. Keep the floor out of service until a working formulation and installed floor pass. No paper reviewed demonstrates a universal durable mosaic-floor recipe at our chosen percentages.

## Copper layout and homemade grounding points

Use a **trial** perimeter loop, one lengthwise center strip and one cross strip; retain it only after the largest tape-free span and completed floor pass the tests in the answers section below. Lay tape on the cured bonding primer and completely cover it with the graphite collector. Adhesive below foil may be insulating if the coating contacts its bare upper face; **electrical joints between foil pieces must then be soldered or mechanically clamped**, not merely adhesive-overlapped. Conductive-adhesive tape is convenient if affordable; ordinary copper foil is viable with qualified joints. Keep flux residue off the coating surface and verify continuity before covering.

```text
                  4.5 m
        G1 ┌──────────┬──────────┐
           │          │          │
       4 m ├──────────┼──────────┤
           │          │          │
           └──────────┴──────────┘ G2
G1 and G2 each have a protected wire to the common bonding bar.
```

For each terminal, fabricate a deburred copper contact plate provisionally **50 × 50 × 1 mm**, securely clamp the collector tape beneath/against it, and provide a bolted copper-compatible lug connection. Locate plates at sheltered wall edges; recess/profile them into the repaired substrate so they do not create a trip or thin-coating ridge. Confirm the connection remains accessible for continuity checks; protect it with a cover. Select fastener sizes and anchors for the actual substrate after locating concealed services. Trial the coating's contact with the copper; bright metal beneath epoxy does not guarantee an electrical interface.

Allow **15 m total of 4 mm² green/yellow copper and 15 m protective conduit** for two routes; the electrician verifies size, attachment and actual lengths. Both points bond to the **existing verified common building earthing network**, covered in the [earthing proposal](earthing-proposal.md). Use no isolated earth rod, neutral or plumbing connection. Preserve rack/circuit PE. Insert no arbitrary resistor in protective bonding. Movement joints must remain functional; electrically connect coating sections using a protected flexible bonding bridge rather than relying on rigid tape over an opening joint.

## Room quantities

For graphite-filled layers, estimate density by the reciprocal rule using **binder density 1.15 kg/L** and **graphite true density 2.20 kg/L**:

```text
Mixture density = 1 / [(1−w)/1.15 + w/2.20] kg/L
Net layer mass (kg) = area (m²) × thickness (mm) × density (kg/L)
Planning mass = net mass × 1.10
```

These are engineering allowances for a void-free, 100%-solids mixture, not powder bulk density or measured coverage. At 35%, density ≈1.381 kg/L; at 40%, ≈1.421 kg/L. Measure cured density and actual pilot consumption, then revise the estimate. For a solvent-bearing binder, these quantities are not valid without solids/shrinkage correction; choose unfilled 100%-solids binder for this plan.

| Use | Thickness / consumption | A+B with 10% loss | Graphite with 10% loss |
| --- | --- | ---: | ---: |
| Unfilled bonding primer | 18 × 0.30 kg/m² net | 5.94 kg | 0 |
| Collector, 40 wt% | 18 m² × 0.25 mm; 6.396 kg net compound | 4.22 kg | 2.81 kg |
| Wearing layer, 35 wt% | 18 m² × 1.00 mm; 24.851 kg net compound | 17.77 kg | 9.57 kg |
| Minor repair binder | Provisional; add quartz separately | 2.00 kg | 0 |
| First trial round and pilot | Reserved material | 2.50 kg | 1.50 kg |
| **Calculated allocation** | Rounded lines shown | **32.43 kg** | **13.88 kg** |
| **Budget purchase** | Round up to actual packaging | **35 kg A+B** | **15 kg graphite** |

The compound allocation is **7.036 kg collector** and **27.336 kg wearing layer** including loss. Extra purchased material is reserve, not permission to increase thickness. At example A:B = 100:40, a 35 kg binder purchase contains **25 kg A + 10 kg B**. At another ratio, divide the same total using the recipe formula. Reserve **5 kg dry quartz for repairs only**; major levelling is excluded.

Tape: `[2(4.5+4)+4.5+4+2 m tails] × 1.10 = 30.25 m`; budget **one 50 m roll**, provisionally 10 mm wide. Grounding: **2 fabricated terminal assemblies**. For a new room substitute its area in the density equation; tape for this layout is `[3(L+W)+2] × 1.10`. Site repairs, bonding routes and mobilization need separate measurement.

| Wearing formulation alternative | 1 mm compound with loss, 18 m² | Wearing A+B | Wearing graphite | Whole-project purchase allowance including other uses |
| --- | ---: | ---: | ---: | --- |
| Passing 30 wt% | 26.58 kg | 18.60 kg | 7.97 kg | 35 kg binder, 15 kg graphite |
| Budgeted passing 35 wt% | 27.34 kg | 17.77 kg | 9.57 kg | 35 kg binder, 15 kg graphite |
| Passing 40 wt% | 28.14 kg | 16.89 kg | 11.26 kg | 35 kg binder, **16 kg graphite** |

These allowances still assume the 40% collector passes. If the final thickness changes, recalculate; a 2 mm wearing layer approximately doubles its material requirement. Filled epoxy at 1 mm is a thin coating, not a heavy-duty screed. Verify actual caster/point loads before choosing thickness and allow rack load spreading if needed.

## Cost table and affordability

**Graphite source checked online:** [Pourian's graphite catalog](https://www.metal-powder.ir/%DA%AF%D8%B1%D8%A7%D9%81%DB%8C%D8%AA) displays **450,000 IRT per 1 kg**, nominal −45 μm and ≥99.9% purity. Availability, flake morphology and price at purchase require confirmation. This is a retail reference, not a bulk quotation. Other rates below are explicit **unquoted planning allowances**, including the 350,000 IRT/kg matched A+B binder rate. No claim is made that those prices have been verified locally. Use this table to compare small-volume quotes; cheap metallurgical carbon is not automatically an equivalent filler.

| Item | Purchase quantity | Unit IRT | Line IRT | Basis |
| --- | ---: | ---: | ---: | --- |
| Raw unfilled epoxy A+B | 35 kg | 350,000 | 12,250,000 | Allowance; matched resin + hardener |
| Fine graphite | 15 kg | 450,000 | 6,750,000 | Displayed retail reference above |
| Dry quartz for repairs only | 5 kg | 50,000 | 250,000 | Allowance |
| Copper tape / foil | 50 m | 45,000 | 2,250,000 | Allowance |
| DIY terminal assemblies | 2 sets | 250,000 | 500,000 | Allowance; plates, lugs, bolts, covers |
| Bonding cable | 15 m | 120,000 | 1,800,000 | Allowance |
| Protective conduit | 15 m | 40,000 | 600,000 | Allowance |
| Joint sealant, backing and bridge materials | 1 lot | 800,000 | 800,000 | Allowance |
| Mixing/application tools and PPE | 1 lot | 1,800,000 | 1,800,000 | Allowance; mixer hire, scales, buckets, tools |
| Grinder and extraction hire | 1 job | 2,500,000 | 2,500,000 | Allowance; owner preparation labor |
| Substrate moisture and adhesion tests | 1 job | 2,500,000 | 2,500,000 | Allowance |
| Borrowed/hired ESD tester and pilot walking test | 1 job | 2,500,000 | 2,500,000 | Allowance; separate from final commissioning |
| Electrician connection and continuity | 1 visit | 2,000,000 | 2,000,000 | Allowance |
| Final ESD commissioning | 1 job | 3,500,000 | 3,500,000 | Allowance; calibrated equipment and report |
| Freight and local transport | 1 lot | 1,000,000 | 1,000,000 | Allowance |
| Initial ESD footwear | 2 pairs | 1,000,000 | 2,000,000 | Allowance; qualify with floor |
| Residue-free approved cleaner | 1 lot | 500,000 | 500,000 | Allowance |
| **Base cash estimate** | | | **43,500,000** | Owner mixing/application labor unpaid |
| **20% contingency** | | | **8,700,000** | Minor variance; not major remediation |
| **DIY planning total** | | | **52,200,000 IRT** | **2,900,000 IRT/m²** |

Raw coating ingredients (binder, graphite and repair quartz) cost **19,250,000 IRT** in this model, approximately **1,069,444 IRT/m²** including repair/trial reserve and packaging surplus. With copper and bonding materials, material cost is higher. A cheaper bulk graphite or binder quote reduces cost linearly: every 100,000 IRT/kg reduction saves **1.5 million IRT for graphite**, or **3.5 million IRT for binder**, before contingency.

Optional hired preparation/application labor: allow **6,500,000 IRT**, making the base 50,000,000 IRT and total with 20% contingency **60,000,000 IRT**. Owner time is approximately **40–56 hours**, excluding cure waits, rack relocation and repeat formulation rounds. Buying test instruments outright is not budgeted; borrowing/hiring or sharing a lab avoids that capital expense.

Compared with the previous 81,000,000 IRT proposal, the owner-applied planning total is **28,800,000 IRT lower (35.6%)**, but that is not a like-for-like proven saving: labor scope and formulation risk differ. Additional trials or remediation can consume the difference. We save on specialty coatings and fabricated hardware while retaining measurement.

Exclusions: tax if charged, rack relocation/downtime, weak mosaic replacement, full-room levelling, moisture barrier, building earthing repairs, laboratory abrasion/slip services beyond the provisional pilot checks, repeated trial rounds, additional footwear and recurring verification. The total is an estimate, not a purchase quote.

## Step-by-step room implementation

1. **Measure and inspect.** Confirm area, tile/mosaic composition, slab condition, hollow or loose units, moisture, cracks and joint locations. Locate services before any drilling. Fix loose units and weak bedding. Establish equipment relocation and load requirements; tape and coatings need continuous access under racks.
2. **Qualify the raw formulation first.** Execute the batch and mock-up procedure above. Select a reproducible passing recipe and record actual wet-film thickness, cured thickness, consumption, cure time, mixing method and tools. Do not extrapolate a favorable powder test to a finished floor.
3. **Empty and contain the room.** Relocate equipment under the operations plan, isolate cooling air paths from grinding dust, and ventilate the work. Use dust-extracted grinding, eye/skin protection and respiratory protection selected for the actual products. No loose graphite handling next to live electronics.
4. **Prepare and check moisture.** Remove oil, wax and polish; diamond-grind to a clean, dull, profiled surface and vacuum. Test moisture by the chosen binder's accepted method, including the underlying slab; a dry tile face is insufficient. Use its stated moisture limit and stop for mitigation if exceeded. Maintain the binder's application climate and at least 3°C surface margin above dew point as a project control. Conduct the adhesion trial on the prepared mosaic.
5. **Repair and level.** Fill static defects with the trialled epoxy/quartz mortar. Respect its priming/cure sequence. Preserve movement joints with compatible sealant and electrical bridging details. Make the floor flat enough for thin coatings; do not fill hollows with excess conductive wearing mixture.
6. **Apply ordinary epoxy bonding primer.** Mix neat A+B at its correct weight ratio, spread at the qualified rate, nominally 0.30 kg/m² net, and eliminate pinholes. Record start/finish and recoat windows from the actual binder data. If porosity needs a second coat, revise quantities. Do not dilute it to imitate a commercial solvent primer.
7. **Install collectors and homemade terminals.** Once primer condition is suitable, press foil to the agreed layout; create soldered or clamped continuous junctions. Recess/profile terminal plates, make robust copper-to-copper contacts and keep accessible connection faces protected. Check copper circuit continuity using a suitable low-resistance meter before burying it. The electrician prepares protected routes to the common building bar.
8. **Apply the 40% graphite collector coat.** Use the qualified dispersion and A+B ratio. Target 0.25 mm cured thickness with approximately 6.40 kg net mixture over 18 m². Verify continuous coverage over every collector, without dry graphite islands or protruding foil. After the qualified cure period, measure its connection to the bonding system; remedy failed regions before coating over them.
9. **Apply the selected wearing formula.** Budgeted 35% recipe: about 24.85 kg net compound at 1.0 mm; the purchase calculation includes loss separately. Work in small timed batches with separate mixing/spreading roles to keep a wet edge. Check thickness rather than emptying all stock onto the floor. Use the pilot's tools and technique. Keep batch records. No insulating clear sealer, pigmented paint or wax above this layer.
10. **Cure and finish the connections.** Follow the raw binder's temperature-dependent cure and full-load release; graphite addition does not justify a shorter schedule. Protect from dust, water, condensation and premature loading. The electrician completes accessible terminal connections, verifies both routes and fits labels/covers. Require a full-cure hardness assessment and load release before rack return.
11. **Commission the actual room.** Measure at least **10 distributed surface-to-ground locations** plus representative point-to-point pairs, using the applicable floor test method (ANSI/ESD STM7.1 or IEC 61340-4-1), calibrated resistance meter and standard electrodes. Include doorway, corners, collector-distant points, batch boundaries and repairs. Record voltage, RH, temperature, locations, cleaning and all failures/retests. Verify actual personnel footwear resistance and walking voltage as specified above. Ordinary multimeter readings or silver-painted laboratory coupons are not substitutes for these installed-surface tests.
12. **Return racks and establish maintenance.** After electrical, mechanical and full-load acceptance, return equipment with suitable load spreading/handling. Retain rack/circuit protective earth and grounded workbench/wrist-strap arrangements for exposed electronics. Use residue-free cleaning that passed the pilot. Recheck resistance after cleaning changes, repairs or abnormal wear; inspect for black transfer and dust. Set an initial quarterly floor/bonding verification schedule, adjusted by the ESD specialist, and qualify replacement footwear.

| Phase | Owner effort allowance | Elapsed planning allowance |
| --- | ---: | --- |
| Material selection, batches and pilot | 12–16 h | About 1–2 weeks with cure and test booking |
| Room preparation, repairs and collectors | 16–24 h | About 2–4 working days plus repair cure |
| Mixing and application | 8–12 h | About 2–3 days, governed by actual recoat windows |
| Commissioning coordination and records | 4 h | After full cure and specialist availability |
| **Total** | **40–56 h** | **About 2–4 weeks after materials arrive**, longer for failed trials or remediation |

Do not borrow the factory ESD product's pot life, humidity limits or four-day cure for this formulation. The raw binder data and our qualified panels determine those values. The recipe can be made affordably; successful electrical and mechanical tests determine whether the resulting floor is ready for the datacenter.

## Answers to the meter, footwear, wire and tape questions

### Can an ordinary multimeter prove that the finished floor meets ESD standards?

**No. It can help find wiring faults, but it cannot establish ESD compliance.** Use its resistance/continuity function on an isolated, de-energized copper network to check for broken tape joints, disconnected wires or gross changes. Account for test-lead resistance. A continuity buzzer on copper does not test the coating. Do not measure resistance on energized circuits or lift a building protective-earth connection while equipment is operating.

Floor qualification needs a calibrated high-resistance meter with the specified test voltages, electrodes, positioning and timing. An ordinary multimeter usually has a low test voltage and insufficient high-resistance range; sharp probes also give an uncontrolled contact area. An “OL” reading can mean the meter is out of range, not necessarily that the floor fails. A low reading from improvised probes does not establish a pass. [EOS/ESD measurement-equipment guidance](https://www.esda.org/esd-overview/esd-fundamentals/part-4-training-and-auditing/) describes 10/100 V measurement capability and high-resistance ranges.

| Measurement | Appropriate equipment / procedure | What it establishes |
| --- | --- | --- |
| Copper tape and terminal continuity | Low-resistance instrument; a multimeter can screen for opens | Connection integrity, not floor ESD performance |
| Floor-to-ground and point-to-point resistance | ESD resistance meter with standard weighted conductive electrodes, following STM7.1 or applicable IEC method | Electrical behavior of the installed surface |
| Person through footwear/floor to ground | Meter and hand electrode configured for STM97.1 or applicable IEC method | Actual personnel grounding path |
| Walking body voltage | Body-voltage measuring system meeting STM97.2 or applicable IEC requirements | Charge generated during walking; both resistance and this test must pass |

For the ANSI floor resistance procedure, the cited [EOS/ESD test-voltage explanation](https://forum.esda.org/t/tr53-test-voltage-for-surface-rtg-measurements/1018) describes 10 V below 10⁶ Ω and 100 V at/above 10⁶ Ω. Follow the chosen current method for switching, dwell time and electrode geometry. A generic insulation tester fixed at 250/500/1,000 V is not a substitute; a suitable instrument must support the required ESD settings and range. Never improvise a person test with a high-voltage insulation tester. Borrow/hire the ESD instruments or commission a measurement service, as already budgeted.

### What is an ESD resistance meter, and why is it different from a multimeter?

An **ESD resistance meter is a high-resistance measuring instrument designed for static-control materials**. It applies a specified voltage, measures the very small resulting current, and calculates resistance. It uses the same electrical principle as an ordinary ohmmeter; there is no separate kind of “ESD resistance.” The difference is its measurement capability and the standardized test arrangement.

A typical floor-testing setup uses one weighted conductive electrode on the floor and a lead to the verified grounding point for floor-to-ground resistance. For point-to-point resistance, use two specified electrodes on the surface. Electrode dimensions, contact material, force, separation, test voltage and measurement time follow the selected test method. Do not confuse resistance in ohms with a sheet-resistivity indication in ohms per square.

**A normal multimeter can measure resistance, including some graphite/epoxy readings.** My earlier statement concerns proving compliance, not an inability to measure any resistance. Four differences matter:

| Difference | Why it matters for this floor |
| --- | --- |
| Resistance range | ESD qualification can involve hundreds of megohms, up to a 1 GΩ limit. A meter whose maximum is 40 MΩ cannot distinguish an acceptable 100 MΩ path from an unacceptable 2 GΩ path: both may display OL. Actual ranges vary by model. |
| Applied voltage | Ordinary resistance modes use a low test voltage/current determined by the meter. The floor method specifies 10/100 V conditions. Filled polymers and their contacts need not behave like an ideal fixed resistor; results at different voltages may differ. |
| Contact and geometry | Sharp probes sample tiny, pressure-dependent spots. Specified weighted electrodes provide controlled contact. Finding one exposed graphite particle does not characterize the floor surface. |
| Test procedure | Calibration, timing, conditioning, humidity, locations and records are part of the measurement. A meter alone does not supply these, or the separate walking-voltage test. |

For a concrete range example, [Fluke lists 40 MΩ for its 117 multimeter](https://www.fluke.com/en-us/product/electrical-testing/digital-multimeters/fluke-117). This is an example, not a claim about every multimeter. [EOS/ESD instrument guidance](https://www.esda.org/esd-overview/esd-fundamentals/part-4-training-and-auditing/) describes a high-resistance meter with 10/100 V capability, suitable electrodes and a broad measuring range.

**Example using Ohm's law:** at 100 MΩ, 100 V produces 1 μA; 1 V produces only 10 nA. At 1 GΩ, 100 V produces 100 nA. Measuring such small currents reliably requires suitable input circuitry, leads and control of leakage. These arithmetic examples explain instrument demands; they are not instructions to build a mains-powered test circuit.

An ordinary meter is useful for copper continuity and rough comparative screening when the reading is inside its specified range. Record its model, range and probe arrangement, but label the result “screening,” not an ESD pass. A specialist laboratory instrument could also perform the resistance measurement if it meets the chosen method; the instrument's label is less important than its verified specifications. For affordable qualification, borrow or hire an appropriate meter and electrodes, then arrange the separate person/footwear walking-voltage test already included in the plan.

### What are ESD footwear and affordable alternatives?

**ESD footwear provides a controlled path from the wearer, through the shoe sole, to the ESD floor.** Ordinary insulating rubber soles may leave a person electrically isolated even on a good floor. ESD shoes are designed and tested for charge control; a generic “antistatic” description alone does not qualify a shoe/floor combination. ESD footwear is not electrical-insulating footwear for live electrical work.

A lower-cost alternative is a reusable heel or full-foot grounder fitted to each ordinary shoe. The conductive tab is placed inside the shoe in contact with the wearer according to its instructions, while the exterior conductive pad contacts the floor. **Wear one on each foot** so contact remains available as the other foot lifts. Do not substitute bare copper straps. [Desco's foot-grounder guide](https://www.desco.com/PDF/Desco_FootGrounder_Selection_Chart.pdf) explains the inside tab and use on both feet.

Qualify the actual footwear or grounders with our cured floor: person/system resistance <10⁹ Ω and walking voltage <100 V. Keep soles clean, verify grounders before use with a suitable footwear tester, and repeat qualification after changing footwear types. The current budget includes two pairs of ESD shoes; replacing those with grounders requires local prices and the same system tests, not an assumed saving. [EOS/ESD personnel-grounding requirements](https://www.esda.org/esd-overview/esd-fundamentals/part-3-basic-esd-control-procedures-and-materials/).

### What wire size should connect the floor terminals?

For this small room, **retain the planning choice of one 4 mm² insulated green/yellow copper conductor from each of the two floor terminals to the common verified bonding bar**, protected in conduit, with properly crimped compatible lugs. The allowance is 15 m combined, not 15 m per point. The size is conductor cross-sectional area, not diameter. A solid circular 4 mm² conductor has an equivalent diameter of about 2.26 mm; stranded cable is sold by total copper area.

This is a practical preliminary size for the floor connections, **not a universal ESD or Iranian code requirement**. The [Sika conductive-primer installation sheet](https://usa.sika.com/content/dam/dms/us01/4/sikafloor_-220_wconductive.pdf) gives an example using No. 10 or No. 12 copper wire. This supports using robust copper connections, but does not approve our site or DIY assembly. [Schneider's protective-conductor guidance](https://www.electrical-installation.org/enwiki/Sizing_of_protective_earthing_conductor) gives mechanical minima of 2.5 mm² protected or 4 mm² unprotected for a separate PE conductor, alongside fault-duty sizing; those PE rules are not themselves an ESD-floor cable specification.

The electrician must determine the conductor's function, local requirements, terminal capacity, fault exposure and protective arrangements, and increase the size if those require it. Do not use this 4 mm² floor lead as the main building earthing conductor or rack PE. There is no benefit in calculating its size from tiny normal static discharge current alone: robustness, reliable connections and electrical safety matter. Tape and terminal contacts must also be checked; a larger wire cannot correct a poor coating-to-copper interface.

### Are a perimeter and two center lines sufficient, or is 15–25 cm spacing required?

**The perimeter plus cross is a reasonable trial layout for a continuously conductive collector layer; its sufficiency for our DIY coating has not been demonstrated.** I cannot guarantee it before measurement. Our earlier sparse layout is now explicitly conditional on the full-stack pilot and installed-floor results. The copper is a collector network: the graphite-filled layer must carry charge from the surface to that network. Dense tape reduces the lateral travel distance but cannot repair an insulating top surface, missing through-thickness conduction, brittle coating or poor grounding.

I double-checked manufacturer instructions as evidence about layout principles, not as an instruction to purchase their coatings:

| Primary reference | What it actually says | What can be concluded |
| --- | --- | --- |
| [Flowcrete Flowfresh application manual, June 2022, printed page 62](https://www.flowcrete.eu/media/25797/fc_aig_flowfresh_application_manual_int_20220602.pdf) | Its tested ESD system uses a conductive primer, copper about **150 mm from borders**, grids of **8 × 8 m or at most 10 × 10 m**, and no floor point more than 5 m from tape. | The 150 mm is a border offset, **not 150 mm grid spacing**. Its performance cannot be transferred directly to our homemade collector. |
| [Sika ESD/ECF earthing brochure, printed page 9](https://grc.sika.com/dam/dms/gr01/a/Brochure_Sika%20Technology_Concepts_for%20ESD_Conductive%20Flooring.pdf) | Describes grounding-point distances on a metre scale and additional copper for longer distances. | Dense 15–25 cm tape spacing is not universal across conductive resin systems. Our formulation still needs its own tests. |

**Decision for affordability:** first trial the perimeter/cross with the qualified conductive collector. If it passes with operating margin at the largest tape-free spans, retain it. If readings rise excessively between collectors, compare 50 cm and 25 cm grids on the same full stack before installing the room. A 25 cm grid is a conservative optional layout if we choose to spend more copper; 15 cm is not established as necessary by the sources reviewed. Do not treat either dense option as an automatic ESD pass.

A 1 m² pilot alone cannot reproduce the sparse room layout's approximately 1 m maximum distance to tape. Before choosing sparse tape, additionally test a **2.25 × 2.0 m full-stack panel/bay** or an equivalent representative floor trial with collectors around its boundary, measuring its center and remote positions. In the room, the cross creates four bays of that size; each bay center is approximately 1 m from the nearest idealized tape centerline. Account for actual wall offsets and tape width. If this larger trial is newly built, it requires extra materials beyond the original 1 m² pilot reserve; use measured coverage and add its test cost. Alternatively make and qualify one actual room bay first, then decide whether to extend or rework it, following the binder's recoat/joint procedures.

| Layout for 4.5 × 4 m, idealized tape at boundaries | Maximum geometric distance to a tape line | Net tape excluding terminal tails | Tape with 2 m tails and 10% allowance | 50 m rolls / purchase | Tape cost at 45,000 IRT/m |
| --- | ---: | ---: | ---: | ---: | ---: |
| Perimeter + two crossed centers, budget baseline | About 1 m | 25.5 m | 30.25 m | 1 / 50 m | 2,250,000 |
| Grid at ≤50 cm | 25 cm | 80.5 m | 90.75 m | 2 / 100 m | 4,500,000 |
| Grid at ≤25 cm | 12.5 cm | 152.5 m | 169.95 m | 4 / 200 m | 9,000,000 |
| Grid at ≤15 cm | 7.5 cm | 250.0 m | 277.20 m | 6 / 300 m | 13,500,000 |

For a complete boundary-to-boundary grid with maximum pitch `s`, net length is `W × [ceil(L/s)+1] + L × [ceil(W/s)+1]`; shortened edge cells are allowed. A real inset perimeter has different lengths and small outside strips: recalculate from its actual drawing. These cost comparisons include extra tape purchase only; dense grids also add joint-making time and inspection. Keep every intersection electrically continuous by the selected qualified joint method.

| Layout option | Revised base cash, tape-only adjustment | Revised total including 20% contingency |
| --- | ---: | ---: |
| Sparse baseline, if validated | 43,500,000 IRT | 52,200,000 IRT |
| 50 cm grid | 45,750,000 IRT | 54,900,000 IRT |
| 25 cm grid | 50,250,000 IRT | 60,300,000 IRT |
| 15 cm grid | 54,750,000 IRT | 65,700,000 IRT |

The additional larger-span qualification, any extra labor and remediation are excluded from these tape-only adjustments. Test the cured collector before the wearing coat and test the final surface at bay centers, seams, doorways and repairs; record all readings. Select pitch from passing results and cost, not from confidence in the sketch.

<div style="page-break-before: always;"></div>

## One-page project summary

**Purpose:** finish the 18 m² Hormuz mosaic floor using ordinary raw epoxy, graphite and copper collectors. Make the conductive layers ourselves. The proposed formulations remain trial recipes until the actual materials and installed surface pass electrical and mechanical checks.

| Item | Working design / quantity |
| --- | --- |
| Layer sequence | Prepared/repaired mosaic → neat epoxy primer → copper collectors → graphite collector → graphite wearing layer |
| Primer | About 0.30 kg/m² neat A+B |
| Collector | Trial **40 wt% graphite**, 0.25 mm cured thickness |
| Wearing layer | Screen 30/35/40%; budget **35 wt% graphite**, 1.0 mm cured thickness |
| Purchase allowance | **35 kg matched A+B binder, 15 kg fine graphite, 5 kg repair quartz**; no quartz in conductive layers |
| Grounding | **Two terminals, each with protected 4 mm² copper to the common bonding bar**; 15 m cable combined, subject to electrician review |
| Copper baseline | Perimeter/cross, **50 m roll**, conditional on largest-span validation |
| Denser options | 50 cm: 100 m purchase; 25 cm: 200 m; 15 cm: 300 m; all still require tests |
| Cash estimate | Sparse baseline **52.2 million IRT** including 20% contingency; tape-only 25 cm alternative **60.3 million IRT** |

**Recipe:** graphite percentage is of **A+B+graphite total mass**. For 1 kg total at 35%, use 650 g A+B and 350 g graphite; at 40%, use 600 g A+B and 400 g graphite. Split A+B using its own supplier's weight ratio. Disperse powder into A, add the correct B, remix and spread within qualified working time. Keep one powder grade/lot and repeatable mixing; add no solvent or insulating topcoat.

**Implementation:** make repeat trial batches; check cure, adhesion, wear, slip and electrical behavior. Validate the largest tape-free span before selecting pitch. Empty the room, grind and vacuum, verify moisture, repair, prime, install/check copper and terminals, apply/test collector, apply wearing layer, fully cure and commission before returning racks. Follow the raw binder's actual cure and recoat instructions. Plan about 2–4 weeks, longer for repeat trials or remediation.

**Verification:** an ordinary multimeter can screen copper continuity; it cannot prove floor ESD compliance. Borrow/hire a calibrated **10/100 V ESD resistance meter with standard electrodes** and a suitable walking-voltage system. Measure at least 10 distributed floor-to-ground points plus point-to-point tests, including places farthest from tape. Preferred project floor range is 10⁶–10⁸ Ω; qualify the actual person/footwear/floor at **<10⁹ Ω and walking voltage <100 V**. Use ESD shoes or tested grounders on both feet; ordinary insulating shoes may defeat the floor.

**Limits and upkeep:** prices are planning allowances except the cited graphite retail reference. Additional large-span trial material/testing, relocation, major repairs and tax are excluded. Dense copper cannot fix insulating or shedding epoxy. Keep rack PE, clean without wax, inspect wear and recheck after repairs, cleaner or footwear changes.
