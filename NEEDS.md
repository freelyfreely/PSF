# What the tool is waiting on

The inputs the project needs to go further, sorted **by who or what can supply them** — steward-held
knowledge, sources fetchable now, external data, tooling, and decisions. This is deliberately a
different cut from [MAP.md](MAP.md)'s "Deliberately unfinished," which is organized by *document*. This
one asks a single question of every open thread: *what would actually unblock it, and where does that
come from?* Keep it honest about which needs are cheap and which are the real gates.

Written session 6 (2026-07-18) from the AI collaborator's side, in answer to "what do you feel you
need at this juncture?" — so it is also a standing record of the tool's own edges.

---

## I. What only the steward holds — lived ethnoecology

The highest-value inputs in the whole project, and none of them are on the internet. Freely holds
them; the tool cannot be researched into them.

- **The indicator ground-truth pass.** Every `[inferred]` and `[needs ground-truth]` tag in
  [INDICATORS.md](INDICATORS.md) is a question addressed to the steward. This is the input device the
  second axis needs (see §III and [SYNTROPY.md](SYNTROPY.md) VIII), and it is the single largest gate
  in the project. Until it is ratified, INDICATORS may not feed reader-facing copy.
- **Where the frost line actually bites.** Temperature is the *hard* axis of the fit model, derived from
  elevation by lapse rate. The elevation at which frost genuinely threatens on each side of the island
  is lived knowledge that would sharpen every `frost:true` verdict. Repeatedly flagged `[needs
  ground-truth]` in INDICATORS.
- **The missing indicator entries.** Wet-forest natives beyond ʻōhiʻa (hāpuʻu / tree-fern stands), the
  mesic and dry native remnants, upcountry pasture weeds (gorse, banana poka, the ginger complex),
  ironwood, and everything above the frost line. INDICATORS is currently short and lowland-biased.
- **A stated position on native / introduced.** [SYNTROPY.md](SYNTROPY.md) VI and the albizia case hold
  the tension open by design. Whether — and how — the tool ever *says* the syntropic read of albizia
  ("supply the successor, take the nitrogen") is a values call only the steward makes, and it is
  readiness-sequenced (some truths must be withheld until the reader has shifted — [INSIGHTS.md]
  2026-07-17).

## II. Higher-tier sources fetchable now — and the proof they're worth it

These exist in the literature and the AI collaborator can pull them with web tools. The ʻulu case this
session is the proof of value: a Hawaiʻi-calibrated source (**Mausio et al. 2020**) not only sourced the
disputed 157-in rainfall figure but *expanded* the band past the shipped guess — the
expand-when-justifiable rule ([SOURCES.md](SOURCES.md)) has legs.

- **Elevitch, *Species/Traditional Trees of Pacific Island Agroforestry*** (agroforestry.net) — the
  recommended next cross-read for every canoe plant and the guild support species. Long owed; partially
  available as free PDFs.
- **Morton, *Fruits of Warm Climates*** (hort.purdue.edu, fully online) — the tropical fruit entries
  where Ferns runs thin. Acerola was already recrystallized against it; the rest of the fruit await.
- **Place-and-species-specific models like Mausio 2020.** Worth actively looking for one per major
  crop — a suitability model fitted to Hawaiʻi observations outranks a generic tropical database *here*
  (SOURCES.md authority order). These are the sources that let bands *widen* with evidence.
- **CTAHR / DLNR publications** for the `[established]` indicator entries — the sourcing INDICATORS owes
  before it can ship. Fetchable; not yet fetched.

*Constraint worth naming:* **permacultureplants.com returns 403 to plain fetch** and its long bylined
articles are reachable only through a real browser session. That is a §IV tooling gap, not a §II
knowledge gap.

## III. External data & rasters — including a possible second axis from the ground itself

The tool currently reads three rasters (rain, elevation, and temperature derived from elevation). Two
more classes of data would change what it can do — and one of them **partially dissolves the standing
claim that the second axis is in no raster.**

- **Substrate / lava-flow age (USGS geologic map of the Island of Hawaiʻi).** This is the interesting
  one. [SYNTROPY.md](SYNTROPY.md) VIII, [MAP.md](MAP.md), and [INDICATORS.md](INDICATORS.md) all state
  that the colonization → accumulation → abundance axis "is in no raster." That is not fully true.
  **Surface age is mapped, and surface age is the strongest single predictor of how far soil
  development has gone** — a 1990 flow and a 10,000-year flow at the same rain and elevation are at
  opposite ends of the consolidation axis, and the map knows which is which. It does **not** replace the
  vegetation reading (a 3,000-year flow under albizia and the same flow bare are different, and only the
  plants tell you) — but it could give the tool a *raster first-pass on the second axis* before any
  conversation happens. This deserves its own architectural note; it means the second axis is
  "raster-seeded, conversation-refined," not "conversation-only."
- **Land-cover / vegetation rasters** (Hawaiʻi GAP land cover, LANDFIRE, or the Carnegie/ASU canopy
  work). A coarse remote-sensed "what is growing there" — guinea-grass sea vs. albizia canopy vs. bare
  lava — could pre-fill the indicator question the conversational layer is meant to ask. Lower
  resolution than a person standing on the ground, but non-zero, and available today.
- **Soil survey (USDA SSURGO/gSSURGO for Hawaiʻi County).** Where it exists, it carries drainage class
  and depth directly — the variables the fit model currently infers. Coverage on young lava is thin
  (there often *is* no soil to survey), which is itself information.

## IV. Capabilities the AI collaborator currently lacks

Honest tooling edges hit this session and before:

- **A real-browser fetch path.** Needed for 403 / JS-only sources (permacultureplants.com) and for
  authenticated data. The Nimble web tools exist but are **unauthenticated in this environment**; a
  connected browser session would close both the §II 403 gap and much of §III.
- **PDF rendering.** `poppler` is not installed, so image-based PDFs won't render; text PDFs only come
  through a `pypdf` fallback. This bit twice this session — the CTAHR breadfruit profile (a scanned
  getmedia PDF) would not extract, and the `Context/` agroforestry PDFs are only partly reachable. The
  Mausio numbers came through an HTML mirror instead; a scan-only source would have blocked.
- **A way to actually *drive* `site.html`.** The in-app browser renders local files as static snapshots
  **without executing JavaScript**, so the map, the fit logic, and the new `succ` pill can be
  syntax-verified and node-tested but not *seen behaving*. Confirming a fit-model change visually (e.g.
  that ʻulu now reads "good" on 150-in ground) needs a real browser or a local dev server. This is why
  this session's verification stopped at "parses, no console errors, node-checked" rather than "watched
  it work."

## V. Decisions only the steward can make

Not research — judgment. Each of these is a fork the AI collaborator should not take alone:

- **The `succ` rendering wording.** Plain words now ship (`first in` / `early crop` / `fast nurse` /
  `long-lived` / `old-growth`, with Götsch's class in the tooltip). The mapping is a single editable
  object in `site.html` (`SUCC_PLAIN`); the words want the steward's ear.
- **Reservoir → display surfacing.** The 19 → whole-reservoir trajectory is open by decision
  ([MAP.md](MAP.md), [[psf-project]]). How the tool draws from a growing reservoir without overwhelming
  a phone or hiding the depth is a design pass waiting on direction.
- **The soul guide.** Tam's request; the shape is sketched (Stage Zero honored, second axis added) but
  the voice and how hard it engages the 6:3:1+1 memo are the steward's call.

---

## The short version — the two real gates

Most of the above is cheap or fetchable. Two things are the actual gates, and both are §I:

1. **The steward's indicator ground-truth pass** — the second axis cannot become runnable without it.
2. **A real-browser / dev-server capability** (§IV) — so changes to a shipped, JS-driven artifact can be
   *watched working*, not just reasoned about.

Everything else — sources, rasters, the substrate-age idea — can move as soon as someone points at it.

*Open: promote the substrate-age finding (§III) into an architecture note of its own — it revises a
claim that currently appears verbatim in three documents.*
