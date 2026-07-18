# Indicator plants — reading the second axis

The input device for the reading [SYNTROPY.md](SYNTROPY.md) VIII says the tool cannot currently take.
Rain and elevation come off a raster; **consolidated life does not.** It is read off the plants
already standing on the ground, and this document is where that reading is kept.

Götsch's method leans on a Cerrado indicator list — each common volunteer reporting pH, compaction, a
buried hardpan, a missing micronutrient. His central claim about them is the one to carry over:

> "The indicator plants, contrary to what many think, are not pests, but valuable instruments that
> nature has to heal the open wounds, caused, in most cases, by the human being itself."

Hawaiʻi has no equivalent list. This is a first pass at one.

---

## Status — read this before using anything below

**This document is a scaffold, not a record.** It is the only file in the knowledge layer written
*ahead of* its sourcing rather than distilled from it, and it is marked that way deliberately so the
condition is visible rather than silent.

Every entry carries a confidence tag:

- **[established]** — the species identity, its ecology, and its behaviour in Hawaiʻi are
  well-documented and I hold them with confidence. Still owed a citation to CTAHR / DLNR / the
  invasive-species literature before it ships anywhere reader-facing.
- **[inferred]** — reasoned from the plant's ecology and from Götsch's framework. Plausible, not
  observed. Flagged per the `raw/` **Inferences** convention.
- **[needs ground-truth]** — the reading that matters most is precisely the one only lived Puna
  experience can settle. These are questions addressed to the steward.

Per the [SOURCES.md](SOURCES.md) firewall, **nothing here may supply a number to a plant record.**
Indicators report the state of *ground*, not the requirements of *species*. Those are different
claims and they must not leak into each other.

Where the lived reading and this draft disagree, the lived reading wins and the disagreement is the
finding — the [add-lived-bands.py](add-lived-bands.py) law applies here as everywhere.

## How to read an indicator

Three questions, in order. The plant is the answer to all three.

1. **Where is this ground on the axis?** Colonization (raw substrate, no soil) → accumulation
   (banking sun as organic matter) → abundance (enough consolidated life to feed large mammals with
   no input).
2. **What specifically is missing?** The indicator names the limit — compaction, acidity, a
   nutrient, water that stands, water that never comes, fire.
3. **Is the succession moving or stalled?** This is the question Götsch's Cerrado list mostly does
   not have to ask and Hawaiʻi's does. Several of the most common covers here are not stages passed
   through. They are **arrested states** that hold ground indefinitely, and they change the whole
   recommendation — see §IV.

Then the crutch follows: `crutch = (what the species needs) − (what this ground has)`. The indicator
sizes the second term.

---

## I. Colonization — substrate, not soil

Ground where the succession has not begun, or has been returned to zero.

**Bare ʻaʻā and pāhoehoe** · **[established]**
No soil, no water retention, extreme surface heat, all nutrients locked in unweathered rock. ʻAʻā
(broken, clinkery) offers root pockets and shade at depth; pāhoehoe (smooth, sheeted) offers almost
nothing until it cracks. The distinction is practical, not cosmetic — ʻaʻā is plantable far sooner.
*Reports:* the true zero. *Crutch:* total for anything demanding; near-zero for the right pioneer.
*Suggests:* this is where noni (#38) belongs, and the standing recommendation to promote it toward
the front of the wet-coast succession is exactly right. Also ʻuala (#1) into pockets with any pocket
of ash or organic catch.

**ʻŌhiʻa lehua** (*Metrosideros polymorpha*) · **[established]**
The primary colonizer of new lava, and Götsch's own illustration of a colonization system — his book
uses a photograph of ʻōhiʻa taking a 1960 flow south of Kona. Endemic, enormously variable in form
across moisture and elevation.
*Reports:* the succession has started, and started natively. On young substrate, the earliest
consolidated life there is.
*Crutch:* still large for food crops, but the ground is no longer inert.
*Suggests:* do not clear it. It is the free head start, and under Rapid ʻŌhiʻa Death (ROD, *Ceratocystis*)
it is also a plant not to wound — sap-flow wounds are an infection route. **Any praxis note involving
cutting ʻōhiʻa must carry the ROD caution.** *[needs ground-truth: current ROD guidance for the
specific district.]*

**Lichens, mosses, ferns in cracks** · **[established]**
The first biology. Where these are thickening, weathering is under way.
*Reports:* colonization proceeding on its own schedule. *Suggests:* patience is cheaper than input
here; a fermented-scraps application (see [PRAXIS.md](PRAXIS.md)) is the highest-leverage thing a
person can do, because the limit is biology, not minerals.

## II. Accumulation — organic matter banking, food for large mammals not yet

**Uluhe / false staghorn fern** (*Dicranopteris linearis*) · **[established]**
The thicket fern that blankets wet disturbed slopes in dense, springy, waist-to-chest mats.
Aluminum-tolerant, thrives on acidic, low-phosphorus, leached ground, and is a genuine native
colonizer of landslides and disturbance.
*Reports:* wet, acidic, leached, low-phosphorus ground; a real accumulation system; also **recent
disturbance**, since uluhe takes light gaps.
*Crutch:* large for anything demanding. Phosphorus is the likely first limit.
*Suggests:* Götsch's rule against skipping stages applies hard here — importing fertility to plant a
fruit tree into uluhe buys pest pressure. Better: cut in strips or islands (his "concentrating
energy" move), pile the cut fern on the line, and plant the toughest placenta into the concentrated
strip. Cassava (#5) and ʻuala (#1) are the candidates. **But see §IV — uluhe also arrests.**

**Guinea grass** (*Megathyrsus maximus*, formerly *Panicum maximum*) · **[established]**
Tall bunchgrass, huge biomass, dominant on lowland disturbed and abandoned ground.
*Reports:* an accumulation system with meaningful fertility — guinea grass is not a poverty
indicator; it wants better ground than the fire grasses do. Also reports **abandonment** and,
critically, **a fire cycle** where it has cured and stood.
*Crutch:* moderate, and shrinking fast if it is managed rather than fought.
*Suggests:* this is the single most favourable starting condition on this list, and the one most
often treated as a problem. Götsch's brachiaria method transfers almost directly: strip it 80 cm
wide, fluff the strip, mow several metres each side and pile the cuttings on the line, plant into the
concave. It regrows and you cut it again. Note his stratum rule — pair it with trees of a *different*
stratum, and cut **before it flowers** (§V).
*[needs ground-truth: does guinea grass behave this tractably in Puna, or does the regrowth rate
outrun a person with a machete?]*

**Cane grass / California grass** (*Urochloa mutica* and kin) · **[inferred, identity needs confirming]**
Coarse sprawling grasses of wet lowland ground, often where water sits.
*Reports:* wet, frequently a drainage problem; accumulation.
*Crutch:* moderate; the limit is more likely water sitting than fertility.
*Suggests:* the mound-and-plant logic already in the fit engine's rain asymmetry — too much water is
a drainage problem a mound solves. Kalo (#2) is the plant that wants what everything else is
complaining about. *[needs ground-truth: which of these grasses is actually the common one, and where.]*

**Haole koa / leucaena** (*Leucaena leucocephala*) · **[established]**
Dry and mesic lowland thickets, especially leeward and on disturbed roadside ground. Nitrogen-fixing
legume, coppices hard, seeds prolifically.
*Reports:* dry-to-mesic accumulation, and **nitrogen already being supplied**. Often alkaline or
at least not strongly acidic ground.
*Crutch:* smaller than it looks, because the nitrogen problem is solved and standing.
*Suggests:* in Götsch's terms this is a free secondary-1 nurse that arrived on its own. Cut hard,
drop everything, plant into the strip. Pigeon pea (#6) is doing the same job on the shipped list;
where haole koa is already present, the pigeon-pea step may be **skippable** — the site supplies it.
This is the clearest single example of an indicator shortening the crutch to zero for a whole step.

**Fountain grass** (*Cenchrus setaceus*) · **[established]**
Leeward and Kona-side lava and dry ground; fine bunchgrass that carries fire readily.
*Reports:* dry, hot, low elevation-to-mid leeward; a **fire-driven arrested state** more than a
progressing accumulation.
*Crutch:* large, and water is the binding limit, not fertility.
*Suggests:* the honest answer on much of this ground may be the tool's designed "nothing on this list
will feed you here" — or a very short list. Acerola (#27), post-recrystallization, reads as a drier-
ground plant and is a genuine candidate here; that repositioning now has a second use.

**Kikuyu grass** (*Cenchrus clandestinus*) · **[established]**
Upcountry pasture sod, cool and mesic, dense mat-forming.
*Reports:* cooler elevations, real soil, decent fertility — this is comparatively *good* ground.
Also reports grazing history and likely compaction from stock.
*Crutch:* small on fertility, real on compaction.
*Suggests:* the compaction is the thing to read. Götsch's guanxuma equivalent — a dense mat over a
pan. Deep-rooting first (ʻuhi #41, cassava #5) before anything fussy. *[needs ground-truth: is this
the right upcountry read, and where does the frost line actually bite?]*

## III. Approaching abundance — ground that will feed people

**Volunteer papaya, banana clumps, self-seeded chili, purslane** · **[established for purslane,
inferred for the rest]**
Götsch names purslane (*Portulaca oleracea*) explicitly as an indicator that appears "in the best
soils, protecting them." Papaya is *his* example of a plant that only comes right in an abundance
system — on his own farm after forty years, papaya and kalo are the demanding crops he can finally
grow.
*Reports:* abundance, or its near edge. Fertility, structure, and biology are in place.
*Crutch:* small to none. **Do not step backward** — putting accumulation-stage species into this
ground is Götsch's first named error.
*Suggests:* go straight to the demanding entries. This is where the understory spices (Part V), cacao
(#44), and the fussier fruit belong. It is also the ground where the tool currently over-recommends
pioneers, because it cannot see it.

**Deep leaf litter, worm casts, mycelium in the litter, dark friable soil** · **[established]**
Not a plant, but the reading that outranks the plants.
*Reports:* the thing the whole axis is actually measuring.
*Suggests:* trust it over any species-level indicator that disagrees.

## IV. The arrested states — Hawaiʻi's particular problem

This section has no counterpart in Götsch's Cerrado list, and it is the most important part of this
document. Several dominant covers here are **not stages the succession passes through.** They hold
ground for decades, and reading them as "early accumulation, be patient" gives exactly the wrong
advice. They are why succession here needs a hand rather than time.

**Strawberry guava** (*Psidium cattleianum*) · **[established]**
Forms dense monotypic stands in wet and mesic forest, shades out the understory, mats the root zone,
and does not hand over to anything.
*Reports:* an accumulation system that has **stopped**. The soil beneath is often reasonable.
*Crutch:* the limit is not fertility — it is light and the absence of a successor.
*Suggests:* this is precisely Götsch's stall case (the cecropia with no guapuruvu beneath it). The
intervention is not fertility, it is **introducing the missing successional class into a cut gap.**
Clear-fell in patches, plant every stratum at once into the opening, use the cut biomass on site.
Note that the fruit is food and the wood is good — an arrested state is also a standing resource.

**Albizia** (*Falcataria moluccana*) · **[established]**
Enormous fast nitrogen-fixing canopy tree, brittle, storm-dangerous, dominant across lowland Puna.
*Reports:* nitrogen in abundance — arguably the largest free fertility input on the island — over
ground that may otherwise be young. Also reports real hazard: these limbs fall and kill.
*Crutch:* nitrogen is solved. Light is the constraint, and safety is a genuine cost.
*Suggests:* the most interesting entry on this list. In Götsch's frame albizia is a secondary-1
emergent doing its job magnificently with nothing beneath it to hand over to. The syntropic reading
is not "remove the invasive" but "supply the successor and take the nitrogen" — plant the canopy and
sub-canopy classes into managed gaps, let the albizia feed them, and let it retire as they rise.
**This directly contradicts standard Hawaiʻi invasive-species guidance**, which is removal-first.
That tension is real, it is not mine to resolve, and it must be argued rather than assumed — see the
native/introduced discussion in [SYNTROPY.md](SYNTROPY.md) VI. *[needs ground-truth: what does the
steward actually do with albizia, and what does the district's practice say?]*

**Uluhe, in its arresting mode** · **[established]**
The same fern as §II. Its mats can suppress woody regeneration for a very long time, holding a slope
in accumulation indefinitely.
*Suggests:* read it twice — as a stage where woody seedlings are coming through it, as a stall where
they are not. The presence or absence of tree seedlings *in* the mat is the tell.

**Christmasberry** (*Schinus terebinthifolius*) · **[established]**
Dense thickets on dry and mesic disturbed lowland; allelopathic tendencies.
*Reports:* arrested mesic-to-dry accumulation, often on old pasture.
*Suggests:* same structural move as strawberry guava — the successor is what is missing.

**Cured standing grass, anywhere** · **[established]**
Guinea grass or fountain grass that has flowered, seeded, and dried in place.
*Reports:* two things at once, and both matter. **Fire load**, which is a safety and a succession
question — fire returns this ground to zero and selects for the grass again. And, per §V,
**senescence broadcast to the whole system.**

## V. The reading that applies to every entry above

**Flowering is information, and it is contagious.** A plant allowed to flower and seed tells the
whole community to age, and growth slows system-wide rather than locally
([SYNTROPY.md](SYNTROPY.md) V). Every grass on this list flowers fast.

So the single most transferable technique in this document is not a species choice. It is: **cut the
cover before it flowers.** That one act keeps the system vegetative, keeps the biomass coming,
suppresses the fire load, and removes the aging signal — and it costs nothing but timing.

Götsch's paired warning applies too: a plant from a much earlier accumulation stage mixed into a
later one should be *removed*, not merely pruned, because pruning leaves it cycling faster than its
neighbours and broadcasting age from inside the system.

---

## What is owed on this document

1. **The steward's pass.** Every `[inferred]` and `[needs ground-truth]` tag is a question. The
   lived reading wins; where it disagrees with the draft, the disagreement is the finding and gets
   written down as one.
2. **Sourcing.** CTAHR, DLNR Forestry & Wildlife, and the Hawaiʻi invasive-species literature for the
   `[established]` entries, per the [SOURCES.md](SOURCES.md) authority order. Until then this file
   is knowledge held, not knowledge sourced, and it must not feed reader-facing copy.
3. **The missing entries.** This list is short and lowland-biased. Absent: the wet-forest natives
   beyond ʻōhiʻa (hāpuʻu and what a tree-fern stand reports), the mesic and dry native remnants,
   ironwood, gorse and the upcountry pasture weeds, banana poka, the ginger complex, the ground the
   ranches hold, and everything above the frost line.
4. **The decision this enables.** Once the readings are ratified, the conversational layer has a
   script: *what is growing on your ground?* → indicator → successional state → crutch per candidate
   → the derived order. That is the whole second axis, and it turns
   [succession.md](succession.md) III from a stated intention into a runnable procedure.

*Open: does this want to become structured data (`raw/`-style, one file per indicator) rather than
prose? Probably — but only after the readings are ratified. Structuring a guess hardens it.*
