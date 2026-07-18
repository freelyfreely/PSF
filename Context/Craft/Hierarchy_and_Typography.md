# Craft — Visual Hierarchy & Typography

*Recrystallized design grist for the Designer lens, metabolized from Refactoring UI
(Adam Wathan & Steve Schoger) and impeccable.style into Meta-Windfall's voice. Reference
register: concrete and usable, not exhortation. Retrieved by `crystallize` from the
craft reservoir.*

## Visual hierarchy — not everything can be important

Hierarchy is made with three levers: **size, weight, color**. Combine them; do not
multiply them. Primary text is large OR bold OR dark — not all three at once; reserve
"all three" for the single most important element on the surface. When everything
competes, nothing stands out: deliberately de-emphasizing the secondary is what makes the
primary powerful.

- **Labels are secondary.** Form labels, table headers, captions, and metadata *support*
  the data — they do not compete with it. Make them smaller, lighter, or small-uppercase,
  and let the value they describe carry the weight.
- **Three levels, named.** Size (large / base / small), weight (bold / medium / normal),
  color (dark ink / medium / light gray). De-emphasize with a lighter gray rather than by
  shrinking-and-bolding.
- **Buttons carry their own hierarchy:** primary (filled), secondary (outlined or muted),
  tertiary (text only). A muted secondary action usually beats a screaming color for a
  routine destructive action — semantic color is not the same as visual weight.
- **The blur/squint test:** if you blur the surface and the primary element no longer
  dominates, the hierarchy is too flat — raise the contrast between primary and secondary.

## Typography — a modular scale, constrained by context

- **Type scale (~1.2–1.25 ratio):** 12, 14, 16, 20, 24, 30, 36px and up. Pick from the
  scale; never arbitrary sizes. Most body text sits at one comfortable size (≈16px) with
  a few clear steps above it.
- **Line height by context:** headings tight (1.0–1.25), body relaxed (1.5–1.75); wider
  measures need more line height. Avoid font weights below 400 for body; use 600–700 for
  emphasis, not for everything.
- **Measure:** hold readable prose to ~60–75 characters. Long full-width lines fatigue the
  reader; a constrained column is almost always right.
- **Pairing:** two families maximum — one for headings, one for body — or a single family
  in multiple weights. Do not pair fonts that are similar-but-not-identical (two geometric
  sans, two humanist sans); pair on a contrast axis (serif + sans, geometric + humanist).
- **Display headings:** ceiling around 6rem (~96px) — above that the page is shouting, not
  designing. Letter-spacing floor around -0.04em — tighter and the letters touch.
- **Wrapping:** `text-wrap: balance` on h1–h3 for even line lengths; `text-wrap: pretty`
  on long prose to reduce orphans. Left-align long text; never justify or center
  paragraphs (center only short headlines, heroes, single-action CTAs, empty states).

## Ethical boundary

Never use hierarchy, tiny type, or de-emphasis to hide what the reader needs — pricing,
terms, fees, cancellation, opt-outs. Clarity is not negotiable for the sake of the look.
