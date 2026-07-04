# Prompts para generar a Dr. Cuack en Nanobanana / Whisk

Guía para crear **al personaje en cualquier rol y con cualquier expresión**,
manteniéndolo **idéntico** entre imágenes, y que salga **listo para vectorizar**
con `calcado/calcar.py` (vtracer + svgo).

> **Regla de oro de la consistencia:** genera **una sola** imagen base perfecta,
> guárdala, y de ahí en adelante en Whisk **usa esa imagen como _Subject_** y en
> el prompt describe **solo lo que cambia** (ropa, expresión). Nunca vuelvas a
> describir al personaje desde cero: eso lo cambia.

---

## 0) Cómo lograr consistencia en Whisk

Whisk mezcla tres entradas: **Subject** (qué), **Style** (cómo se ve) y
**Scene** (dónde/qué hace). Para nuestra mascota:

| Slot de Whisk | Qué poner |
|---|---|
| **Subject** | La imagen **base** de Dr. Cuack (una vez la tengas). Es el ancla de identidad. |
| **Style** | La misma base, o un sticker ya bueno, para fijar el trazo plano. |
| **Scene / prompt** | **Solo el cambio**: “wearing a lab coat holding a flask”, “angry expression”… |

Si no usas los slots, pega el prompt completo (ancla + cambio) en texto. Los
slots dan más consistencia; el texto da más control.

---

## 1) Generar la imagen BASE (hazla primero, una sola vez)

Pega esto tal cual. Genera varias, elige la mejor cara, y **esa es tu ancla**.

```
A cute chubby baby duck cartoon mascot, front view, full body, standing,
friendly and smart. Round plump body covered in warm yellow feathers (#FFCF3F
with soft #F0AE2B shading). A small rounded orange bill (#EE8E1E). Big round
friendly dark eyes. A tiny tuft of three little feathers on top of the head.
Wearing round thick-framed black nerd glasses. Neutral happy expression.

STYLE: flat vector cartoon, bold clean dark-navy outline (#23303E), smooth
cel-shading, cute chibi proportions, professional mascot sticker illustration.
Single centered character, solid pure white background (#FFFFFF), no text,
no shadow on the floor, 1:1 square, 1024x1024, crisp edges.
```

Guárdala como `calcado/fuente/dr-cuack-base.png`.

---

## 2) Ancla fija (el “estilo” — repítelo o úsalo como Style en Whisk)

Todo lo demás = **base como Subject** + uno de los cambios de abajo. Si vas por
texto puro, antepón siempre este bloque para no perder el look:

```
Same cute yellow baby duck mascot "Dr. Cuack": same round body, same face,
same big dark eyes, same orange bill, same head tuft, same round black nerd
glasses, same proportions and colors. Flat vector cartoon, bold dark-navy
outline, cel-shading. Single centered character, solid pure white background,
no text, full body, 1:1, 1024x1024.
```

---

## 3) Roles (cuerpo completo) — cambia solo la ropa/atrezzo

Fórmula: **base (Subject)** + `+ ROL`. El acento sale del design system del kit.

| Rol | `+ ROL` (pega esto como escena/cambio) | Acento |
|---|---|---|
| **científico** | `wearing an open white lab coat, safety goggles pushed up on the forehead, holding a small conical flask with bubbling green liquid` | esmeralda `#106E50` |
| **matemático** | `wearing a dark-blue vest and a red bow tie, holding a piece of chalk, a small green chalkboard with "a²+b²=c²" beside it` | azul `#1E4078` |
| **profesor** | `wearing a graduation cap with tassel and a tie, holding an open book` | azul + terracota |
| **ingeniero** | `wearing a construction hard hat and a reflective vest, holding a rolled blueprint` | ámbar `#B45F0A` |
| **médico** | `wearing a white medical coat with a stethoscope around the neck and an ID badge with a red cross` | — |
| **programador** | `wearing a purple hoodie with the hood down and headphones, holding a laptop showing "</>"` | índigo `#463782` |
| **gánster** | `wearing a pinstripe suit, a fedora hat with a band, and dark sunglasses` | gris `#2B3440` |
| **agente-IA** *(nuevo)* | `wearing a sleek dark hoodie, a small floating holographic robot/AI orb beside its head, subtle circuit patterns` | índigo `#463782` |
| **hacker-ético** *(nuevo)* | `wearing a hoodie, sitting at a laptop with green code on screen, focused` | esmeralda |

> **Consistencia de gafas:** siempre gafas **de nerd de marco grueso**, salvo el
> **gánster**, que lleva **gafas oscuras**.

Para un rol nuevo cualquiera: `+ wearing [ropa], holding [objeto]` — nada más.

---

## 4) Estados / expresiones (para emojis y stickers)

Para **emojis** pide **primer plano de la cabeza**; para stickers, cuerpo entero.
Cambia solo la cara. Antepón: `close-up of the duck's head, ` (emoji) y añade una
de estas:

| Estado | Expresión (pega el cambio) |
|---|---|
| feliz | `big warm smile, cheerful eyes` |
| risa | `laughing hard, eyes closed, open beak, tiny tears of joy` |
| amor | `heart-shaped eyes, blushing cheeks, sweet smile` |
| cool | `confident smirk, wearing dark sunglasses` |
| nerd | `proud grin, big nerd glasses, one tooth showing` |
| triste | `sad droopy eyes, small frown, downturned brows` |
| llorando | `crying with big teary eyes, mouth open, blue tear drops` |
| enojado | `angry frown, furrowed brows, red cheeks, steam` |
| sorprendido | `shocked wide eyes, open beak, raised brows` |
| guiño | `winking one eye, playful smile, tongue out slightly` |
| dormido | `eyes closed, peaceful, a small "Z Z Z" and a sleep bubble` |
| fiesta | `party hat, confetti around, big excited smile` |
| pensando | `thoughtful look, one wing on chin, a small thought bubble` |
| saludo | `waving one wing, friendly open smile` |
| explotado | `mind-blown, top of the head exploding with a comic burst and sparks` |

---

## 5) Requisitos técnicos (para que `calcar.py` lo trace limpio)

El vectorizador necesita imágenes **planas**. Exige siempre:

- ✅ **Fondo blanco puro sólido** (`solid pure white background #FFFFFF`) — nada
  de fondos de color, degradados ni escenas; el flood-fill borra el blanco.
- ✅ **Colores planos** con sombreado *cel* suave; **evita** degradados
  fotográficos, texturas, granulado.
- ✅ **Contorno grueso y definido** (dark navy) — ayuda al trazo.
- ✅ **Un solo personaje, centrado, cuerpo completo, 1:1, 1024×1024+**.
- ✅ **Sin texto** dentro de la imagen (el texto se pone después en LaTeX/SVG).
- ✅ **Sin sombra en el piso** (complica el recorte de fondo).

**Negative / evita:** `photographic, 3D render, realistic, gradient background,
busy scene, multiple characters, text, watermark, drop shadow on floor, cropped,
cut off`.

---

## 6) Flujo completo (de Whisk al SVG del kit)

```bash
# 1. Genera en Whisk con los prompts de arriba y descarga el PNG.
# 2. Vectoriza (vtracer + svgo, fondo transparente + animación):
cd assets/personaje/calcado
python3 calcar.py ~/Descargas/mi-pato.png dr-cuack-base
#    → svg/dr-cuack-base.svg  +  png/dr-cuack-base.png

# 3. (Opcional) Genera todas las variantes/stickers/emojis componiendo:
python3 componer.py --png
```

> Si un rol te queda muy distinto al calcar, es que el PNG no era plano: regénéralo
> con fondo blanco sólido y colores planos, y repite.
