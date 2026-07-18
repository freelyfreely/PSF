# The Sources of Prep Set Forget

Where the plant records come from, which authority outranks which, and the conventions the
records follow. [MAP.md](MAP.md) holds the structure of the whole; [PRODUCT.md](PRODUCT.md)
holds who it is for; this file holds the provenance behind the words in
[plant-copy.md](plant-copy.md). Update it when a source or a convention changes, not when a
sentence does.

## The authority order

The tiers are the ones [authority-overlay.ts](authority-overlay.ts) encodes, with one addition
that this project earns by where it lives.

1. **University extension and government science.** CTAHR / UH Mānoa, USDA (GRIN, APHIS), the
   state Department of Agriculture, the Rainfall Atlas of Hawaiʻi, USGS. First for anything
   local and decidable — climate at a point, pest and disease status, identity.
2. **Lived ground-truth.** The steward's own field experience on this island. This sits high,
   not low, for one question only: *does this plant actually thrive here, with little input?*
   Where a published climate band is silent or reflects a mainland greenhouse, the lived band
   carries the record — and it is **labeled as lived**, never dressed up as a raster reading.
   This is the [add-lived-bands.py](add-lived-bands.py) law in prose form: the lived band never
   silently overrides the published one; where they differ, the difference is the finding.
3. **Horticultural databases.** Ferns / Useful Tropical Plants and PFAF (below) for cultivation
   detail — soil, propagation, uses, the numeric bands.
4. **Community fora and grower knowledge.** Rare-fruit societies, permaculture writing,
   plantation-era and dooryard practice. Good for texture and for the plants the databases miss.
5. **General reference.** Encyclopedic sources, last and lightest.

Where two tiers disagree on a decidable fact, the higher tier wins. Where they disagree on the
holistic judgment — *is this a good plant for this person's ground?* — no source wins; that is
handed back to the living, per the gate's own boundary (below).

## The databases, and what each is good for

| Source | Reach | Good for | Watch |
|---|---|---|---|
| **Ferns — Useful Tropical Plants** (tropical.theferns.info) | Ken Fern's tropical corpus | The primary cultivation bands: rainfall, temperature, altitude, soil, propagation, uses | Thin or absent for a few kitchen crops and gathered plants; units are metric/mm |
| **PFAF** (pfaf.org) | The temperate-first sibling of Ferns, same lineage | Cross-checking Ferns; sometimes the more current of the two | Temperate bias — its climate bands can understate a plant's tropical range |
| **Elevitch, Species Profiles for Pacific Island Agroforestry** (agroforestry.net) | Extension-grade Pacific agroforestry | Food *and* support species written almost in this project's spirit; the strongest fit for the canoe plants and the guild | *To be integrated* — the recommended next cross-read |
| **CTAHR / UH Mānoa extension** (ctahr.hawaii.edu) | Hawaiʻi-specific | The real local pest, disease, and climate picture | The authoritative word on anything Hawaiʻi-particular |
| **USDA APHIS / HDOA** | US / Hawaiʻi pest status | Current pest and disease establishment (e.g. the citrus psyllid and HLB status) | — |
| **Morton, Fruits of Warm Climates** | Tropical fruit | The tropical fruit trees where the temperate databases run thin | Older; cross-check current names and pests |
| **Native Plants Hawaiʻi / CTAHR / DLNR Forestry** (nativeplants.hawaii.edu, dlnr.hawaii.gov) | The endemic and indigenous flora | The one place the databases above cannot help: native plants like the māmaki, read by forest type and elevation, not a raster band | The authority for anything endemic — range, ecology, the native web it sits in |
| **Grower and cooperative practice** (e.g. Hawaiʻi ʻUlu Cooperative) | Working Hawaiʻi farms | Propagation, spacing, guild companions the databases omit — how a plant is actually put in the ground here | Practice, not a controlled trial; corroborate the numbers, trust the placement |
| **Peer-reviewed medical / nephrology literature** | Specific human-health cautions | The load-bearing hazard facts (star-fruit caramboxin and renal risk; the raw-katuk-juice lung injury) | Used only to state a plain caution, never as horticulture |
| **permacultureplants.com** | Long bylined secondary articles | Soft, anecdotal colour only | 403 to plain fetch, reachable only through a real browser; footnoted secondary, never a primary source. Only ʻulu has been cross-read against it |

All numeric bands in the records are converted to **inches and feet** — what a person here actually
uses — regardless of the source's units.

## The conventions

- **Units.** Inches of rain, feet of elevation, °F. Always.
- **Bands are bands, never points.** A single frozen optimum (80.6–80.6) is a defect: nothing but
  an exact match can pass it. Every climate field is a real range.
- **Lived bands are labeled.** Where the number is ground-truth rather than a published reading,
  the record says so in plain words ("Ground-truth, not a raster — the published record is thin
  here"). The reader can see which kind of knowing they are standing on.
- **The `*(light sourcing)*` marker is retired.** It briefly flagged entries written from thin or
  general knowledge. As of this pass no record carries it: the kitchen-door annuals are grounded
  in lived Puna experience, the two proprietary greens (longevity and sissoo spinach) in lived
  ground-truth where Ferns is silent, and citrus's pest picture is cross-read against the
  extension and APHIS record. The marker's absence is the standard; if it ever returns, it means
  a record shipped that still owes a source.
- **Hazards are named plainly and early**, in the plant's own terms — the raw chaya, the raw
  kukui nut, the noni smell, the wild-yam bitterness — never buried under the praise.

## Judgments that are held lightly

Some facts are true in one frame and misleading in another, and the records say so rather than
importing the wrong frame's certainty.

- **"Pest" is a monoculture word.** A pest's weight in a conventional orchard is not its weight in
  a diverse, healthy dooryard planting, where mixed strata, soil biology, and natural predators
  change the arithmetic. The citrus greening note is written this way on purpose: the psyllid
  vector is established in Hawaiʻi, the disease itself has never been found here, and the orchard's
  fear is held lightly for the dooryard tree. More targeted research could sharpen this distinction
  later; until then it is stated as a caution, not a verdict.
- **"Difficulty" is contextual, not intrinsic.** Any plant not bred into dependence can be a
  level-one prep-set-forget in the right community. The companion — often a pioneer already growing,
  strongly pruned to stimulate rather than overpower — is the largest difficulty reducer there is,
  and it is free and in place. This is why the companion/placement layer and any future
  "difficulty" reading are the same feature, and why they are written last, against the whole
  integrated set.

## The gate, and its boundary

[gate.py](gate.py) is a **necrosis detector, not a truth-checker**: it fires only on mechanically
decidable defects — a genus where a species belongs, a point masquerading as a band, a deciding
field with no source, a rainfall band that matches nowhere on the island, a row copied byte-for-byte
between two plants. It must never try to become a better global table; the holistic meeting is
handed back to the living. Note that `gate.py` reads a structured record store (`spine.jsonl`) from
when this repo was attached to the wider Meta-Windfall body; in this standalone repo the same
criteria are applied by hand to the prose in [plant-copy.md](plant-copy.md).

## Provenance notes worth keeping

- **Citrus greening (HLB).** The Asian citrus psyllid vector has been established statewide since
  2003; the *disease* has never been found in Hawaiʻi, and active surveillance works to keep it out.
  Sources: CTAHR PD-112; USDA APHIS; state surveillance reporting. The record reflects vector-here,
  disease-not, and holds the orchard's alarm lightly for a dooryard tree.
- **Longevity spinach (*Gynura procumbens*) and sissoo / Brazilian spinach (*Alternanthera
  sissoo*).** Ferns and PFAF carry the plants but no usable climate bands; their climate lines are
  lived Puna ground-truth, labeled as such. Sissoo is a *sterile* cultivar of *A. sessilis* (a
  serious Hawaiʻi weed) — it sets no seed and stays put, which is why it is safe to grow here and
  its weedy parent is not.
- **The canoe and native plants** (noni, kukui, kō, ʻuhi, hōʻiʻo, ʻawa) lean on the ethnobotanical
  and extension record and on lived knowledge; Elevitch's Pacific agroforestry profiles are the
  recommended cross-read to firm their bands.
- **The Part V understory spices** (black pepper, cardamom, vanilla) are Ferns bands, converted.
  Cardamom's are the tell: it wants 2,000–4,900 ft and 50% shade, i.e. the coffee band under a
  canopy, not the coast — the record places it, not a wish. Vanilla's one-morning flower and
  obligate hand-pollination (its wild bee absent here) are horticultural fact, and the Edmond
  Albius history is well documented.
- **Katuk** carries a real, narrow hazard held at its true size: Ferns says "none known," but the
  medical record shows heavy daily consumption of *raw* katuk juice (a 1990s Taiwan slimming fad)
  caused bronchiolitis obliterans. The record states it as *dose and preparation* — cook it, eat
  it as a vegetable, do not juice it by the pitcher — not as a blanket alarm on an everyday
  Southeast Asian green. This is the [[psf-project]] held-lightly discipline applied to a food
  hazard rather than a pest.
- **Star fruit (carambola)** carries a genuine, non-negotiable caution: caramboxin, a neurotoxin
  that sound kidneys clear and failing kidneys cannot. Unlike the monoculture-pest judgments, this
  one is *not* held lightly — it is stated plainly, because the frame does not change the fact.
  Named early, per the hazards convention.
- **Abiu** ships with an explicit gap: Ferns carries no firm rainfall band, so the record labels
  the number unverified and reasons from the plant's Amazon-rainforest ecology. It is now first in
  line for the Elevitch/Morton cross-read (the same move that resolved acerola below).
- **Acerola** is the worked example of the recrystallization pass: its bands were flagged
  "unverified" against a thin Ferns entry, and are now cross-read against Morton, *Fruits of Warm
  Climates* — real cold tolerance (mature to 28°F), a drought-adapted low/medium-rainfall habit
  (it may hold fruiting until the rain returns, which repositions it toward the drier ground), the
  Hawaiʻi cropping pattern (a May flush, then small ones to December), and the counterintuitive
  vitamin-C curve (highest green, falling as it ripens). The pattern for the rest: replace the
  hedge-word "unverified" with a sourced band and a named cross-read.
- **Māmaki** is the one endemic on the list and does not belong to the horticultural databases at
  all. Its band is read from Native Plants Hawaiʻi / CTAHR / DLNR (wet-to-mesic forest understory,
  200–6,000 ft), its propagation from ʻUlu Cooperative practice, and its ecological weight — a
  stingless island nettle, sole host of the Kamehameha butterfly (pulelehua) — from the native
  record. It is labeled *native range, not a raster*, the endemic sibling of the lived-band rule.

## The open sourcing work

The proposed list is now written (Part V of [plant-copy.md](plant-copy.md): black pepper, cardamom,
vanilla, katuk, winged bean, roselle, abiu, star fruit, and the native māmaki). What remains is
depth, not breadth:

- Cross-read the tropical-fruit entries against **Elevitch** and **Morton** where Ferns is thin —
  this is the core of the record-by-record **recrystallization** pass. The abiu (no rainfall band)
  and the acerola (thin bands) are first in line.
- Firm the canoe/native bands (noni, kukui, kō, ʻuhi, hōʻiʻo, ʻawa, cacao) and the māmaki against
  Elevitch, CTAHR, and the native record.
- Firm the two lived-band greens (longevity, sissoo) and the Part V bands where they were converted
  from a single database — cardamom, vanilla, and katuk especially — against a second source.
- Resolve the citrus HLB note against a clean, current CTAHR / HDOA reading when one parses.
- Reconcile the cross-plant guild claims (the provisional "by year five the ʻulu is over it" beats)
  in the placements/guild pass, which is written last against the whole integrated set.
