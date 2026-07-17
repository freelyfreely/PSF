"""Stroke 2 — add the lived bands to the PSF `plant` schema.

Reads the current primary typed schema from the live store, appends the lived-band
fields beside each published match-axis, and writes it back through the ops API
(the daemon holds in-memory state — never hand-append to workspace/field/*.jsonl).

The law this encodes: the lived band NEVER overrides the published band. It stands
beside it. Where they disagree, the disagreement is the finding — shown to the reader,
not collapsed. This is `numbers-are-soft-interfaces.md` made structural.

Run:  python projects/psf/add-lived-bands.py          (dry run — prints the diff)
      python projects/psf/add-lived-bands.py --write  (writes through the API)
"""
import json, sys, urllib.request

API = "http://localhost:8001/api/op/"
SCHEMAS = "workspace/field/project_schemas.jsonl"

LIVED_FIELDS = [
    {
        "path": "climate.rainfall_in_lived",
        "type": "range",
        "role": "match-axis",
        "description": (
            "Annual rainfall band (in/yr) where growers REPORT it actually thriving on the Big "
            "Island. Distilled from community sources (permies/reddit/houzz/tropicalfruitforum). "
            "Stands BESIDE climate.rainfall_in — never overrides it. Where the two disagree, that "
            "disagreement is the finding and is shown to the reader."
        ),
    },
    {
        "path": "climate.elevation_ft_lived",
        "type": "range",
        "role": "match-axis",
        "description": (
            "Elevation band (ft) where growers REPORT it actually thriving here — e.g. breadfruit "
            "fruiting at 4,000 ft in Volcano in a sheltered pocket, well above the published max. "
            "Stands beside climate.elevation_ft; never overrides."
        ),
    },
    {
        "path": "climate.temp_f_lived",
        "type": "range",
        "role": "attribute",
        "description": "Temperature band growers report it thriving in (°F). Beside climate.temp_f, never overriding.",
    },
    {
        "path": "lived_reports",
        "type": "object",
        "role": "attribute",
        "description": (
            "The grower voice itself, as an array of {quote, place, elevation_ft, source_id, "
            "stance}. The soft data kept AS VOICE, not averaged into a number — the raw material "
            "for the card's 'The Voice' section. source_id must be a STABLE source id (see Stroke "
            "3), never a run-local S1/PS1 token."
        ),
    },
    {
        "path": "published_lived_divergence",
        "type": "string",
        "role": "attribute",
        "description": (
            "Prose naming where the published band and the lived reports disagree, and what that "
            "means for a grower deciding. This field is the point of the whole schema: it is where "
            "a global envelope gets caught being wrong about this island. Empty when they agree."
        ),
    },
]


def current_schema():
    last = None
    with open(SCHEMAS, encoding="utf-8") as fh:
        for line in fh:
            try:
                d = json.loads(line)
            except Exception:
                continue
            s = d.get("schema") or {}
            if d.get("op") == "put" and s.get("scope") == "folder:PSF" and s.get("name") == "plant":
                last = s
    if not last:
        sys.exit("no `plant` schema found under folder:PSF")
    return last


def main():
    s = current_schema()
    have = {f["path"] for f in s["fields"]}
    add = [f for f in LIVED_FIELDS if f["path"] not in have]
    if not add:
        print("lived bands already present — nothing to do.")
        return
    print(f"current `plant` schema: {len(s['fields'])} fields")
    for f in add:
        print(f"  + {f['path']:<38} {f['type']:<7} {f['role']}")
    fields = s["fields"] + add
    if "--write" not in sys.argv:
        print(f"\ndry run — would write {len(fields)} fields. re-run with --write")
        return
    body = json.dumps({
        "project": "projects/psf",
        "entity": s.get("entity", "Plant"),
        "name": "plant",
        "kind": "typed",
        "fields": fields,
        "primary": True,
    }).encode()
    req = urllib.request.Request(API + "set_project_schema", data=body,
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=30) as r:
        out = json.loads(r.read())
    print("\n" + str(out.get("content"))[:300])


if __name__ == "__main__":
    main()
