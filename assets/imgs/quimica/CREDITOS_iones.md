# Créditos — PDFs vectoriales `ion_*` (derivados)

Estos `ion_*.pdf` se generaron desde `assets/svg-src/quimica/ion_*.svg`
(**Tabler Icons, licencia MIT**) recoloreados a esmeralda `#106E50` con:

```
sed 's/currentColor/#106E50/g' ion_X.svg | rsvg-convert -f pdf -o ion_X.pdf
```

Licencia y detalle completo (incl. aptitud para `SVGMobject`/Manim):
`assets/svg-src/quimica/CREDITOS_iones.md`.

Se usan en `material/9/ciencias/tabla-periodica/iones.tex` (Video 4).
