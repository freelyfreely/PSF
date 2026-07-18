# Craft — Refusals & Diagnostics (the AI-tell, and how to catch it)

*Recrystallized design grist for the Designer lens, metabolized from impeccable.style and
Refactoring UI. Reference register. Retrieved by `crystallize`. The refusals are the
form-stroke equivalent of the empty throne: the discipline of what NOT to do.*

## The slop test

If someone could glance at the surface and say "an AI made that" without doubt, it has
failed. Run the category-reflex check at two altitudes:

- **First-order:** if the theme and palette are guessable from the category alone, it is
  the first training-data reflex. Rework the scene and color strategy until the answer is
  not obvious from the domain.
- **Second-order:** if the aesthetic is guessable from category-plus-the-obvious-anti-
  reference ("AI tool but not SaaS-cream → editorial-typographic"; "fintech but not
  navy-and-gold → terminal dark"), the first reflex was dodged and the second was not.
  Rework until neither is obvious.

## Absolute refusals (match and rewrite)

If you are about to write any of these, rewrite the element with different structure:

- **Side-stripe borders** — a colored `border-left`/`border-right` > 1px as an accent on
  cards, callouts, alerts. Use full borders, a background tint, a leading number/icon, or
  nothing.
- **Gradient text** (`background-clip: text` over a gradient). Use one solid color;
  emphasis through weight or size.
- **Glassmorphism by default** — decorative blur/glass. Rare and purposeful, or nothing.
- **The hero-metric template** — big number, small label, supporting stats, gradient
  accent. A SaaS cliché.
- **Identical card grids** — same-sized icon + heading + text repeated endlessly. Vary the
  treatment; feature some items, minimize others. Cards are the lazy answer; nested cards
  are always wrong.
- **The tiny tracked uppercase eyebrow over every section** (small all-caps kicker —
  "ABOUT", "PROCESS"). One named kicker as a deliberate system is voice; an eyebrow on
  every section is AI grammar.
- **Numbered section scaffolding (01 / 02 / 03) by reflex.** Numbers earn their place only
  when the section truly *is* an ordered sequence the reader needs; otherwise drop them.
- **Text that overflows its container** — long heading words + large clamp scales +
  narrow grids overflow on tablet/mobile. The viewport is part of the design; test the
  copy at every breakpoint.
- **The cream / sand / beige body background** — the saturated warm-neutral AI default.
  Token names like `--paper`, `--cream`, `--sand`, `--linen`, `--parchment` are tells in
  themselves. Carry warmth through accent, type, and imagery, not the body background.

## Quick diagnostics (audit any surface)

- Does the hierarchy read when you squint (blur test)? If not, raise primary/secondary
  contrast.
- Does it hold in grayscale? If color is doing the structural work, strengthen
  size/weight/spacing first.
- Is there enough whitespace? Almost always: no. Add it, especially between groups.
- Are labels de-emphasized against their values? Is the measure constrained (~65ch)?
- Do colors clear WCAG contrast? Is the spacing on the 4/8/16/24/32/48/64 scale, with no
  arbitrary `13px`/`17px`/`23px`?
- Is motion intentional and eased-out (no bounce), with a `prefers-reduced-motion`
  alternative? Reveal animations must enhance an already-visible default, never gate
  content visibility on a class-triggered transition.

## Restraint is the signature

Aim for the quiet confidence of a well-made thing — intentional, uncluttered, nothing
arbitrary, every choice committed. When making it look impressive would distort or flatten
the meaning, choose the meaning. The surface serves the substance and honors its sources;
it never overshadows what it carries.
