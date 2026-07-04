# Prompts — avatar personal estilo memoji con camiseta de Millonarios

Avatar tipo memoji **que se parece al autor**, con la camiseta de Millonarios
(con escudo — avatar personal, uso privado), en varias poses para calcar con
`calcado/calcar.py` y animar en SVG. Si el modelo dibuja el escudo deforme,
regenerar o cambiar a «a single white star above the heart» sin escudo.

> **El parecido sale de tu foto, no del prompt.** En Whisk pon una **selfie
> tuya** (frontal, bien iluminada, fondo simple) como **Subject**. El prompt
> solo fija estilo + ropa + pose. Sin foto, el modelo inventa una cara.

## 1) Pose BASE (genérala primero — será el ancla de las demás)

Subject: **tu selfie**. Prompt:

```
Turn this person into a cute memoji-style cartoon avatar, full body, chibi
proportions (big head, small body), front view, standing, arms relaxed at the
sides, friendly smile. Keep the person's recognizable features: same hairstyle,
same facial hair, same skin tone, same glasses if present.

Wearing the official Millonarios FC home jersey: royal blue with white trim on
the collar and sleeves, the official Millonarios FC crest on the chest and a
white number 10, dark blue shorts.

STYLE: flat vector cartoon, bold clean dark-navy outline, smooth cel-shading,
NO 3D render, NO photographic gradients. Single centered character, solid pure
white background, no text, no floor shadow, 1:1 square, 1024x1024, crisp edges.
```

Genera varias, elige la que mejor te capture, y **esa imagen pasa a ser tu
Subject** para todas las poses (así la cara no cambia entre imágenes).

## 2) Ancla de estilo (antepónla si vas por texto puro)

```
Same memoji-style cartoon avatar of the same person: same face, same hair,
same skin tone, same royal blue football jersey with white star and number 10.
Flat vector cartoon, bold dark-navy outline, cel-shading, chibi proportions.
Single centered character, full body, solid pure white background, no text,
no floor shadow, 1:1, 1024x1024.
```

## 3) Poses (cambia solo esta línea)

Pensadas para animarlas después (saludo, celebración, hablar, señalar):

| Archivo sugerido | `+ POSE` |
|---|---|
| `avatar-base` | `standing, arms relaxed at the sides, friendly smile` |
| `avatar-saludo` | `one arm raised waving hello, open smile` |
| `avatar-pulgar` | `giving a thumbs up with one hand, confident smile` |
| `avatar-brazos` | `arms crossed, proud confident smirk` |
| `avatar-gol` | `celebrating a goal, both arms raised in victory, mouth open cheering` |
| `avatar-pensando` | `one hand on chin, thoughtful expression, eyes looking up` |
| `avatar-senalando` | `pointing to the side with one hand, explaining, friendly teacher gesture` |
| `avatar-balon` | `one foot resting on a classic black-and-white football, hands on hips` |

**Consistencia:** misma imagen base como Subject en todas; en el texto cambia
**solo** la línea de pose. Si una pose le cambia la cara, regenera — no la
aceptes.

## 4) Calcar y animar

```bash
cd assets/personaje/calcado
python3 calcar.py ~/Descargas/avatar-base.png avatar-base
python3 calcar.py ~/Descargas/avatar-saludo.png avatar-saludo
# ... una por pose → svg/ animado (respiración) + png/ 1024 transparente
```

Con las poses calcadas se pueden animar en SVG/CSS: *idle* (respiración +
parpadeo) sobre la base, saludo en bucle, celebración de gol, y alternar poses
por clase CSS o JS en la web.

**Checklist de la imagen fuente** (si no, el calco sale sucio): fondo blanco
puro · colores planos sin degradado 3D · contorno definido · un solo personaje
completo (que no se corte) · sin texto · sin sombra en el piso.
