"""Rebuild the flyer's map as the site's rainfall map, plus the windward arc.

The flyer and the site should not be two different islands. This lifts MAP out of
site.html and emits the same bands — real isohyets closed along the real coast by
close-isohyets.py — as static SVG, since the flyer carries no script and has to
print.

The crisp contour lines the site draws on top are dropped here: at ~220px wide they
land under half a pixel and read as dirt rather than data. The windward arc goes on
last, in ink, because it is the one thing this sheet is about.
"""
import json
import re

SITE = "site.html"
FLYER = "flyer-windward.html"
ARC_FROM, ARC_TO, ARC_VIA = "Honokaʻa", "Pāhoa", "Hilo"


def parse_pts(d):
    n = [float(x) for x in re.findall(r"-?\d+\.?\d*", d)]
    return list(zip(n[0::2], n[1::2]))


def rain_fill(r):
    r = int(r)
    if r < 20:
        return "var(--rain1)"
    if r < 40:
        return "var(--rain2)"
    if r < 70:
        return "var(--rain3)"
    if r < 110:
        return "var(--rain4)"
    return "var(--rain5)"


def windward(MAP):
    ring = parse_pts(MAP["islandD"])
    if ring[0] == ring[-1]:
        ring = ring[:-1]
    town = {t["n"]: tuple(t["xy"]) for t in MAP["towns"]}

    def near(p):
        return min(range(len(ring)), key=lambda i: (ring[i][0] - p[0]) ** 2 + (ring[i][1] - p[1]) ** 2)

    a, b, via = near(town[ARC_FROM]), near(town[ARC_TO]), near(town[ARC_VIA])

    def walk(i, j, fwd):
        out, n = [], len(ring)
        while i != j:
            out.append(i)
            i = (i + 1) % n if fwd else (i - 1) % n
            if len(out) > n:
                break
        out.append(j)
        return out

    arc = min((c for c in (walk(a, b, True), walk(a, b, False)) if via in c), key=len)
    return "M" + "L".join("%.1f %.1f" % ring[i] for i in arc)


def main():
    MAP = json.loads(re.search(r"var MAP=(\{.*?\});", open(SITE, encoding="utf-8").read(), re.S).group(1))
    contours = sorted(MAP["isoFill"], key=lambda s: int(s))

    L = []
    L.append('<svg class="mini" viewBox="0 0 %d %d"' % (MAP["W"], MAP["H"]))
    L.append('           aria-label="Hawaiʻi Island, shaded by yearly rainfall: dry on the leeward side,')
    L.append('                       wet on the windward. The windward coast — Hāmākua, Hilo, Puna — is')
    L.append('                       marked in ink along the northeast shore.">')
    L.append("        <defs>")
    L.append('          <clipPath id="fl-clip"><path d="%s"/></clipPath>' % MAP["islandD"])
    L.append('          <filter id="fl-soft" x="-30%" y="-30%" width="160%" height="160%">')
    L.append('            <feGaussianBlur stdDeviation="12"/>')
    L.append("          </filter>")
    L.append("        </defs>")
    L.append('        <g clip-path="url(#fl-clip)">')
    L.append('          <path d="%s" fill="var(--rain1)"/>' % MAP["islandD"])
    for c in contours:
        for d in MAP["isoFill"][c]:
            L.append('          <path d="%s" fill="%s" filter="url(#fl-soft)"/>' % (d, rain_fill(c)))
    L.append("        </g>")
    L.append('        <path class="coast" d="%s"/>' % MAP["islandD"])
    # The arc marks the wettest coast, which is exactly where the map is darkest:
    # ink on rain5 is only 3.2:1. So it is cased — a paper-coloured line under an ink
    # one — which reads on the dark teal AND on the dry tan at the Hāmākua end, and
    # still survives a photocopier.
    arc = windward(MAP)
    L.append('        <path class="on-case" d="%s"/>' % arc)
    L.append('        <path class="on" d="%s"/>' % arc)
    L.append("      </svg>")
    svg = "\n".join(L)

    f = open(FLYER, encoding="utf-8").read()
    f = re.sub(r'<svg class="mini".*?</svg>', lambda m: svg, f, flags=re.S)
    open(FLYER, "w", encoding="utf-8").write(f)
    msg = ("flyer map: %d bands over the real coast, windward arc %s to %s via %s"
           % (sum(len(MAP["isoFill"][c]) for c in contours), ARC_FROM, ARC_TO, ARC_VIA))
    # Windows consoles default to cp1252 and choke on the place names.
    print(msg.encode("ascii", "replace").decode("ascii"))


if __name__ == "__main__":
    main()
