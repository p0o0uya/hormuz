# Hormuz presentation — revised draft

The current presentation is [Hormuz-15min-Draft-02.pptx](../../assets/park/Hormuz-15min-Draft-02.pptx), saved in **`/etc/hormuz/assets/park`**. It is a Persian widescreen PowerPoint with **19 main slides scheduled for 15 minutes** and **five optional appendices**. [PDF preview](../../assets/park/Hormuz-15min-Draft-02.pdf), [speaker notes](../../assets/park/Hormuz-15min-Draft-02-speaker-notes.md) and the [component completeness review](../../assets/park/datacenter-completeness-review.md) are in the same directory. Notes are also embedded in every slide. Appendix discussion and questions are outside the 15-minute slot.

Slide 1 starts directly with the philosophy: AI/vibe coding, application infrastructure needs, the cost/risk of concentration, and the proposed small, geographically distributed model. Slide 2 explains AI-assisted access to knowledge, team labor and material-focused spending. Slide 3 maps eight essential families. Slides 4–18 explain components individually, each with a design idea, execution plan, editable illustration and acceptance criterion. Slide 19 closes with the pilot sequence and requested incubator support. Slides 20–24 provide issue mapping, open design work, historical budget, sales scenarios and sources.

All eight component issues (#2–#9), including their follow-up comments, were read and cross-checked against the final proposals. The review explicitly adds scope that lacked a complete design: site readiness, prolonged-outage power, cooling production/continuity, water leaks, networking, cyber isolation, server/storage capacity, customer backups/off-site recovery, and integrated operations. Existing issue-backed studies are marked in teal; proposed completions are marked in amber. No GitHub issues or messages were created.

The source facts remain in the [Hormuz brief](../hormuz-brief.md). The presentation uses AI as a design aid and infrastructure-demand thesis; it does not claim an already built DIY inverter/UPS, a deployed multisite network, standards certification or quantified savings. Material-focused spending still accounts for founder time, instruments, testing and specialist work. Historic financial comparisons stay in the appendices. The two-hour backup goal remains distinct from the 15-minute commercial UPS reference. New scope is unpriced until surveyed and quoted.

## Presenting and revising

Open the PPTX in PowerPoint and use Presenter View for the notes. Rehearse against the per-slide schedule: its total is 900 seconds, but actual speaking pace must be checked. Vazirmatn is the design font; install it for consistent Persian layout. If substituting another Persian font, inspect wrapping. The PDF provides a fixed-layout reading preview.

Before the final talk, replace unresolved site, inventory and price assumptions only with verified results. The single-site pilot is the current project; a geographically independent second destination and recovery agreements are future design work. The proposed new work packages in the review are marked G1–G9, not actual GitHub issue numbers. Standard/reference domains guide the scope review; local requirements and full design compliance still need accountable specialist review.

Text and all illustrations are editable native PowerPoint shapes; no external artwork is required. Direct PowerPoint edits do not update the generator. Draft 01 remains available as historical files under `docs/presentation` and `assets/park`; the new script leaves those files untouched.

## Rebuilding

Use Python 3 and `python-pptx` 1.0.2. From `/etc/hormuz`:

```sh
python3 -m venv /tmp/hormuz-slides
/tmp/hormuz-slides/bin/pip install python-pptx==1.0.2
/tmp/hormuz-slides/bin/python docs/presentation/build_presentation_v2.py
libreoffice --headless --convert-to pdf --outdir assets/park assets/park/Hormuz-15min-Draft-02.pptx
```

The [revision generator](build_presentation_v2.py) writes the draft 02 PPTX and Markdown notes directly into `assets/park`, based on its own location rather than the process working directory. Rebuilding overwrites those two draft 02 outputs; PDF export overwrites the preview. LibreOffice Impress and Vazirmatn are required for matching PDF rendering. The original `build_presentation.py` is retained for draft 01.

## Verification

Checks cover package/XML readability, all 24 slides and embedded notes, the 19-slide/900-second main schedule, component-issue coverage, shape and rendered-text page bounds, Markdown links, and matching PDF page count. Rendered slides are visually inspected for Persian shaping, wrapping, layout and diagrams. Microsoft PowerPoint is unavailable here; final rehearsal should include opening the PPTX there. Review coverage does not assert that design tests or field acceptance have passed.
