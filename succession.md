# Succession — the physics of the planting order

A living document, broad to specific, anecdote to quantitative. It holds *why* plants go in when
they go in, and it is the engine the horizontal layer (companion / placement / difficulty) is
**compiled from** — not authored beside. See [MAP.md](MAP.md) for how it sits among the others, and
[SYNTROPY.md](SYNTROPY.md) for the ground beneath this one — what succession is *for*, and where the
apparatus below comes from.

The founding correction (Freely, session 2 of 2026-07-17): **there is no fixed planting order.**
[plant-copy.md](plant-copy.md)'s "wet coast — a planting order" was an artifact of sequencing. Order
is not a property of the list; it is a property of *a site at a moment* — a function of (a) the
plant's own needs, (b) what the ground already supplies, and (c) what companions could supply the
rest. Order is **derived per site**, not written once. This document holds the logic that derives it.

---

## I. Broad — the theory

- **Succession is the product, not the metaphor.** The tool's real work is moving a person from
  seeing land as inert substrate to seeing it as a living community that is already *going
  somewhere*. Every planting is an intervention in a succession already under way. See
  [PRAXIS.md](PRAXIS.md) for the inner side of this.
- **Pioneer → secondary → climax.** Bare/ruined ground wants pioneers (fast, soft, self-sowing,
  often "weeds"); they build soil and shade; secondary species follow into what the pioneers made;
  long-lived canopy closes last. A food forest telescopes this — we plant several stages at once and
  *manage the timing* rather than wait decades.
- **Stratification.** A mature system fills every layer — ground cover, herb, shrub, sub-canopy,
  canopy, vine, and the root/rhizome zone below. Light not caught by one layer is caught by the
  next. The PSF role tags (ground cover / understory / shrub / sub-canopy / canopy / vine) are the
  strata.
- **Disturbance and pruning are tools, not damage.** Cutting a nitrogen-fixer or a pioneer is a
  *transaction*: it drops leaf-mulch and sheds root-nitrogen at the same moment, feeding whatever is
  beside it (Götsch's core move). Pruning a pioneer *stimulates* the system rather than overpowering
  it — which is why the biggest difficulty-reducer is usually a pioneer already on site, cut hard.
- **Boundedness seam (per [psf-project] value):** this document describes pioneer *dynamics* — it
  does **not** catalog every pioneer as a crop. Cecropia, melochia, cane grass live here as named
  exemplars of *how pioneers behave*, summoned per-site by the future conversational layer, never
  resident as display entries. The engine is bounded; the substrate it reasons over is not.

## I-b. The apparatus — two axes and a site reading

Added 2026-07-17 (session 3) from Götsch via [SYNTROPY.md](SYNTROPY.md) III. Everything in §II and
§III below is expressible in these terms, and the horizontal layer should be compiled *in* them.

**Axis 1 — stratum.** Where the plant sits in the light. Götsch reads eleven in the tropics, working
five: emergent · high · medium · low · groundcover. PSF's `str:` field is this axis, already carried
on every shipped record (`ground` / `shrub` / `sub-canopy` / `canopy`). Shade shares per stratum are
adjustable — raise one by lowering its neighbor — and total well over 100% because plants of
different heights and lifespans share the same ground without competing. **An unfilled stratum is an
opening, and a weed will take it.**

**Axis 2 — successional class.** When the plant belongs in the life of the system, by lifespan and
by how much accumulated life it needs beneath it: **placenta 1/2** (≤2 yr) → **secondary 1**
(~10–20 yr) → **secondary 2** (~60–80 yr) → **climax** (80–350 yr). PSF does not currently carry
this field. It should.

The axes are independent, and that independence is the mechanism. Three plants can share a stratum
and differ only in class, and their handover over time *is* the succession — prune the short-lived
one, the longer-lived one stretches into the light and eats the prunings, and eventually retires it.
**A missing successional class is a stall; a missing stratum is a weed.** A full consortium holds a
representative of every stratum from every class, all planted at once.

**The site reading — consolidated life.** Cutting across both axes, a property of the ground rather
than of any plant: **colonization** (raw substrate; Götsch's own illustration is ʻōhiʻa taking a 1960
Kona lava flow) → **accumulation** (banking sun as organic matter; leathery leaves, little
mammal food; where most degraded land sits and stays) → **abundance** (enough consolidated life to
feed large mammals with no external input).

**The crutch.** The quantity that makes the whole thing computable:

> **crutch = (life the species requires) − (life the site has consolidated)**

The crutch is what must be supplied by hand — fertility, water, shade, wind shelter, attention. Its
size predicts pest and weed pressure (pests report the mismatch; they are not the problem, they are
the measurement). It shortens over time under syntropic management and does not under conventional
or organic. And it is the thing PSF has been calling **difficulty** all along: §III.3 below derived
`difficulty = the unmet-needs remainder` independently, before the source was read. Same equation.

Two constraints ride along with it: **do not step backward in succession** (no accumulation-system
species into ground already supporting abundance-system species), and **do not skip stages** —
forcing fertility artificially buys exactly the weed and pest explosions that then get blamed on
diversity.

## II. Specific — the mechanics (quantitative, from raw/)

Load-bearing pairings and timings, each traceable to a plant's [raw/](raw) record. **These are
currently provisional** — several live inside individual copy records as one-sided claims and must be
reconciled here, against each other, in the horizontal pass.

- **Nurse-then-fruit (the guild spine):** ice cream bean (#10) and gliricidia (#11) fix nitrogen,
  coppice, and cast the ~50 % shade that cacao (#44) and coffee (#15) *require* as understory. The
  nurses' "a snack" / "no crop" lines are earned by what they let the understory fruit do. Plant
  nurse first; plant cacao/coffee *into* the shade it makes, never into open ground.
  → In the apparatus: nurse and understory occupy *different strata*, and the pairing works because
  the nurse is a *shorter-lived class* than what it shelters. Götsch's cocoa systems are the worked
  case, and he notes cocoa's own pruning can supply 30% of the system's biomass — the understory
  feeds the guild too, it is not only a beneficiary.
- **Canopy-then-understory:** ʻulu (#12) is slow ~3 yr, deep shade by year ~5 — "that is when the
  kalo (#2) and the cacao go in." Kalo tolerates the light shade a closing canopy throws; it *starts*
  when the sun plants stop.
- **Windbreak-then-tender:** banana (#9) / kō (#40) shelter young ʻulu and cacao from wind on the
  windward side while they establish, then are cut for mulch.
- **Pioneer-dies-on-purpose:** pigeon pea (#6) lives 1–5 yr then dies, leaving soil a tree can stand
  in — "by year five the ʻulu is over it." The death is the hand-off. (Provisional cross-claim: check
  the ʻulu timeline against the pigeon-pea lifespan when reconciling.) **Corroborated:** Götsch lists
  *Cajanus cajan* by name among the accumulation-system species that build a bridge toward abundance
  on soils at pH 4.3 with 1 ppm bioavailable phosphorus.
- **Erosion pairing:** ginger (#4) on a slope must be planted *with* something — bare ground under a
  ginger patch erodes. A companion is not optional here; it is the only cost the plant carries.
- **Native web inside the guild:** māmaki (#59) sited ~2–3 ft off breadfruit with roselle (#56) and
  lemongrass (ʻUlu Coop practice) — the guild built to hold the endemic (and the Kamehameha
  butterfly) inside it, not only the carried crops.
- **The senescence signal (new, and it touches every record):** flowering is information and it
  travels. A plant allowed to flower and seed tells the whole system to age, braking growth
  everywhere — Götsch's goat's-beard-grass case, and the mechanism behind Freely's rule to prune
  weeds *before* they flower. Consequences for the horizontal layer: prefer companions with long
  vegetative cycles; time prunings against flowering, not against the calendar; a fast-cycling weed
  left to flower is a system-wide cost, not a local one. Cross-check every "Forget" beat in copy that
  currently implies a plant may simply be left to seed.
- **Placenta, properly named:** the kitchen-door annuals (Part IV) and the fast greens are not a
  lesser tier of the list. In the apparatus they are *placenta 1 and 2* — the organ that grows the
  forest, planted at maximum density, expected to say goodbye. This reframes the chili-by-the-door
  (#18) from a modest entry point into a structurally correct first move.

## III. Site-logic — deriving the order

Given a site read (rain, elevation from the map tool) **and** what is already growing there:

1. Where in succession is this ground? Bare/ruined → lead with pioneers + the toughest food
   (noni #38 on raw lava; ʻuala #1; cassava #5). Already-vegetated / some canopy → skip to the
   secondary and understory layers the existing shade allows.
2. For each candidate: are its needs *already met* by the site, or must a companion meet them?
   A plant whose shade/nitrogen/wind needs are already supplied is a level-one prep-set-forget
   *here* even if it is "difficult" in the abstract.
3. **Difficulty = the unmet-needs remainder.** This is the same feature as placement (see
   [psf-project]): difficulty is computed from what the site + available companions cannot yet
   supply. It cannot be assigned until the plant is placed. That is why both are written last, and
   why they are written *here*, from the whole set at once — not down any single plant's column.
   **This is Götsch's crutch** (§I-b) — derived here independently, and now sourced.

**The gap this exposes.** Step 1 needs an input the tool does not have. `site.html` reads the raster:
rain, elevation, derived temperature. That answers *can this species live here*. It does not answer
*what will it cost and what will attack it*, which is a function of consolidated life — readable only
off the vegetation already standing. See [SYNTROPY.md](SYNTROPY.md) VIII: the conversational layer is
not an enrichment, it is **the second axis of the instrument**, and the question it exists to ask is
*what is already growing there?*

**The missing input device** is a Hawaiʻi indicator-plant set — the local equivalent of Götsch's
Cerrado list, where each common volunteer reports a soil condition. What does guinea grass say that
false staghorn fern does not? What does a stand of albizia mean about nitrogen, and strawberry guava
about a site's stalled state, and bare ʻaʻā about where the succession has not started? That is
ethnoecological knowledge the steward holds and no database carries. **A first-pass scaffold now
exists — [INDICATORS.md](INDICATORS.md)** — written ahead of its sourcing, every entry confidence-
tagged, awaiting the lived reading. It also adds a category Götsch's list lacks: the *arrested
states* (albizia, strawberry guava, uluhe, christmasberry) that hold ground for decades instead of
progressing, and so demand the successor-into-a-gap move rather than patience.

---

*Open: reconcile every provisional cross-claim above; then compile the companion/placement/difficulty
layer into copy from this document. First succession batch to firm: the nurse→cacao/coffee guild.
Newly open: tag every record with successional class + lifespan (axis 2 has no field yet); audit the
"Forget" beats against the senescence signal; draft the Hawaiʻi indicator-plant set.*
