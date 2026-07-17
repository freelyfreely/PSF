# The Map of Prep Set Forget

What is here, how it fits together, and why it is the way it is. PRODUCT.md holds
who this is for and what it refuses; this file holds the structure and the decisions.
Update it when a decision changes, not when a pixel does.

## The artifacts

- **[site.html](site.html)** — the tool. One file, no build step, no framework. It
  reads the real rain and elevation at any point on the island and says which of the
  plant records fit that ground, in planting order. Everything below about data,
  fit, and the visual arc lives here.
- **[flyer-windward.html](flyer-windward.html)** — the first flyer: eight plants for
  Hāmākua–Hilo–Puna, in planting order. Print-first; it has to survive a photocopier.
  More coasts get their own flyers later, derived the same way from the same records.
- **[plant-copy.md](plant-copy.md)** — the written plant records the site's `P` array
  and the flyer entries are drawn from.
- **[deliverables/](deliverables)**, **[cards-specimen.html](cards-specimen.html)** —
  specimens and outputs.

## The strokes (tooling)

Numbered strokes from the wider project body, kept beside the artifacts:

- **[close-isohyets.py](close-isohyets.py)** — turns the open isohyet polylines in
  [mapdata.js](mapdata.js) into closed, fillable regions along the real coastline.
  The site's rain bands are these regions.
- **[flyer-map.py](flyer-map.py)** — re-emits the site's rainfall map as static SVG
  for the flyer, so the flyer and the site are never two different islands.
- **[add-lived-bands.py](add-lived-bands.py)** — stroke 2: adds lived-band fields
  beside each published match-axis in the schema. The law it encodes: the lived band
  never overrides the published band; where they disagree, the disagreement is the
  finding, shown to the reader.
- **[gate.py](gate.py)** — stroke 5: the validation gate. A necrosis detector, not a
  truth-checker — decidable facets only; the holistic judgment stays with the living.
  `--sendable` lists the species that pass.
- **[authority-overlay.ts](authority-overlay.ts)** — the source-authority tiers
  (extension/university first, community fora second, general reference third) used
  when researching records.

## The data, and where it comes from

Nothing on the map is drawn by hand.

| Thing | Source | How |
|---|---|---|
| Coastline | US Census county boundary (15001) | baked into `MAP` in site.html |
| Rain bands | Rainfall Atlas of Hawaiʻi isohyets | closed by close-isohyets.py, baked in |
| Rain at a point | same Atlas raster, live | ArcGIS `identify` call per click |
| Elevation at a point | USGS 3DEP, live | EPQS call per click |
| Temperature | **derived**, not measured | lapse rate from elevation, labeled derived everywhere it appears |
| Address → point | Nominatim, bounded to the island | falls back to town/subdivision alias matching offline |
| Plant facts | Ferns Tropical Plants Database + the records | units converted to inches and feet — what a person here actually uses |

Nothing is stored, no account, no tracking. Failure states speak plainly: the ocean
click, the unreachable service, and "nothing on this list will feed you here" are
all designed answers, not errors.

## The shape of the site (the decisions)

The page is a descent through a food forest as it establishes:

1. **The night.** It opens dark — the island floating in a near-black sea, the three
   beats stacked as the masthead, Forget italic and dimmed. The door is the map
   itself: press where you live.
2. **The clearing.** The reading appears on a pale dawn band: place, feet, inches,
   what the air does. Live numbers, one honest caveat line.
3. **The canopy closes.** Each entry's ground color is keyed to its time-to-first-food
   (`data-shade` 0–4), and the list is sorted by the same key — so scrolling *is* the
   succession: open clearing at "3 mo," mature leaf-shade by "yr 3." The colophon
   ends back in the dark.

Inside that arc:

- **The spine.** A left rail carries each plant's first-food time on one continuous
  line — the shared clock the planting order hangs on. Gliricidia's rail honestly
  says "— no crop."
- **Type grows with the plant.** Name size follows stratum: ground herbs smallest,
  canopy monumental. A kalo *is* small under the trees.
- **Pace.** Entries whose life-span closes (`data-pace="fast"` — papaya, pigeon pea,
  lilikoʻi) are set tighter and briefer than the long trees.
- **Grow / Prune.** The one gateway to the full Prep · Set · Forget is a wide bordered
  control; open, it becomes "Prune." The vocabulary is the project's own.
- **The tail.** Poor fits are grayed, never deleted: "kept in case you know something
  this map does not." The reader outranks the tool on their own ground.
- **The blur is baked.** The rain bands' Gaussian blur is drawn once through a canvas
  at load (blob URL), not run live in the SVG filter pipeline — an old phone in Puna
  is the target device. Fallback: the vector path with the live filter.
- Cool tones appear in exactly one place: rain. Cool means wet.

## The fit logic (why a plant is shown, cautioned, or grayed)

In `fit()` in site.html: **temperature is hard, rain is medium, elevation murmurs.**

- Frost at this elevation + a frost-tender plant → poor. No argument with frost.
- Rain is asymmetric, and the asymmetry is the honest part: too much water is a
  drainage problem a mound or young lava solves, so wet only ever *cautions*; too
  little water is not solvable without carrying it, so dry beyond tolerance is
  *poor*. A plant that needs a dry season (mango) is poor on ground that never
  gives one.
- Elevation out of range cautions; far out of range is poor.

Verdicts are written as one plain sentence in the entry, in the plant's terms.

## The copy system

Each plant record carries: the **distil** (the one paragraph that earns the entry),
the **prefs** (rain, temp, elevation, sun — plain words first, the precise band in
the tooltip), the three beats (**Prep / Set / Forget**), **the food** (how it is
eaten, including the hazards, plainly), and **carried** (the story the plant brought
with it). The **placements** — which plant stands with which — are deliberately
unwritten: a placement is a claim about two plants, so it can only be written last,
against the whole set at once, when the records are integrated.

## Deliberately unfinished

- The placements / companion column (waiting on record integration).
- Flyers for the other coasts (leeward, upcountry) — same records, same map, new
  planting orders.
- The lived bands standing beside the published bands in the UI.
