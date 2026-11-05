# Hormuz presentation — first draft

[PowerPoint: Hormuz-15min-Draft-01.pptx](Hormuz-15min-Draft-01.pptx) is a Persian, widescreen presentation for the Ilam University incubator. It contains **15 main slides scheduled for 15 minutes**, followed by **four optional appendix slides**. Questions and appendix discussion are outside the 15-minute slot. Speaker notes are embedded in every slide and also available in [speaker-notes.md](speaker-notes.md).

The story moves from customer need to the economic approach, room/design, prototypes, airflow, monitoring/safety, backup-power decision, execution sequence, budget, revenue scenarios, acceptance, team, requested support and next step. Original PowerPoint vector illustrations show racks, a conceptual room plan, material layers, airflow, monitoring, milestones and budget bars. Text, charts and illustration shapes are editable; no external artwork or image permissions are needed.

The primary source is **Hormuz-Cost-Effective-Draft-02**, supported by the eight engineering proposals in `assets/park`. The [source brief](../hormuz-brief.md) records facts, assumptions and inconsistent design bases for future revisions. Main financial slides use the application’s historical planning figures, without contingency, not current quotations. The two-hour backup ambition and 15-minute UPS reference are kept distinct. Unpriced equipment and uncertain test results are disclosed. No new technical certification, market-size estimate, savings percentage or payback claim is introduced.

## Presenting and revising

Open the PPTX in Microsoft PowerPoint, use Presenter View for notes, and rehearse to the per-slide schedule in `speaker-notes.md`. The time budget sums to 900 seconds; actual speaking pace needs rehearsal. Vazirmatn is the design font. Install it for consistent Persian layout, or substitute a compatible Persian font and check line wraps. The PDF is a fixed-layout reading/printing preview.

Before final presentation, update verified inventory and site measurements, obtain pilot quotations, resolve cooling and backup design, and replace financial assumptions only with documented results. Name or event changes can be made directly in PowerPoint. Changes made in PowerPoint are not automatically imported into the generation script.

## Rebuilding

Use Python 3 with `python-pptx` (the first draft used 1.0.2). From the repository root:

```sh
python3 -m venv /tmp/hormuz-slides
/tmp/hormuz-slides/bin/pip install python-pptx==1.0.2
/tmp/hormuz-slides/bin/python docs/presentation/build_presentation.py
libreoffice --headless --convert-to pdf --outdir docs/presentation docs/presentation/Hormuz-15min-Draft-01.pptx
```

LibreOffice Impress and the presentation font must be installed for PDF rendering. Rebuilding overwrites the generated PPTX and speaker-notes Markdown. Diagrams are constructed by the script from native PowerPoint shapes. The optional `preview.jpg` is a contact sheet of rendered slides.

## Verification

The delivery checks cover PPTX parsing and package XML, 19 slides and embedded notes, the 900-second main-slide time budget, shape bounds, matching PDF page count and rendered visual inspection. The PDF is rendered through LibreOffice; Microsoft PowerPoint itself is not available in this environment, so final rehearsal should include opening the PPTX there.
