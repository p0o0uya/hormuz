# Hormuz presentation — polished draft

The current file is [Hormuz-15min-Draft-03.pptx](../../assets/park/Hormuz-15min-Draft-03.pptx), in **`/etc/hormuz/assets/park`**. The Persian widescreen presentation has **20 slides scheduled for 15 minutes**, ending with the monthly financial model. [PDF preview](../../assets/park/Hormuz-15min-Draft-03.pdf) and [speaker notes](../../assets/park/Hormuz-15min-Draft-03-speaker-notes.md) are alongside it. Notes are embedded in every slide. Questions follow the presentation.

The opening preserves the philosophy, AI-assisted access to technical knowledge and the data-center essentials. Component slides highlight quantities/sizes, material and equipment choices, execution steps, reference costs or unpriced scope, and acceptance criteria. The audience deck contains no issue-mapping, review-status or slide-location pages, and no display appendices. References and issue traceability remain in notes and the separate [completeness review](../../assets/park/datacenter-completeness-review.md).

The final two slides explain cost control through existing inventory, selected team-built systems and demand-led equipment purchases, followed by the five revenue lines and seven monthly expense lines. The planning scenario is **138 million tomans revenue** (122 recurring + 16 new installations), **100 million running cost**, and **38 million cash surplus**. Recurring-only surplus is 22; weak sales of 75 produce a 25 deficit. These are historical application assumptions, before depreciation, tax, finance costs and major battery replacement. They do not establish net profit, achieved savings or payback. The capital comparison and two-hour backup scope remain distinct.

The [Hormuz brief](../hormuz-brief.md) preserves source assumptions. Component prices use the application's 13 October 2026 subtotals without contingency, before inventory/shared-item deductions; unpriced components are identified rather than assigned invented figures. The Ethernet monitoring reference is distinguished from the USB pilot. The detailed site/completeness work remains relevant even though its process language is removed from the audience deck.

## Presenting and revising

Open the PPTX in PowerPoint and use Presenter View. Rehearse to the notes' 900-second schedule, including 95 seconds for the final financial slide; actual speaking pace must be checked. Install Vazirmatn for matching Persian rendering, or inspect wrapping after any font substitution. The PDF is a fixed-layout preview.

Text and illustrations are editable PowerPoint shapes. Direct PowerPoint changes do not update the generator. Drafts 01 and 02 remain historical and are not overwritten by the draft 03 generator.

## Rebuilding

From `/etc/hormuz`, use Python 3 with `python-pptx` 1.0.2:

```sh
python3 -m venv /tmp/hormuz-slides
/tmp/hormuz-slides/bin/pip install python-pptx==1.0.2
/tmp/hormuz-slides/bin/python docs/presentation/build_presentation_v3.py
libreoffice --headless --convert-to pdf --outdir assets/park assets/park/Hormuz-15min-Draft-03.pptx
```

The [draft 03 generator](build_presentation_v3.py) writes the PPTX and Markdown notes directly to `assets/park` relative to its own location. Rebuilding overwrites those draft 03 outputs; PDF export overwrites the preview. LibreOffice Impress and Vazirmatn are required for matching PDF rendering. Earlier generators remain available for their respective drafts.

## Verification

Checks cover package/XML readability, all 20 slides and embedded notes, the 900-second schedule, coverage of all eight component issues, absence of audience-facing navigation/review slides, revenue and expense arithmetic, local documentation links, matching PDF page count, and shape/rendered-text bounds. Rendered slides are inspected for Persian shaping, wrapping, annotations and diagram layout. Microsoft PowerPoint is unavailable here; final rehearsal should include opening the PPTX there.
