"""Stroke 5 — the PSF validation gate.

A NECROSIS DETECTOR, not a truth-checker (The_Live_Cavity.md). It finds where a fiber
got taken for an organ — where a code froze out of relationship and began counterfeiting
a living meaning. It must NEVER try to become a better global table. Decidable facets
only (per the BinEval reading); the holistic meeting is handed back to the living.

Every check here fires on a real defect found in the 2026-07-16 audit. If a check
cannot be decided mechanically, it does not belong in this file.

Run:  python projects/psf/gate.py            (report)
      python projects/psf/gate.py --sendable (just the species that pass, one per line)
"""
import json, sys, collections

# Windows consoles default to cp1252 and die on ✓/✗/—. The report is the point; don't
# let the glyphs kill it.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

SPINE = "workspace/acts/spine.jsonl"
SCOPE = "folder:PSF"

# Hawaiʻi Island envelope — the ground truth the picker reads against.
# Rainfall Atlas of Hawaiʻi: island annual rainfall runs ~7in (Ka Lae leeward) to
# ~275in (Kohala/Hilo windward ridges). Elevation: 0 to 13,796ft (Mauna Kea summit),
# but inhabited land tops out ~4,000ft. A band that only matches above 200in/yr
# effectively matches nowhere anyone lives.
ISLAND_RAIN = (7.0, 280.0)
LIVED_ELEV_MAX = 4500.0


def live_records(scope=SCOPE):
    latest = {}
    with open(SPINE, encoding="utf-8") as fh:
        for line in fh:
            if '"plant_record"' not in line:
                continue
            try:
                d = json.loads(line)
            except Exception:
                continue
            if d.get("kind") != "plant_record":
                continue
            p = d.get("payload") or {}
            if p.get("scope") != scope:
                continue
            latest[str(p.get("species", "")).lower()] = p
    return {k: v for k, v in latest.items() if not v.get("forgotten")}


def band(rec, *path):
    c = rec
    for k in path:
        if not isinstance(c, dict):
            return None
        c = c.get(k)
    if isinstance(c, dict) and c.get("min") is not None and c.get("max") is not None:
        return (float(c["min"]), float(c["max"]))
    return None


def parse_absolute_rain(notes):
    """The absolute survival hull, when the record states it in prose."""
    import re
    if not notes:
        return None
    m = re.search(r"[Aa]bsolute rainfall range\s*([\d.]+)\s*-\s*([\d.]+)", str(notes))
    return (float(m.group(1)), float(m.group(2))) if m else None


def paths_of(o, pre=""):
    out = []
    if isinstance(o, dict):
        for k, v in o.items():
            if isinstance(v, dict) and not set(v) <= {"min", "max"}:
                out += paths_of(v, pre + k + ".")
            else:
                out.append(pre + k)
    return out


# Schema generations that must not coexist inside one record. Left = the live path,
# right = the retired path that extraction kept writing after the schema moved.
DRIFT_PAIRS = [
    ("species.common", "name.common"),
    ("family", "name.family"),
    ("syntropic.stratum", "eco.canopy_layer"),
    ("psf.time_to_yield", "use.time_to_yield"),
]


def check(key, p):
    """Return a list of (severity, message). severity: 'fail' blocks; 'warn' informs."""
    r = p.get("record") or {}
    out = []

    # — identity is a real binomial (catches `musa sp.`, `coffea`, `hylocereus sp.`)
    parts = key.split()
    if len(parts) < 2 or parts[-1] in {"sp.", "sp", "spp."}:
        out.append(("fail", f"identity is not a full binomial: '{key}' — a genus is not a plant a person can go buy"))

    rain = band(r, "climate", "rainfall_in")
    elev = band(r, "climate", "elevation_ft")
    temp = band(r, "climate", "temp_f")

    # — match axes present (catches the invisible 7)
    if not rain:
        out.append(("fail", "no climate.rainfall_in — invisible to the picker"))
    if not elev:
        out.append(("fail", "no climate.elevation_ft — invisible to the picker"))

    # — bands are bands, not points (catches breadfruit/mango 80.6–80.6)
    for nm, b in (("rainfall_in", rain), ("elevation_ft", elev), ("temp_f", temp)):
        if b and b[0] == b[1]:
            out.append(("fail", f"climate.{nm} is a POINT ({b[0]}), not a band — a single optimum frozen into a range; nothing but an exact match can pass"))
        if b and b[0] > b[1]:
            out.append(("fail", f"climate.{nm} is inverted: min {b[0]} > max {b[1]}"))

    # — thriving ⊆ absolute survival hull (catches ʻulu: thrives above what it survives)
    absol = parse_absolute_rain((r.get("climate") or {}).get("microclimate_notes"))
    if rain and absol:
        if rain[0] > absol[1] or rain[1] < absol[0]:
            out.append(("fail", f"thriving rainfall {rain[0]}–{rain[1]} is DISJOINT from its own stated absolute hull {absol[0]}–{absol[1]} — it cannot thrive where it cannot survive"))
        elif rain[0] < absol[0] or rain[1] > absol[1]:
            out.append(("warn", f"thriving rainfall {rain[0]}–{rain[1]} exceeds the stated absolute hull {absol[0]}–{absol[1]}"))

    # — plausibility for THIS island (catches the mm÷10 conversions)
    if rain:
        if rain[0] > ISLAND_RAIN[1] or rain[1] < ISLAND_RAIN[0]:
            out.append(("fail", f"rainfall band {rain[0]}–{rain[1]} in/yr lies outside the island entirely ({ISLAND_RAIN[0]}–{ISLAND_RAIN[1]}) — matches nowhere"))
        elif rain[0] > 150:
            mm = f"(mm÷10 bug? {rain[0]}×10÷25.4 = {round(rain[0]*10/25.4,1)}–{round(rain[1]*10/25.4,1)} in)"
            out.append(("fail", f"rainfall MIN {rain[0]} in/yr — only the wettest ridges exceed this; effectively unrecommendable {mm}"))

    # — provenance on the deciding fields (catches rainfall src: null)
    # field_sources is keyed by FLAT dotted path ("climate.rainfall_in"), never nested.
    # Reading it as nested made this check fire on all 44 records unconditionally — it
    # was the gate agreeing with the audit because it repeated the audit's misreading,
    # not because it saw the data. Verified 2026-07-16: 44/44 flat, 0 nested.
    fs = r.get("field_sources") or {}
    for axis in ("rainfall_in", "elevation_ft"):
        if not fs.get(f"climate.{axis}"):
            out.append(("warn", f"field_sources.climate.{axis} is null — the field that decides the recommendation cannot be traced"))

    # — a citation must RESOLVE (Stroke 3). Run-local tags are fine: each record carries its
    # own provenance map, so S1 resolves within the record that cites it. What is fatal is a
    # tag naming nothing — the record showing a citation and unable to say who said it. That
    # was a dangling-reference bug in accreteRecord (fixed), not a property of the tags.
    prov = p.get("provenance") or {}
    refs = {t for tags in fs.values() if isinstance(tags, list) for t in tags if isinstance(t, str)}
    dangling = {t for t in refs if t not in prov}
    if dangling:
        out.append(("fail", f"{len(dangling)} citation(s) resolve to nothing: {sorted(dangling)[:5]} — the claim shows a source and cannot name it"))

    # — schema drift inside the record
    have = set(paths_of(r))
    for live_p, dead_p in DRIFT_PAIRS:
        if live_p in have and dead_p in have:
            out.append(("warn", f"two schema generations coexist: '{live_p}' and retired '{dead_p}'"))

    return out


def main():
    recs = live_records()
    reports = {k: check(k, p) for k, p in recs.items()}

    # — cross-record: byte-identical bands across different species (catches the copied row)
    sig = collections.defaultdict(list)
    for k, p in recs.items():
        b = band(p.get("record") or {}, "climate", "rainfall_in")
        if b:
            sig[b].append(k)
    for b, ks in sig.items():
        if len(ks) > 1:
            for k in ks:
                others = [x for x in ks if x != k]
                reports[k].append(("fail", f"rainfall band {b[0]}–{b[1]} is byte-identical to {others} — a copied row, not a reading of this plant"))

    sendable = [k for k, rs in reports.items() if not any(s == "fail" for s, _ in rs)]

    if "--sendable" in sys.argv:
        for k in sorted(sendable):
            print(k)
        return

    fails = [(k, rs) for k, rs in sorted(reports.items()) if any(s == "fail" for s, _ in rs)]
    warns_only = [(k, rs) for k, rs in sorted(reports.items())
                  if not any(s == "fail" for s, _ in rs) and rs]

    print(f"PSF gate — {len(recs)} live records\n")
    print(f"  BLOCKED : {len(fails)}")
    print(f"  SENDABLE: {len(sendable)}  ({len(warns_only)} of them carry warnings)\n")

    print("=" * 78)
    print("BLOCKED\n")
    for k, rs in fails:
        print(f"  {k}")
        for s, m in rs:
            print(f"    {'✗' if s == 'fail' else '·'} {m}")
        print()

    print("=" * 78)
    print("SENDABLE (warnings do not block)\n")
    for k in sorted(sendable):
        rs = reports[k]
        print(f"  ✓ {k}")
        for s, m in rs:
            print(f"      · {m}")


if __name__ == "__main__":
    main()
