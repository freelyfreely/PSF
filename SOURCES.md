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

**Hawaiʻi-calibrated empirical models sit at tier 1 for this island's bands** (added session 6,
2026-07-18). A climate-suitability model *fitted to observed plant distributions on this island* is
local, decidable science — it belongs in tier 1 and outranks a generic tropical database (tier 3) for
a numeric band *here*, even though a global database outranks it elsewhere. The worked case is ʻulu:
**Mausio, Miura & Lincoln (2020), *PLoS ONE* 15(5):e0228552** re-fit the EcoCrop breadfruit parameters
to 1,200 naturalized trees mapped across Hawaiʻi and found the generic bounds "highly restrictive…
especially in terms of rainfall." Its precipitation figures (optimal 1,500–4,000 mm, absolute
750–8,000 mm) now carry ʻulu's band over Ferns'. Authority is scoped: this outranks Ferns *for
Hawaiʻi rainfall*, not for, say, propagation or a plant it never studied.

**Expand a filtering band, don't contract it, whenever a real source permits** (the session-6 rule).
The tool's fit model treats *dry-beyond-tolerance* as `poor` and *wet-beyond* as a mere `caution`, and
dims poor fits rather than deleting them — all because **the reader knows their own ground.** A band set
too narrow commits the costlier error: it reads a plant `poor` on ground it actually thrives on,
overriding the reader on their own land. So when the evidence is genuinely ambiguous between a tighter
and a wider band, and a citable source supports the wider one, take the wider one. This is *not* licence
to invent headroom — an unsourced wide number is still necrosis (the 157-in upper was correctly flagged
until Mausio sourced it). It is a rule about which way to resolve a real ambiguity: toward the reader's
latitude, with a source.

**The wisdom base is a separate axis, not a higher tier** (added session 3, 2026-07-17). Götsch's
syntropic method and Freely's own writings — collected in [SYNTROPY.md](SYNTROPY.md) — are authority
over *mechanism, stance, and purpose*: what succession is, why pruning works, what difficulty
actually measures, what the tool is for. They are **not** authority over any number in a record. A
band comes from tier 1–5 above or it does not ship. This firewall matters because the wisdom base is
persuasive, general, and would otherwise quietly start supplying facts it does not hold: Götsch's
species are Brazilian, his soils are not ours, and the English text in hand is an unofficial machine
translation. Take the apparatus; leave the numbers.

## The databases, and what each is good for

| Source | Reach | Good for | Watch |
|---|---|---|---|
| **Ferns — Useful Tropical Plants** (tropical.theferns.info) | Ken Fern's tropical corpus | The primary cultivation bands: rainfall, temperature, altitude, soil, propagation, uses | Thin or absent for a few kitchen crops and gathered plants; units are metric/mm |
| **PFAF** (pfaf.org) | The temperate-first sibling of Ferns, same lineage | Cross-checking Ferns; sometimes the more current of the two | Temperate bias — its climate bands can understate a plant's tropical range |
| **Elevitch, Species Profiles for Pacific Island Agroforestry** (agroforestry.net) | Extension-grade Pacific agroforestry | Food *and* support species written almost in this project's spirit; the strongest fit for the canoe plants and the guild | *To be integrated* — the recommended next cross-read |
| **CTAHR / UH Mānoa extension** (ctahr.hawaii.edu) | Hawaiʻi-specific | The real local pest, disease, and climate picture | The authoritative word on anything Hawaiʻi-particular |
| **USDA APHIS / HDOA** | US / Hawaiʻi pest status | Current pest and disease establishment (e.g. the citrus psyllid and HLB status) | — |
| **Morton, Fruits of Warm Climates** | Tropical fruit | The tropical fruit trees where the temperate databases run thin | Older; cross-check current names and pests |
| **Mausio, Miura & Lincoln 2020** (*PLoS ONE* 15(5):e0228552) | Breadfruit, empirically re-calibrated to 1,200 naturalized Hawaiʻi trees | ʻUlu's Hawaiʻi rainfall/temperature bands — tier 1 *for this island* (see authority order) | Scope is breadfruit-on-Hawaiʻi only; a species-and-place-specific model, not a general database |
| **Native Plants Hawaiʻi / CTAHR / DLNR Forestry** (nativeplants.hawaii.edu, dlnr.hawaii.gov) | The endemic and indigenous flora | The one place the databases above cannot help: native plants like the māmaki, read by forest type and elevation, not a raster band | The authority for anything endemic — range, ecology, the native web it sits in |
| **Grower and cooperative practice** (e.g. Hawaiʻi ʻUlu Cooperative) | Working Hawaiʻi farms | Propagation, spacing, guild companions the databases omit — how a plant is actually put in the ground here | Practice, not a controlled trial; corroborate the numbers, trust the placement |
| **Peer-reviewed medical / nephrology literature** | Specific human-health cautions | The load-bearing hazard facts (star-fruit caramboxin and renal risk; the raw-katuk-juice lung injury) | Used only to state a plain caution, never as horticulture |
| **permacultureplants.com** | Long bylined secondary articles | Soft, anecdotal colour only | 403 to plain fetch, reachable only through a real browser; footnoted secondary, never a primary source. Only ʻulu has been cross-read against it |
| **Rebello & Ghiringhello, *Agricultura Sintrópica segundo Ernst Götsch*** (2021) | Götsch's syntropic method, 40 yr of Bahia fieldwork | The **mechanism** layer: strata, successional classes, the colonization→accumulation→abundance reading, the crutch, pruning physiology, indicator plants | Brazilian biomes and species throughout; the *apparatus* transfers, the *species lists* do not. Read via an unofficial machine translation — quote cautiously, and treat any single number as indicative. See [SYNTROPY.md](SYNTROPY.md) |
| **Freely's own writings** (*Boundless Garden* 2019; *Gardens, Borders, Syntropy* 2024; *Syntropy & Technology* 2025) | The project's philosophical spine | Why succession is the product; the syntropy/entropy distinction; the garden-wall critique; fermentation and seed dispersal; the design criteria the tool is judged against | **Not a horticultural source.** Authority over *stance, voice, and what the tool is for* — never over a climate band or a plant fact |

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
  **This judgment now has a stated mechanism** (session 3): in Götsch's reading, pest and weed
  pressure is proportional to the *crutch* — the gap between the fertility a species needs and the
  life the site has actually consolidated. Insects, fungi, and weeds are "the department for the
  optimization of life processes," reporting the true successional state of the ground. So a pest is
  literally a measurement of mismatch, which is why its weight in a monoculture is not its weight in
  a diverse dooryard planting. Held-lightly was the right instinct; [SYNTROPY.md](SYNTROPY.md) IV is
  the reason.
- **"Difficulty" is contextual, not intrinsic.** Any plant not bred into dependence can be a
  level-one prep-set-forget in the right community. The companion — often a pioneer already growing,
  strongly pruned to stimulate rather than overpower — is the largest difficulty reducer there is,
  and it is free and in place. This is why the companion/placement layer and any future
  "difficulty" reading are the same feature, and why they are written last, against the whole
  integrated set. (The engine that derives it: [succession.md](succession.md).)
- **Food hazards sort the same way pests do — frame-dependent vs. frame-independent.** The
  monoculture-word test above has a food-hazard corollary. A hazard that depends on *dose or
  preparation* is held at its true size: katuk caused lung injury only as *raw juice drunk by the
  glassful* (a Taiwan slimming fad), so the record says cook it and eat it, not avoid it. A hazard
  that is *frame-independent* — a real toxin against real physiology — is stated flat, no matter the
  frame: star fruit's caramboxin is dangerous to anyone with kidney disease, full stop. Ask of every
  hazard: does the frame change the fact? If yes, hold it lightly; if no, state it plainly. Both,
  always, named early.

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

**The whole corpus now has `raw/` backing** (session 5, 2026-07-18). Every one of the 56 copy entries
has a provenance record; axis 2 (successional class + lifespan) is complete corpus-wide. Backfilling
the last ~20 records surfaced new flags — the same drift-detection the store exists for:

- **Poha (#30) — CORRECTED in copy.** "Above 800 ft" was a metres→feet slip; Ferns' optimum is 800 m
  (~2,600 ft). Fixed in [plant-copy.md](plant-copy.md); poha is an upcountry crop, not a lowland one.
- **Pumpkin (#45) + ipu (#46) — Ferns is NOT thin for these.** Ferns carries full rainfall/temperature/
  altitude bands for *Cucurbita moschata* and *Lagenaria siceraria*; the Part IV "lived where Ferns is
  thin" framing overstated the gap. Bands added to copy; only the currant tomato (#47) is genuinely
  band-less in Ferns and rides on lived ground-truth.
- **Unsourced reader-facing figures, flagged, not yet resolved** (do not harden into fake numbers):
  chaya (#21) altitude 4,300 ft is not a Ferns figure; cempedak (#29) "best under 450" reads as an
  m/ft ambiguity against Ferns' 1,200 m ceiling; citrus (#48–50) rainfall 40–60 in and altitude
  3,000 ft are not in Ferns (which gives no annual rainfall band for citrus, only a seasonality rule).
- **Annonacin (soursop #26) — an unsourced hazard flag.** *Annona* spp. carry annonacin, linked in
  Caribbean studies to atypical parkinsonism in heavy consumers. Held in the raw record as a cross-read
  target (nephrology/neurology literature, as star fruit's caramboxin was) — **not** in reader copy
  until sourced. The firewall runs the same for hazards as for bands.

**The shipped 19 have `raw/` backing** (session of 2026-07-17). Every plant the tool actually
ships (#1–19) has a one-file-per-plant provenance record in [raw/](raw), each shipped band traced to
its Ferns source in the source's own units with the conversion kept — the store the gate's
necrosis-check reads against. The backfill surfaced three **deciding fields that did not cleanly trace
to Ferns** (the exact defect the gate exists to catch); all three have now been **cross-read and
resolved** — what remains is applying the corrections to the shipped artifacts (`site.html` `P` array
and [plant-copy.md](plant-copy.md)):

- **ʻUlu (#12) — RESOLVED, and expanded (session 6).** The shipped 157-in upper was *unsourced* — Ferns
  caps at 3,000 mm/118 in, Elevitch/Ragone gives 1,500–3,000 mm, and 157 also happened to be ginger's and
  ice-cream-bean's tolerated upper, so it was rightly flagged as possible day-1 bleed. It was briefly
  contracted to ~120 in on those two sources — then **reversed** when the Hawaiʻi-calibrated
  **Mausio et al. 2020** (see authority order) was found: precipitation optimal 1,500–4,000 mm, absolute
  750–8,000 mm, expanded *because* generic bounds under-fit Hawaiʻi's naturalized trees. **Shipped now
  `rain:[60,157]` / `rainTol:[30,315]`** in `site.html` and copy #12 — the 157 restored *with a source*
  and the tolerance widened past the old unsourced 180. The worked example of the expand-when-justifiable
  rule above. (The Elevitch read also *added* the pH Ferns lacked, 6.1–7.4.)
- **Banana (#9) — FIRMED.** First-food now **CTAHR-sourced at 15–18 months** (shipped year-1 low end is
  optimistic → ~15 mo). The 4,000 ft ceiling stays a **labelled lived narrowing** of Ferns' 2,400 m
  (conservative, not an error). Bands read from *M. acuminata* as the proxy for shipped *Musa* spp.
- **Ice cream bean (#10) — NARROW.** Elevitch has **no *Inga* profile** (non-Pacific tree); Ferns and
  PFAF both put the natural range at 110–540 m. The shipped "350–5,000 ft natural range" is unsourced —
  narrow copy to Ferns' 110–540 m natural / 2,200 m cultivation.

One softer flag: **ʻōlena (#3)** is leaned shadeward of Ferns (which rates it full-sun-*or*-light-shade);
the copy's shade preference is a *succession-placement* claim, not a climate reading, and is marked so
it is never cited as a Ferns fact.

**Two shipped-artifact corrections are therefore owed** (`site.html` + copy): ʻulu rain upper
157 → ~120 in, and ice-cream-bean natural range → 110–540 m. Neither is edited silently here — both
live in the shipped `P` array, which is handed to the steward as the finding.

The proposed Part V list is also written ([plant-copy.md](plant-copy.md): black pepper, cardamom,
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
