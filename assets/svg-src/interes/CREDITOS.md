# Créditos SVG — Interés simple y compuesto (capibara/chigüiro colombiano)

Assets para la serie de matemática financiera con un **chigüiro (capibara)
colombiano** como personaje y **naranjas** como "moneda que crece".

**Regla de licencias:** solo CC0 / dominio público / CC BY / MIT / ISC.
**NUNCA CC BY-SA.** Descartados por ser CC BY-SA: `File:Capybara.svg`
(CC BY-SA 4.0) y `File:Capybara icon.svg` (CC BY-SA 3.0) de Wikimedia, y
`arcticons:capybara` (CC BY-SA 4.0).

**Verificación Manim (`SVGMobject`):** todos los archivos de este inventario se
importaron sin error con el `SVGMobject` de Manim (venv del proyecto
`videotutoriales-mate`) y se revisaron por `<image>` (bitmaps), gradientes,
filtros y `<text>`. Método: `head`/`grep` + import real. Preview con
`rsvg-convert`.

---

## 1. CAPIBARA / CHIGÜIRO (personaje) — elegir uno

| Archivo | Fuente | Autor | Licencia | Estilo | Manim (`SVGMobject`) |
|---|---|---|---|---|---|
| **`oc-capybara.svg`** ⭐ | Openclipart id 355183 | — | **CC0 / PD** | Caricatura plana, coloreada, **de frente, sentado con patas visibles** | 27 submobs · 452 pts · 0 img/grad/text — **óptimo** |
| `capibara-gameicons.svg` | game-icons.net (via Iconify) | Caro Asercion | **CC BY 3.0** | Silueta lateral, **capibara anatómico realista** | 1 path · 212 pts · monocolor recoloreable |
| `capibara-gameicons-white.svg` | game-icons.net (Wikimedia) | Caro Asercion | **CC BY 3.0** | Igual, relleno blanco (para invertir) | 1 path · 212 pts |
| `capibara-senal-colombia.svg` | Wikimedia Commons | señal SP-49 (gobierno CO) | **Dominio público** | Señal de tránsito colombiana (rombo amarillo) con silueta de chigüiro | 4 submobs · silueta aislable del rombo |
| `oc-chiguiro-pajarito.svg` | Openclipart id 192068 | — | **CC0 / PD** | "Chigüiro y pajarito": chigüiro marrón realista con pájaro azul en el lomo, **muy colombiano** | 10 submobs · **16 gradientes** (Manim los aplana a color sólido) · 17 532 pts (pesado) |
| `oc-capybara-old.svg` | Openclipart id 26757 | — | **CC0 / PD** | Grabado/line-art vintage (no plano) | 1 path · 14 112 pts (pesado, no recomendado para estilo amable) |

### Recomendación
Para **estilo kawaii/chibi**, usar el original propio **`capibara_kawaii.svg`**
(ver §1-bis). Entre los de terceros, el más apto es **`oc-capybara.svg`** (⭐ CC0)
como alternativa "caricatura libre". Es el más apto para esta serie: plano, coloreado,
amigable, **de frente y sentado con patas al frente** (ideal para "sostener" o
recibir naranjas), 27 submobjetos separables (ojos, hocico, patas → animables
por partes) y muy ligero. Al ser CC0 no exige atribución (igual se acredita).

Alternativa "chigüiro auténtico colombiano": **`oc-chiguiro-pajarito.svg`** —
el más reconocible como chigüiro y con guiño local (el pajarito), pero es
pesado y usa gradientes que Manim aplanará (se pierde el sombreado; conviene
re-rellenar los paths con colores planos si se elige).

Segunda opción limpia: **`capibara-gameicons.svg`** (silueta, 1 path) — perfecta
para recolorear en Manim (rellenar de marrón/naranja) y anexar el sombrero,
pero es de perfil (menos "abrazable").

> Nota: se descartó `oc-capybara-jacket.svg` (Openclipart 349108) por **XML
> malformado** (`unclosed token`, falla en `SVGMobject`) y `oc-capybara2.svg`
> (Openclipart 348465) por traer un **bitmap `<image>` incrustado** (1.1 MB).

---

## 1-bis. CAPIBARA KAWAII / CHIBI — obra propia (CC0) ⭐ recomendado

Como los stickers kawaii de referencia tienen **copyright** (no se copian) y en
el ecosistema libre **no existe un capibara "estilo sticker kawaii" con licencia
permisiva** (búsqueda 2026 en Openclipart, Iconify y SVG Repo, ver §1), se
**dibujó uno ORIGINAL** en TikZ inspirado solo en el *estilo* (no en ningún
sticker concreto).

| Archivo | Origen | Licencia | Estilo | Manim (`SVGMobject`) |
|---|---|---|---|---|
| **`capibara_kawaii.svg`** ⭐ | Obra propia del kit (`tikzlib/interes/capibara_kawaii.tex`) | **CC0** | Chibi MUY tierno (estilo "EconoMonos"): cuerpo redondo pastel, ojos grandes con doble brillo, nariz grande redondeada, cachetes rosa suave, sonrisa feliz | **20 submobs** · paths · 0 img/grad/text — **verificado import OK** |

- **Fuente TikZ:** `tikzlib/interes/capibara_kawaii.tex` (macro `\capibarakawaii`).
  Driver standalone: `assets/svg-src/interes/capibara_kawaii_std.tex`.
- **Regenerar** (desde la raíz del kit):
  ```bash
  ./compile_quiet.sh assets/svg-src/interes/capibara_kawaii_std.tex capibara_kawaii assets/imgs/interes
  pdftocairo -svg assets/imgs/interes/capibara_kawaii.pdf assets/svg-src/interes/capibara_kawaii.svg
  ```
- **Parametrizable / recoloreable:** `\capibarakawaii[hold]` (bracitos arriba
  para sostener la naranja), `[wink]` (guiño → parpadeo), `[blush=false]`;
  colores vía `\colorlet{capicuerpo}{...}` (o los `\providecolor` del `.tex`).
- **Partes separables (submobjects para animar en Manim), orden real (pose neutra):**

  | idx | parte | idx | parte |
  |---|---|---|---|
  | 0–1 | orejas (ext. izq/der) | 11 | ojo izq |
  | 2–3 | orejas (int. izq/der) | 12–13 | brillos ojo izq (grande/chico) |
  | 4 | cuerpo | 14 | ojo der |
  | 5–6 | patitas izq/der | 15–16 | brillos ojo der (grande/chico) |
  | 7–8 | bracitos izq/der | 17 | hocico (parche) |
  | 9–10 | rubor izq/der | 18 | nariz |
  |  |  | 19 | boca (trazo) |

  Parpadeo → escalar en *y* los índices `11–16` (ojos + brillos). Sostener → usar
  `[hold]` o desplazar los bracitos `7,8`. Guiño (`[wink]`) sustituye el ojo izq
  por un trazo curvo (esa pose tiene menos submobjects). Cada pieza tiene su color
  de relleno propio, así que se recolorea por submobject sin tocar el resto.
- **Recomendación:** usar este (`capibara_kawaii.svg`) como personaje kawaii de la
  serie. Es el que mejor calza con el *estilo* pedido (chibi, ojos grandes,
  colores planos pastel), es 100 % libre (CC0, obra propia, sin dependencias de
  fuentes) y está pensado para animarse por partes.

---

## 1-ter. SISTEMA MODULAR DEL CAPIBARA — trajes · fondos · naranjas (obra propia, CC0) ⭐

El capibara kawaii se amplió a un **set actuable estilo "EconoMonos"**: se
**disfraza por escena** y actúa en **contextos** simples, con **naranjas 🍊 como
moneda que crece**. Todo es **obra propia (CC0)**, plano, tierno, recoloreable y
**verificado en `SVGMobject`** (0 `<image>` / gradiente / `<text>`).

- **Fuentes TikZ:** `assets/svg-src/interes/{_estilo_interes,trajes,fondos,naranjas}.tex`
  (colores, macros y frames). Los trajes/naranjas se dibujan **en las mismas
  coordenadas que el capibara** (`tikzlib/interes/capibara_kawaii.tex`, y-arriba).
- **Regenerar TODO** (desde la raíz del kit): `bash assets/svg-src/interes/build_interes.sh`
  (escribe drivers temporales `std_*`/`prev_*`, compila, exporta SVG y PNG, y los
  borra al terminar). PDFs vectoriales en `assets/imgs/interes/`.
- **Recolorear:** `\colorlet{<color>}{...}` antes de dibujar (paleta en `_estilo_interes.tex`),
  o en Manim por submobject (cada pieza tiene su fill propio).

### a) DISFRACES / accesorios — `traje_*.svg` (overlays sueltos, frame `\capiframe`)

Overlays planos que se ponen **sobre el capibara sin taparle la cara** (zona segura:
ojos `(±0.54, 0.50)` tope `y≈0.85`; nariz `(0,0)`; boca `(0,-0.30)`).

| Archivo | Papel | Contenido | Ancla (coords capibara, y-arriba) | Manim |
|---|---|---|---|---|
| `traje_vueltiao.svg` | explicar / colombiano | sombrero vueltiao (ala + copa, caña flecha crema con bandas "pintao") | ala centrada `(0,1.30)` rx 1.78; copa hasta `y≈2.00`; centro-x = capibara | 7 submobs |
| `traje_banquero.svg` | "el banco" | corbatín vino + monóculo dorado con cadenita | corbatín `(0,-0.90)`; monóculo aro r 0.48 sobre ojo der. `(0.54,0.50)`; cadenita a `(0.86,-0.52)` | 8 submobs |
| `traje_comerciante.svg` | "el mercado" | delantal azul (peto+falda+bolsillo) + gorra roja con visera | gorra `(0,1.46)` rx 0.98 + visera `(0,1.02)`; delantal peto `(0,-0.88)`, falda hasta `y≈-1.98` | 10 submobs |
| `traje_academico.svg` | explicar | birrete (mortarboard) + gafas redondas | banda `(0,1.48)`, tabla cima `y≈2.04`, borla a `(1.16,0.98)`; gafas aros r 0.46 sobre ambos ojos | 11 submobs |
| `traje_ahorrador.svg` | ahorrar | gorrito mostaza con pompón **+ alcancía-cerdito al lado** (con una naranja-moneda entrando por la ranura) | gorrito `(0,1.50)` + pompón `(0,2.14)`; cerdito cuerpo `(1.98,-1.14)` rx 0.64, hocico `(2.56,-1.16)` | 17 submobs |

> Todos comparten el **frame `\capiframe`** = `(-2.75,-2.10)–(2.75,2.25)` con `border=8pt`.

### b) CAPIBARA YA VESTIDO — `capibara_<traje>.svg` (compuesto, turn-key para Manim) ⭐

Composición autoritativa **capibara + traje en el mismo dibujo** (bbox ajustado, sin
frame). Es la forma **recomendada** para animar el look en Manim (un solo
`SVGMobject`, posición garantizada): `capibara_vueltiao` (27), `capibara_banquero`
(28), `capibara_comerciante` (30), `capibara_academico` (31), `capibara_ahorrador`
(37 submobs). Previews PNG: `assets/imgs/interes/prev_look_*.png`.

> **⚠️ Alineación en Manim (gotcha real):** superponer un `traje_*.svg` suelto sobre
> el capibara **NO auto-registra**. `SVGMobject` **recorta al contenido visible** e
> **ignora el `viewBox`/frame**, y normaliza cada archivo a un tamaño por defecto;
> `should_center=False` **tampoco** los alinea. Por eso: para el look listo usa el
> **SVG compuesto** `capibara_<traje>.svg`; para superponer un overlay recoloreado,
> escálalo con la **misma razón** que el capibara (misma unidad TikZ) y ubícalo con el
> **ancla** de la tabla, o recompón en TikZ. (El frame compartido solo sirve para
> mantener proporciones entre exportes, no para registro automático en Manim.)

### c) CONTEXTOS / fondos — `fondo_*.svg` (escena 16:9, van DETRÁS del capibara)

Escenarios flat en lienzo `\escenaframe` = `(-6.40,-3.60)–(6.40,3.60)` (16:9). El
**piso** está a `y≈-1.95` para que el capibara (pies en `y≈-1.96`) **pise el suelo**;
va **centrado y al frente a escala 1**. Previews: `prev_escena_*.png`.

| Archivo | Escena | Elementos | Manim |
|---|---|---|---|
| `fondo_neutro.svg` | limpio | pared crema + piso + halo suave + sombra de pie | 5 submobs |
| `fondo_banco.svg` | banco | 2 columnas con estrías + arco/frontón + mostrador lateral | 18 submobs |
| `fondo_mercado.svg` | mercado | toldo a rayas rojo/crema (festón) + puesto de madera + postes | 29 submobs |
| `fondo_finca.svg` | finca/campo | cielo + sol con rayos + nubes + colinas + pasto + matas | 33 submobs |

### d) NARANJAS = dinero — `naranja*.svg` (obra propia, complementan las de §3)

Naranja plana propia (círculo + brillo + ombligo + hoja), a juego con el capibara.

| Archivo | Uso | Contenido | Manim |
|---|---|---|---|
| `naranja.svg` | unidad ("1") | 1 naranja centrada, r≈0.5 | 7 submobs |
| `naranja_pila.svg` | "muchas" (crecimiento) | **pirámide de 10** (4-3-2-1), base `y≈-0.55`, cima `y≈1.70` | 70 submobs |
| `naranja_canasta.svg` | "saco/canasta" | canasta de mimbre rebosante de naranjas | 45 submobs |

> Macro `\naranjaen{x}{y}{s}` (en `naranjas.tex`) coloca/escala una naranja para
> armar pilas de cualquier cantidad (**1 → varias → muchas**). Preview de las tres:
> `prev_dinero_naranjas.png`.

### e) CAPIDÓLARES = el DINERO que crece — `capidolar_*.svg` (obra propia, CC0) ⭐

**Moneda propia de la serie.** Con los capidólares el reparto queda claro: los
**capidólares** son el **capital/ahorro que crece con el interés** y las **naranjas
pasan a ser los BIENES** que se compran (`naranjas.tex`). Todo **obra propia (CC0)**,
plano, dorado/mostaza, a juego con el capibara kawaii, **recoloreable** y
**verificado en `SVGMobject`** (import OK · 0 `<text>`/`<image>`/gradiente/filtro).

- **Fuente TikZ:** `tikzlib/interes/capidolar.tex` (colores + macros). Depende de
  `_estilo_interes.tex` (oro/orodark) y `capibara_kawaii.tex` (colores/estilo capi;
  reusa la **carita** vía `\capicara`). Regenera con `bash assets/svg-src/interes/build_interes.sh`.
- **Símbolo propio de la moneda:** una **"Ȼ"** = *C abierta a la derecha + barra
  vertical* (macro `\dgcur`). **Todos los números/símbolos se dibujan como TRAZOS
  TikZ (paths), nunca como texto/fuente** → tras `pdftocairo -svg` quedan `<path>`
  (0 `<text>`): sin dependencia de fuentes, ideal para `SVGMobject`.
- **Recolorear:** `\colorlet{oro}{...}\colorlet{capidorofill}{...}` antes de dibujar.

| Archivo | Papel | Contenido | Manim (`SVGMobject`) |
|---|---|---|---|
| **`capidolar_moneda.svg`** ⭐ | unidad de dinero ("1") | moneda redonda: canto serrado + anillo dorado, cara mostaza con la **carita del capibara** + valor **`Ȼ1`** | 52 submobs · 2.01×2.00 |
| `capidolar_billete.svg` | montos grandes | billete: doble marco + **retrato del capibara en óvalo** + valor **`Ȼ10`** | 23 submobs · 3.68×2.00 |
| `capidolar_pila.svg` | crecimiento (1→muchas) | **torre de 6 monedas** (vistas de lado), `Ȼ` en la cima | 26 submobs · 1.38×2.00 |
| `capidolar_saco.svg` | ahorro / monto acumulado | saco de lona con amarre + **`Ȼ`** al frente | 5 submobs · 2.31×2.00 |
| `naranja_precio.svg` | inflación | naranja (**= bien**) con **cartelito de precio** (muestra `Ȼ`, sin texto) | 12 submobs · 1.96×2.00 |

- **Macros turn-key:** `\capidolarmoneda`, `\capidolarbillete`, `\capidolarpila`,
  `\capidolarsaco`, `\naranjaprecio`. Bloques reutilizables: `\capicara` (carita),
  `\capipuck{cx}{cy}` (una moneda de lado → arma pilas de cualquier altura para
  animar el crecimiento del interés compuesto), `\dgcur/\dgone/\dgzero{x}{y}{s}`.
- **Previews PNG:** `prev_capidolar_{moneda,billete,pila,saco}.png`,
  `prev_naranja_precio.png`, `prev_capidolar_crece.png` (1→3→6 torres) y catálogo
  `tikzlib/previews/capidolar.png`.

---

## 2. SOMBRERO (toque colombiano) — para el "capibara colombiano"

| Archivo | Fuente | Licencia | Notas | Manim |
|---|---|---|---|---|
| **`sombrero-vueltiao-2.svg`** ⭐ | Openclipart id 144283 | **CC0 / PD** | Vueltiao auténtico (caña flecha gris/blanca) sobre círculo con la bandera de Colombia | 20 submobs · 0 text/grad · limpio |
| `sombrero-vueltiao-1.svg` | Openclipart id 145609 | **CC0 / PD** | Vueltiao amarillo/negro estilizado. Trae un `<text>` "Sombrero Vueltiao" que **Manim ignora** (no se dibuja); el sombrero en sí queda limpio | 17 submobs |
| `sombrero-gameicons.svg` | game-icons.net (Iconify) | **CC BY 3.0** | Sombrero genérico (estilo mexicano) monocolor, **recoloreable** como comodín | 1 path |

**Recomendado:** `sombrero-vueltiao-2.svg` (vueltiao real, CC0). Si se quiere solo
el sombrero sin el círculo tricolor, aislar los submobjetos del sombrero y
descartar los del fondo.

---

## 3. NARANJA / MANDARINA (la "moneda" que crece) — elegir uno

| Archivo | Fuente | Licencia | Notas | Manim |
|---|---|---|---|---|
| **`naranja-fluent-flat.svg`** ⭐ | Microsoft Fluent Emoji (flat) `tangerine` | **MIT** | Naranja plana con hoja verde, súper limpia, **sin atribución obligatoria** | 2 submobs · 0 grad |
| `naranja-twemoji.svg` | Twemoji `1f34a` | **CC BY 4.0** | Naranja plana clásica (fills sólidos) | 3 submobs |
| `naranja-noto.svg` | Google Noto Emoji `tangerine` | **CC BY 4.0** (Apache-2.0 código) | Estilo Noto, plano | 6 submobs |
| `naranja-fluent.svg` | Fluent Emoji (3D/color) `tangerine` | **MIT** | Versión con volumen; trae **1 gradiente** (Manim lo aplana) | 12 submobs |

**Recomendado:** `naranja-fluent-flat.svg` (MIT, plano, sin gradientes). Ideal
para duplicar/escalar como unidad monetaria.

---

## 4. ÍCONOS DE APOYO — Tabler Icons

Fuente: **Tabler Icons** (via Iconify). Licencia **MIT** (sin atribución
obligatoria; se acredita igual). Trazo de línea, 1–2 submobjetos, 0 img/grad/text.
Recoloreables. Los ejes/curvas de crecimiento pueden hacerse **nativos** en
Manim/TikZ; estos íconos sirven como refuerzo visual.

| Archivo | Icono Tabler | Uso |
|---|---|---|
| `icono-crece-linea.svg` | `trending-up` | crecimiento lineal (interés simple) |
| `icono-curva.svg` | `chart-line` | curva / gráfica (interés compuesto) |
| `icono-calendario.svg` | `calendar-month` | tiempo (periodos) |
| `icono-reloj.svg` | `clock-hour-3` | tiempo / plazo |
| `icono-moneda.svg` | `coin` | dinero / capital |
| `icono-saco-dinero.svg` | `moneybag` | ahorro / monto acumulado |
| `icono-flecha-crece.svg` | `arrow-up-right` | "crece" |
| `icono-cerdito-ahorro.svg` | `pig-money` | ahorro (bonus) |

---

## 5. PROPS de VALOR AGREGADO e IMPUESTOS (bloques F y G) — libres, recoloreados al tema

Props planos para los videos y las guías de **valor agregado** ("de la naranja al
jugo") e **impuestos** ("¿para qué sirven?"). Todos **libres (NUNCA CC BY-SA)**,
paths planos, **0 `<image>`/gradiente/`<text>`**, **verificados import OK en
`SVGMobject`** (venv de `videotutoriales-mate`) y recoloreados a la paleta de la
serie (índigo `#46377E` · dorado capidólar `#D2A63C` · naranja fruta `#F59E0B`).
PNG para LaTeX en `assets/imgs/interes/` (`rsvg-convert -w 600`).

| Archivo | Fuente | Autor | Licencia | Edición aplicada | Manim (`SVGMobject`) |
|---|---|---|---|---|---|
| **`jugo_vaso.svg`** | Twemoji `cup-with-straw` (1f964) | Twitter | **CC BY 4.0** | líquido azul → **naranja** (jugo): `#55acee→#F59E0B`, `#3b88c3→#D97706`, `#88c9f9→#FBBF24`; pitillo a rayas intacto | 14 submobs · vaso de jugo de naranja |
| **`exprimidor.svg`** | game-icons `manual-juicer` | Delapouite | **CC BY 3.0** | `currentColor` → índigo `#46377E` (recoloreable) | 1 path · exprimidor manual de cítricos |
| **`recibo_iva.svg`** | Twemoji `receipt` (1f9fe) | Twitter | **CC BY 4.0** | + barra dorada `#D2A63C` marcando la **línea del IVA** (sin `<text>`, apta SVGMobject) | 4 submobs · factura con línea IVA resaltada |

> **Atribución (para la ficha del video):** *"Emoji de Twitter Twemoji, CC BY 4.0"*
> (`jugo_vaso`, `recibo_iva`) y *"Manual juicer icon by Delapouite, game-icons.net,
> CC BY 3.0"* (`exprimidor`). **Ninguno es CC BY-SA.** Descartados por no encajar:
> `twemoji:beverage-box` (caja, no vaso), `twemoji:tumbler-glass` (lee como trago con
> hielo), `tabler:receipt` (line-art monocromo, sin relleno plano de la serie).
> El "IVA" se marca como **barra de color** (no texto) porque `SVGMobject` **ignora
> `<text>`**: una etiqueta escrita no se dibujaría en Manim.

- **Regenerar / recolorear:** los tres se re-descargan de Iconify
  (`https://api.iconify.design/<set>/<icono>.svg`) y se reaplican los reemplazos de
  color de arriba; o se editan los fills directamente (cada pieza tiene su color).

---

## Resumen de licencias (para la ficha/atribución del video)

- **CC0 / Obra propia del kit (sin atribución):** `capibara_kawaii.svg` y todo el
  **sistema modular** (§1-ter): `traje_*.svg`, `capibara_<traje>.svg`, `fondo_*.svg`,
  `naranja{,_pila,_canasta}.svg`, y los **CAPIDÓLARES** (§1-ter-e):
  `capidolar_{moneda,billete,pila,saco}.svg` + `naranja_precio.svg` — dibujados en
  TikZ, originales (símbolo `Ȼ` propio, no copia de moneda/logo real), sin
  dependencias de fuentes.
- **CC0 / Dominio público (sin atribución):** `oc-capybara.svg`,
  `oc-chiguiro-pajarito.svg`, `oc-capybara-old.svg` (Openclipart);
  `sombrero-vueltiao-1/2.svg` (Openclipart); `capibara-senal-colombia.svg`
  (señal oficial CO, Wikimedia).
- **MIT (sin atribución, se acredita):** naranjas Fluent Emoji; íconos Tabler.
- **CC BY (requiere atribución):** `capibara-gameicons*.svg` — *"Capybara icon
  by Caro Asercion, game-icons.net, CC BY 3.0"*; naranjas Twemoji (*"Twitter,
  CC BY 4.0"*) y Noto (*"Google Noto Emoji, CC BY 4.0"*); **props §5**:
  `jugo_vaso.svg`/`recibo_iva.svg` (*"Twemoji, Twitter, CC BY 4.0"*) y
  `exprimidor.svg` (*"Delapouite, game-icons.net, CC BY 3.0"*).
- **NINGUNO es CC BY-SA.** ✅

### Cómo re-descargar
- Openclipart: `https://openclipart.org/download/<ID>` (sigue el 301 al slug).
- Iconify (Tabler/Fluent/Twemoji/Noto/game-icons):
  `https://api.iconify.design/<set>/<icono>.svg`.
- Wikimedia: página `File:` → enlace del archivo original.

## Mapas — caso Colombia (interés / historia económica)

| Archivo | Fuente | Autor | Licencia | Notas |
|---|---|---|---|---|
| **`mapa_colombia.svg`** ⭐ | Wikimedia `File:Colombia-map-sr.svg` | Obradovic Goran | **Dominio público (PD)** | Colombia (crema) + vecinos e **istmo de Panamá**, Caribe, Pacífico, ríos y estrella en Bogotá. Modificado: se quitaron los rótulos en serbio. Verificado en `SVGMobject` (65 submobs, 0 text/img/grad). |
| `mapa_panama.svg` | Wikimedia `File:BlankMap-World.svg` | Canuckguy et al. | **Dominio público (PD)** | Silueta de Panamá aislada para la escena "pérdida de Panamá 1903". Verificado en `SVGMobject` (5 members, 236 pts). |

Atribución (PD, no obligatoria): *"Colombia-map-sr.svg de Obradovic Goran"* y *"BlankMap-World.svg, Canuckguy et al."*, ambos Wikimedia Commons, Dominio público. Descartados por CC BY-SA los location-maps de Milenioscuro/Alexrk/NordNordWest.
