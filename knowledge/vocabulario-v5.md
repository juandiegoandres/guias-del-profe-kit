# Vocabulario semántico (design system v5)

Las secciones son **semántica pura**: escribes el *qué*, no el *cómo*. Sin
`\vspace`, color inline ni `minipage` de maquetación. Cambiar el diseño = editar
solo `design/preamble.tex`. (Confirma la firma exacta de cada macro en el
preamble antes de usarla — este archivo es la referencia conceptual.)

## Configuración

- `\setsubject{mat|cnat|csoc|eco}` — color e ícono de asignatura
  (azul / verde / terracota / índigo).
- `\printmodetrue` (tinta mínima, impresora) / `\printmodefalse` (color, pantalla).
- Metadatos antes de `\begin{document}`:
  `\renewcommand{\docgrado}{9°}`, `\docasignatura`, `\doctipo`, `\doctitulo`,
  `\docsubtitulo`, `\docperiodo`.

## Entornos de contenido

| Entorno | Uso |
|---|---|
| `\begin{definicion}{Título}` | Concepto/regla clave (filete lateral). |
| `\begin{ejemplo}{Título}` | Resuelto; glosa al margen con `\opg{cuenta}{porqué}`. |
| `\begin{procedimiento}{Título}` | Pasos: `\paso{n}{...}` + `\porque{...}` (lenguaje cercano). |
| `\begin{nota}[Título]` | Aparte gris (dato, sabías, video). |
| `\begin{alerta}{Título}` | Advertencia ámbar; sub-ítems con `\caso{}{}`. |
| `\begin{destacado}{Título}` | Idea esencial (triángulo + degradado). |
| `\begin{practica}{Título}` | Ejercicios: niveles `\basico` / `\intermedio` / `\reto`, ítems `\ejer{}`. |
| `\begin{hoja}{Título}` | Worksheet recortable (borde punteado, página aparte, Nombre/Fecha). |
| `\begin{evaluacion}[subt]` | ICFES 2 columnas; `\icfes{}{}{}{}{}`, `\pregabierta{}`. |
| `\begin{tablahoja}{cols}` | Tabla con rejilla completa para llenar a mano (nicematrix). |

## Aperturas y macros sueltas

- `\aperturacapitulo{n}{título}{subtítulo}` — portada de capítulo.
- `\aperturaseccion{archivo-img}{título}{intro}` — portada de sección (imagen +
  regla + «qué verás»; hace `\clearpage` e incluye el `\section`).
- `\figura{archivo}{pie}` — imagen, con placeholder automático si falta el arte.
- `\resaltar{texto}` — realce inline. **CORTO** (es caja indivisible; frases
  largas desbordan).
- `\linea[ancho]`, `\lineaescritura`, `\desbloquea{}`.

## Beamer (`design/beamer.tex`)

`\portada{kicker}{TÍTULO}{subtítulo}` · `\seccion{frase}` (divisor) ·
`\idea{TEXTO}` · `\pregunta{}` · `\accion{}` · `\resalta{}` / `\marca{}` ·
timelines `lineah`/`lineav` · `mapa` (nodo central + `\rama`).

> Para láminas a sangre propias, **no uses `current page` + remember picture**
> (ver `preflight-checklist.md` §5): usa `background canvas` con coords absolutas.
