# 🖼️ Galería de diseños

Como una **galería de plantillas** (estilo Overleaf), pero ligera: cada profe
sube **un `.tex` corto y autocontenido** con un diseño hecho con IA para alguna
categoría. Con el tiempo construimos una **biblioteca comunitaria** de estilos.

> Diferencia con `templates/`: ahí están los **puntos de partida oficiales** (uno
> por tipo). Aquí van **variaciones y estilos de la comunidad** (muchos por
> categoría). El agente puede ofrecerte: *«¿el estilo base o uno de la galería?»*.

## Categorías

`ficha/` · `guia/` · `libro/` · `worksheet/` · `quiz/` · `examen/` · `beamer/` ·
`infografia/` · `portada/`

## Cómo aportar un diseño

Crea una carpeta `gallery/<categoría>/<autor>-<nombre>/` con **tres archivos**:

```
gallery/quiz/jdandres-icfes/
  example.tex     ← .tex corto y autocontenido que COMPILA
  preview.png     ← miniatura (1 página renderizada)
  meta.md         ← ficha: título, autor, categoría, descripción, licencia
```

- `example.tex` debe **compilar solo** (con su propio preámbulo o usando el
  design system del kit). Cuanto más corto y claro, mejor.
- `preview.png`: renderiza la primera página (`pdftoppm -png -r 150 -singlefile`).
- `meta.md`: usa la plantilla de [`_template/meta.md`](_template/meta.md).

Luego: `git add gallery/ && git commit && git push` (o un Pull Request).

## Índice

| Categoría | Diseño | Autor | Preview |
|---|---|---|---|
| quiz | [ICFES · Civilizaciones](quiz/jdandres-icfes/) | @juandiegoandres | <img src="quiz/jdandres-icfes/preview.png" width="160"/> |

*(Agrega tu fila aquí cuando subas un diseño.)*
