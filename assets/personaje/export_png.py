#!/usr/bin/env python3
"""
Exporta los SVG de Dr. Cuack a PNG (fondo transparente) usando Chromium
headless. Requiere Chromium (en Claude Code web ya está en /opt/pw-browsers).

Uso:  python3 export_png.py [tamaño]     # por defecto 1024

Nota: Chromium headless recorta la parte inferior de la ventana cuando su
tamaño coincide exactamente con el contenido, así que se captura con margen
extra y se recorta el PNG (bug verificado; no quitar el PAD).
"""
import os, struct, subprocess, sys, tempfile, zlib

HERE = os.path.dirname(os.path.abspath(__file__))
CHROMIUM = os.environ.get("CHROMIUM", "/opt/pw-browsers/chromium")
PAD = 120

def read_png(fn):
    d = open(fn, "rb").read()
    pos, idat = 8, b""
    while pos < len(d):
        ln = struct.unpack(">I", d[pos:pos+4])[0]
        typ = d[pos+4:pos+8]
        if typ == b"IHDR":
            w, h, bd, ct = struct.unpack(">IIBB", d[pos+8:pos+18])
        if typ == b"IDAT":
            idat += d[pos+8:pos+8+ln]
        pos += 12 + ln
    raw = zlib.decompress(idat)
    bpp = {0: 1, 2: 3, 4: 2, 6: 4}[ct]
    stride = w*bpp + 1
    prev = bytearray(w*bpp)
    rows = []
    for y in range(h):
        f = raw[y*stride]
        row = bytearray(raw[y*stride+1:(y+1)*stride])
        for i in range(len(row)):
            a = row[i-bpp] if i >= bpp else 0
            b = prev[i]
            if f == 1: row[i] = (row[i]+a) & 255
            elif f == 2: row[i] = (row[i]+b) & 255
            elif f == 3: row[i] = (row[i]+(a+b)//2) & 255
            elif f == 4:
                c = prev[i-bpp] if i >= bpp else 0
                p = a+b-c; pa, pb, pc = abs(p-a), abs(p-b), abs(p-c)
                pr = a if pa <= pb and pa <= pc else (b if pb <= pc else c)
                row[i] = (row[i]+pr) & 255
        prev = row
        rows.append(bytes(row))
    return w, h, ct, rows

def write_png(fn, w, h, ct, rows):
    def chunk(typ, data):
        c = struct.pack(">I", len(data)) + typ + data
        return c + struct.pack(">I", zlib.crc32(typ+data) & 0xffffffff)
    ihdr = struct.pack(">IIBBBBB", w, h, 8, ct, 0, 0, 0)
    raw = b"".join(b"\x00"+r for r in rows)
    open(fn, "wb").write(b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", ihdr)
                         + chunk(b"IDAT", zlib.compress(raw, 9)) + chunk(b"IEND", b""))

def render(svg, out, size):
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False) as f:
        f.write(f'<!doctype html><style>html,body{{margin:0;padding:0}}</style>'
                f'<img src="file://{svg}" style="display:block;width:{size}px;height:{size}px">')
        html = f.name
    try:
        subprocess.run([CHROMIUM, "--headless", "--no-sandbox", "--hide-scrollbars",
                        f"--window-size={size},{size+PAD}",
                        "--default-background-color=00000000",
                        f"--screenshot={out}", f"file://{html}"],
                       check=True, capture_output=True)
        w, h, ct, rows = read_png(out)
        write_png(out, w, size, ct, rows[:size])
    finally:
        os.unlink(html)

if __name__ == "__main__":
    size = int(sys.argv[1]) if len(sys.argv) > 1 else 1024
    svgdir = os.path.join(HERE, "svg")
    outdir = os.path.join(HERE, "png")
    os.makedirs(outdir, exist_ok=True)
    for f in sorted(os.listdir(svgdir)):
        if not f.endswith(".svg"):
            continue
        out = os.path.join(outdir, f.replace(".svg", ".png"))
        render(os.path.join(svgdir, f), out, size)
        print("→", out)
