# Syntropy — the ground beneath the physics

[succession.md](succession.md) holds *why plants go in when they go in.* This holds why succession
is worth building a tool around at all. It is the deepest layer of the knowledge stack and the one
that has, until now, lived only in voice — carried implicitly by the copy's word choices and the
site's dark palette, never written down where it could be reasoned from.

Two bodies feed it. **Ernst Götsch's syntropic agriculture**, as set out in Rebello & Ghiringhello's
*Agricultura Sintrópica segundo Ernst Götsch* (2021), supplies the working apparatus — the strata,
the successional classes, the three system-levels, and the pruning physiology. **Freely's own
writings** (*Boundless Garden*, 2019; *Gardens, Borders, Syntropy*, 2024; *Syntropy & Technology*,
2025) supply the frame the apparatus sits in, and go further than Götsch in one direction: they say
what the whole thing is *for*.

The rule from [SOURCES.md](SOURCES.md) still holds here — this document is philosophy and mechanism,
not climate data. **Nothing in it may be used to state a band in a plant record.** It shapes what the
tool asks and how it speaks; the numbers still come from `raw/`.

---

## I. The distinction underneath everything

> "My emphasis is on supporting syntropy — that is, the ability of life to self-organize and
> spontaneously create dynamic order on all scales. From my perspective, the distinction between
> syntropy and entropy is the fundamental distinction in the universe." — Freely, 2024

Entropy is the running-down that any closed system is subject to. Syntropy is what life does
instead: it concentrates, complexifies, and builds order, and it does this by being an *open*
system — one that takes in flux rather than defending an equilibrium.

The load-bearing corollary, and the one that most changes how the tool should speak: **any system
that can be fully defined and bounded is a closed system**, and will run down. Freely's sharpest
formulation of this is biological — the assumption of life as a closed system striving to maintain a
normative equilibrium is "exactly wrong, and actually a projection of cultural conditioning" — but
it lands directly on garden design, on software design, and on this project's own architecture.

**The garden and its wall.** *Garden* shares a root with *guard*; *paradise* was originally a walled
garden. From inside, the wall is necessary — it protects what is nice from the hostile disorder
outside. But the wall is also the confession: the more entropic the outside, the more the garden
must extract from it to stay nice, and the more the ability to see order self-organize at larger
scales is lost. Freely's resolution is the project's whole horizon:

> "If the garden were to become a self-organizing forest — resilient, intelligent, sovereign, and
> willful; treated as an ally rather than a slave — eventually the walls would no longer be needed,
> because the power of the forest would sustain and evolve itself, and spread into its surroundings."

This is the honest statement of what Prep Set Forget is trying to do. Not to help someone build a
better walled garden. To start something whose success is measured by its spread past its own edge.

**The stance that follows.** "Remember that you don't *grow* plants — or children for that matter,
or organizations. You can allow and participate in their growth, or you can oppose it." Götsch says
the same from the other side: *we think we are the intelligent ones, but we are only part of an
intelligent system.* This is the source of [PRODUCT.md](PRODUCT.md)'s rule that the copy speaks in
the third person about plants and never instructs the reader — the voice was derived from this
stance before the stance was written down.

## II. Why abundance is the origin and not the goal

*Boundless Garden* (2019) makes an argument the rest of this project quietly rests on: **the human
body is evidence that we come from abundance.**

Before fruit, every animal–plant interaction was extractive — eating a leaf, root, or seed cost the
plant something, and animals evolved digestive armor against plant defenses. Fruit changed the
terms: it is a plant making something as attractive as possible with *no strings attached*, because
being eaten is the service. The animals that specialized in fruit needed no armor, and all that
evolutionary capacity went elsewhere — color vision, smell tuned to the exact molecules of ripeness,
grasping hands, mental maps of where things fruit and when, and the metabolically extravagant
primate brain that a four-year-old sends three-quarters of their blood sugar to.

Cognition did not emerge *against* scarcity. It emerged *from* abundance, as the form abundance took
in us. And the relationship ran both ways: fruit-eating primates disperse seed further than wind
carries it, scarify it through digestion, and deposit it fertilized. The forest they eat from is the
forest they make.

Two things follow that the tool should carry:

- **Scarcity is what we fell into, not what produced us.** A person standing on their lot in Puna is
  not being asked to heroically wring food out of a stingy world. They are being asked to re-enter
  something their body already assumes.
- **The human role is keystone frugivore, and the work is reparation.** The niche left by the
  dispersers we drove extinct is open. Planting is not an imposition on a wild system; it is a
  primate doing what primates always did, badly remembered.

This is also where the project's answer to the native/introduced objection comes from — see §VI.

## III. Götsch's apparatus — the two axes

Götsch's contribution is that he made the above *operable*. His system places every plant on two
axes at once, and almost everything else falls out of that placement.

### Axis 1 — stratum (where in the light)

A tropical forest fills every height. Götsch identifies **eleven strata** in the tropics (fewer
toward the poles, as sunlight falls off), usually collapsed for working purposes into five:
**emergent · high · medium · low · groundcover**. Each stratum has a characteristic share of the
light, and the shares are read as *shade cast*, which is why they can exceed 100%: syntropic
agriculture "works with four dimensions — width, length, height, and time," and plants of different
heights and lifespans occupy the same ground without competing.

At full canopy in a managed cocoa system the distribution runs roughly: emergent 20–25%,
high 40–45%, medium 70–80%, low ~95%, groundcover ~15% — about 210% total. Two months after a hard
pruning the same system reads 2–6% / 7–10% / 8–12% / 85–90% / 6–8%. **The stratum percentages are
not fixed;** you can raise one by lowering its neighbor. What is fixed is that an unfilled stratum
is an opening, and something will fill it.

> *"The lack of species in the stratification creates opportunity for unwanted weeds."*

This is the mechanical reason PSF's design principle "succession is structure" is right, and the
reason the site's `str:` field — already present on all nineteen shipped plants — is the more
load-bearing of its two axes.

### Axis 2 — successional class (when in the life of the system)

Independent of height, each plant belongs to a class by lifespan and by how much accumulated life it
needs under it:

| Class | Life cycle | Character |
|---|---|---|
| **Placenta 1 / 2** | up to ~2 years | Vegetables, tubers, beans, cassava, pineapple, papaya. Planted at maximum density. They *protect and create the embryo* — the forest of the future. |
| **Secondary 1** | ~10–20 yr | Fast, soft, prune-responsive. Cecropia is the type specimen. |
| **Secondary 2** | ~60–80 yr | Takes over as secondary 1 retires. |
| **Climax** | 80–350+ yr | Arrives last, needs the most accumulated life beneath it. |

The word **placenta** is worth keeping exactly as Götsch uses it. The annuals are not filler while
you wait for the trees. They are the organ that grows the trees.

**The two axes are independent, and that is the whole point.** Three plants can all be emergent —
cecropia (secondary 1, 10–20 yr), guapuruvu (secondary 2, 60–80 yr), dandá (climax, 80+ yr) — and
their relationship over time *is* the succession. Prune the cecropia and the guapuruvu stretches; the
prunings feed it, the light feeds it, and the growth hormones released feed everything. Eventually
the guapuruvu passes the cecropia, and the cecropia says goodbye, having done its work. If the
guapuruvu were not there, the cecropia would simply age and die and the system would stall. **A
missing successional class is a stall; a missing stratum is a weed.**

A full consortium therefore holds **a representative of every stratum from every successional
class** — planted at the same time, not in sequence. This is the formal statement of what
[succession.md](succession.md) means by "a food forest telescopes this."

### The third reading — where the *site* is

Cutting across both axes is a property of the ground itself, which Götsch calls the quantity and
quality of *consolidated life*:

- **Colonization system** — life beginning on raw substrate. Bacteria, algae, lichens, mosses; then
  the first vascular pioneers. *Götsch's own example is ʻōhiʻa (Metrosideros polymorpha) colonizing
  a 1960 lava flow south of Kona — photograph credited to Craig Elevitch* (p. 40). The book reaches
  Hawaiʻi before we reach the book.
- **Accumulation system** — plants with high carbon-to-nitrogen ratios, leathery leaves, little
  fruit for large mammals. Sun energy is being banked as organic matter. Most degraded land on earth
  is here, and stays here.
- **Abundance system** — enough consolidated life that food for large mammals (us) is produced
  without external input. Götsch calls it "our luxury system." After 40 years he says his own farm
  has *not yet arrived*.

## IV. The crutch — the single most useful idea in the book

Plant something that needs an abundance system into ground that is only an accumulation system, and
you must supply the difference yourself: manure, rock dust, lime, phosphate, irrigation, spray,
attention. Götsch calls that supplied difference a **crutch**, and its size is measurable:

> **crutch = (life the species requires) − (life the site has consolidated)**

Everything follows from this quantity.

- **It is what "difficulty" actually is.** [succession.md](succession.md) III already derived this
  independently — *"difficulty = the unmet-needs remainder"* — and this is the same equation with
  forty years of fieldwork behind it. That convergence is the strongest single piece of evidence
  that PSF's derived-not-authored rule is correct.
- **It explains pests.** The size of the crutch predicts the pressure from insects, fungi, and
  weeds. They are not enemies; they are, in Götsch's phrase, "the department for the optimization of
  life processes," reporting the true successional state of the field. A pest outbreak is a
  *measurement*. This is the mechanism behind [SOURCES.md](SOURCES.md)'s "pest is a monoculture
  word" — that judgment was held lightly on intuition, and now has a stated cause.
- **It is the only kind of difficulty that can be reduced for free.** Raise the site's consolidated
  life and every plant's crutch shortens at once. This is why the biggest difficulty-reducer is a
  pioneer already on the ground, pruned hard, and why placement and difficulty are one feature.
- **In syntropic management the crutch shortens over time**; in conventional and organic agriculture
  it does not. That is the actual difference between them, stated in one line.

**The corresponding warnings**, both of which the tool must eventually be able to give:

1. **Do not take steps backward in succession.** Don't put an accumulation-system species into ground
   that already supports abundance-system species.
2. **Do not skip stages.** Forcing fertility artificially opens the door to exactly the weed
   explosions and pest outbreaks that then get blamed on the diversity.

## V. Disturbance, pruning, and the information a plant broadcasts

**Syntropic agriculture is disturbance.** Not damage tolerated — disturbance *sought*, because the
systems we inherit are missing their disturbance vectors (wind, storm, flood, large herbivores).
Pruning substitutes for the missing vector, and it does four things at once:

1. drops leaf and branch as mulch **in place**;
2. sheds root nitrogen at the same moment;
3. opens light to every stratum below;
4. releases growth hormones that travel the mycorrhizal network and stimulate **the whole system**,
   not just the pruned plant.

The fourth is the one usually missed, and Götsch's evidence for it is good: after Hurricane Richard
flattened and effectively pruned Central American forest in 2010, cocoa growers had an exceptional
crop the following year. Renate Götsch's name for the effect on their own devastated land was *a
second springtime*.

**The senescence signal.** This is the mechanism that makes Freely's 2024 pruning rule precise.
Freely: *"prune them before they flower to keep the system in a youthful vegetative state."* Götsch,
independently, on goat's-beard grass among mombasa: if it is only pruned rather than removed, "in
addition to producing little biomass, its cycle will be much faster… it will flower earlier and
transmit this aging information to the entire system, braking the development of plants."

**Flowering is information, and it is contagious.** A plant that flowers and sets seed tells the
system it is time to age. This is why pruning timing matters more than pruning quantity, why
selecting a companion with a long vegetative cycle matters, and why a fast-cycling weed left to
flower slows *everything*, not merely its own patch. It is also, read across, the sharpest available
argument for [PRAXIS.md](PRAXIS.md)'s pruning-to-keep-food-in-reach: cutting is not restraint of the
plant, it is a message sent to the whole community.

**Mulch in place vs. mulch imported.** Freely, 2024: *"soil is mainly produced underground, by roots
and exudates… Spreading mulch repeatedly over bare ground as a substitute for true soil building by
weed roots is generally an entropic practice, despite how commonplace and unquestioned it is."* This
does **not** contradict chop-and-drop; it sharpens it into a test. Biomass generated by the system
and dropped where it grew is the system feeding itself. Biomass trucked in and spread over ground
that has no roots working under it is a wall — importing order from outside to keep this patch nice.
Same material, opposite direction of flow. The question to ask of any mulch: *did this grow here?*

## VI. The material cycles Götsch does not cover

Three practices from Freely's writings extend the picture past the book, and they matter because
they are the cheapest possible interventions — the ones a person can start tonight.

- **Terra preta, and fermentation over composting.** Pre-Columbian Amazonians built anthropogenic
  dark earths up to ten feet deep, still fertile millennia later, on some of the poorest soil on
  earth: household waste, bones, excreta, and hearth charcoal sealed in vessels, where endophytic
  microbes already present in the food drove a lactic-acid fermentation — pickling it, killing
  pathogens, removing smell, and producing ideal worm food. Worms then mixed the fine biochar into
  the soil, where it holds water, nutrients, and mycorrhizae indefinitely. This was waste disposal
  that was soil creation that was agriculture, requiring no clearing, fertilizing, or irrigation.
  *"It was gardening by being alive in one place."* Slash-and-burn is its degenerate descendant —
  "terra preta with the intelligence removed."
  **The operative claim: composting is not a syntropic use of food waste; it destroys most of its
  value.** Ferment scraps with their seeds and apply them. No inoculant is needed — the microbes are
  already in the food.
- **Disperse the seed.** Ferment and scatter the seed of every fruit that grows well, so populations
  grow exponentially rather than one planting at a time. Add a little soil from mature forest to
  pre-seed the mycorrhizae that will matter later. This is the primate's actual job (§II) and it is
  free.
- **Weeds as allies, with uses.** Celebrate them for their resilience, prune before flower, learn
  their food, medicine, and craft uses; failing that, grow mushrooms on them or gasify them. Think
  of pruning as a substitute for the light herbivory that is common in wild forest and absent around
  human settlement — where we tend to have either no herbivory or the excessive herbivory of feral
  livestock.

**On introduced species**, the two bodies agree and the agreement is worth stating plainly, because
it is contested ground in Hawaiʻi. Götsch: where a biome has lost its resilience, native species
often *cannot* recolonize it, and hardy exotics can be "bridges" to a biodiverse primary forest.
Freely: every ecosystem's inhabitants arrived at some point, a fixed native baseline is a line drawn
on shifting sand, and under a changing climate the question is not whether the vacuum gets filled
but whether it gets filled haphazardly or by cultivation.

**PSF holds this position with care, and does not import it wholesale.** Hawaiʻi is not the Cerrado;
endemism here is extraordinary, extinction is not hypothetical, and the tool speaks to people for
whom "introduced species" names a real grief. The project's own resolution is already in the
repo and is better than either source's: **the guild can be built to hold the native web inside it**
— māmaki sited into the breadfruit guild, carrying the Kamehameha butterfly with it (see
[INSIGHTS.md](INSIGHTS.md), 2026-07-17). Restoration and a carried-crop food forest are usually
treated as opposed. The guild is where they reconcile. That is PSF's contribution back, and it should
be argued from, never assumed.

## VII. Syntropy as a criterion for the tool itself

*Syntropy & Technology* (2025) turns the same lens on software, and it applies to this repo without
adjustment.

Freely's argument to Sep Kamvar is that a syntropic technology spreads not like a precipitate
crystallizing at a threshold but like **autocooperativity in protoplasm**: one molecule binds, the
perturbation changes its neighbor's binding preference, that change propagates along the backbone,
and the transition runs the length of the system — provided the *near-neighbor interaction energy*
is positive. Sep's four qualities (evidently better, evidently cheaper, low activation energy, high
viral coefficient) get restated: the viral coefficient *is* near-neighbor interaction energy, and it
rises when an experience changes a person's relationships, which in turn raises their propensity to
propagate it.

Sep's critique lands squarely on syntropic agroforestry: it is evidently better, but not evidently
cheaper in the near term, the activation energy is high, and each new farm does not naturally
produce the next one. Freely's counter is that better/cheaper are artifacts of the reference frame —
an apple versus an apple tree — and that narrowing the frame always flatters the entropic option.

**This is the design brief for Prep Set Forget, and it is worth being blunt about it:**

- **Activation energy is the primary metric.** The chili by the kitchen door is not a modest example;
  it is the whole strategy. Every friction removed between a person and their first planting is worth
  more than a better recommendation.
- **Near-neighbor energy is the second.** Ask of any feature: does using this change how someone
  relates to a neighbor, a lot, a fence line? The flyer that survives a photocopier scores higher
  here than a feature that requires an account.
- **The reference frame is a design surface.** The tool's job includes widening what counts. This is
  what the honest-numbers principle is *for* — and it is why "nothing on this list will feed you
  here" must remain a legitimate answer.
- **The Minimum Viable Seed test.** Freely's answer to the catalyst-versus-aperture tension: "A small
  seed and a large seed can grow into the same size tree, but a large seed cut in half won't." The
  boundedness value in this project is only defensible if the bounded thing is a *whole small seed*
  — a microcosm of the eventual system — rather than a slice of a large one. This is the
  articulation the store/story split was reaching for, and the sharpest available test of any
  proposed scope cut.

And the note to keep beside the overwhelm, since this document is a large one:

> "That feeling of overwhelm when facing the web of contingencies is the medicine that ensures that
> the eventual course of action emerges from distillation of the whole rather than a parochial pile
> of parts."

## VIII. What this changes about the tool — the finding

Stated plainly, because it is the practical consequence of everything above:

**Site.html reads climate. Götsch says climate is the second question.**

The tool asks the raster for rain, elevation, and derived temperature, and returns a fit. Those are
real constraints — a plant outside its climate band is stressed, and prolonged stress suppresses the
immune system of the plant *and* of the biocenosis around its roots, which is Götsch's own reason for
respecting them. But climate determines only whether a species *can* live here. **Where the site sits
on the colonization → accumulation → abundance axis determines what it will cost to keep alive, what
will attack it, and what has to be planted first.** That axis is only *partly* in a raster: lava-flow
surface age (USGS) maps how far soil development has likely gone and can seed a first-pass reading — but
the decisive signal is read off the vegetation already standing on the ground — the indicator plants —
and PSF cannot currently ask for that.

[succession.md](succession.md) III already knows this: it opens *"given a site read (rain, elevation
from the map tool) **and** what is already growing there."* The second input has no interface.

This is the strongest argument yet for the conversational/LLM layer, and it reframes it. That layer
is not an enrichment or a nice-to-have for the pioneer substrate. **It is the second axis of the
instrument.** One good question — *what is already growing there?* — converts a climate filter into
a successional reading. A substrate-age raster can *seed* that reading; only a conversation can sharpen
it to the ground actually underfoot — **raster-seeded, conversation-refined.**

---

*Open: derive the Hawaiʻi indicator-plant set (the local equivalent of Götsch's Cerrado list —
what guinea grass, cane grass, false staghorn fern, albizia, strawberry guava, and bare ʻaʻā each
report about a site's consolidated life). That list is the missing input device, and it is
ethnoecological knowledge the steward already holds.*
