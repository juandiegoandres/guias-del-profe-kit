# Créditos — assets de `curiosidades.tex` (Química 9º · Video de cierre)

Usados en `material/9/ciencias/tabla-periodica/curiosidades.tex` y pensados para
que **ciencias-animador** anime el video (Manim). Notas de puesta en escena por
lámina: `assets/svg-src/quimica/NOTAS_animacion_curiosidades.md`.

> **Licencias permisivas: MIT / CC BY 3.0 / CC BY 4.0 + «libre uso personal y
> comercial» (bottts). Ninguna es CC BY-SA.** Todos los SVG son **planos, de
> `<path>`/`<circle>`, sin `<text>` ni bitmaps → aptos `SVGMobject`/Manim.**

---

## 1. Personaje: ROBOT CIENTÍFICO adaptable 🤖 (5 expresiones)

- Assets: **`robot_{explica,senala,sorprendido,celebra,sostiene}.svg`** → PDF
  `assets/imgs/quimica/robot_*.pdf`.
- **Origen:** estilo **«bottts»** de **Pablo Stanley** (https://bottts.com/),
  servido por la API de **DiceBear** (`9.x/bottts`).
- **Licencia:** el arte de *Bottts* es **«Free for personal and commercial use»**
  (permisivo, **sin copyleft/share-alike**; confirmado en la metadata RDF del SVG).
  El código de DiceBear es **MIT**. **NO es CC BY-SA.**
  > Nota de licencia: *bottts* NO es exactamente CC0/CC BY/MIT sino una licencia
  > propia «libre para uso personal y comercial». Cumple la regla dura (no es
  > CC BY-SA) y sirve para clases/MOOC. Si se quiere una licencia con nombre
  > estándar, alternativa: robot de **game-icons** (CC BY 3.0) — pero es una sola
  > silueta, no adaptable por expresión.
- **Personaje ADAPTABLE:** es **el mismo robot** (mismo `seed=Zap-lab-9`,
  `baseColor=7cb342` verde) con la **cara-pantalla cambiada por escena** (solo
  varían `eyes=` y `mouth=`):
  | pose (`robot_…`) | `eyes` / `mouth` | lectura |
  |---|---|---|
  | `explica`     | `round` / `smile01`      | narra, presenta |
  | `senala`      | `frame1` / `grill01`     | atento, dirige la mirada |
  | `sorprendido` | `bulging` / `square01`   | asombro (ojos saltones, boca abierta) |
  | `celebra`     | `happy` / `smile02`      | feliz, cierres |
  | `sostiene`    | `roundFrame01` / `diagram`| techy, mostrar un aparato |
- **Generar más expresiones** (mismo robot):
  ```
  curl -s "https://api.dicebear.com/9.x/bottts/svg?seed=Zap-lab-9&backgroundColor=transparent&baseColor=7cb342&eyes=<x>&mouth=<y>" -o robot_x.svg
  ```
  (`eyes`: round, frame1, bulging, happy, glow, hearts, robocop, sensor, shade01…
   `mouth`: smile01, smile02, grill01, grill02, square01, square02, diagram, bite…)
- No tiene brazos → los **props** (§2) se colocan **al lado** y el robot los "mira"
  / los señala con la pantalla; el animador puede unirlos.
- **Apto Manim/`SVGMobject`:** sí (`<text>`=0, `<image>`=0; todo `<path>`/`<circle>`
  de colores planos). Verificado con `rsvg-convert -w 190 robot_*.svg`.
- Encaja con el tema esmeralda (robot verde). Props de laboratorio extra: `prop_bata`,
  `prop_matraz`/`prop_matraz2` (§5).

## 2. Íconos temáticos de las curiosidades (`cur_*`) — props por escena

- Fuente: `cur_*.svg` · PDF esmeralda `#106E50`: `assets/imgs/quimica/cur_*.pdf`.
- **Origen:** **Tabler Icons** (https://tabler.io/icons) — **MIT**.
- `sed 's/currentColor/#106E50/g' cur_X.svg | rsvg-convert -f pdf -o cur_X.pdf`
- Mapa alias → ícono Tabler → uso como PROP del personaje:
  - `cur_bebida`   ← `bottle`             → bebida deportiva (electrolitos)
  - `cur_bateria`  ← `battery-charging`   → batería ion-litio (Li⁺)
  - `cur_nuclear`  ← `radioactive`        → energía / residuos nucleares
  - `cur_atomo_fis`← `atom-2`             → núcleo / fisión
  - `cur_sal`      ← `salt`               → salero / sal (NaCl, yodo)
  - `cur_pasta`    ← `dental`             → pasta dental / flúor
  - `cur_corazon`  ← `heart`              → Ca²⁺ / corazón
  - `cur_energia`  ← `bolt`               → impulso nervioso / electricidad
  - `cur_agua`     ← `droplet`            → gota de sudor / cloro del agua
  - `cur_planta`   ← `building-factory-2` → central (versión línea)
  - `cur_calor`    ← `flame`              → calor → vapor → turbina
  - `cur_celular`  ← `device-mobile`      → celular (baterías)
  - `cur_powerbank`← `battery-4`          → power bank / capacidad (mAh)
  - `cur_carro`    ← `car`                → auto eléctrico
  - `cur_solar`    ← `sun-electricity`    → energía solar almacenada
  - `cur_enchufe`  ← `plug-connected`     → cargar / potencia (W)
  - `cur_cargador` ← `charging-pile`      → cargador de auto eléctrico

## 3. Plantas nucleares y energía (`nuc_*`) — vectores planos

- Fuente: `nuc_*.svg` · PDF esmeralda transparente: `assets/imgs/quimica/nuc_*.pdf`.
- **Origen:** **game-icons.net** (autores **Delapouite** y **Lorc**) — **CC BY 3.0**
  (requiere atribución al autor; NO es CC BY-SA).
- Conversión (los game-icons traen un rect de fondo negro que se elimina):
  `sed 's|<path d="M0 0h512v512H0z"/>||; s/#fff/#106E50/g' nuc_X.svg | rsvg-convert -f pdf -o nuc_X.pdf`
  - `nuc_planta`     ← Delapouite `nuclear-plant`  → **torre de refrigeración con vapor + símbolo radiactivo** (la estrella para el reactor)
  - `nuc_torre`      ← Delapouite `water-tower`     → torre (apoyo / paisaje industrial)
  - `nuc_generador`  ← Delapouite `power-generator` → generador / turbina
  - `nuc_atomo`      ← Lorc `atomic-slashes`        → átomo con órbitas (energía nuclear)
  - `nuc_radiactivo` ← Lorc `radioactive`           → símbolo radiactivo grande
  - `nuc_residuos`   ← Delapouite `nuclear-waste`   → barril de residuos radiactivos (el "en contra")

## 4. Paisajes / escenas de fondo (`esc_*` game-icons · `bg_*` Tabler)

- **`esc_*`** — **game-icons.net** (Delapouite / Lorc) — **CC BY 3.0** — siluetas
  planas rellenas (buenas como capas de fondo recolorables):
  - `esc_montanas` (Lorc `mountains`), `esc_colinas` (Delapouite `hills`),
    `esc_carretera` (Delapouite `mountain-road`), `esc_sol` (Lorc `sun`),
    `esc_amanecer` (Delapouite `sunrise`), `esc_ciudad` (Delapouite `modern-city`).
- **`bg_*`** — **Tabler Icons** — **MIT** — versión **de línea** (más limpia, combina
  con el estilo del deck): `bg_montana`, `bg_sol`, `bg_nube`, `bg_arboles`,
  `bg_ciudad`.
- Uso previsto: ambientar (cielo/sol/nubes arriba, colinas/ciudad abajo) para que
  la escena de la central nuclear y las de "vida real" se vean **con profundidad**.

## 5. Props de ciencia extra (`prop_*`)

- `prop_matraz` (Tabler `flask`, **MIT**), `prop_idea` (Tabler `bulb`, **MIT**),
  `prop_matraz2` (game-icons Lorc `bubbling-flask`, **CC BY 3.0**),
  `prop_bata` (game-icons Delapouite `lab-coat`, **CC BY 3.0**).
- Para dar el "aire de laboratorio" al personaje (matraz en la mano, bombillo de
  idea al pensar, bata).

## 6. Gags / accesorios temáticos del personaje (`gag_*`)

Accesorios que le ponen un **chiste alusivo** al personaje por escena (guiño por
juego de palabras o referencia de ciencia). Puesta en escena: ver
`NOTAS_animacion_curiosidades.md` § *Gags por escena*. Todos **planos, Manim-safe**
(`<text>`=0, `<image>`=0; verificado con `rsvg-convert`).

| archivo | origen | licencia | gag |
|---|---|---|---|
| `gag_casco_hierro.svg` | **game-icons.net** — Delapouite `closed-barbute` | **CC BY 3.0** (atrib.; NO share-alike) | casco de **hierro** (Fe²⁺/Fe³⁺, «no se decide») |
| `gag_interrogacion.svg`| **Tabler Icons** `question-mark` | **MIT** | los `?` de indecisión (2+ vs 3+) |
| `gag_conejo_pila.svg`  | **game-icons.net** — Delapouite `rabbit` | **CC BY 3.0** | **conejito de las pilas** (batería ion-litio) |
| `gag_gorro_chef.svg`   | **Tabler Icons** `chef-hat` | **MIT** | gorro de chef (sal / NaCl / yodo) |
| `gag_gorro_helice.svg` | **game-icons.net** — Delapouite `propeller-beanie` | **CC BY 3.0** | gorro de **hélice = turbina** (nuclear, chiste limpio) |
| `gag_vincha.svg`       | **Original ZapiaLab** | **CC0** | vincha deportiva (electrolitos / sudor) |
| `gag_munequera.svg`    | **Original ZapiaLab** | **CC0** | muñequera deportiva (electrolitos / sudor) |
| `gag_cepillo.svg`      | **Original ZapiaLab** | **CC0** | cepillo con pasta (flúor) |

- Recolor / PDF igual que los demás: game-icons `sed 's|<path d="M0 0h512v512H0z"/>||; s/#fff/#106E50/g'`;
  Tabler y originales `sed 's/currentColor/#106E50/g'`.
- **Reutilizados como gag** (ya en el kit): `cur_agua` (gota de sudor), `cur_bebida`
  (botella deportiva), `cur_sal` (salero), `cur_energia` (rayo del conejo),
  `nuc_radiactivo` (símbolo ☢ del gorro de hélice).

---

### Atribución obligatoria en los créditos del video
> Personaje (robot 🤖): estilo **«Bottts»** de **Pablo Stanley** vía **DiceBear**
> — libre uso personal y comercial (código MIT). Íconos de energía/paisaje por
> **Delapouite** y **Lorc** — game-icons.net, **CC BY 3.0**. Íconos de interfaz:
> **Tabler Icons** — **MIT**.
