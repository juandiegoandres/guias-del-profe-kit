# Estándar de personajes (rig canónico)

Reglas para que **todas** las mascotas (Dr. Cuack, Capi, futuras) sean coherentes,
se calquen limpias y sirvan tanto para impreso como para **video animado**.

## 1. Lienzo canónico: 1024×1024

- El SVG es **vectorial** (escala infinito): el número del lienzo no afecta la
  calidad final, solo el sistema de coordenadas. Lo fijamos en **1024**.
- Las fuentes de **Flow** salen a otro tamaño (p. ej. **1766×1766**). No importa:
  `calcar.py` **normaliza** cualquier tamaño a 1024 escalando el contenido
  (arreglado — antes recortaba). Todas las mascotas quedan en el **mismo sistema
  de coordenadas** → las piezas y el rig alinean.

## 2. Fondo blanco puro — OBLIGATORIO

`calcar.py` borra el fondo con flood fill **desde el blanco**. Si la imagen de Flow
tiene fondo de color, el calco sale **con ese fondo** (no transparente). Siempre:
`solid pure white background #FFFFFF`, sin sombra en el piso, sin degradado.

## 3. Pose canónica (para que todo sea una familia)

Genera SIEMPRE la base y las profesiones así, para que encuadren igual:

- **Frontal, cuerpo completo, centrado**, mirando al frente.
- **Brazos en reposo a los lados**, boca cerrada, ojos abiertos (pose neutra).
- Pies visibles, **~10 % de margen** alrededor (que no se corte).
- Cuadrado 1:1, colores planos, contorno grueso definido.

Las profesiones/roles = **misma pose + traje** (generadas enteras en Flow). Es el
método correcto para trajes (caen naturales); no los pegamos por capas.

## 4. Para VIDEO: el títere (partes separadas)

Un personaje que **habla y gesticula** necesita **boca, ojos y brazos como capas
separadas** (lip-sync, parpadeo, saludo). El calco plano no lo da solo. Dos vías:

- **Isolar partes en el base** (`#mouth`, `#eye-l/#eye-r`, `#arm`) para animarlas
  en Manim/CSS. Es lo que da lip-sync y parpadeo suaves.
- **Frames de expresión** desde una **model sheet** (ver §5): la cara con distintas
  bocas/ojos, que se intercambian como fotogramas.

IDs estables del rig (heredados de Dr. Cuack): `#duck`(raíz, bob) › `#head`
(pivote 256,288) › `#eye-l #eye-r` (párpados `.lid`) › `#mouth`/`#bill-lower`
(pivote inferior) › `#arm-up` (pivote hombro). Reúsalos en cada personaje.

## 5. Model sheet (una imagen, varias expresiones) — para expresiones y frames

Generá en Flow **UNA imagen** con la mascota repetida en rejilla, misma escala,
fondo blanco, para cortarla en frames. Sirve para emojis, stickers y frames de
video. **Prompt** (ejemplo Capi — cambia el personaje):

```
A character expression sheet of the same capybara mascot "Capi", arranged in a
clean 3x3 grid on a solid pure white background, evenly spaced, each pose the
SAME size and centered in its cell. Same capybara in every cell: warm brown fur,
cream belly and muzzle, big friendly dark eyes, rounded ears, chibi proportions.
Flat vector cartoon, bold dark-brown outline, cel-shading, NO 3D, NO photo.

Cells (left→right, top→bottom):
1 neutral, mouth closed   2 big happy smile        3 talking, mouth open
4 mouth wide open ("ah")  5 eyes closed (blink)    6 wink, one eye closed
7 thinking, paw on chin   8 one arm raised waving  9 thumbs up

No text, no labels, no borders, even spacing, 1:1 square, high detail.
```

Para **lip-sync fino**, en vez (o además) pedir una fila solo de **bocas**:
`mouth closed / slightly open / wide open / "O" shape / smile` — mismo tamaño.

## 6. Escenarios / escenas — NO como capas SVG

Los fondos van **aparte, de cuadro completo, en 16:9** (formato video), generados
en Flow: `a flat vector illustration of a [classroom / bank / lab / football
stadium], soft colors, no characters, 16:9, high detail`. En Manim/HTML se pone el
títere **encima** del fondo. Máxima reutilización, cero problema de alineación.

## 7. Reglas cortas que ya nos costaron

- **svgo solo con `svgo.config.mjs`** (el default rompe la animación).
- **vtracer `colorPrecision 6`** (4 revive el fondo magenta; 5 pesa más).
- **Verificá en imagen** siempre (`rsvg-convert` si no hay Chromium).
- Cross-personaje: **no** se comparte ropa de cuerpo (siluetas distintas); sí se
  comparten fondos, props sostenibles y efectos.

## 8. Iconos / props de escena: de dónde SÍ (y de dónde NO)

**NO usar Icons8 (iconos8.es).** Su fricción **no es técnica, es de licencia**: el
tier gratis exige **atribución** (link-back a icons8.com en *cada* uso) —
impráctico para video **monetizado**— y quitarla requiere plan **pago**. Scrapearlo
con Playwright rodearía su paywall/atribución = contra sus ToS + riesgo legal en
contenido monetizado. **No es el camino.**

**SÍ: fuentes abiertas, sin atribución, comercialmente seguras y AUTOMATIZABLES.**
La mejor es la **API de Iconify** (sin login, sin API key, verificada):

```
https://api.iconify.design/{set}/{nombre}.svg
https://api.iconify.design/lucide/trending-up.svg?color=%23106E50&width=120
```

- 200k+ iconos de sets **abiertos** (MIT/Apache/CC): `tabler`, `lucide`, `ph`
  (phosphor), `mdi`, `material-symbols`, `game-icons`, `twemoji`, `noto`, `fluent`.
- Se le pasa **color** (acento del design system) y **tamaño** por query param.
- Para ilustraciones grandes: **SVG Repo** (filtrar CC0/Public Domain),
  **Openclipart** (CC0), **unDraw** (ilustraciones libres).
- Verifica la licencia del **set** puntual (Iconify la muestra) y arrastra créditos
  si el set los pide. Descarga por `curl`/`requests`, no por Playwright.

## 9. Formato video "presentador" (decisiones)

- **Resolución del personaje: ALTA.** El grid 3×3 dejó celdas de solo ~589 px →
  al escalar el busto (~1.7×) se ve **pixelado/tosco/sin suavizar**. Para video
  (sobre todo busto), generar las expresiones **grandes**: **una por imagen a
  resolución completa** (1024–1766 px) o **máx 4 por hoja** (celdas ≥880 px). Para
  el presentador conviene una **hoja de BUSTO** (cabeza+hombros) generada grande,
  para que la cara salga con detalle. Calcar desde fuentes grandes = trazo nítido
  a cualquier tamaño.
- **Voz: HIGH natural, SIN pitch de caricatura.** Por defecto `PITCH = 1.0`
  (voz Piper high tal cual, p. ej. `es_AR-daniela-high`). El pitch-shift queda como
  opción, **apagado por defecto**.
- **El personaje es NARRADOR, no está siempre en pantalla.** Aparece en momentos
  (intro, puntos clave, cierre) y se **retira** para dejar el contenido/diagrama
  a cuadro completo. `LayoutPresentador` debe soportar **entrada/salida** de Capi;
  las escenas alternan "Capi narrando" con "solo contenido".
- **Tamaño del busto: ajustable** (perilla `CAPI_ALTURA`/posición) — revisar el
  balance personaje vs. contenido por escena.
