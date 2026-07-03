#!/usr/bin/env python3
"""
Calca una imagen PNG (generada p. ej. con Nanobanana) a SVG vectorial limpio.

Flujo:  PNG con fondo blanco → quitar fondo (flood fill desde los bordes +
dilatación anti-halo) → vectorizar con imagetracerjs (paleta automática de
colores planos) → eliminar el fondo del SVG → envolver con animación de
respiración → exportar PNG transparente.

Uso:
    python3 calcar.py entrada.png nombre-variante
    # produce: fuente/nombre.png  svg/nombre.svg  png/nombre.png (1024)

Requisitos: node + imagetracerjs (se instala solo la primera vez), Chromium
headless para el PNG (ver export_png.py).

Consejos para la imagen fuente: fondo blanco sólido, colores planos sin
degradados, contornos definidos, 1024×1024 o más.
"""
import json, os, shutil, struct, subprocess, sys, zlib
from collections import Counter, deque

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
from export_png import read_png, write_png, render  # noqa: E402

SENTINEL = (255, 0, 255)  # magenta: marca el fondo para borrarlo del SVG

ANIM = """  <style>
    #duck { animation: bob 4.2s ease-in-out infinite; transform-origin: 50% 100%; }
    @keyframes bob { 0%,100% { transform: translateY(0) } 50% { transform: translateY(1.2%) } }
    @media (prefers-reduced-motion: reduce) { #duck { animation: none } }
  </style>
"""


def quitar_fondo(src, dst, tol=40, dilatar=5):
    w, h, ct, rows = read_png(src)
    bpp = {0: 1, 2: 3, 4: 2, 6: 4}[ct]
    px = [bytearray(r) for r in rows]

    def blanco(x, y):
        i = x * bpp
        r = px[y]
        return r[i] > 255 - tol and r[i + 1] > 255 - tol and r[i + 2] > 255 - tol

    seen = [[False] * w for _ in range(h)]
    q = deque()
    for x in range(w):
        for y in (0, h - 1):
            if blanco(x, y) and not seen[y][x]:
                seen[y][x] = True
                q.append((x, y))
    for y in range(h):
        for x in (0, w - 1):
            if blanco(x, y) and not seen[y][x]:
                seen[y][x] = True
                q.append((x, y))
    while q:
        x, y = q.popleft()
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < w and 0 <= ny < h and not seen[ny][nx] and blanco(nx, ny):
                seen[ny][nx] = True
                q.append((nx, ny))
    for _ in range(dilatar):
        grow = []
        for y in range(h):
            for x in range(w):
                if not seen[y][x]:
                    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < w and 0 <= ny < h and seen[ny][nx]:
                            grow.append((x, y))
                            break
        for x, y in grow:
            seen[y][x] = True
    for y in range(h):
        r = px[y]
        for x in range(w):
            if seen[y][x]:
                i = x * bpp
                r[i], r[i + 1], r[i + 2] = SENTINEL
    write_png(dst, w, h, ct, [bytes(r) for r in px])
    return w, h


def paleta_auto(prep, maxcolors=14, mindist=42):
    """Colores planos dominantes del arte, siempre con el centinela y blanco."""
    w, h, ct, rows = read_png(prep)
    bpp = {0: 1, 2: 3, 4: 2, 6: 4}[ct]
    c = Counter()
    for y in range(0, h, 2):
        r = rows[y]
        for x in range(0, w, 2):
            i = x * bpp
            c[(r[i], r[i + 1], r[i + 2])] += 1
    pal = [SENTINEL, (255, 255, 255)]

    def lejos(col):
        return all(sum((a - b) ** 2 for a, b in zip(col, p)) > mindist ** 2 for p in pal)

    for col, _ in c.most_common(4000):
        if len(pal) >= maxcolors:
            break
        if lejos(col):
            pal.append(col)
    return pal


def trazar(prep, out_svg, pal):
    js = f"""
const ImageTracer = require('imagetracerjs');
const Jimp = require('jimp');
(async () => {{
  const img = await Jimp.read({json.dumps(prep)});
  const imgdata = {{ width: img.bitmap.width, height: img.bitmap.height, data: img.bitmap.data }};
  const pal = {json.dumps([dict(r=r, g=g, b=b, a=255) for r, g, b in pal])};
  let svg = ImageTracer.imagedataToSVG(imgdata, {{
    pal, colorsampling: 0, numberofcolors: pal.length, colorquantcycles: 1,
    ltres: 1, qtres: 1, pathomit: 16, strokewidth: 0, blurradius: 0,
    roundcoords: 1, viewbox: true, rightangleenhance: false, linefilter: true
  }});
  svg = svg.replace(/<path fill="rgb\\(255,0,255\\)"[^/]*\\/>/g, '');
  require('fs').writeFileSync({json.dumps(out_svg)}, svg);
}})().catch(e => {{ console.error(e); process.exit(1); }});
"""
    if not os.path.isdir(os.path.join(HERE, "node_modules", "imagetracerjs")):
        subprocess.run(["npm", "install", "imagetracerjs", "jimp@0.22.12",
                        "--no-audit", "--no-fund"], cwd=HERE, check=True,
                       capture_output=True)
    tmp = os.path.join(HERE, "_trace_tmp.js")
    with open(tmp, "w") as f:
        f.write(js)
    try:
        subprocess.run(["node", tmp], cwd=HERE, check=True, capture_output=True)
    finally:
        os.unlink(tmp)


def envolver(out_svg, nombre):
    s = open(out_svg).read()
    i = s.index(">", s.index("<svg")) + 1
    s = (s[:i] + f"\n  <desc>Dr. Cuack — {nombre} (calcado)</desc>\n"
         + ANIM + '  <g id="duck">\n' + s[i:s.rindex("</svg>")] + "  </g>\n</svg>")
    open(out_svg, "w").write(s)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)
    src, nombre = sys.argv[1], sys.argv[2]
    for d in ("fuente", "svg", "png"):
        os.makedirs(os.path.join(HERE, d), exist_ok=True)
    fuente = os.path.join(HERE, "fuente", f"{nombre}.png")
    if os.path.abspath(src) != os.path.abspath(fuente):
        shutil.copy(src, fuente)
    prep = os.path.join(HERE, "_prep.png")
    quitar_fondo(fuente, prep)
    pal = paleta_auto(prep)
    print("paleta:", ["#%02X%02X%02X" % c for c in pal[1:]])
    svg = os.path.join(HERE, "svg", f"{nombre}.svg")
    trazar(prep, svg, pal)
    envolver(svg, nombre)
    os.unlink(prep)
    png = os.path.join(HERE, "png", f"{nombre}.png")
    render(svg, png, 1024)
    print("→", svg)
    print("→", png)
