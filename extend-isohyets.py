"""Add the missing high-rainfall isohyets (160-300 in/yr) to MAP.iso.

The existing map stops at 140 in/yr and buckets everything wetter than that
into one flat band, which is wrong for upper Puna / Hamakua / windward Hilo —
real rainfall there runs up to ~300 in/yr. The state's own Rainfall Atlas of
Hawaii vector isohyets (the same authority this project already trusts for
the coastline and the live per-point rain lookup) has those contours; this
script fetches them and reprojects them into the site's existing SVG frame.

Only ADDS keys above 140 — the already-correct 10-140 bands are left as they
are, so this touches exactly the part of the map that was wrong.

Run: python extend-isohyets.py
Then: python close-isohyets.py   (rebuilds MAP.isoFill for the new bands)
      python flyer-map.py        (refreshes the flyer's static copy)
"""
import json
import re
import urllib.request
import urllib.parse

TARGETS = ["site.html", "mapdata.js"]
LAYER = "https://geodata.hawaii.gov/arcgis/rest/services/Climate/MapServer/13/query"
BBOX = {"xmin": -156.07, "ymin": 18.9, "xmax": -154.8, "ymax": 20.28,
        "spatialReference": {"wkid": 4326}}
MIN_NEW = 140  # strictly greater than this gets added; 140 itself is kept as-is


def fetch_high_isohyets():
    params = {
        "where": "contour>%d" % MIN_NEW,
        "outFields": "contour,objectid",
        "geometry": json.dumps(BBOX),
        "geometryType": "esriGeometryEnvelope",
        "spatialRel": "esriSpatialRelIntersects",
        "inSR": "4326",
        "outSR": "4326",
        "returnGeometry": "true",
        "f": "json",
    }
    data = urllib.parse.urlencode(params).encode()
    with urllib.request.urlopen(LAYER, data=data, timeout=60) as r:
        d = json.loads(r.read())
    if "error" in d:
        raise SystemExit("ArcGIS error: %s" % d["error"])
    return d["features"]


def to_d(pts, K, S, minX, minY):
    def proj(lon, lat):
        return (lon * K - minX) * S, (-lat - minY) * S
    xy = [proj(*p) for p in pts]
    body = "L".join("%.1f %.1f" % p for p in xy[1:])
    return "M%.1f %.1f" % xy[0] + ("L" + body if body else "")


def main():
    src = open("site.html", encoding="utf-8").read()
    m = re.search(r"var MAP=(\{.*?\});", src, re.S)
    MAP = json.loads(m.group(1))
    K, S, minX, minY = MAP["K"], MAP["S"], MAP["minX"], MAP["minY"]

    feats = fetch_high_isohyets()
    print("fetched %d isohyet segment(s) above %d in/yr" % (len(feats), MIN_NEW))

    by_level = {}
    for f in feats:
        c = int(f["attributes"]["contour"])
        for path in f["geometry"]["paths"]:
            by_level.setdefault(c, []).append(to_d(path, K, S, minX, minY))

    for c in sorted(by_level):
        print("  %4d: %d segment(s)" % (c, len(by_level[c])))

    for path in TARGETS:
        s = open(path, encoding="utf-8").read()
        mm = re.search(r"var MAP=(\{.*?\});", s, re.S)
        if not mm:
            print("%s: no inline MAP, skipped" % path)
            continue
        m2 = json.loads(mm.group(1))
        for c, segs in by_level.items():
            m2["iso"][str(c)] = segs
        # isoFill is stale now (new nesting) -- drop it, close-isohyets.py rebuilds it.
        m2.pop("isoFill", None)
        new_blob = "var MAP=" + json.dumps(m2, separators=(",", ":"), ensure_ascii=False) + ";"
        s2 = re.sub(r"var MAP=\{.*?\};", lambda _: new_blob, s, count=1, flags=re.S)
        open(path, "w", encoding="utf-8").write(s2)
        print("%s: MAP.iso extended to %d in/yr, isoFill cleared for rebuild"
              % (path, max(int(k) for k in m2["iso"])))


if __name__ == "__main__":
    main()
