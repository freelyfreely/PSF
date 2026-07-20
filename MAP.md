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
  report about its consolidated life — the reading no raster *fully* carries (lava-flow surface age
  seeds it; the vegetation refines it) and the conversational layer exists to take. A confidence-tagged
  scaffold, written ahead of its sourcing, awaiting the lived reading.
- **[INSIGHTS.md](INSIGHTS.md)** — *the seedbed.* Whatever doesn't fit the others yet, date-stamped,
  periodically promoted or let go.
- **[NEEDS.md](NEEDS.md)** — *the edges.* What the tool is waiting on, sorted by who or what can supply
  it (steward-held knowledge, fetchable sources, external rasters, tooling, decisions) — the orthogonal
  cut to "Deliberately unfinished" below.

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
  drainage problem a mound or young lava solves, so wet never goes *poor* — but it is
  also **graduated** (fixed session 8). Above the *preferred* band yet still inside
  *tolerance* is fine ground, not a problem: the card stays good and says only "on the
  wet side of its range, but well within what it takes." Wetness earns the caution and
  the mound-and-drainage advice only once it passes *tolerance*. (Dry stays the
  dangerous direction: drier than preferred cautions even inside tolerance; drier than
  tolerance is *poor*. A plant that needs a dry season — mango — is poor on ground that
  never gives one.) This keeps the tool from greeting its own wet coast with a wall of
  warnings — the failure the old "wet always cautions" rule produced at Pahoa.
- Elevation out of range cautions; far out of range is poor.
- **The band shown is the band judged.** The rain pill's displayed range is derived
  from the same `p.rain` numbers `fit()` reasons on, so a card can never show "up to
  157" beside a "too wet" verdict (the drift that surfaced session 8). Qualitative
  lived bands ("wet to mesic") are left as authored, per the labeled-not-disguised rule.

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
is only *partly* in a raster — lava-flow surface age seeds it — and the finer read is off what is
already growing. `succession.md` III has always assumed this input ("*and* what is already growing
there") and it has never had an interface. **Raster-seeded, conversation-refined.**

So the conversational / LLM layer is not an enrichment tier for the pioneer substrate. **It is the
instrument's missing second axis**, and it exists to ask one question: *what is already growing
there?* The input device it needs is a Hawaiʻi indicator-plant set, which does not exist in any
database. A first-pass scaffold — [INDICATORS.md](INDICATORS.md) — is now written, confidence-tagged
and awaiting the steward's ground-truth; it is the one document in the layer written *ahead of* its
sourcing, and marked so.

## Deliberately unfinished

- **The `raw/` store now covers the whole corpus** (session 5, 2026-07-18): all 56 copy entries have a
  one-file-per-plant `raw/` record (57 files — the citrus trio share one), each band traced to Ferns in
  the source's units with the conversion kept, or labelled lived/general where Ferns is silent. The
  session-4 gap (the Part III fruit #20–37, the Part IV annuals #45–47, the citrus) is closed.
- **The recrystallization pass** (advanced session 5): the copy has been reconciled against the now-
  complete `raw/` store. Corrections applied to [plant-copy.md](plant-copy.md): ʻulu rain 157→120 in;
  ice-cream-bean natural range 350–5,000 ft → 360–1,770 ft (110–540 m); **poha altitude "above 800 ft"
  → "above ~2,600 ft (800 m)", a metres→feet unit slip the store caught**; pumpkin + ipu gained their
  Ferns rain bands (the Part IV "Ferns is thin for the annuals" framing was wrong — only the currant
  tomato is genuinely band-less). **Still owed:** the same ʻulu + ice-cream-bean fixes in `site.html`'s
  `P` array (the shipped tool still shows the old numbers); and unsourced reader-facing figures now
  flagged in the store — chaya altitude 4,300 ft, cempedak "best under 450", citrus rainfall 40–60 in
  and altitude 3,000 ft — owed a source or a relabel. Deeper cross-reads (Elevitch/Morton for the
  fruit) continue; abiu (#57, still no rainfall band) remains first in line.
  **Session 6 (2026-07-18) worked the shipped-artifact half of the recrystallization drift, and turned up
  a rule:** ice-cream-bean's natural range `350–5,000 ft` → `360–1,770 ft (110–540 m)` (cultivation ceiling
  7,200 ft kept). ʻUlu's rainfall went the *other* way: the unsourced shipped `[60,157]/tol[40,180]` was
  first contracted to `[60,120]/tol[40,120]` on Ferns+Elevitch — then **reversed and expanded** once a
  Hawaiʻi-calibrated source was found: **Mausio, Miura & Lincoln (2020), *PLoS ONE***, an EcoCrop model
  re-fitted to 1,200 naturalized breadfruit trees mapped in Hawaiʻi, gives precipitation optimal
  1,500–4,000 mm and absolute 750–8,000 mm. Shipped now `rain:[60,157]` / `rainTol:[30,315]`. The 157 was
  unsourced, not wrong. **This is the origin case of the expand-when-justifiable rule (SOURCES.md): widen a
  filtering band rather than narrow it whenever a real source permits, because a too-narrow band wrongly
  reads a plant "poor" on ground it thrives on — the costlier error under "the reader knows their own
  ground."** Still owed on this line: the unsourced reader-facing figures flagged in the store (chaya
  4,300 ft, cempedak "under 450", citrus 40–60 in / 3,000 ft) — each now a candidate to *source-and-widen*,
  not trim.
- **Axis 2 now ships, and it renders** (session 6): the derived `succ:` field is compiled from each
  `raw/` record's *Succession (axis 2)* line into all 19 shipped `P` entries (placenta 1/2 · secondary
  1/2 · climax), sitting beside `str:` (axis 1). It renders as a small `.succ` pill next to the stratum
  pill — **plain word visible, Götsch's class in the tooltip** (PRODUCT.md's "plain word before the
  technical term," the same idiom the pref bands already use). Plain mapping lives in one editable
  `SUCC_PLAIN` object in `site.html`: `first in` / `early crop` / `fast nurse` / `long-lived` /
  `old-growth`. The wording is the steward's to tune (see [NEEDS.md](NEEDS.md) §V). Stratum says *where
  in the light*; `succ` says *when in its life* — the two axes, finally both visible in the tool.
- **Numbering "gap" #48–50 resolved** (session 5): the citrus entry *is* #48–50 (orange · grapefruit ·
  lemon, one entry across three species). The copy does not skip — it collapses three numbers into one
  heading. The corpus is 56 entries across a 1–59 numbering because the citrus triple and the true
  absence of any #-labels between #47 and #51 net out; the count is honest.
- **The horizontal layer** — placement / companion / difficulty — compiled from
  [succession.md](succession.md) once its cross-claims are reconciled.
- Consolidating the scattered field techniques from copy "Set/Forget" beats into
  [PRAXIS.md](PRAXIS.md).
- Promote noni (#38) toward the front of the wet-coast succession — it is the pioneer for raw lava,
  not a wider-palette footnote.
- Flyers for the other coasts (leeward, upcountry) — same records, same map, new planting orders.
- The lived bands standing beside the published bands in the UI.
- **Successional class — now in the store, not yet in the ship.** Every `raw/` record for the shipped
  19 now carries a *Succession (axis 2)* line (class + lifespan) alongside the stratum (`str:`, axis 1)
  — done session 4 (2026-07-17). What remains: a derived `succ:` field in `site.html`, compiled from
  `raw/`, so both axes are visible in the tool and available to the placement pass. See
  [succession.md](succession.md) I-b.
- **The senescence audit:** re-read every "Forget" beat in the copy against the finding that flowering
  broadcasts aging to the whole system. Some beats may imply a plant can be left to seed when it
  should not be.
- **The Hawaiʻi indicator-plant set** — [INDICATORS.md](INDICATORS.md) is a first-pass scaffold;
  what is owed is the steward's ground-truth pass (ratifying or overturning each `[inferred]` /
  `[needs ground-truth]` tag), the CTAHR/DLNR sourcing for the `[established]` entries, and the
  missing entries (wet-forest natives, upcountry and dry-side weeds, everything above the frost line).
- **The reservoir, now surfaced** (steward, session 6; built session 6/7). The steward set the
  direction: **all 59 — and every subsequent plant — belong in the reservoir the tool draws from; there
  is no curated subset.** As of session 7 the site carries the **whole written corpus — 57 cards** (the
  38 beyond the hand-built 19 were generated from [plant-copy.md](plant-copy.md) + [raw/](raw) and
  spliced into the `P` array; the citrus trio is one card, so 57 not 59). Per-site `fit()` does the
  narrowing; the whole reservoir stands behind it. **The per-plant fit-tuning pass is now done (session
  7):** all 38 reservoir cards were re-distilled by hand against `raw/` — the generator's truncated
  Prep/Set/Forget prose restored in full from the copy's *Detailed* beats, the empty `prefs` detail
  columns filled with the sourced numbers, and the fit bands (rain/rainTol/elev/frost/needsDry) tuned to
  the ore under the **expand-don't-contract** doctrine ([SOURCES.md](SOURCES.md)). Bands without a
  published source are labeled lived/general in the pref tooltip (the lived greens, abiu, currant tomato).
  The pass caught a class of generator inversions worth recording: **`needsDry:true` was mis-set on
  wet-loving plants** (jackfruit, cempedak, acerola, rose apple, citrus — each "wants no dry season" or
  "dislikes drought," so the flag falsely read the wet coast as *poor*); **elevation bands were inverted
  on the two upland crops** (poha and cardamom had `[0,ceiling]`, flagging the hot lowland as ideal when
  both want the cool mid-elevations — fixed to `[floor,ceiling]`); **noni's `rainTol` floor (28) sat above
  its lived 10-in dry floor**, contradicting its defining bare-lava-pioneer role; and several cards carried
  the *tolerance* ceiling in the *preferred* slot. A band-order sweep across all 57 cards is clean. The
  `succ`/`str` axes still trace to `raw/`. Remaining owed: the guild **placements** (written last, from
  the whole set at once). The Minimum Viable Seed test ([SYNTROPY.md](SYNTROPY.md) VII) now applies to the
  *shape the reservoir grows into*. Generator lives in the session scratchpad (`gen.js`).
