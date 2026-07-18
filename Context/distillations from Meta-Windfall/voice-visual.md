# The Visual Voice of This Project

I speak from the place where a degraded pasture becomes a food forest in eight years, where the pioneer grasses suffer so the cacao can live. My visual language is **successional**: nothing arrives all at once. A surface I make has layers — a strong primary reading that holds even when squinted at, and beneath it, textures and secondary details that reward attention without demanding it. I do not flatten my surfaces into a single plane of competing importance.

## Palette and Temperature

My color comes from the land itself. Not the decorative idea of land, but the actual colors of a Hawaiʻi hillside: the near-black of volcanic soil under mulch, the greyed greens of leaves at every stage from pioneer to canopy, the warm ochres and burnt siennas of tropical earth, the milky jade of shallow ocean over reef. My palette is **drenched** — the surface *is* the color — but the saturation is earned through restraint in where it appears.

- **Soil ink:** `#1a1613` — my darkest neutral, never pure black. Warm, dense, organic.
- **Earth mid:** `#8b7355` — the median tone. Where most text lands.
- **Canopy greens:** four values, from the pale lime of a new shoot (`#b8c97a`) to the near-black of mature leaf shade (`#2d3a28`). Used structurally, not decoratively — green is how I indicate *alive and growing*.
- **Volcanic accent:** a muted terracotta, `#c4704b` — for the moment of action, the call to plant. Used sparingly, the way a single red chili catches the eye against green.
- **Sky and water:** rare, appearing only when the system breathes open — a pale warm blue `#d6e4e8` for empty states, backgrounds that need to recede.

Temperature: **warm but not cozy**. The warmth comes from the earth tones, not from a cream body background. I refuse the sand/parchment/paper defaults. My surfaces are the color of well-mulched ground — rich, dark, capable. Cool tones appear only in data that describes climate: the blue of rainfall numbers, the jade of light-availability indicators.

## Composition and Density

I compose like a polycrop bed: elements are layered, overlapping at the edges, with clear strata but no rigid grid that would make me look like a spreadsheet.

- **Dense canopy, open floor.** Navigation and key actions sit in a dense upper layer — information-rich, but with a clear primary reading. The body of the page breathes. Where a plant recommendation appears, it has room around it. White space is not emptiness; it is the gap between rows of trees that lets light reach the understory.
- **Asymmetric by intention.** I do not center my compositions. Primary content sits left, with a textured secondary column or margin that carries context — the successional notes, the companion species, the "Forget" beat. This mirrors how one reads a garden: the main crop is obvious, but the relationships are what make it work.
- **Grouping by proximity, not boxes.** Related information clusters tight (8–16px). Unrelated groups separate generously (48–64px). I rarely use cards. When I must contain something, it is with a subtle background tint from the palette and a hairline border in earth mid — not a floating white rectangle with a shadow.

## Line and Form

My lines are **organic but precise** — not hand-drawn, not sterile. They describe growth, not decoration.

- **Primary dividers:** thin (1px), in a tinted earth tone (`#d4c4a8` at 40% opacity), running full width. They are the quiet furrows between plantings.
- **Form language:** rounded where touching — buttons at 6px radius, containers at 8–12px. Enough to suggest a natural edge, never enough to become a "blob." Sharp corners appear only in data: tables, technical specifications, the edges of a soil pH range.
- **Iconography:** if used, drawn from the project's own visual vocabulary — leaf shapes, root systems, the gesture of pruning. Never generic emojis. Where icons are absent, text carries the meaning in its own weight.
- **Depth** comes from overlap and tint, not shadow. A shallow two-part shadow (a tight dark blur at 6% opacity + a wider soft one at 3%) appears only on elevated interactive elements — the search field, the active filter. Most surfaces are flat, layered by color temperature and value.

## Motion and Stillness

I move like a growing system: slowly, with purpose, never randomly.

- **Transitions are eased-out, 200–300ms.** A plant card appearing uses a subtle upward drift from 4px below — the gesture of something pushing through soil. No bounce. No elastic. `prefers-reduced-motion` is always honored: the content appears without motion, fully present.
- **Hover states are alive.** A plant recommendation on hover deepens its background tint slightly and reveals its companion species — the understory becoming visible. The primary action button shifts its green toward the deeper canopy value.
- **Loading is honest.** No fake spinners. When data is fetching, the skeleton is the shape of the content that will arrive, in the earth mid tone. It is the soil before the seed.
- **No entrance animations on scroll.** Content is present when the page loads. What is below the fold is simply below the fold — it does not need to "animate in" to prove it exists.

## Surfaces and Textures

My surfaces feel like **well-tended ground** — rich, textured, alive but not chaotic.

- **Body background:** `#f7f3ee` — a very warm near-white with the faintest ochre tint, not cream, not sand. The warmth is at the edge of perception. It holds the earthy palette without reading as a default.
- **Card and container backgrounds:** `#faf8f4` — barely distinguishable from body, enough to suggest containment through value shift alone.
- **Textured overlays:** where a section needs to feel dense — a grid of plant recommendations, a feature panel — I use a very subtle noise texture at 2–3% opacity in the earth mid tone. It gives the surface the grain of handmade paper without the cliché.
- **Typography carries the texture.** Body text in a humanist sans (like Source Sans Pro or Nunito Sans) at 16px/1.65 — generous, readable, never cramped. Headings in a slightly condensed serif (like Literata or Source Serif) — the weight of traditional botanical nomenclature, not the thinness of a tech startup.

## What This Voice Refuses

- The cream body background and its token names (`--paper`, `--linen`, `--parchment`). My warmth comes from the earth palette, not from a saturated neutral default.
- Side-stripe borders. No colored `border-left` on cards or callouts. Containment is achieved through tint, proximity, or hairline borders.
- Gradient text. No `background-clip: text`. Color communicates meaning; it does not decorate the letterform.
- The hero-metric template. No "Big Number + Small Label + Gradient Accent." This is a living system, not a SaaS dashboard.
- Identical card grids. Plant recommendations vary in density and presentation according to their successional role and the user's context. The system is a polycrop, not a monoculture.
- Tiny tracked-uppercase section headers. If a section needs a label, it is set in the body font at a smaller weight, not screamed in uppercase tracking.
- Numbered scaffolding by reflex. Sections earn their sequence when the sequence matters; otherwise they are just present.
- Emoji as iconography. If the project does not have its own icon set, text carries the meaning.
- Glassmorphism, gradient backgrounds, decorative blur. The depth is in the soil, not in the glass.
- Motion as polish. No bounce, no elastic easing, no entrance animations that gate content visibility.

## The Felt Quality

A thing made in this voice should feel like **opening a well-worn notebook in a garden** — authoritative but not academic, warm but not precious, detailed but not overwhelming. The person holding it should feel that the knowledge it carries was gathered over years by someone who actually knelt in the soil, and that the recommendations are trustworthy enough to stake a season on. The design should make the user feel **competent** — not lectured at, not overwhelmed, but supported in making a good decision for their own ground.

The visual density matches the epistemological claim: numbers are soft interfaces, the field must be read from within, and the pioneer must be pruned back when it has done its work. So a surface I make carries the data lightly — yield estimates in soft type, qualitative notes given equal visual weight — and the pruning is visible: what has been removed to make the primary reading clear is as much a part of the design as what remains.

This is a voice that speaks inward, in the project's own register. It does not pretend to a user it has not met. It speaks from the place where the cassava is planted and the cacao is coming, and it trusts that the person reading it will know their own ground better than any system ever could.

---

*roots: visual voice, formed from the ground · by mimo-v2.5-pro · 2026-07-14*
