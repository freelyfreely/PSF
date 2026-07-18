# Insights & inspirations — the seedbed

The catch-all: whatever doesn't yet fit in [raw/](raw), [plant-copy.md](plant-copy.md),
[succession.md](succession.md), or [PRAXIS.md](PRAXIS.md). A place ideas germinate before they are
structured — **not** an archive where things go to be forgotten.

**The discipline (so it stays a seedbed, not a graveyard):** date-stamp every entry. Periodically,
each entry is either *promoted* into one of the structured documents or *let go*. An item that has
sat here unmoved for a long time is a signal to decide, not to keep indefinitely.

Format: `### YYYY-MM-DD — hook` · a paragraph · then `→ where it wants to go`.

---

### 2026-07-18 — The corpus is fully backed, and the backfill caught meta-drift
Session 5 wrote `raw/` records for the last ~20 entries and completed axis 2 across all 56, so the
whole corpus is now sourced one file per plant. As with the session-4 backfill, demanding a source for
every field caught what prose alone hid — but this time the sharpest catch was not a stray number, it
was a *stray rationale*. The Part IV copy explained that the annuals' bands are lived "where the Ferns
entries are thin." Fetching Ferns showed it carries full bands for the tropical squash and the ipu;
only the currant tomato is genuinely band-less. So the store catches **meta-drift** — a documented
reason that is itself wrong — not just numeric drift. A stated justification is a claim like any other,
and the firewall applies to it too. (Also caught: poha's "above 800 ft" was a metres→feet unit slip —
Ferns' optimum is 800 m ≈ 2,600 ft, which is why the copy's own "the upland, not the hot coast" logic
never fit the number it was attached to.)
→ Structured into the store, [SOURCES.md](SOURCES.md), and [MAP.md](MAP.md) this session. The general
form — *back-filling provenance audits the reasons, not only the figures* — sharpens the session-4
"drift detector" note below.

### 2026-07-18 — The firewall runs the same for hazards as for bands
Writing the soursop (#26) record, the pull was to add the annonacin / atypical-parkinsonism caution
that circulates around *Annona* — it feels responsible to warn. But I have no source in hand, only
memory of Caribbean studies. Star fruit's caramboxin earned its flat statement because it was cross-read
against the nephrology literature; annonacin has not been, here. So it goes into the raw record as a
*flagged cross-read target*, explicitly kept out of reader copy until sourced. The lesson: the
temptation to fabricate is strongest exactly where the stakes feel highest (a health warning), and that
is precisely where the firewall matters most. An unsourced hazard is still unsourced, however
well-intentioned.
→ Flag recorded in [raw/annona-muricata.md](raw/annona-muricata.md) and [SOURCES.md](SOURCES.md). A
candidate for a stated rule: *hazards get sourced to the same tier as bands before they ship.*

### 2026-07-17 — Store vs. story: the architecture that unlocked the rest
The strain across the project (the retired `*(light sourcing)*` marker, single-sourced bands,
provisional cross-plant claims stuck inside one plant's beats, the "planting order" fiction) was one
thing wearing many faces: [plant-copy.md](plant-copy.md) was doing the job of both a data store and
finished prose. Splitting them — `raw/` as the ore, copy as the refined metal, succession as the
physics, praxis as the doing — resolved all of them at once, and revived the store `gate.py` was
built to check (the absent `spine.jsonl`, now `raw/`).
→ Structured into the whole repo this session. Kept here as the origin note.

### 2026-07-17 — Difficulty, placement, and order are one derived quantity
Three things we kept treating as separate columns — a plant's *difficulty*, its *companion/placement*,
and its position in the *planting order* — are the same thing seen from three angles: each is a
function of the site's current state and what companions can supply. None can be authored once; all
are *computed per site* from unmet needs. This is why they are all "written last, from the whole set
at once."
→ Belongs in [succession.md](succession.md) III (partly there) and the horizontal-layer spec.

### 2026-07-17 — The guild can be built to hold the native web
Māmaki (#59) is the sole endemic on the list and the only larval host of the Kamehameha butterfly.
Its presence suggests a design principle beyond food: the guild can be composed so that the native
web (host plants, native pollinators) lives *inside* the food system, not walled off from it. A
carried-crop food forest and native-species restoration are usually treated as opposed; the guild may
be where they reconcile.
→ Candidate principle for [succession.md](succession.md) / a future "native inclusion" note.

### 2026-07-17 — Two kinds of food hazard, two handling rules
Katuk (raw-juice lung injury) and star fruit (caramboxin/renal) are both real food hazards, but they
demand opposite handling. Katuk's is *frame-dependent* (dose + raw preparation; the cooked vegetable
is safe) → held at true size. Star fruit's is *frame-independent* (a real toxin, real physiology) →
stated flat. The same sort that SOURCES.md applies to *pests* (monoculture-word vs. fact) applies to
*food hazards*. Worth generalizing into a stated rule.
→ **Promoted** into [SOURCES.md](SOURCES.md) "judgments held lightly" as the food-hazard corollary
(this session) — the first seed to graduate the seedbed.

### 2026-07-17 — The crutch: we derived Götsch's equation before reading Götsch
[succession.md](succession.md) III was written this morning with *"difficulty = the unmet-needs
remainder — computed from what the site + available companions cannot yet supply."* Götsch, from
forty years in Bahia, calls the same quantity the **crutch**: what you must supply by hand because
the site has not consolidated the life the species requires. Identical equation, arrived at
independently from the shape of the problem. This is the strongest evidence yet that the
derived-not-authored rule is not a stylistic preference but a description of how the physics actually
works — and it means the horizontal layer has a name, a literature, and a way to be checked.
→ **Promoted** into [SYNTROPY.md](SYNTROPY.md) IV and [succession.md](succession.md) I-b this session.

### 2026-07-17 — The tool reads one axis of two
Site.html reads rain, elevation, and derived temperature — a climate filter, which answers *can this
species survive here*. Götsch's decisive variable is orthogonal to all of it: where the ground sits
on colonization → accumulation → abundance, which determines what a plant will *cost*, what will
attack it, and what must go in first. That axis is in no raster. It is read off the plants already
standing. This reframes the conversational/LLM layer completely — it is not enrichment for the
pioneer substrate, it is **the second axis of the instrument**, and it exists to ask one question:
*what is already growing there?*
→ [SYNTROPY.md](SYNTROPY.md) VIII, [succession.md](succession.md) III. Wants a design decision next.

### 2026-07-17 — Flowering is contagious information
A plant allowed to flower and set seed broadcasts senescence to the whole community and brakes growth
system-wide. Freely's 2024 rule (prune weeds before they flower, keep the system vegetative and
young) and Götsch's goat's-beard-grass observation are the same finding from two directions. The
consequence is not small: it means pruning *timing* outranks pruning quantity, that a companion's
vegetative cycle length is a selection criterion, and that several "Forget" beats in the copy which
imply a plant can simply be left to seed may be quietly wrong.
→ Promoted to [PRAXIS.md](PRAXIS.md) II and [succession.md](succession.md) II. **The copy audit is
still owed.**

### 2026-07-17 — The Minimum Viable Seed test for boundedness
From *Syntropy & Technology*: "A small seed and a large seed can grow into the same size tree, but a
large seed cut in half won't." This is the test the boundedness value has been missing. A bounded
scope is defensible when the bounded thing is a *whole small seed* — a microcosm containing every
part of the eventual system — and indefensible when it is a slice of a large one. It gives a way to
judge any proposed cut: does what remains still contain all the organs?
→ [SYNTROPY.md](SYNTROPY.md) VII. Candidate for promotion into the project's stated values.

### 2026-07-17 — Hawaiʻi has no indicator-plant list, and that is the missing input device
Götsch's method leans on a Cerrado indicator list — each common volunteer reporting pH, compaction, a
missing micronutrient, a buried hardpan. Hawaiʻi's equivalent does not exist in any database, but the
knowledge does exist: what guinea grass says that false staghorn fern does not, what a stand of
albizia means about nitrogen, what strawberry guava says about a stalled succession, what bare ʻaʻā
says about a succession that has not begun. This is ethnoecological knowledge the steward holds
personally, and it is the exact input the second axis needs to be readable.
→ **Started** as [INDICATORS.md](INDICATORS.md) — a confidence-tagged scaffold written ahead of its
sourcing, awaiting the steward's ground-truth pass. The writing surfaced a category Götsch's list
lacks entirely (§ below).

### 2026-07-17 — Hawaiʻi's succession arrests; the Cerrado's mostly doesn't
Writing [INDICATORS.md](INDICATORS.md) turned up the structural difference between Götsch's context
and this one. His indicators mostly report *stages a system is passing through*. Several of the
dominant covers here — albizia, strawberry guava, uluhe in its mat mode, christmasberry — are not
stages passed through but **arrested states** that hold ground for decades. Read as "early, be
patient" they give the opposite of the right advice. The correct move is Götsch's own stall remedy
(the cecropia with no successor beneath it): introduce the missing successional class into a cut gap,
don't wait and don't fertilize. This is *why* Hawaiʻi's succession needs a hand where a
less-disturbed system needs only time — and albizia is the sharpest case, because the syntropic
reading ("supply the successor, take the free nitrogen") directly contradicts removal-first invasive
guidance. That contradiction is real and unresolved; it is the native/introduced tension of
[SYNTROPY.md](SYNTROPY.md) VI wearing work boots.
→ INDICATORS.md IV. Wants the steward's judgment and, eventually, a stated position.

### 2026-07-17 — The guild is where restoration and food production reconcile (strengthened)
The māmaki note above gains a second leg. Götsch argues that a biome past its resilience often cannot
be recolonized by its own natives, and that hardy introduced species can be *bridges* back to
biodiverse forest; Freely argues a fixed native baseline is a line on shifting sand. Both are
arguments PSF should know but must not import wholesale — Hawaiʻi's endemism and its extinctions are
not the Cerrado's, and "introduced species" names a real grief here. The repo's own position is
better than either source's: build the guild to hold the native web *inside* it. Worth writing as a
stated position rather than leaving as two unreconciled halves.
→ [SYNTROPY.md](SYNTROPY.md) VI holds the tension explicitly. A fuller statement is owed.

### 2026-07-17 — The naturalized larder: a utilization track distinct from planting
Two of the steward's corrections rhyme. Haole koa seed, soaked and sprouted to leach mimosine, is the
third most popular tempeh substrate in Indonesia. Albizia's high-N wood is ideal mushroom substrate.
Neither is a plant to *recommend planting* — both are already everywhere. They point at a whole track
PSF doesn't have yet: **utilization of existing naturalized plants** — turning the "invasive problem"
into a standing, unharvested food supply. This is distinct from the plant-recommendation spine (what
to put in) and distinct from the indicator reading (what the ground reports). It is a third question:
*what is already growing here that you could already be eating?* It sits close to the PRAXIS
recognition practice (hōʻiʻo, the passiflora on the lava) but scaled to the naturalized-invasive
biomass. Explicitly a **later** expansion, past the bounded display — but a large one, and it may be
where the tool's food-sovereignty weight (Tam's campaign horizon) actually concentrates: the fastest
calories are the ones already standing.
→ Its own future layer. Not near-term. Noted so it isn't re-discovered from scratch.

### 2026-07-17 — The albizia reframe is downstream of the person, not upstream
Sharpest instance so far of why PSF's real product is the inner succession. The syntropically
"correct" albizia move (coppice it, take the nitrogen and the mushrooms, supply a successor) is
blocked less by botany than by cognition: people are rigid and mechanical about a dangerous invasive,
and slow to change without an embodied insight (steward's words). So the reframe cannot be *told* in
first contact — only *occasioned* for someone already moving. Design consequence: some of the truest
recommendations are the ones the tool must **withhold** until the reader has shifted, or they read as
crank advice and burn trust. The bounded display isn't only a scope decision; it's a readiness-
sequencing decision. What you don't say yet is part of the method.
→ Belongs with [PRAXIS.md](PRAXIS.md) I and the eventual conversational-layer design.

### 2026-07-17 — Back-filling raw/ after the copy is a drift detector, not just bookkeeping
The shipped 19 were written from Ferns during day 1, but the `raw/` provenance files never existed —
copy *was* the store. Writing the store back underneath the finished prose (this session) was expected
to be clerical: record the mm/°C/m, keep the conversion, point at the copy entry. It wasn't. The act
of demanding a source for every shipped number surfaced three deciding fields that **do not trace to
Ferns at all** — ʻulu's 157-in rain upper (Ferns caps at 118), banana's 4,000 ft ceiling (a lived
narrowing of 2,400 m) and its unsourced year-1 first-food, ice cream bean's 350–5,000 ft "natural
range" (Ferns: 110–540 m). None are necessarily *wrong* — breadfruit really is wet-tolerant — but each
is currently a number with no paper behind it, which is precisely the necrosis [gate.py](gate.py) is
built to catch. The lesson generalizes: the store/story split isn't only tidiness, it is a *test*. As
long as copy is its own store, drift is invisible; the moment you force each field to name a source,
the unsourced ones fall out. This is the strongest practical vindication yet of the derived-not-authored
architecture — and it means the recrystallization pass has a natural first target list (the three
flags) rather than a vague "cross-read everything."
→ Flags recorded in [SOURCES.md](SOURCES.md) "open sourcing work" and in the individual `raw/` files.
The Elevitch cross-read (already owed) is where they resolve.

---

*Open: seed more freely here. The cost of a stray idea kept and later dropped is low; the cost of a
good one lost is high.*
