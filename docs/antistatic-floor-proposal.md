# Antistatic epoxy finish over the Hormuz mosaic floor

Prepared 13 October 2026. Design basis: the **4.5 m × 4 m = 18 m² room** in the [airflow proposal](airflow-proposal.md), fully emptied before coating. Currency: **Iranian tomans (IRT); 10 IRR = 1 IRT**. Confirm actual dimensions, mosaic type, moisture and supplier availability before procurement. This is a preliminary design and estimate; it does not certify the installed floor.

## Recommended construction

Use a compatible, factory-formulated ESD flooring system over sound, mechanically prepared mosaic. The sequence is **mosaic → repair/levelling as needed → epoxy bonding primer → copper tape and grounding terminals → conductive primer → ESD epoxy wearing layer**. Both epoxy components (resin and hardener) are included in the quantities below. The finish is opaque and covers the mosaic pattern.

The ordinary bonding primer provides adhesion; the separate conductive primer distributes charge to the copper tape. The wearing layer must itself provide a conductive path through its thickness. Copper tape beneath ordinary insulating epoxy does not make its surface antistatic.

For a reference specification, use the [Sika MultiDur ES-56 ESD system](https://gbr.sika.com/en/construction/flooring/anti-static-esd-systems/sikafloor-multidures-56esd.html): Sikafloor-150/151 bonding primer, 220 W Conductive, compatible earthing kit, and 2350 ESD wearing resin with approved quartz. Reference thickness is approximately 1.5–2 mm. A locally available equivalent is acceptable with documented substrate compatibility, complete layer specification, consumption, electrical performance and installation instructions. Do not interchange products merely because all are described as epoxy.

**Loose graphite powder: 0 kg in the recommended installation.** Buy conductive primer and ESD resin with their conductive additives already formulated. A universal graphite percentage cannot be specified: grade, particle size, dispersion, loading and cured thickness affect resistance, adhesion and strength. Do not add graphite to a proprietary coating or change its hardener ratio. If using a supplier's graphite-based system, require its written additive grade and dosage, then calculate `graphite mass = specified dosage × specified resin mass`; the supplier must define whether dosage is relative to resin, A+B or total compound. Qualify a cured trial panel for adhesion and ESD performance before ordering room quantities. A DIY mixture remains an experimental alternative with no reliable room-scale quantity or certified performance established here.

## Grounding layout

Budget a perimeter loop, one lengthwise strip and one widthwise strip, connected through two protected terminal points near opposite corners. This is a conservative estimating layout, not a requirement for every conductive-primer system. The supplier may approve shorter collector strips. Tape dimensions and joints must follow the chosen system; allow 10 mm wide, conductive-adhesive copper tape provisionally. Ordinary craft tape may have insulating adhesive.

```text
                 4.5 m
       G1 ┌──────────┬──────────┐
          │          │          │
      4 m ├──────────┼──────────┤
          │          │          │
          └──────────┴──────────┘ G2
       G1 and G2: accessible grounding terminals
       Lines: buried copper tape, covered by conductive primer
```

Connect both points by protected, labeled conductors to the same verified building bonding network. Allow **15 m total 4 mm² green/yellow copper** for two routes; actual size and route are for the electrician to confirm. Use the [existing earthing proposal](../assets/park/earthing-proposal.md) for building earth integration. Do not use neutral, plumbing or a separate isolated earth rod. Floor tape does not replace rack/circuit protective earth. The electrician determines connection details and whether any resistance device is prescribed by the selected system; do not insert an arbitrary resistor into protective bonding.

Use system terminals with mechanically secured tape contacts, accessible lugs and protective covers. Tape intersections require supplier-approved electrically continuous joints; adhesive overlap alone is insufficient unless qualified. The [Sika conductive kit instructions](https://gbr.sika.com/en/construction/flooring/ancillaries/sikafloor-conductiveset.html) describe clamped strips, protected studs and final cable connection after cure. Locate anchors clear of concealed services; preserve movement joints and use an approved flexible electrical bridge where separate floor sections need continuity.

## Material quantities and scaling

These are planning quantities for **all 18 m² including under racks**, with 10% application loss before purchase rounding. Purchase amounts are minimum budgeting allowances, not confirmed commercial pack sizes. Obtain sealed A+B kit sizes and round up again if necessary; the grounding kit may be sold in a larger multipack. Spare material is not a reason to apply thicker coats.

| Material | Calculation / basis | With loss | Budget purchase |
| --- | --- | ---: | ---: |
| Epoxy bonding primer, A+B | 18 × 0.50 kg/m² | 9.90 kg | **10 kg** |
| Repair mortar / grout filler | Provisional minor static repairs | Site dependent | **5 kg** |
| Conductive primer, A+B | 18 × 0.10 kg/m² | 1.98 kg | **2.5 kg** |
| Wearing mixture, resin + quartz | 18 × 2.50 kg/m² | 49.50 kg total | Split below |
| ESD wearing resin, A+B | Mixture ÷ 1.20 | 41.25 kg | **45 kg** |
| Dry approved quartz, 0.1–0.3 mm | 20% of A+B mass | 8.25 kg | **10 kg** |
| Loose graphite | Factory-formulated system | 0 kg | **0 kg** |
| Copper tape | 2(4.5 + 4) + 4.5 + 4 + 2 m terminal allowance | 30.25 m | **50 m roll** |
| Grounding terminals | Two separately connected points | 2 points | **2 complete points** |
| Bonding cable / protective conduit | Two site routes including slack | 15 m each assumed | **15 m each** |

The [reference system consumption table](https://gbr.sika.com/en/construction/flooring/anti-static-esd-systems/sikafloor-multidures-56esd.html) specifies bonding primer 0.3–0.5 kg/m², conductive primer 0.08–0.10 kg/m², and wearing mixture up to 2.5 kg/m² with 20% quartz, with at least two earth connections per room. Here 20% is interpreted as filler relative to A+B; confirm this basis with the supplying manufacturer. At net 2.5 kg/m², resin consumption is 2.083 kg/m² and quartz is 0.417 kg/m². Apply according to the approved thickness and coverage, not all purchased material.

For another room, replace 18 with measured coated area `A`, multiply each coating rate by `A × 1.10`, and round to available complete kits. For this tape arrangement use `[3(L+W)+2] × 1.10` metres. Repair, levelling, cable, terminals and mobilization do not scale simply with area. If racks remain, measure accessible area and allow later treatment of isolated patches; this baseline assumes relocation and continuous coverage.

The 5 kg repair allowance does **not** cover a full-room scratch coat. If preparation exposes deep joints, loose mosaic or uneven levels, survey and price a compatible levelling layer separately. Estimate it as `area × average thickness in mm × manufacturer's kg/m²/mm`, plus loss; do not use the wearing layer to fill hollows.

## Cost table

All unit prices below are **unquoted planning allowances in IRT**, set for this estimate rather than researched retail offers. They are not Sika quotations or confirmed Ilam prices. Use the [editable CSV](antistatic-floor-estimate.csv) to replace them with written local quotes, exact pack sizes and tax. No foreign-exchange assumption is needed.

| Item | Purchase quantity | Unit IRT | Line IRT |
| --- | ---: | ---: | ---: |
| Epoxy bonding primer A+B | 10 kg | 350,000 | 3,500,000 |
| Epoxy repair mortar / grout filler | 5 kg | 300,000 | 1,500,000 |
| Conductive primer A+B | 2.5 kg | 1,200,000 | 3,000,000 |
| ESD epoxy wearing resin A+B | 45 kg | 650,000 | 29,250,000 |
| Approved dry quartz 0.1–0.3 mm | 10 kg | 50,000 | 500,000 |
| Loose graphite powder | 0 kg | 0 | 0 |
| Conductive-adhesive copper tape | 50 m | 45,000 | 2,250,000 |
| Compatible grounding terminal kit | 2 points | 750,000 | 1,500,000 |
| Protected green/yellow copper bonding cable | 15 m | 120,000 | 1,800,000 |
| Conduit / protective trunking | 15 m | 40,000 | 600,000 |
| Lugs labels and terminal covers | 1 lot | 500,000 | 500,000 |
| Movement-joint sealant and backing | 1 lot | 800,000 | 800,000 |
| Dust-extracted grinding and vacuum hire | 1 job | 2,500,000 | 2,500,000 |
| Application tools and PPE | 1 lot | 1,800,000 | 1,800,000 |
| Substrate survey moisture and adhesion tests | 1 visit | 2,500,000 | 2,500,000 |
| Preparation and coating crew | 1 job | 6,500,000 | 6,500,000 |
| Electrician bonding and continuity verification | 1 visit | 2,000,000 | 2,000,000 |
| ESD commissioning and written test report | 1 job | 3,500,000 | 3,500,000 |
| Freight and local transport | 1 lot | 1,000,000 | 1,000,000 |
| Initial ESD footwear | 2 pairs | 1,000,000 | 2,000,000 |
| Approved residue-free cleaning supplies | 1 lot | 500,000 | 500,000 |
| **Materials subtotal, including footwear and cleaner** | | | **47,700,000** |
| **Tools, labor and services subtotal** | | | **19,800,000** |
| **Base cash estimate** | | | **67,500,000** |
| **20% contingency** | | | **13,500,000** |
| **Planning budget** | | | **81,000,000 IRT** |

Budget including contingency is **4,500,000 IRT/m²**. As a market cross-check, [Armelat's Persian indicative table](https://www.armelat.com/blog/detail/epoxy/) lists antistatic epoxy at 1.7–2.7 million IRT/m² for 2–3 mm, and preparation at 120,000–350,000 IRT/m². Those advertised rates do not establish equivalent material, small-job charges, grounding or ESD test scope. Do not add an advertised turnkey rate to this itemized budget; that would double count work.

Excluded: VAT if charged, rack/server relocation and downtime, major tile replacement, full levelling, moisture mitigation, new earthing infrastructure, thresholds/skirting, additional footwear, and periodic testing after handover. Contingency does not establish an adequate allowance for these excluded works.

## Step-by-step installation

1. **Survey and choose the complete system.** Measure floor area and cable routes, identify cement mosaic/terrazzo versus glazed tile, tap-check for loose or hollow units, and map cracks and movement joints. Obtain written manufacturer acceptance for coating this mosaic and the agreed mechanical/electrical criteria. Make a representative trial area using the actual products; allow it to cure and verify adhesion before proceeding.
2. **Empty and isolate the room.** Plan rack relocation and downtime with operations. Cover/isolate adjoining equipment and prevent dust entering cooling ducts. Arrange dust extraction, ventilation and access control. Use epoxy-resistant gloves and eye protection, and respiratory protection selected for grinding dust and each product's safety sheet. Do not dry-sweep or spread conductive powders near electronics. An experienced coating crew applies the system; an electrician handles building bonding.
3. **Confirm moisture and climate.** Test the underlying substrate as well as the surface; a dry tile face does not establish a dry slab. Use the manufacturer's accepted moisture method. For the reference wearing product, the limit is <4% by weight using its stated method, with no rising moisture. Maintain 15–30°C and a substrate at least 3°C above dew point. Use the strictest humidity limit among all layers (the cited conductive primer limits RH to 75%). Stop for moisture mitigation or drying when results fail; do not seal an actively damp mosaic. [Wearing-product data](https://gbr.sika.com/en/construction/flooring/anti-static-esd-systems/sikafloor-2350-esd.html), [conductive-primer data](https://ind.sika.com/en/construction/flooring/electro-static-dischargeesdprotectionandcontrol/conductive-flooring/sikafloor-220-wconductive.html).
4. **Prepare the mosaic mechanically.** Remove wax, polish, grease and cleaning residue. Diamond-grind with extraction to remove gloss and produce the supplier's required profile; vacuum thoroughly. Replace unsound units and stabilize the substrate. Acid washing alone is not preparation. Verify trial-area adhesion against the supplier's criterion; sound cementitious substrates for the cited conductive primer require at least 1.5 MPa tensile strength. Preserve active joints. [Conductive-primer preparation guidance](https://ind.sika.com/en/construction/flooring/electro-static-dischargeesdprotectionandcontrol/conductive-flooring/sikafloor-220-wconductive.html).
5. **Repair and level.** Fill static cracks, missing grout and holes with compatible epoxy mortar, following its priming sequence. Use a separate approved scratch/levelling coat if necessary. Allow cure and reprepare as instructed. Leave movement joints functioning; obtain a system detail for edges and conductive bridges.
6. **Apply the bonding primer.** Mix complete A+B kits at the product's specified ratio, with the specified mixer and mixing time. Apply a uniform coat at the approved coverage, allowing about 9 kg net at the selected 0.5 kg/m² rate. Eliminate pinholes; absorbent areas may need more primer and revised quantities. Record application time, temperature and recoat deadline. Do not broadcast sand on the final receiving surface unless the conductive-system instructions require it.
7. **Install tape and terminal assemblies.** After the bonding primer reaches the specified condition, lay and press the approved tape to the agreed plan. Secure connections mechanically with compatible terminal kits. Have the electrician verify continuity across tape junctions and prepare both protected routes to the common bonding bar. Keep terminal contact surfaces masked during coating, accessible after cure and protected from traffic.
8. **Apply the conductive primer and test it.** Mix at its own A:B ratio and roll a continuous film over the prepared surface and collectors at 0.08–0.10 kg/m². About 1.8 kg is the net maximum-rate quantity for 18 m². Let it cure, then test continuity and resistance to the groundable points against the manufacturer's intermediate-layer limit. Repair failures before covering. For the cited product, the 20°C overcoat window is approximately 17 hours to 5 days; use the actual supplied data sheet. [Conductive-primer application data](https://ind.sika.com/en/construction/flooring/electro-static-dischargeesdprotectionandcontrol/conductive-flooring/sikafloor-220-wconductive.html).
9. **Apply the formulated ESD epoxy.** Keep a wet edge with separate mixing and spreading roles. For reference 2350 ESD, A:B is 82:18 by weight; mix using its prescribed sequence, add only the approved dry quartz, transfer to a clean container and remix. For each 10 kg A+B, the estimating filler quantity is 2 kg. Spread evenly with the prescribed serrated tool and spike-roll within working time. Net room mixture is 45 kg (37.5 kg resin plus 7.5 kg quartz), maximum 2.5 kg/m². At 20°C the reference pot life is about 25 minutes; select batch sizes the crew can finish in time. Add no graphite, solvent, extra hardener or unapproved filler. [Wearing-product mixing and application instructions](https://gbr.sika.com/en/construction/flooring/anti-static-esd-systems/sikafloor-2350-esd.html).
10. **Cure and complete bonding.** Keep the floor free of dust, water, condensation and traffic. The reference wearing product allows foot traffic after about 24 hours, light traffic after 48 hours and full cure after four days at 20°C; colder conditions extend this. Wait for the supplier's full-load release before returning racks or rolling heavy equipment. Remove terminal masking and have the electrician complete and verify both final bonding connections. Do not apply ordinary clear epoxy, varnish, wax or paint over the ESD surface.
11. **Commission before occupancy.** Follow the test plan below, record all results and repair/retest failures. Restore equipment only after the floor, electrical connections and mechanical condition pass. Keep product batch numbers, mix logs, climate records, actual consumption and the as-built collector/terminal plan.

Allow roughly **8–12 calendar days after material delivery**, including trial cure, preparation, application, full cure and testing at about 20°C. Procurement, substrate remediation and operational relocation can extend this. Schedule each recoat by its actual minimum/maximum window rather than a fixed day number.

## Acceptance and ongoing use

Before ordering, agree floor resistance to ground and point-to-point limits with the supplier and ESD specialist. As preliminary project goals use **<10⁹ Ω** for both, plus the supplier's specified range and an electrical safety review of any very low values. These are ESD goals, not proof of shock protection. Specify the applicable editions of IEC 61340-4-1 or ANSI/ESD STM7.1 and the facility's ESD-control standard in the test plan.

After full cure, commission **at least 10 distributed floor-to-ground measurements** for this room and representative point-to-point tests. Include the doorway, corners, aisle, areas remote from terminals and repaired areas. Use a calibrated ESD resistance meter and standard weighted electrodes, not a handheld multimeter or improvised probes; the cited system recommends 10–20 conductivity readings for 10–100 m². Record locations, test voltage, temperature, RH, cleaning state, both grounding paths and pass/fail values. Investigate and retain failed results as well as subsequent retests; a single good reading does not establish room performance. [Reference system test guidance](https://gbr.sika.com/en/construction/flooring/anti-static-esd-systems/sikafloor-multidures-56esd.html).

If flooring is used to ground personnel, verify the **actual person/footwear/floor combination**: system resistance <10⁹ Ω and walking body voltage <100 V using ANSI/ESD STM97.1 and STM97.2, or the corresponding applicable IEC methods. Qualify it at the lowest expected operating RH, not only humid commissioning conditions. Ordinary rubber shoes can defeat an ESD floor. The [EOS/ESD Association footwear/flooring explanation](https://www.esda.org/news/understanding-footwear-and-flooring-in-esd-control/) explains why separate compliant products do not guarantee a passing combination and why cleaning residues matter.

Provide compatible ESD footwear to every operator using the floor as a personnel-grounding system. Maintain separate rack bonding and appropriate grounded workstations/wrist straps for handling exposed electronics. Clean with the flooring supplier's approved method and residue-free cleaner; avoid wax and insulating mats. Set an initial quarterly floor/bonding verification schedule with the ESD specialist, retest after repairs or cleaner changes, and qualify replacement footwear. This schedule is a project recommendation, not a claimed universal standard interval.
