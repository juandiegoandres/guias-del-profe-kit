# Créditos y licencias — SVGs para Iones (Video 4) y Propiedades (Video 5)

> Este archivo cubre **solo los SVGs con prefijo `ion_*`** (lote de iones /
> propiedades periódicas). Otros agentes deben usar su propio prefijo y su
> propio archivo de créditos para no pisar este.

Building blocks para que **ciencias-animador** anime en Manim el paso
átomo → ion (perder/ganar electrón), cargas y estabilidad de gas noble.

## Fuente y licencia

Todos son de **[Tabler Icons](https://tabler.io/icons)** — **licencia MIT**
(permite uso comercial y modificación; NO es copyleft, NO es CC BY-SA).
Repositorio: `https://github.com/tabler/tabler-icons` (carpeta `icons/outline`
y `icons/filled`). Descargados con `curl` el 2026-07-02.

Trazo original `stroke="currentColor"` → se recolorea con
`sed 's/currentColor/#106E50/g'` (esmeralda del tema) antes de rasterizar o
convertir a PDF.

## Apto para `SVGMobject` (Manim) — VERIFICADO

Auditoría estructural: 0 bitmaps, 0 `linearGradient/radialGradient`, 0 `<filter>`,
0 `clipPath/mask`, 0 base64. Solo `<path>` planos.
Importación real probada con **Manim 0.20.1** (`SVGMobject(f)`): todos importan
con submobjetos separables y puntos > 0.

| Archivo | Icono Tabler | paths | submob. Manim | Uso didáctico |
|---|---|---|---|---|
| `ion_atomo.svg` | `atom-2` (outline) | 7 | 7 | Átomo con núcleo + electrones (los puntos son submobjetos separables → **animar un e⁻ que sale/entra**) |
| `ion_atomo_simple.svg` | `atom` (outline) | 3 | 3 | Átomo clásico (núcleo + 2 órbitas), silueta limpia |
| `ion_electron.svg` | `circle` (filled) | 1 | 1 | Electrón suelto (disco relleno) |
| `ion_punto.svg` | `point` (filled) | 1 | 1 | Electrón / punto pequeño alterno |
| `ion_carga_mas.svg` | `plus` (outline) | 2 | 2 | Signo **+** (catión) |
| `ion_carga_menos.svg` | `minus` (outline) | 1 | 1 | Signo **−** (anión) |
| `ion_carga_mas_circ.svg` | `circle-plus` | 3 | 3 | Carga **+** en círculo (badge de catión) |
| `ion_carga_menos_circ.svg` | `circle-minus` | 2 | 2 | Carga **−** en círculo (badge de anión) |
| `ion_estable.svg` | `shield-check` | 2 | 2 | **Estabilidad / octeto completo** (configuración de gas noble) |
| `ion_flecha_der.svg` | `arrow-right` | 3 | 3 | Flecha de proceso (átomo → ion) |

## Notas para el animador

- Para animar "el átomo pierde un electrón": usa `ion_atomo.svg`; los electrones
  entran como submobjetos independientes, así que se puede tomar uno con
  `atom.submobjects[i]` y desplazarlo fuera con `Transform`/`MoveToTarget`.
- Recolorear por submobjeto es directo (todos heredan `currentColor`).
- Si se necesita un electrón "orbital" adicional, reusar `ion_electron.svg` y
  posicionarlo a mano en una órbita.
