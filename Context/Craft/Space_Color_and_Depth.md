# Craft — Spacing, Color & Depth

*Recrystallized design grist for the Designer lens, metabolized from Refactoring UI
(Wathan & Schoger) and impeccable.style. Reference register. Retrieved by `crystallize`.*

## Spacing & sizing — a constrained scale defines relationships

- **Use a scale, never arbitrary values:** 4, 8, 16, 24, 32, 48, 64px. `padding: 13px`
  breeds inconsistency; a fixed scale forces deliberate, harmonious decisions.
- **Spacing between groups must exceed spacing within groups** — proximity *is* meaning.
  An icon and its label sit tight (4–8px); a card's sections separate at ~24px; page
  sections breathe at 48–64px.
- **Start with too much whitespace, then remove — you will almost never remove enough.**
  Generous space reads as premium; dense reads as overwhelming. Whitespace is structure,
  not waste.
- **Constrain widths:** prose to 45–75ch, forms to ~300–500px. Full-bleed is almost never
  right.

## Color — grayscale first, color last

Design in grayscale first; add color last. This forces hierarchy through space, contrast,
and weight before color becomes a crutch. If it does not work in grayscale, color will
not save it.

- **Systematic palette:** each color gets 5–9 shades (near-white 50 → near-black 900).
  The darkest ink is *not* pure black — use a very dark tinted neutral (e.g. `#111827`),
  never `#000000` on `#ffffff`.
- **Tint the grays.** Pure grays look lifeless. Add a little saturation toward the brand
  hue — cool toward blue, warm toward yellow/brown — a chroma of ~0.005–0.015, not a
  default warm tint on everything.
- **Contrast is non-negotiable:** body text ≥ 4.5:1, large text (≥18px or bold ≥14px)
  ≥ 3:1, placeholders the same 4.5:1. The single most common failure — and the first
  reason a surface feels hard to read and cheap — is pale gray body text on a tinted
  near-white. If it is even close, bump the text toward the ink end. Gray text on a
  *colored* background washes out; use a darker shade of the background's own hue instead.
- **Pick a color strategy before picking colors** (the commitment axis): **Restrained**
  (tinted neutrals + one accent ≤10% — the product default), **Committed** (one saturated
  color carries 30–60% of the surface), **Full palette** (3–4 deliberate named roles), or
  **Drenched** (the surface *is* the color). Carry "warmth" through accent, type, and
  imagery — not by defaulting the body background to cream/sand/beige.
- **Never rely on color alone** to convey meaning; pair it with text or an icon.

## Depth & shadows — elevation through restraint

- Small shadows = slightly raised (buttons, cards); large = floating (dropdowns, modals).
  If everything floats, nothing has depth.
- A good shadow has two parts: a tight dark layer for crispness plus a larger soft one for
  atmosphere. Shadow color is transparent dark, never opaque gray.
- Prefer a hairline border + a soft, low-opacity shadow over a heavy box. Corners on one
  consistent radius. Depth can also come from a lighter top border + darker bottom border,
  or subtle overlap — not only from drop shadows.
