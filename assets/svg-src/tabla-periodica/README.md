# Tabla periódica — export SVG (para Manim / ciencias-animador)

SVG **generados** a partir del recurso TikZ del kit
(`tikzlib/ciencias/tabla_periodica.tex`). Son **obra propia** del kit (no llevan
licencia de terceros). Fuentes trazadas a **paths** (sin dependencia de fuentes)
→ aptos para `SVGMobject` de Manim.

| SVG | Contenido |
|---|---|
| `tabla_periodica.svg` | Tabla completa (118 elementos) coloreada por familia + leyenda |
| `tendencia_radio.svg` | Tabla atenuada + flechas: radio atómico (↓ grupo, ← periodo) |
| `tendencia_ei.svg`    | Energía de ionización (↑ grupo, → periodo) |
| `tendencia_en.svg`    | Electronegatividad (↑, →; resalta el F) |

## Regenerar (desde la raíz del kit)

```bash
# 1) TeX -> PDF vectorial (dos pasadas, limpia auxiliares)
./compile_quiet.sh assets/svg-src/tabla-periodica/tabla_periodica_std.tex   tabla_periodica   assets/imgs/tabla-periodica
./compile_quiet.sh assets/svg-src/tabla-periodica/tendencia_radio_std.tex   tendencia_radio   assets/imgs/tabla-periodica
./compile_quiet.sh assets/svg-src/tabla-periodica/tendencia_ei_std.tex      tendencia_ei      assets/imgs/tabla-periodica
./compile_quiet.sh assets/svg-src/tabla-periodica/tendencia_en_std.tex      tendencia_en      assets/imgs/tabla-periodica

# 2) PDF -> SVG (paths, sin fuentes)  ·  poppler pdftocairo
for f in tabla_periodica tendencia_radio tendencia_ei tendencia_en; do
  pdftocairo -svg assets/imgs/tabla-periodica/$f.pdf assets/svg-src/tabla-periodica/$f.svg
done
```

> **Nota:** en este Mac `dvisvgm --pdf` NO tiene backend PDF (falta mutool) y
> `pdf2svg` no está instalado. La ruta que funciona es **`pdftocairo -svg`**
> (poppler), que ya escribe el texto como paths — verificado: 0 `<text>`, todo
> `<path>`. Alternativa: `rsvg-convert` sirve para SVG→PNG (verificación), no
> para PDF→SVG.

## Uso en Manim

```python
tabla = SVGMobject("assets/svg-src/tabla-periodica/tabla_periodica.svg")
```
Como es todo paths, no requiere las fuentes Inter instaladas en el entorno Manim.
