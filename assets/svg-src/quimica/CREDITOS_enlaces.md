# Créditos SVG — Enlace químico y estructuras de Lewis (videos 6 y 7)

> Archivo propio del lote videos 6–7. NO incluye los SVG de otros agentes
> (`atomo-*`, `ion_*`, `orbital-*`, `bohr-*`, `metal-*`, `diamante-*`,
> `flama-*`, etc.), que tienen sus propios créditos.

Todos los SVG de este lote son **originales**, dibujados como recurso TikZ
(`tikzlib/ciencias/lewis.tex`) y exportados con `pdftocairo -svg`.

- **Licencia:** CC0 / dominio público (obra propia del kit). NUNCA CC BY-SA.
- **Apto `SVGMobject` (Manim):** SÍ. Verificado: **0 `<text>`** (todo el texto es
  path), **0 `<image>`** (sin bitmaps), **0 gradientes/filtros**. Formas planas,
  submobjetos separables (átomos, enlaces y puntos son paths independientes).
- **Origen:** `tikzlib/ciencias/lewis.tex` → standalone en
  `tmp/quimica-svg/{figuras_multi,lewis_simbolos}.tex` → `pdftocairo -svg`.
- **Re-generar:** ver cabecera de cada `.tex` en `tmp/quimica-svg/`.

## Inventario

| Archivo | Contenido | Uso |
|---|---|---|
| `lewis_electron.svg` | un electrón (punto) | pieza atómica para animar |
| `lewis_simbolos.svg` | símbolos de Lewis Li…Ne (periodo 2) | valencia / octeto |
| `lewis_h2.svg` | H–H (enlace simple, dueto) | covalente simple |
| `lewis_o2.svg` | O=O (doble + 2 pares libres c/u) | covalente doble |
| `lewis_n2.svg` | N≡N (triple + 1 par libre c/u) | covalente triple |
| `lewis_h2o.svg` | H₂O angular (2 pares libres) | molécula polar |
| `lewis_co2.svg` | O=C=O lineal | molécula, dobles enlaces |
| `lewis_nh3.svg` | NH₃ piramidal (1 par libre) | molécula |
| `lewis_ch4.svg` | CH₄ (4 enlaces, sin pares libres) | molécula |
| `lewis_oh_ion.svg` | OH⁻ con corchetes y carga | ion poliatómico |
| `enlace_mar_electrones.svg` | mar de electrones (metálico) | esquema |
| `enlace_red_ionica.svg` | red cristalina NaCl (Na⁺/Cl⁻) | esquema iónico |

## Nota para el animador (Manim)

- Colores usados: `ink` RGB(28,28,30), `cnat` RGB(16,110,80), `cnatlima`
  RGB(124,169,60). En los Lewis moleculares el texto/enlaces salen en negro
  (`ink`) sobre fondo transparente.
- Los puntos de electrón son círculos independientes → animables uno a uno
  (ideal para "aparecer" electrones de valencia o transferirlos).
- La transferencia Na→Cl del video se arma en escena combinando
  `lewis_simbolos` (o los átomos sueltos) + una flecha de Manim; no se exportó
  como figura fija para dar libertad de animación.
