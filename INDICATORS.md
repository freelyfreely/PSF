# Indicator plants — reading the second axis

The input device for the reading [SYNTROPY.md](SYNTROPY.md) VIII says the tool cannot currently take.
Rain and elevation come off a raster; **consolidated life is only partly rasterable.** Lava-flow surface
age (USGS) proxies how far soil development has likely gone — a first-pass seed — but the finer read is
off the plants already standing on the ground, and this document is where that reading is kept
(**raster-seeded, conversation-refined**).

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
  invasive-species literature before it ships anywhere reader-facing. **Entries marked "lived
  ground-truth" are the highest tier there is** (per [SOURCES.md](SOURCES.md) authority order) — the
  steward's own field observation — and are labeled as lived, never dressed up as a raster reading.
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
nothing until it cracks — but where it cracks, it *channels rain*, and the cracks become linear
oases. The distinction is practical, not cosmetic — ʻaʻā is plantable sooner, but a rain-fed
pāhoehoe crack is where the first food actually grows.
*Reports:* the true zero, except along the water-channeling cracks. *Crutch:* total for anything
demanding; near-zero for the right pioneer in a crack.
*Suggests:* this is where noni (#38) belongs, and the standing recommendation to promote it toward
the front of the wet-coast succession is exactly right. Also ʻuala (#1) into any pocket of ash or
organic catch.

**What actually colonizes bare lava here** · **[established — lived ground-truth, not a raster]**
From five days (2024) walking 30+ miles of bare lava west of Kalapana, foraging the whole subsistence
— which came down to **coconut, noni, and roughly a thousand tiny wild *Passiflora foetida* fruits.**
The two happiest, most abundant colonizers in the rain-channeled pāhoehoe cracks:
- **ʻuhaloa** (*Waltheria indica*) — indigenous, drought-hardy, medicinal (the sore-throat root).
- **love-in-a-mist / wild passionfruit** (*Passiflora foetida*) — naturalized, and on this ground a
  genuine forage crop, not a weed: thousands of small fruits.
With, less densely: **noni** (#38) here and there, and **rattlepods** (*Crotalaria* sp., naturalized,
nitrogen-fixing — a pioneer legume doing the haole-koa job on rawer ground).
*Reports:* that the colonization story on bare pāhoehoe is **crack-hydrology first, species second** —
the plants mark where rain concentrates. *Suggests:* the earliest edible layer on new lava is real
and is mostly *already there to be recognised* (a [PRAXIS.md](PRAXIS.md) recognition case) rather than
planted; the plantable additions are noni and, into caught pockets, ʻuala.

**ʻŌhiʻa lehua** (*Metrosideros polymorpha*) · **[established]**
The primary native colonizer of new lava, and Götsch's own illustration of a colonization system —
his book uses a photograph of ʻōhiʻa taking a 1960 flow south of Kona. Endemic, enormously variable
across moisture and elevation.
*Reports:* the succession has started, and started natively.
*Suggests:* **leave it be.** (Steward's instruction, 2026-07-17.) ʻŌhiʻa was here long before people
and has already suffered much; it is not a plant to cut into, gap, or manage as substrate. On Rapid
ʻŌhiʻa Death: the wound-infection pathway is real but the wounds are **almost entirely feral-ungulate
bark-scraping**, not a reason to frame ʻōhiʻa as a plant one prunes — the opposite. Any earlier
implication that ʻōhiʻa is a clearable head-start is withdrawn. It is a neighbour, not a resource.

**The coastal strand on new lava** · **[established — lived ground-truth]**
At the ocean edge of the same walk, a distinct and *happy* community on very young rock: **naupaka
kahakai** (*Scaevola taccada*, indigenous strand shrub), a **pickleweed-like succulent** (salicornia-
form — likely ʻākulikuli, *Sesuvium portulacastrum*, or a true pickleweed; *[needs ID]*), **beach
morning glory / pōhuehue** (*Ipomoea pes-caprae*, the great sand-and-lava binder), and a **thriving
swath of aloe** (naturalized, and thriving is the word). Coconut throughout.
*Reports:* salt, wind, and drought are the binding constraints here, not fertility or succession
stage — this is a *halophyte* zone, a different axis than the inland colonization one. *Suggests:*
the tool should probably recognise a coastal-strand condition as its own answer rather than forcing
it onto the rain/elevation fit — the plants that work here are salt-selected, and most of the food
list will honestly read "not here." Worth its own thought later.

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

**Cane grass** (*Pennisetum purpureum* / *Cenchrus purpureus*, elephant / napier grass) · **[established — identity corrected by steward, 2026-07-17]**
Tall (to 10+ ft), dense, high-biomass cane grass of wet lowland ground. **Not** *Urochloa* — that was
my error; the common cane grass here is Pennisetum.
*Reports:* wet, fertile, vigorous accumulation — this is high-productivity ground, and a huge standing
biomass source.
*Crutch:* small on fertility, real on the labour of getting through the stand.
*Suggests:* Götsch flags exactly this species-class as *high* stratum — pair it only with trees that
out-top it or with crops of a very different stratum, never with a same-stratum cultivar, because its
cut material resprouts readily and takes the line back. Cut before flower (§V); the biomass is the
gift. Where water also stands, the kalo (#2) drainage logic applies.

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
*Also — it is itself food* **[established, steward 2026-07-17]:** the seeds, soaked and sprouted to
leach the mimosine, are the **third most popular tempeh substrate in Indonesia.** Not a reason to
*plant* it (it needs no help), but a clear candidate for a future **"utilization of existing
naturalized plants"** track — the same move as albizia-for-mushrooms below. The naturalized substrate
is already an unharvested larder; that is a whole expansion the bounded display doesn't touch yet.

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
*Caveat — purslane is not a clean abundance signal here* **[corrected, steward 2026-07-17]:** the
steward has seen purslane happy on **new oceanside lava.** So on Hawaiʻi it reads as opportunistic and
salt/heat-tolerant, not specifically as best-soil the way Götsch's Cerrado reading has it. Treat
purslane as *ambiguous* — corroborate abundance with the litter/structure reading below, never on
purslane alone. A clean instance of the firewall in action: Götsch's indicator does not transfer
unchecked.

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
*Suggests:* the most interesting entry on this list, and the steward confirms the scale — "truly an
enormous ecosystem-pump." In Götsch's frame albizia is a secondary-1 emergent doing its job
magnificently with nothing beneath it to hand over to. Two utilization paths, both **later down the
line**, not near-term display:
- **Mushrooms.** Its high-nitrogen wood is ideal substrate for mushroom cultivation — which would
  make this "invasive" an *extraordinary* food source. (Steward, 2026-07-17. Same track as haole-koa
  tempeh: harvesting the naturalized larder.)
- **Coppice, don't fell-and-replace.** In principle the syntropic "supply the successor, take the
  nitrogen" move works, and chopping young trunks occasionally to keep the pump running is not
  impractical.

**But the overriding consideration is the falling-limb hazard** — these limbs kill, and that outranks
the cleverness. And a real, non-botanical constraint the steward names and the tool must respect:
*most people here (perhaps everywhere) are rigid and mechanical in their thinking, slow to change
unless an embodied insight arises.* A recommendation that asks someone to see their dangerous invasive
as an ecosystem-pump is asking for exactly that shift — so it cannot be *told*, only *occasioned.*
This is the [PRAXIS.md](PRAXIS.md) inner-succession point with teeth: the albizia reframe is
downstream of a change in the person, not upstream of it. Keep it out of the first contact; it is for
someone already moving. The native/introduced tension stands, unresolved by design —
[SYNTROPY.md](SYNTROPY.md) VI.

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
