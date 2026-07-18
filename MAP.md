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
  and the flyer entries are drawn from. **The refined story, distilled from `raw/`** — not
  the store itself.
- **[deliverables/](deliverables)**, **[cards-specimen.html](cards-specimen.html)** —
  specimens and outputs.

### The knowledge layer (store vs. story)

Added session 2 (2026-07-17): the plant copy was doing two jobs — data of record *and* finished
prose. These split them apart. The governing move is **separate the store from the story**; order,
placement, and difficulty are **derived per site**, never authored once (there is no fixed planting
order — see [succession.md](succession.md)).

- **[raw/](raw)** — *the ore.* One file per plant: every source's numbers side by side (units kept
  and converted), plus inferences and anecdotes. The source of truth [plant-copy.md](plant-copy.md)
  is distilled from, and the store [gate.py](gate.py) checks against (the revived `spine.jsonl`).
- **[SOURCES.md](SOURCES.md)** — *the method.* Authority order, databases, conventions (units,
  lived-band labeling), the judgments held lightly.
- **[SYNTROPY.md](SYNTROPY.md)** — *the ground.* The deepest layer: what succession is *for*, and the
  apparatus the physics is expressed in. Götsch's syntropic method (strata × successional class, the
  colonization→accumulation→abundance reading, the crutch, pruning physiology) and Freely's own
  writings (syntropy vs. entropy, the garden wall, abundance as origin, the design criteria the tool
  is judged against). Authority over mechanism and stance; **never over a number** — see
  [SOURCES.md](SOURCES.md).
- **[succession.md](succession.md)** — *the physics.* Broad to specific: succession theory, the
  guild mechanics (traceable to `raw/`), and the site-logic that derives the planting order. The
  engine the horizontal layer (companion / placement / difficulty) is compiled from.
- **[PRAXIS.md](PRAXIS.md)** — *the doing.* The outer techniques (the living cutting, chop-and-drop,
  reading the harvest signal) and the inner succession that is the project's real product.
- **[INDICATORS.md](INDICATORS.md)** — *the second axis.* What the plants already standing on a site
  report about its consolidated life — the reading no raster carries and the conversational layer
  exists to take. A confidence-tagged scaffold, written ahead of its sourcing, awaiting the lived
  reading.
- **[INSIGHTS.md](INSIGHTS.md)** — *the seedbed.* Whatever doesn't fit the others yet, date-stamped,
  periodically promoted or let go.

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
| Plant facts | [raw/](raw) store (Ferns + Morton + CTAHR/native + lived), distilled to the records | units converted to inches and feet — what a person here actually uses |

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
against the whole set at once, when the records are integrated. Placement, difficulty, and the
planting order are one derived quantity (all functions of the site's state + available companions),
compiled from [succession.md](succession.md) — not three separate columns.

## The second axis (the standing architectural gap)

Added session 3. The fit logic above reads **climate** — it answers *can this species survive here*.
The syntropic reading says the variable that decides cost, pest pressure, and planting order is
orthogonal to climate: where the ground sits between raw substrate and consolidated abundance. That
is not in any raster; it is read off what is already growing. `succession.md` III has always assumed
this input ("*and* what is already growing there") and it has never had an interface.

So the conversational / LLM layer is not an enrichment tier for the pioneer substrate. **It is the
instrument's missing second axis**, and it exists to ask one question: *what is already growing
there?* The input device it needs is a Hawaiʻi indicator-plant set, which does not exist in any
database. A first-pass scaffold — [INDICATORS.md](INDICATORS.md) — is now written, confidence-tagged
and awaiting the steward's ground-truth; it is the one document in the layer written *ahead of* its
sourcing, and marked so.

## Deliberately unfinished

- **The recrystallization pass:** cross-read every `raw/` record against a second source
  (Elevitch / Morton), then re-distil the copy. Acerola (#27) is the worked example done; abiu (#57,
  no rainfall band) is first in line. ~48 records remain.
- **The horizontal layer** — placement / companion / difficulty — compiled from
  [succession.md](succession.md) once its cross-claims are reconciled.
- Consolidating the scattered field techniques from copy "Set/Forget" beats into
  [PRAXIS.md](PRAXIS.md).
- Promote noni (#38) toward the front of the wet-coast succession — it is the pioneer for raw lava,
  not a wider-palette footnote.
- Flyers for the other coasts (leeward, upcountry) — same records, same map, new planting orders.
- The lived bands standing beside the published bands in the UI.
- **Successional class has no field.** Every record carries a stratum (`str:`) — axis 1 — and nothing
  for axis 2 (placenta 1/2 · secondary 1/2 · climax, with lifespan). Both are needed before placement
  can be compiled. See [succession.md](succession.md) I-b.
- **The senescence audit:** re-read every "Forget" beat in the copy against the finding that flowering
  broadcasts aging to the whole system. Some beats may imply a plant can be left to seed when it
  should not be.
- **The Hawaiʻi indicator-plant set** — [INDICATORS.md](INDICATORS.md) is a first-pass scaffold;
  what is owed is the steward's ground-truth pass (ratifying or overturning each `[inferred]` /
  `[needs ground-truth]` tag), the CTAHR/DLNR sourcing for the `[established]` entries, and the
  missing entries (wet-forest natives, upcountry and dry-side weeds, everything above the frost line).
- **The 19/59 selection.** `site.html` carries nineteen plants; the corpus carries fifty-nine. The
  shipped set is currently bounded by where day 1 stopped rather than by a decision about which
  plants earn the display. Making the nineteen a *chosen* nineteen is owed — and the Minimum Viable
  Seed test ([SYNTROPY.md](SYNTROPY.md) VII) is the criterion: does the shipped set contain every
  organ of the whole system, or is it a slice of a larger one?
