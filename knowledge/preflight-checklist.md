# Pre-flight checklist — gotchas de LaTeX/Beamer para el agente

> **Para el agente (Claude Code / Antigravity / OpenCode):** lee este archivo
> **antes de generar LaTeX** y **antes/después de compilar**. No es teoría: cada
> punto es un error real que ya costó iteraciones. Tratarlo como un *linter*.
>
> **Cómo crece:** cada vez que aparezca un bug nuevo, añade una entrada al final
> de la sección que corresponda con el formato **Regla · Síntoma · Causa · Fix**.
> Mantenerlo corto y accionable.

---

## 0. Reglas de oro (siempre)

- **Compila con `./compile_quiet.sh`, nunca `lualatex` directo.** El script hace
  2 pasadas internas y limpia los auxiliares.
- **Máximo 2 intentos de compilación.** Si falla el 2.º, reporta los errores y
  para — no compiles en bucle.
- **Verifica SIEMPRE en imagen.** «Compiló sin error» ≠ «se ve bien». Renderiza a
  PNG (`pdftoppm -png -r 110 archivo.pdf /tmp/x`) y revisa: texto fugado, cajas
  vacías, desbordes, glifos faltantes, solapamientos.
- **Edita, no reescribas.** Para corregir algo puntual, `Edit` sobre la parte;
  no regeneres el archivo entero.

---

## 1. Fuentes y glifos

- **`→` y símbolos Unicode NO existen en Charter (serif).** Salen como cuadrito
  (tofu). · Síntoma: «Idea ▯ Diseñar». · Fix: usar math: `\(\rightarrow\)`. En
  Inter (sans) sí renderiza, pero math es universal — úsalo por defecto.
- **Glifos `✗` (U+2717) y `▢` (U+25A2) ausentes** en TeX Gyre Heros/Pagella. ·
  Fix: dibujar la marca/caja con TikZ, o usar `X` y una caja dibujada
  (`\framebox`/tikz rectangle).
- **Inter Display Black tiene word-space nativo muy estrecho.** · Síntoma: los
  titulares grandes se pegan («Prototipacon IA»). · Fix: inyectar
  `\spaceskip=0.30em\relax` en el nodo del título (`\newcommand{\aire}{...}`).
  `WordSpace=` de fontspec **no** alcanzó.

## 2. Math y caracteres especiales en texto

- **`___` (guiones bajos literales) en texto entran en modo math** y desordenan
  todo (texto en itálica apretada). · Fix: escribir `\_` o reformular sin
  guiones.
- **`\;` (espacio matemático) fuera de math** es frágil. · Fix: usar `\quad`,
  `\,` o `~`.

## 3. Tablas

- **`\rowcolor` exige `\usepackage[table]{xcolor}`** (carga colortbl). · Síntoma:
  imprime literal `black!10` antes del texto de la celda. · Fix: añadir la
  opción `[table]`.
- **Filas anchas (iconos/flujo) se cortan por la derecha.** · Fix: envolver la
  `tabular` en `\resizebox{\linewidth}{!}{ ... }`.
- **Tablas para rellenar a mano** → rejilla completa (nicematrix `hvlines` /
  entorno `tablahoja`). **Tablas didácticas (cuerpo)** → `booktabs`, sin rejilla.
- **B/N (fotocopia):** encabezado con `\rowcolor{black!12}` y texto **negro**
  (mejor que blanco sobre fondo oscuro al fotocopiar).

## 4. Listas y entornos

- **`\item[\macro[arg]]` rompe la lista.** El `]` del argumento opcional interno
  cierra el `\item[` antes de tiempo; el texto del ítem se fuga (a veces a otra
  página). · Fix: blindar con llaves: `\item[{\macro[arg]}]`.
- **Realce inline (`\resalta`, nodo TikZ) es indivisible.** · Síntoma: frase
  larga se sale del margen y se corta. · Fix: resaltar **solo lo clave** (corto);
  el resto, texto normal que sí parte línea.

## 5. TikZ y diagramas

- **`current page` + `[remember picture, overlay]` NO es fiable con
  `compile_quiet.sh`.** · Síntoma: el contenido de las láminas a sangre
  (portada, divisores, demo) sale **corrido hacia arriba**, con el título fuera
  de la diapositiva («la slide 1 se ve rara»). Afecta a todos los decks del
  proyecto. · Fix robusto: dibujar la lámina como **fondo** con coordenadas
  absolutas, sin remember picture:
  ```latex
  \setbeamertemplate{background canvas}{%
    \begin{tikzpicture}
      \useasboundingbox (0,0) rectangle (\paperwidth,\paperheight);
      \fill[paper] (0,0) rectangle (\paperwidth,\paperheight);
      \node[...] at ($(0,\paperheight)+(1.2,-1.9)$) {...};  % calc desde la esquina
    \end{tikzpicture}}
  \begin{frame}[plain]\strut\end{frame}
  ```
- **No anides `tikzpicture` dentro de un `\node{}` de otra `tikzpicture`.** Los
  iconos definidos como `\begin{tikzpicture}...\end{tikzpicture}` revientan si se
  meten en un nodo. · Fix: colocarlos **sueltos en una `tabular`** (columnas de
  iconos + flechas), o definirlos como `\pic`.
- **`\draw (0,0) grid (2,2)` no da el 2×2 que esperas** (salió 3×3 visual). ·
  Fix: dibujar las líneas explícitas con `\foreach` (3 horizontales + 3
  verticales para 2×2).
- **Flechas:** cargar `\usetikzlibrary{arrows.meta}` para `-{Stealth}`.
- **Conectores limpios:** usar ruteo ortogonal `|-` (vertical-luego-horizontal),
  no diagonales que se cruzan. Etiquetas (Sí/No) en chip con `fill=paper`.

## 6. Beamer

- **Cuerpo serif (estética Medium):** `\usefonttheme{serif}` + `\setmainfont`.
- **Agrupa los `\setbeamertemplate` locales en `{ ... }`** alrededor del frame
  para que el scope (footline oculto, background) se restaure después.
- **Una sola URL por `\href`.** Dos URLs en un `\href` lo rompe. En fondo oscuro,
  color claro (`accent!75!white`) + `\underline` para que se lea como enlace.
- **`\hypersetup{colorlinks=true, urlcolor=...}`** para enlaces clickeables.

## 7. Contenido (no solo que compile — que esté BIEN)

- **`\MakeUppercase` destruye notación sensible a mayúsculas.** · Síntoma:
  alelos `Aa`→`AA` (¡borra dominante/recesivo!), configuración `2p`→`2P`. · Fix:
  no uses uppercase en contenido con semántica de caso; estiliza por fuente, no
  por mayúsculas.
- **Revisa la exactitud científica/matemática**, no solo la compilación
  (genética, química, factorización: verifica resultados y notación).
- **Datos que cambian rápido** (precios de modelos IA, nombres de herramientas):
  verifícalos al día. Precios de **Anthropic** → usar el skill `claude-api`
  (fuente oficial), nunca de memoria. Marca en el documento «verifica antes de
  publicar».

---

## Plantilla para añadir un gotcha nuevo

```
- **<Regla en imperativo>.** · Síntoma: <qué se ve mal>. · Causa: <por qué>. ·
  Fix: <solución concreta, con snippet si aplica>.
```
