# Insights & inspirations — the seedbed

The catch-all: whatever doesn't yet fit in [raw/](raw), [plant-copy.md](plant-copy.md),
[succession.md](succession.md), or [PRAXIS.md](PRAXIS.md). A place ideas germinate before they are
structured — **not** an archive where things go to be forgotten.

**The discipline (so it stays a seedbed, not a graveyard):** date-stamp every entry. Periodically,
each entry is either *promoted* into one of the structured documents or *let go*. An item that has
sat here unmoved for a long time is a signal to decide, not to keep indefinitely.

Format: `### YYYY-MM-DD — hook` · a paragraph · then `→ where it wants to go`.

---

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
→ Wants its own document or a `raw/`-style store. **The highest-value unwritten thing in the project.**

### 2026-07-17 — The guild is where restoration and food production reconcile (strengthened)
The māmaki note above gains a second leg. Götsch argues that a biome past its resilience often cannot
be recolonized by its own natives, and that hardy introduced species can be *bridges* back to
biodiverse forest; Freely argues a fixed native baseline is a line on shifting sand. Both are
arguments PSF should know but must not import wholesale — Hawaiʻi's endemism and its extinctions are
not the Cerrado's, and "introduced species" names a real grief here. The repo's own position is
better than either source's: build the guild to hold the native web *inside* it. Worth writing as a
stated position rather than leaving as two unreconciled halves.
→ [SYNTROPY.md](SYNTROPY.md) VI holds the tension explicitly. A fuller statement is owed.

---

*Open: seed more freely here. The cost of a stray idea kept and later dropped is low; the cost of a
good one lost is high.*
