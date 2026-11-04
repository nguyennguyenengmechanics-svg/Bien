# Visual identity — Video học thuật trực quan

## Style Prompt
Continue the user's cream engineering explainer series. Teach one mechanism at a time with large original diagrams, clear labels, mathematical relationships and stepwise numerical examples. Serif headlines feel like a technical textbook; sans captions and data remain easy to read on a phone. Bold orange highlights identify the important concept; saturated blue carries data and analysis; dark green carries validity checks and practical principles. Thick colored connectors make branches unmistakable. Topic-specific visual metaphors must be rebuilt for each source.

## Colors
- #F1F0E4: cream background
- #142D38: ink and structural outlines
- #B83B16: strong orange emphasis, cautions and contrasting branch
- #0A527B: saturated blue, data, loading and analysis
- #2D6842: dark green, applicability and practical principles
- #FFE1BD: pale orange highlight background
- #FFFFFF: white diagram cards

## Typography
- DejaVu Serif Bold: display headlines, about 78 px on 1080×1920.
- DejaVu Sans regular: captions, about 36 px; Bold: key phrases, data, equations and branch titles.
- Main reading labels at least 28 px in a 900-unit SVG viewBox. Shorten text or enlarge cards when it does not fit.
- Never let inline strong nodes become separate flex columns: wrap the complete text in a span.
- Emphasize about one or two important phrases per caption, not the entire caption.
- Natural wrapping; short deliberate display-title line breaks are acceptable. No manual breaks in ordinary body text to hide an overflow.

## Layout
- Vertical 1080×1920, cream canvas, content roughly 80 px from left/right, 90 px top, 110 px bottom.
- Header and scene number → topic label → headline → one-line principle/formula → large white diagram → practical rule → caption zone → source line/progress.
- The supplied template uses approximately 620 px for diagrams and 238 px for captions. Adjust based on content, preserving readable sizes; do not force every subject into identical geometry.
- Headline usually two lines. Main diagram must remain useful without reading a paragraph.
- Use full-size flex content containers with padding and gap; reserve absolute positioning for layers and caption slots.

## Motion
- Seekable paused deterministic GSAP timeline registered with HyperFrames.
- Push transitions between scenes; completed outgoing content stays visible until transition.
- Stage arrows, curves, labels, calculations and branches to follow the explanation.
- Deformation, force movement or changing curves should explain the mechanism; clearly label exaggeration and illustrative data.
- Finite repeats only. No flashing, jitter or motion without explanatory purpose.
- A meaningful title must already be present at frame 0.

## What NOT to Do
- No walls of text, generic robots, unrelated footage or tiny SVG labels.
- No blanket claims that a model or threshold guarantees safety or works for every material.
- No unlabelled toy data, invented experiments, fake FEA heatmaps or unverified scientific images.
- Do not use color alone to distinguish meaning: add names, units, symbols or labels.
- Do not sacrifice technical correctness for a more dramatic hook.
