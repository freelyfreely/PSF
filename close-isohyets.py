"""Turn the open isohyet polylines in mapdata.js into closed, fillable regions.

The Atlas contours arrive as open lines that run off the coast and stop. Filling
one directly makes SVG close it with a straight chord across the island, which is
geometric nonsense. So each contour is closed the honest way: walk the real
coastline between the two points where the contour meets it.

That leaves one choice per contour — the coast can be walked either way round, and
only one of the two encloses the WET side. It is picked by nesting, which is the
one thing rainfall guarantees: the region for contour c contains every higher
contour and none of the lower ones.

Splices MAP.isoFill into every file carrying an inline MAP literal. Leaves MAP.iso
untouched: the crisp lines on top still draw from the original open paths.

Note that site.html inlines its own copy of MAP and does not load mapdata.js —
nothing does. Both are updated to keep them from drifting further apart.
"""
import json
import re

TARGETS = ["site.html", "mapdata.js"]


def parse_pts(d):
    """M/L polyline -> [(x, y)]. The data uses nothing else."""
    nums = [float(n) for n in re.findall(r"-?\d+\.?\d*", d)]
    return list(zip(nums[0::2], nums[1::2]))


def ring_of(d):
    pts = parse_pts(d)
    if pts[0] == pts[-1]:
        pts = pts[:-1]
    return pts


def near_idx(ring, p):
    """Index of the coastline vertex closest to p."""
    best, bi = float("inf"), 0
    for i, q in enumerate(ring):
        dd = (q[0] - p[0]) ** 2 + (q[1] - p[1]) ** 2
        if dd < best:
            best, bi = dd, i
    return bi, best ** 0.5


def walk(ring, a, b, fwd):
    """Coastline vertices from index a to index b, one way round."""
    out, n, i = [], len(ring), a
    while i != b:
        out.append(ring[i])
        i = (i + 1) % n if fwd else (i - 1) % n
        if len(out) > n:
            break
    out.append(ring[b])
    return out


def inside(poly, p):
    """Ray casting."""
    x, y = p
    c = False
    n = len(poly)
    for i in range(n):
        x1, y1 = poly[i]
        x2, y2 = poly[(i + 1) % n]
        if (y1 > y) != (y2 > y):
            xi = x1 + (y - y1) / (y2 - y1) * (x2 - x1)
            if x < xi:
                c = not c
    return c


def to_d(poly):
    body = "L".join("%.1f %.1f" % p for p in poly[1:])
    return "M%.1f %.1f" % poly[0] + ("L" + body if body else "") + "Z"


def probes(iso, c):
    """Sample points from every other contour, split by wetter / drier than c."""
    hi, lo = [], []
    for k, paths in iso.items():
        if int(k) == c:
            continue
        bucket = hi if int(k) > c else lo
        for d in paths:
            pts = parse_pts(d)
            bucket.append(pts[len(pts) // 2])
    return hi, lo


def build(MAP):
    ring = ring_of(MAP["islandD"])
    iso = MAP["iso"]
    out = {}

    for k in sorted(iso, key=lambda s: int(s)):
        c = int(k)
        hi, lo = probes(iso, c)
        polys = []

        for d in iso[k]:
            pts = parse_pts(d)
            ia, da = near_idx(ring, pts[0])
            ib, db = near_idx(ring, pts[-1])

            # A contour that never reaches the coast is already its own loop.
            endgap = ((pts[0][0] - pts[-1][0]) ** 2 + (pts[0][1] - pts[-1][1]) ** 2) ** 0.5
            if max(da, db) > 25 and endgap < 60:
                polys.append(pts)
                continue

            cands = [pts + walk(ring, ib, ia, True), pts + walk(ring, ib, ia, False)]

            # Score by nesting: contain the wetter contours, exclude the drier.
            def score(poly):
                return (sum(inside(poly, p) for p in hi) / max(len(hi), 1)
                        - sum(inside(poly, p) for p in lo) / max(len(lo), 1))

            polys.append(max(cands, key=score))

        out[k] = [to_d(p) for p in polys]
        print("  %4s in  %d region(s)" % (k, len(polys)))

    return out


def main():
    for path in TARGETS:
        src = open(path, encoding="utf-8").read()

        m = re.search(r'var MAP=(\{.*?\});', src, re.S)
        if not m:
            print("%s: no inline MAP, skipped" % path)
            continue

        print("%s:" % path)
        MAP = json.loads(m.group(1))
        fills = build(MAP)

        # Splice rather than re-serialise the whole object, so the diff stays to
        # the one key being added and the existing formatting survives.
        blob = '"isoFill":' + json.dumps(fills, separators=(",", ":")) + ',"towns":'
        assert src.count('"towns":') == 1, path
        open(path, "w", encoding="utf-8").write(src.replace('"towns":', blob))
        print("  spliced MAP.isoFill\n")


if __name__ == "__main__":
    main()
