# raw/ — the ore

The source-of-truth data store, one file per plant. Everything a record is built from lives
here, source by source, with disagreements preserved rather than averaged. [plant-copy.md](../plant-copy.md)
is **distilled from** these files; it must not state a deciding field that isn't backed here.
This is the store [gate.py](../gate.py) was written to check against (the old `spine.jsonl`,
revived natively) — the necrosis check is "does every deciding field in copy trace to a source
in raw."

See [SOURCES.md](../SOURCES.md) for the authority order and conventions these files follow.

## Schema

Each `<genus-species>.md` carries, in order:

- **Identity** — binomial, family, common names, PSF role, copy entry number.
- **Succession (axis 2)** — the successional class (placenta 1/2 · secondary 1/2 · climax) and the
  lifespan, added 2026-07-17 (session 4). Axis 1 (stratum) is the PSF `str:` field, already shipped;
  this is the second, independent axis from [SYNTROPY.md](../SYNTROPY.md) III / [succession.md](../succession.md)
  I-b. **The lifespan is the datum; the class is the label** — where a plant sits between two classes
  (the 3–6 yr fruits, pigeon pea), the file says so rather than forcing a bin. `site.html` does not yet
  carry a derived `succ:` field; when it does, it compiles from here.
- **Climate & site — by source** — rainfall, temperature, altitude, soil/pH, light. Each line
  gives the raw value *in the source's own units* and the conversion to inches / feet / °F. Every
  contributing source is named inline (Ferns, Morton, CTAHR, lived Puna, …).
- **Propagation & timing — by source** — how it's started, days/years to first food.
- **Uses / food — by source** — edible parts, preparation, nutrition.
- **Hazards — by source** — stated plainly; note whether held-lightly (monoculture-frame) or flat
  (frame-independent fact), per the [SOURCES.md](../SOURCES.md) discipline.
- **Inferences** — what is *reasoned* from ecology where the data is absent, flagged as inference,
  never as a reading.
- **Anecdotes** — soft / lived / grower-forum / secondary colour, labeled as texture.
- **Distilled to** — the copy entry this feeds, and any judgment call made in distillation.

Units law (from SOURCES.md): the store keeps the source's units *and* the conversion; copy ships
inches, feet, °F only. mm ÷ 25.4 = in · m × 3.28 = ft · (°C × 9/5) + 32 = °F.
