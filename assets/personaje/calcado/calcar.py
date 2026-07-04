#!/usr/bin/env python3
"""
Calca una imagen PNG (generada p. ej. con Nanobanana/Whisk) a SVG vectorial limpio.

Flujo:  PNG con fondo blanco → quitar fondo (flood fill desde los bordes +
dilatación anti-halo, marcado con centinela magenta) → vectorizar con vtracer
(curvas spline, sin ruido) → eliminar el fondo del SVG → envolver con animación
de respiración → optimizar con svgo → exportar PNG transparente.

vtracer (motor de vectorizer.ai) da curvas suaves y sin motas, muy superior al
imagetracerjs anterior; svgo recorta ~50-60 % del peso sin tocar el dibujo.

Uso:
    python3 calcar.py entrada.png nombre-variante
    # produce: fuente/nombre.png  svg/nombre.svg  png/nombre.png (1024)

Requisitos: node + @neplex/vectorizer + svgo (se instalan solos la 1ª vez),
Chromium headless para el PNG (ver export_png.py).

Consejos para la imagen fuente: fondo blanco sólido, colores planos sin
degradados, contornos definidos, 1024×1024 o más.
"""
import json, os, shutil, struct, subprocess, sys, zlib
from collections import deque

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
    # limpiar islas: conservar solo la figura principal
    comp = [[0]*w for _ in range(h)]
    sizes = {}
    cid = 0
    for yy in range(h):
        for xx in range(w):
            if not seen[yy][xx] and comp[yy][xx] == 0:
                cid += 1
                qq = deque([(xx, yy)])
                comp[yy][xx] = cid
                n = 0
                while qq:
                    cx, cy = qq.popleft()
                    n += 1
                    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx, ny = cx+dx, cy+dy
                        if 0 <= nx < w and 0 <= ny < h and not seen[ny][nx] and comp[ny][nx] == 0:
                            comp[ny][nx] = cid
                            qq.append((nx, ny))
                sizes[cid] = n
    main = max(sizes, key=sizes.get)
    for yy in range(h):
        for xx in range(w):
            if not seen[yy][xx] and comp[yy][xx] != main:
                seen[yy][xx] = True
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


def _asegurar_deps():
    for mod in ("@neplex/vectorizer", "svgo"):
        pkg = mod.split("/")[-1] if "/" in mod else mod
        marca = os.path.join(HERE, "node_modules", *mod.split("/"))
        if not os.path.isdir(marca):
            subprocess.run(["npm", "install", mod, "--no-audit", "--no-fund"],
                           cwd=HERE, check=True, capture_output=True)


def trazar(prep, out_svg, canvas=1024):
    """Vectoriza con vtracer (spline), borra el fondo centinela y NORMALIZA a un
    lienzo canónico (1024×1024 por defecto) escalando el contenido, sea cual sea el
    tamaño de la fuente de Flow (1024, 1766, …). Así todas las mascotas comparten el
    mismo sistema de coordenadas y componer.py alinea bien."""
    w, h, _ct, _rows = read_png(prep)
    js = f"""
import {{ vectorize, ColorMode, Hierarchical, PathSimplifyMode }} from '@neplex/vectorizer';
import {{ readFile, writeFile }} from 'node:fs/promises';
const png = await readFile({json.dumps(prep)});
let svg = await vectorize(png, {{
  colorMode: ColorMode.Color,
  hierarchical: Hierarchical.Stacked,
  mode: PathSimplifyMode.Spline,
  filterSpeckle: 4,      // elimina motas (la mancha gris de imagetracerjs)
  colorPrecision: 6,
  layerDifference: 16,
  cornerThreshold: 60,
  lengthThreshold: 4,
  spliceThreshold: 45,
  maxIterations: 10,
  pathPrecision: 2,
}});
// borrar el fondo: cualquier path magenta (centinela, tolerante a la cuantización).
// vtracer emite `d` antes de `fill`, así que se busca fill en cualquier parte del tag.
svg = svg.replace(/<path\\b[^>]*?fill="#([0-9A-Fa-f]{{6}})"[^>]*?\\/>/g, (m, hex) => {{
  const r = parseInt(hex.slice(0,2),16), gg = parseInt(hex.slice(2,4),16), b = parseInt(hex.slice(4,6),16);
  return (r > 200 && gg < 70 && b > 200) ? '' : m;
}});
// NORMALIZAR a lienzo canónico {canvas}: escalar el contenido de la fuente ({w}x{h})
// y fijar viewBox, para que TODAS las mascotas compartan el mismo sistema de coords.
const kx = {canvas} / {w}, ky = {canvas} / {h};
const _open = svg.indexOf('>', svg.indexOf('<svg')) + 1;
const _inner = svg.slice(_open, svg.lastIndexOf('</svg>'));
svg = `<svg xmlns="http://www.w3.org/2000/svg" width="{canvas}" height="{canvas}" viewBox="0 0 {canvas} {canvas}">\\n`
    + `<g transform="scale(${{kx}} ${{ky}})">` + _inner + `</g>\\n</svg>`;
await writeFile({json.dumps(out_svg)}, svg);
"""
    _asegurar_deps()
    tmp = os.path.join(HERE, "_trace_tmp.mjs")
    with open(tmp, "w") as f:
        f.write(js)
    try:
        subprocess.run(["node", tmp], cwd=HERE, check=True, capture_output=True)
    finally:
        os.unlink(tmp)


def optimizar(svg):
    """svgo con la config segura para animación (../svgo.config.mjs). Idempotente."""
    cfg = os.path.join(HERE, "..", "svgo.config.mjs")
    subprocess.run(["npx", "svgo", "--config", cfg, svg, "-o", svg],
                   cwd=HERE, check=True, capture_output=True)


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
    svg = os.path.join(HERE, "svg", f"{nombre}.svg")
    trazar(prep, svg)
    envolver(svg, nombre)
    optimizar(svg)
    os.unlink(prep)
    png = os.path.join(HERE, "png", f"{nombre}.png")
    render(svg, png, 1024)
    print("→", svg, f"({os.path.getsize(svg)//1024} KiB)")
    print("→", png)
