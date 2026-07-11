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
- **El `<nombre_salida>` de `compile_quiet.sh` es el `jobname` y la carpeta de
  build es `/tmp` (compartida).** · Síntoma: compilas `guia_profe` y el PDF final
  sale con el contenido de OTRO documento (p. ej. la `guia_profe` de otro tema:
  la portada dice «Química» pero el PDF muestra «Factorización»/«Genética»); el nº
  de páginas «cuadra» y no hay error. · Causa: dos documentos con el **mismo**
  `<nombre_salida>` (`guia_profe`, `beamer`, `taller`…) colisionan en
  `/tmp/<nombre>.pdf`/`.log`; si hay otra compilación en curso, `mv` puede mover el
  PDF del otro. · Fix: usa un `<nombre_salida>` **único por documento** (p. ej.
  `qtp_gprofe`, `qtp_beamer`) y luego `mv`-lo al nombre canónico. **Verifica
  SIEMPRE el contenido real** (`pdftotext -f 1 -l 1 x.pdf - | head`), no solo el
  nº de páginas.
- **La colisión de `<nombre_salida>` va MÁS ALLÁ del `mv`: puede abrir el `.tex`
  equivocado y/o dejar un PDF corrupto.** · Síntoma: (a) el log arranca abriendo
  `.../OTRO-tema/guia_profe.tex` aunque pasaste la ruta correcta —el PDF sale con
  errores «\genotipo/\sffamily invalid in math mode» de un tema ajeno y truncado a
  2 págs; (b) `pdfinfo`/`pdftoppm` fallan con «Bad 'Length' attribute in stream» y
  el render no sale. · Causa: `TEXINPUTS` incluye la raíz con `//` (recursivo), así
  que ante `guia_profe.tex`/`taller.tex`/`beamer.tex` repetidos en varias carpetas,
  auxiliares **obsoletos** en `/tmp/<jobname>.*` (de una compilación previa de OTRA
  carpeta con el mismo jobname) confunden la resolución; y correr `lualatex`/
  `pdftoppm` manuales sobre el **mismo** jobname a la vez corrompe el PDF. · Fix:
  **`rm -f /tmp/<jobname>.*` ANTES de compilar**, no corras builds/renders manuales
  concurrentes con el mismo jobname, y **verifica en el log la primera ruta abierta**
  (`sed -n '3,4p' /tmp/latex_<jobname>.log`): debe ser tu archivo, no el de otro tema.
- **Señal temprana de PDF stale: `compile_quiet.sh` imprime `PDF OK |  |` con el
  campo de páginas VACÍO (entre los dos `|` no hay «Output written on…»).** ·
  Síntoma: la línea de éxito sale sin nº de páginas y el PDF movido es de otro tema
  o de una versión anterior. · Causa: la 2.ª pasada de lualatex falló (no escribió
  «Output written»), pero el `/tmp/<jobname>.pdf` de una pasada/compilación previa
  seguía ahí y el script lo `mv`-e igual. · Fix: si ves `PDF OK |  |`, trata el
  build como FALLIDO: `rm -f /tmp/<jobname>.*` y recompila; confirma con
  `pdfinfo <out>.pdf | grep Pages` que el nº de páginas es el esperado. Al generar
  N documentos que comparten `<nombre_salida>` (varios `taller`/`guia_profe`),
  **limpia `/tmp/<jobname>.pdf` entre cada uno**.

---

## 0.b Metadatos / config del documento

- **`\printmodetrue`/`\printmodefalse` NO existe en `design/preamble.tex`.** ·
  Síntoma: aunque el vocabulario lo menciona, ponerlo aborta la compilación
  («Undefined control sequence»). · Causa: quedó documentado pero no implementado.
  · Fix: no lo uses. El sistema imprime en color por defecto; si algún día se
  necesita modo tinta-mínima, hay que definir el `\newif` en el preamble primero.
- **Ocultar la institución (material genérico):** el preamble fija
  `\hdrinstituto` y el sello «ITSTZ · Zapatoca» está *hardcodeado* en `secstage`
  (lo usa `\aperturaseccion`) y en el footline de `design/beamer.tex`. · Fix: en
  guías, `\renewcommand{\hdrinstituto}{}` y evita `\aperturaseccion`/
  `\aperturacapitulo`; en Beamer, redefine `\setbeamertemplate{footline}` sin la
  sigla (hecho en `design/tema-eco-beamer.tex`).

- **Los metadatos `\renewcommand{\docgrado}{...}` / `\docasignatura` / `\doctipo` /
  `\doctitulo` / `\docsubtitulo` / `\docperiodo` NO existen en `design/preamble.tex`.**
  · Síntoma: las plantillas `templates/guia_profe.tex` (y el vocabulario) los usan, pero
  compilar con ellos aborta con «Undefined control sequence \docgrado». · Causa: quedaron
  documentados pero nunca se implementó el bloque de metadatos ni un `\maketitle`. · Fix:
  no los uses. Identifica el documento con `\renewcommand{\hdrcapitulo}{Asig · Grado · Tema}`
  y abre con un `\section{...}`; para ocultar la institución, `\renewcommand{\hdrinstituto}{}`.

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
- **`\faShieldAlt` compila pero NO tiene glifo** (fontawesome5 en lualatex): la
  compilación pasa sin error, pero en el PDF el ícono sale **vacío / hueco** (no
  hay «escudo»). · Causa: ese nombre no está mapeado a un glifo dibujable en la
  versión de fontawesome5 del sistema. · Fix: usar **`\faUserShield`** (escudo con
  figura, sí renderiza) para «seguridad». Verifícalo siempre en imagen: «compila»
  ≠ «tiene glifo». Regla general: ante un ícono fontawesome dudoso, renderiza a PNG
  y confirma que dibuja algo.

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
- **`tablahoja`/nicematrix NO dibuja la rejilla dentro de `hoja`** (ni de otra
  tcolorbox `breakable`). · Síntoma: la tabla sale como texto suelto, sin líneas,
  aunque compile sin error. · Causa: nicematrix no rastrea posiciones dentro de
  cajas partibles. · Fix: dentro de `hoja` usa `tabular` con `\hline` en todas las
  filas (`\renewcommand{\arraystretch}{2.4}` para celdas altas), o saca la tabla
  fuera de la caja breakable.
- **B/N (fotocopia):** encabezado con `\rowcolor{black!12}` y texto **negro**
  (mejor que blanco sobre fondo oscuro al fotocopiar).

## 4. Listas y entornos

- **`\item[\macro[arg]]` rompe la lista.** El `]` del argumento opcional interno
  cierra el `\item[` antes de tiempo; el texto del ítem se fuga (a veces a otra
  página). · Fix: blindar con llaves: `\item[{\macro[arg]}]`.
- **Membresía en lista CSV (resaltar elementos, etc.): dos trampas de etoolbox.**
  · Síntoma: el resaltado nunca coincide (todo queda igual). · Causa 1:
  `\forcsvlist{\h}{\milista}` **no expande** el macro-lista (lo trata como 1 ítem);
  hay que expandirlo: `\expandafter\forcsvlist\expandafter{\expandafter\h\expandafter}\expandafter{\milista}`.
  · Causa 2: `\ifstrequal{#1}{\cursym}` **no expande** sus argumentos (compara contra
  el texto literal `\cursym`, no su valor). · Fix: mete el ítem en un macro
  (`\def\item{#1}`) y compara dos macros con **`\ifdefstrequal{\item}{\cursym}{}{}`**
  (sí expande ambos). Patrón usado en `tikzlib/ciencias/tabla_periodica.tex`.
- **Realce inline (`\resalta`, nodo TikZ) es indivisible.** · Síntoma: frase
  larga se sale del margen y se corta. · Fix: resaltar **solo lo clave** (corto);
  el resto, texto normal que sí parte línea.
- **Los contadores reseteados por `[section]` (`ejemplo`, `figura`, `ejer`) NO se
  reinician con `\section` en `design/preamble.tex`.** · Síntoma: el 2.º ejemplo de
  una sección nueva sale como «Ejemplo 7», no «Ejemplo 1»; la numeración corre
  continua por todo el documento. · Causa: el preamble fija `\setcounter{secnumdepth}{0}`
  (secciones sin número) + `\titleformat`; el reset por sección no se dispara. · Fix:
  cuéntalo como numeración continua (para *ejemplos trabajados* seguidos queda bien y
  hasta más claro), o usa `\subsection` para los rótulos que NO deban numerarse (p. ej.
  las partes del solucionario: «Parte A — …» sin el prefijo «Ejemplo N»).
- **`\figura` se partía en un salto de página.** · Síntoma: la imagen queda al
  pie de una página y el pie de figura («Figura N. …») salta solo al inicio de la
  siguiente, con un hueco en blanco. · Causa: el `center` de `\figura` era
  divisible, así que un page break podía caer entre `\includegraphics` y el pie.
  · Fix (ya aplicado en `design/preamble.tex`): imagen + pie envueltos en un
  `minipage{\linewidth}` centrado = bloque indivisible (si no cabe, baja entero a
  la página siguiente). No requiere cambios en los documentos.

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
- **No derives nombres de nodo de una coordenada `#1` con decimales/signo.** ·
  Síntoma: `\node[...](u#1)...` y luego `[below of=u#1]` con `#1 = 4.6` aborta con
  «Package pgf Error: No shape named `u4' is known» (pgf trunca el nombre en el
  punto). · Causa: `.`/`-` no son válidos en nombres de nodo. · Fix: pásale a la
  macro un **nombre simbólico aparte** (`ramauno`, `ramados`…), no la coordenada.
  Patrón usado en `\ramamapa` de `tikzlib/ciencias/termodinamica.tex`.
- **No mezcles coordenada absoluta con `++` en un mismo `\draw ... -- ...`** para
  «rayos» radiales (sol, estrella). · Síntoma: los rayos, en vez de rodear el
  centro, salen disparados hacia el origen `(0,0)`. · Causa: `(\a:0.5) ++(cx,cy)`
  hace el primer punto relativo al centro, pero el segundo `(\a:0.72)` es
  **absoluto** cerca de `(0,0)`; el `--` los une atravesando el lienzo. · Fix: usa
  `calc` y suma explícita: `($(cx,cy)+(\a:0.5)$) -- ($(cx,cy)+(\a:0.72)$)`.
  Verificado en `\transfcalor` (sol de la radiación).
- **Figura TikZ reutilizable para guía + Beamer:** define colores didácticos
  (`calido`/`frio`) con `\definecolor` **a nivel de archivo** (no dentro del macro)
  y usa `subjectcolor` como acento. Se `\input` igual en `design/preamble.tex` y en
  `design/beamer.tex` (ambos traen `calc, arrows.meta, positioning`). Para meterla
  en una columna Beamer o a lo ancho de una guía, escala con
  `\resizebox{\linewidth}{!}{\figura}`. Patrón: `tikzlib/ciencias/termodinamica.tex`.

## 6. Beamer

- **Cuerpo serif (estética Medium):** `\usefonttheme{serif}` + `\setmainfont`.
- **Agrupa los `\setbeamertemplate` locales en `{ ... }`** alrededor del frame
  para que el scope (footline oculto, background) se restaure después.
- **Una sola URL por `\href`.** Dos URLs en un `\href` lo rompe. En fondo oscuro,
  color claro (`accent!75!white`) + `\underline` para que se lea como enlace.
- **`\hypersetup{colorlinks=true, urlcolor=...}`** para enlaces clickeables.
- **Las láminas a sangre del design system (`\portada`, `\seccion`, `\idea`,
  `\accion`) usan `remember picture`+`current page` → salen corridas hacia arriba
  con `compile_quiet.sh`** (mismo bug del §5). · Síntoma: en la portada el kicker
  y el título se van fuera por arriba; el sello/divisor queda descuadrado. Las
  láminas de *contenido* normales (con `\frametitle`) NO se afectan. · Fix: en el
  deck, `\renewcommand` esas macros con `\setbeamertemplate{background canvas}` +
  coordenadas absolutas `(0,0) rectangle (\paperwidth,\paperheight)` y
  `\begin{frame}[plain]\strut\end{frame}` dentro de un grupo `{ }`. Ancla el
  contenido **respecto al centro** (`\paperwidth*0.5,\paperheight*0.5`): los
  layouts simétricos (divisor, idea) salen perfectos; para la portada (layout
  vertical asimétrico) mete kicker+título+filete+subtítulo en **un solo nodo
  multilínea** centrado, no en nodos sueltos con offsets (se descuadran).
- **El emoji 🔴/🟢/🟡 no existe en las fuentes de LaTeX/Beamer (sale tofu o
  rompe).** · Fix: dibuja el punto del semáforo con TikZ —
  `\tikz[baseline=-0.4ex]\node[circle,fill=<color>,inner sep=0pt,minimum size=0.85em]{};`
  Aplica también en las guías ZapiaLab (regla del semáforo).
- **`\faLanguage` (fontawesome5) renderiza como tofu (cuadrito doble) en el
  cuerpo.** · Fix: usar `\faGlobeAmericas` para la caja «Tech English» (sí
  renderiza), o un icono ya probado en el preamble.
- **`design/beamer.tex` carga xcolor SIN `[table]` → beamer NO trae colortbl.**
  · Síntoma: `\rowcolor{eco!12}` (o `\columncolor`/`\cellcolor`) sale **impreso
  literal** pegado a la 1.ª celda («eco!12Variable») en vez de teñir la fila. ·
  Causa: sin colortbl, `\rowcolor` no está definido. · Fix: `\usepackage{colortbl}`
  en el tema/deck (ya hecho en `design/tema-eco-beamer.tex`). Las **guías** no
  sufren esto porque `design/preamble.tex` sí carga colortbl.
- **Beamer NO carga `enumitem` → `\begin{itemize}[clave=valor]` imprime las
  opciones como TEXTO.** · Síntoma: «eftmargin=1.3em, itemsep=3pt» aparece pegado
  al primer ítem (la `l` inicial se la come el `\large` previo). · Causa: el
  `itemize` nativo de beamer no acepta argumento opcional con claves. · Fix:
  `\usepackage{enumitem}` (+ `\setlist{...}` opcional) en el tema. Hecho en
  `design/tema-eco-beamer.tex`. En las guías ya funciona (preamble carga enumitem).
- **`design/beamer.tex` NO carga `lmodern` → el math CM solo existe en tamaños
  fijos.** · Síntoma: al usar math a tamaños Display (`\Large $\approx$`,
  `$M=C(1+i)^n$` en `\accion/idea`), decenas de avisos «Font shape `OML/cmm/...`
  in size <NN> not available». Compila, pero rompe el objetivo de 0 advertencias.
  · Causa: el design system dice «math en Latin Modern» pero el beamer nunca lo
  carga. · Fix: `\usepackage{lmodern}` (Latin Modern escalable a cualquier tamaño).
- **`\textbf` dentro de una fontfamily de peso específico (`\DisplaySB` = Inter
  Display SemiBold) → «TU/InterDisplaySemiBold/b/n undefined».** · Síntoma: 1 aviso
  por deck; los `\idea{... \textbf{...}}`/`\chipf{}` lo disparan. · Causa: fontspec
  autodetecta el bold de una **familia** («Inter Display») pero NO de un **nombre
  de peso** («Inter Display SemiBold»). · Fix: darle BoldFont explícito con
  `\renewfontfamily\DisplaySB{Inter Display SemiBold}[..., BoldFont={Inter Display
  SemiBold}]` (misma SemiBold: sin cambio visual, el énfasis ya es grande).
- **`\figinline` (wrapfigure) dentro de un `ejemplo`/párrafo CORTO desborda sobre
  la caja siguiente.** · Síntoma: la leyenda de 2–3 líneas del float queda pegada
  o encima del borde superior del `destacado`/`nota` que sigue (verificado en
  imagen, guía oferta-demanda). · Causa: si el texto que envuelve es más corto que
  la altura de imagen+leyenda, el contenido full-width posterior sube al lado del
  float. · Fix: usa `\figinline` solo donde haya ≥6 líneas de texto que envolver y
  **leyenda de 1 línea**; si el bloque es corto, mejor no floto (deja el TikZ/gráfica
  que ya lleva la página) o usa `\figura` centrada fuera del párrafo.
- **Los titulares grandes de las láminas a sangre (`\portada/\seccion/\idea/
  \pregunta`) parten palabras** («he-rencia», «nin-guno»). Feo en video. · Fix:
  meter `\nohyf` (`\hyphenpenalty=10000\exhyphenpenalty=10000`) al inicio del nodo
  del titular. En cuerpos de párrafo largos, además ponerlo dentro del grupo del
  texto o mantener el texto corto (ragged no siempre basta).
- **`\nohyf` (subir `\hyphenpenalty`) NO evita la hipernación dentro de nodos
  TikZ con `text width`.** · Síntoma: pese a `\nohyf`, `\idea`/`\portada`/`mapa`
  siguen partiendo palabras («inte-rés», «maña-na», «ECO-NOMÍA», «con-sigue»);
  verificado en imagen. · Causa: en el nodo TikZ, `\hyphenpenalty=10000` no surte
  efecto (font/align lo ignoran). · Fix probado: anular el guion del **font
  activo** con `\hyphenchar\font=-1` **después del `\selectfont`** del tamaño en
  uso. Como es por instancia de tamaño, va justo antes del texto en cada grupo:
  `{\DisplayBlk\fontsize{36}{40}\selectfont\hyphenchar\font=-1\relax #2}`. Para el
  `mapa` (nodos de la base), prepende el reset en cada argumento:
  `\rama{..}{..}{\hyphenchar\font=-1\relax Texto\\ \scriptsize sub}`. Patrón usado
  en `design/tema-eco-beamer.tex` (helper `\nh`).
- **`design/beamer.tex` NO carga `fontawesome5`.** Si un tema o deck usa `\faLeaf`
  etc., debe cargarlo (`\usepackage{fontawesome5}`). El tema `tema-cnat-beamer.tex`
  ya lo hace.
- **Exportar una figura TikZ a SVG (para Manim/`SVGMobject`): usa
  `pdftocairo -svg`, no `dvisvgm --pdf`.** · Síntoma: `dvisvgm --pdf x.pdf` falla
  con «can't retrieve number of pages». · Causa: en este Mac dvisvgm se compiló
  sin backend PDF (mutool ausente) y `pdf2svg` no está instalado. · Fix: compila
  el `standalone` a PDF con `compile_quiet.sh` y convierte con
  `pdftocairo -svg in.pdf out.svg` (poppler). Escribe el texto como **paths** (0
  `<text>`) → sin dependencia de fuentes, ideal para `SVGMobject`. Verifica el SVG
  con `rsvg-convert -w 950 out.svg -o /tmp/x.png`.
- **Números/símbolos en un SVG para `SVGMobject`: dibújalos como TRAZOS TikZ, no
  como `\node{texto}`.** · Síntoma: querías un «1» o una «Ȼ» y `pdftocairo -svg`
  los mete como `<text>` (fuente) → `SVGMobject` los ignora o depende de la fuente.
  · Fix: traza el glifo con `\draw` (p. ej. un «1» = banderilla+asta+base; un «0» =
  `ellipse`; una «Ȼ» = `arc` abierto + barra vertical). Así quedan `<path>` puros.
  Ejemplo real: `tikzlib/interes/capidolar.tex` (`\dgone`, `\dgzero`, `\dgcur`).
  Verifica: `grep -cE "<text|<image|Gradient|<filter" out.svg` debe dar `0`.
- **SVG no se embebe directo en lualatex.** · Fix: descargar el SVG libre
  (Tabler MIT, Openclipart CC0…), recolorearlo (`sed 's/currentColor/#106E50/g'`)
  y convertirlo a **PDF vectorial** con `rsvg-convert -f pdf` (librsvg, `brew
  install librsvg`). Embeber con `\includegraphics`. Anotar fuente+licencia.
- **Láminas de «frase grande» (`\idea`/`\pregunta`/`\seccion`): el `\baselineskip`
  de `\fontsize{S}{L}` debe ser ~1.5·S, no ~1.3·S.** · Síntoma: con fuentes Display
  (Black/SemiBold) de 22–30 pt, las líneas del titular —tanto las que parten por
  `text width` como las de `\\` manual— **se montan verticalmente y se tocan**. ·
  Causa: Display tiene ascendentes/descendentes altos; `L=1.3·S` deja el cuerpo casi
  pegado. · Fix: subir el leading (`\idea` 30/40 → 28/44; body de `\pregunta` 22/28
  → 22/34). Regla práctica: `L ≥ 1.5·S` para titulares Display. Verifica siempre en
  imagen que ninguna línea toque a la siguiente.
- **Layout «científico» (retrato + párrafo + `\resalta` de pista): con `\vspace{0.5em}`
  la caja `\resalta` se encima con el párrafo si el texto es largo (2+ párrafos).** ·
  Síntoma: la caja de realce toca la última línea del párrafo anterior. · Causa: la
  columna `[c]` reparte poco aire y `\resalta` es un nodo indivisible con inner ysep
  mínimo. · Fix: en la lámina de texto largo, sube el `\vspace` previo a `\resalta` a
  ~`1.05em` (las de texto corto quedan bien con 0.5em; ajusta solo la larga).
- **`tablahoja`/nicematrix tampoco dibuja rejilla dentro del entorno `ejemplo`**
  (no solo en `hoja`/breakable): la tabla sale sin líneas. · Fix: tabla didáctica
  → `tabular`+`booktabs` (`\toprule/\midrule/\bottomrule`); tabla para llenar a
  mano → `tabular` con `\hline` en todas las filas y `\arraystretch{2.4}`.

- **La tabla periódica completa (`tabla_periodica.tex`) en una lámina con
  `\frametitle` MÁS un pie de texto se sale por abajo.** · Síntoma: a
  `\resizebox{0.9\textwidth}{!}{\tablaperiodica[...]}` la rejilla (7 periodos + 2
  filas f) es tan alta que el pie explicativo (`\large`) queda **cortado por el
  borde inferior** de la diapositiva. Compila sin error. · Causa: la tabla ocupa
  casi todo el `\textheight`; frametitle + tabla + 2 líneas grandes no caben en
  16:9. · Fix: baja el ancho a **`\resizebox{0.72\textwidth}`** y usa
  **`\normalsize`** (no `\large`) con pie de 1–2 líneas cortas. Verifica en imagen
  que el pie completo se vea sobre el footline.
- **Renderizar/`pdfinfo` sobre PDFs con figuras PDF vectoriales embebidas
  (tabla_periodica.pdf, tendencias) lanza cientos de `Syntax Error … Bad 'Length'
  attribute in stream` de poppler.** · Síntoma: avalancha de errores en
  `pdftoppm`/`pdfinfo`. · Causa: ruido de poppler leyendo el XObject PDF embebido
  por lualatex; **no** indica PDF corrupto. · Fix: ignóralo — los PNG sí se
  generan. Redirige el stderr (`2>/dev/null`) para no ahogar el log.

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
