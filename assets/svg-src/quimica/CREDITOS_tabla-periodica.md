# Créditos y licencias — SVG animables · Química 9º (tabla periódica y enlace)

> Lote **videos 2 (Organización) y 3 (Configuración electrónica)**. SVG libres,
> pensados para animarse con `SVGMobject` de Manim (ciencias-animador).
> **Regla de licencia aplicada:** solo CC0 / Dominio público / CC BY / MIT / ISC.
> **NUNCA CC BY-SA** (share-alike) — varias piezas buenas se descartaron por esto (ver abajo).
>
> **Test "apto Manim":** Manim no estaba instalado en la máquina, así que se validó
> con el proxy acordado: `rsvg-convert` (render OK) + inspección de estructura
> (`<path>` vs `<image>`/`<linearGradient>`/`<radialGradient>`/`<filter>`).
> Criterio: apto = solo paths/trazos, sin bitmaps embebidos, sin gradientes/filtros
> complejos (esos Manim los aplana o ignora). Submobjetos separables = animable por partes.

## Aceptados (en esta carpeta)

| Archivo | Qué es | Fuente | Licencia | Apto Manim |
|---|---|---|---|---|
| `atomo-tabler.svg` | Símbolo de átomo (núcleo + 2 órbitas cruzadas) | Tabler Icons | **MIT** | **Sí** (3 paths) |
| `atomo2-tabler.svg` | Átomo con electrones como puntos en arcos | Tabler Icons | **MIT** | **Sí** (7 paths, partes separables) |
| `atomo-lucide.svg` | Átomo (línea) | Lucide | **ISC** | **Sí** (2 paths) |
| `orbita-lucide.svg` | Órbita con cuerpo (electrón girando) | Lucide | **ISC** | **Sí** (2 paths) |
| `electron-orbit-tabler.svg` | Círculo con punto central: electrón en una capa | Tabler Icons | **MIT** | **Sí** (2 paths) |
| `metal-gameicons.svg` | Lingote / barra de metal | game-icons.net (Lorc) | **CC BY 3.0** | **Sí** (1 path) |
| `orbital-1s-wikimedia.svg` | Orbital 1s como círculo (esfera en corte) | Wikimedia (`K1s atomic orbital icon`) | **Dominio público** | **Sí** (1 path) |
| `orbital-2p-wikimedia.svg` | Orbital 2p (corte esquemático con plano nodal) | Wikimedia (`L2p0`) | **Dominio público** | **Sí** (1 path) |
| `orbital-3p-wikimedia.svg` | Orbital 3p (corte con nodo radial) | Wikimedia (`M3p0`) | **Dominio público** | **Sí** (2 paths) |
| `orbital-3d-dz2-wikimedia.svg` | Orbital 3d (corte con 2 planos nodales) | Wikimedia (`M3d0`) | **Dominio público** | **Sí** (1 path) |
| `orbital-s-wikimedia.svg` | Orbital s como esfera sombreada sobre ejes x/y/z (con rótulo "s") | Wikimedia (`Orbital s`) | **Dominio público** | **Parcial** — 60 `linearGradient` + 160 `radialGradient` (esfera difusa). Renderiza bien y sirve como `\includegraphics`; en Manim los gradientes se aplanan a color plano (perderá el degradado). Es el visual más "bonito" de la esfera s. |
| `bohr-esp-wikimedia.svg` | Modelo de capas de Bohr: núcleo + capas n=1,2,3 + salto de energía | Wikimedia (`Bohr atom model Spanish`) | **CC BY 4.0** | **Parcial** — 6 paths pero 3 `<filter>` (sombras) que Manim ignora; además los rótulos están en **inglés** ("Increasing energy", "Photon is emitted E=hf"). Sirve como referencia del modelo de capas; para el video conviene re-rotular en Manim. |
| `diamante-tabler.svg` | Gema/diamante (proxy visual de no metal, p. ej. carbono/azufre) | Tabler Icons | **MIT** | **Sí** (2 paths). *Semántica floja*: es un ícono ilustrativo, no un símbolo estándar de "no metal". |
| `flama-tabler.svg` | Llama (reactividad de no metales) | Tabler Icons | **MIT** | **Sí** (1 path). Ícono ilustrativo. |

## Notas de uso (importante para el animador)

- **Formas de orbital p (mancuerna) y d (trébol):** las versiones limpias en SVG que
  existen en Wikimedia (`S-p-Orbitals`, `D orbitals`, `Shapes of hybrid orbitals`) son
  todas **CC BY-SA → descartadas**. Las piezas PD aceptadas (`orbital-2p/3p/3d`) son
  **cortes esquemáticos** (círculo con planos nodales), no la mancuerna/trébol que el
  estudiante espera. **Recomendación:** para las láminas y el video, dibujar los lóbulos
  (mancuerna p, trébol d) **nativos en Manim** (superficies paramétricas) o en TikZ —
  quedan más claros y bajo control. En el deck `config_electronica.tex` los orbitales
  s/p/d se dibujan así (TikZ), no con estos SVG.
- **Icono de "no metal":** no hay un símbolo estándar; `diamante`/`flama` son proxies.
  Alternativa: representar los no metales como molécula diatómica (p. ej. Cl₂) dibujada.

## Descartados por licencia (NO usar — CC BY-SA / share-alike)

- `Bohr atom model.svg` — CC BY-SA 3.0
- `Stylised Lithium Atom` (átomo de Bohr estilizado) — CC BY-SA 3.0
- `S-p-Orbitals.svg` (mancuerna p bonita) — CC BY-SA 3.0
- `D orbitals.svg` (trébol d) — CC BY-SA 3.0
- `Diagrama orbital Carbono.svg` — CC BY-SA 4.0
- `Shapes of hybrid orbitals.svg` — CC BY-SA 4.0
- Serie `Electron shell NNN <elemento>.svg` (diagramas de capas de Bohr por elemento,
  H, C, O, Na, Cl…) — **CC BY-SA 2.0 UK**. Habrían sido ideales para los ejemplos, pero
  el share-alike las excluye. Sustituto libre: `bohr-esp-wikimedia.svg` (CC BY 4.0) o
  dibujar las capas en TikZ/Manim.

## Atribución para los créditos del video (piezas que la exigen)

- **CC BY 4.0** — `bohr-esp-wikimedia.svg`: "Bohr atom model, JabberWok/Wikimedia Commons, CC BY 4.0".
- **CC BY 3.0** — `metal-gameicons.svg`: "Metal bar icon by Lorc, game-icons.net, CC BY 3.0".
- **MIT / ISC / Dominio público** — no exigen atribución, pero se listan por transparencia.
