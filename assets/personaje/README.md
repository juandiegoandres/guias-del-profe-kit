# Dr. Cuack — mascota del kit

Personaje original del kit **Guías del Profe**: un pato amarillo científico-matemático
con gafas redondas, pensado para ilustrar guías, presentaciones y material web.
Es un diseño propio (inspirado en la vibra de las mascotas tipo pato, sin copiar
ningún personaje con derechos), dibujado a mano en SVG con degradados, sombreado
y proporciones editoriales — no figuras geométricas planas.

![Dr. Cuack](png/dr-cuack-base.png)

## Archivos

| Ruta | Qué es |
|---|---|
| `svg/dr-cuack-*.svg` | Personaje por variante. **Autocontenido y animado** (CSS embebido). |
| `png/dr-cuack-*.png` | Export estático 1024×1024, fondo transparente (para LaTeX/impresión). |
| `stickers/svg/` y `stickers/png/` | Stickers tipo meme con borde troquelado y texto (WhatsApp/Telegram/guías). |
| `demo.html` | Galería con las 8 variantes + stickers y botones *hablar / saludar / fondo oscuro*. Abrir en el navegador. |
| `build.py` | Generador: compone base + capas de profesión y regenera `svg/` y `demo.html`. |
| `export_png.py` | Regenera los PNG con Chromium headless (`python3 export_png.py 1024`). |

## Variantes y paleta

Los acentos salen del design system del kit (`design/preamble.tex`):

| Variante | Atrezzo | Acento |
|---|---|---|
| `base` | gafas redondas | — |
| `cientifico` | bata, gafas de seguridad, matraz burbujeante | esmeralda `#106E50` |
| `matematico` | chaleco, pajarita, tiza, pizarra con `a²+b²=c²`, símbolos flotantes | azul `#1E4078` |
| `profesor` | birrete con borla, corbata, libro abierto | azul + terracota |
| `ingeniero` | casco, chaleco reflectivo, plano enrollado | ámbar |
| `medico` | bata, estetoscopio, carné con cruz | — |
| `programador` | hoodie con capucha, audífonos, laptop `</>` | índigo `#463782` |
| `ganster` | fedora con banda terracota, traje de rayas, gafas oscuras, palillo | gris `#2B3440` |

## Stickers

9 stickers tipo meme en `stickers/` (`build.py` los genera): *ESTO ESTÁ BIEN*
(con llamas), *CONFÍA EN MÍ, SOY INGENIERO*, *FUNCIONA EN MI MÁQUINA*,
*AQUÍ MANDO YO*, *¿QUÉ MIRAS, BOBO?*, *PRESIONA F*, *MATEMÁGICAS*,
*RECETA: REPASAR* y *¡EUREKA!*. Llevan borde troquelado blanco (filtro
`feMorphology`), sombra suave y texto auto-ajustado. Para añadir uno:
entrada nueva en el dict `ST` de `build.py` (variante + líneas de texto +
extras como llamas/chispas/gota de sudor) y regenerar.

## Animación

Cada SVG trae una animación *idle* automática: respiración (bob), inclinación
sutil de cabeza, parpadeo, mechones al viento y micro-animaciones por variante
(burbujas del matraz, borla del birrete, símbolos flotantes). Respeta
`prefers-reduced-motion`.

Clases opcionales sobre el elemento raíz `<svg>` (requieren SVG inline u
`<object>`, no `<img>`):

- `talk` — abre y cierra el pico (para “hablar”).
- `wave` — saluda con el ala levantada (variantes con `#arm-up`).

Estructura de capas con IDs estables para animar desde fuera (GSAP, CSS, JS):

```
#duck            grupo raíz (bob)
├─ #feet         patas
├─ #wing-left / #wing-right
├─ #body
├─ (ropa por variante: #coat #vest #hoodie …)
├─ #head         (pivote en 256,288)
│  ├─ #hair      mechones
│  ├─ #eye-left / #eye-right  (párpados .lid para parpadeo)
│  ├─ #beak      → #bill-lower (pico inferior, pivote 256,248)
│  └─ #glasses
├─ #arm-up       ala levantada con prop (pivote 330,320)
└─ props: #flask #pizarra #libro #plano #laptop …
```

## Uso

- **Web/HTML:** `<img src="svg/dr-cuack-base.svg">` (anima solo) o inline para
  controlar clases.
- **LaTeX:** usar el PNG — `\includegraphics[width=3cm]{assets/personaje/png/dr-cuack-matematico.png}`.
- **Nueva profesión:** en `build.py`, añadir una entrada al dict `V` con las
  capas (`clothing`, `head_gear`, `props`, `front`, `behind`, `css_extra`) y
  correr `python3 build.py`.

## Gotcha de render (verificación en imagen)

Chromium headless **recorta ~70 px inferiores** cuando `--window-size` coincide
exacto con el contenido. `export_png.py` ya lo evita capturando con margen y
recortando; si haces capturas a mano, deja margen vertical extra.
