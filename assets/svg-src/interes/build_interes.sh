#!/bin/bash
# build_interes.sh — genera drivers standalone, compila, exporta SVG (apto
# SVGMobject) y renderiza PNG de composicion (capibara + traje / en fondo / naranjas).
# Uso (desde la raiz del kit):  bash assets/svg-src/interes/build_interes.sh
set -e
KIT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"
SRC="assets/svg-src/interes"
IMG="assets/imgs/interes"
cd "$KIT"
mkdir -p "$IMG"

HEAD='\documentclass[border=8pt]{standalone}
\usepackage{xcolor}\usepackage{tikz}\usetikzlibrary{calc}
\input{assets/svg-src/interes/_estilo_interes.tex}
\input{tikzlib/interes/capibara_kawaii.tex}
\input{assets/svg-src/interes/trajes.tex}
\input{assets/svg-src/interes/fondos.tex}
\input{assets/svg-src/interes/naranjas.tex}
\input{tikzlib/interes/capidolar.tex}
\begin{document}\begin{tikzpicture}'
FOOT='\end{tikzpicture}\end{document}'

# gen_svg <name> <frame> <body...>   -> exporta SVG apto SVGMobject
gen_svg () {
  local name="$1"; local frame="$2"; shift 2; local body="$*"
  printf '%s\n%s\n%s\n%s\n' "$HEAD" "$frame" "$body" "$FOOT" > "$SRC/std_$name.tex"
  ./compile_quiet.sh "$SRC/std_$name.tex" "$name" "$IMG" >/dev/null
  pdftocairo -svg "$IMG/$name.pdf" "$SRC/$name.svg"
  echo "  SVG  $name"
}

# gen_png <name> <frame> <body...>   -> PNG de preview (composicion)
gen_png () {
  local name="$1"; local frame="$2"; shift 2; local body="$*"
  printf '%s\n%s\n%s\n%s\n' "$HEAD" "$frame" "$body" "$FOOT" > "$SRC/prev_$name.tex"
  ./compile_quiet.sh "$SRC/prev_$name.tex" "prev_$name" "$IMG" >/dev/null
  pdftocairo -png -r 150 -transp -singlefile "$IMG/prev_$name.pdf" "$IMG/prev_$name"
  echo "  PNG  prev_$name"
}

echo "== SVG overlays sueltos, frame capi (para recolorear/animar por partes) =="
gen_svg traje_vueltiao    '\capiframe' '\trajevueltiao'
gen_svg traje_banquero    '\capiframe' '\trajebanquero'
gen_svg traje_comerciante '\capiframe' '\trajecomerciante'
gen_svg traje_academico   '\capiframe' '\trajeacademico'
gen_svg traje_ahorrador   '\capiframe' '\trajeahorrador'

echo "== SVG compuestos: capibara YA vestido (turn-key para Manim) =="
gen_svg capibara_vueltiao    '' '\capibarakawaii\trajevueltiao'
gen_svg capibara_banquero    '' '\capibarakawaii\trajebanquero'
gen_svg capibara_comerciante '' '\capibarakawaii\trajecomerciante'
gen_svg capibara_academico   '' '\capibarakawaii\trajeacademico'
gen_svg capibara_ahorrador   '' '\capibarakawaii\trajeahorrador'

echo "== SVG fondos (frame escena) =="
gen_svg fondo_neutro   '\escenaframe' '\fondoneutro'
gen_svg fondo_banco    '\escenaframe' '\fondobanco'
gen_svg fondo_mercado  '\escenaframe' '\fondomercado'
gen_svg fondo_finca    '\escenaframe' '\fondofinca'

echo "== SVG naranjas (bbox natural) =="
gen_svg naranja         '' '\naranjaunit'
gen_svg naranja_pila    '' '\naranjapila'
gen_svg naranja_canasta '' '\naranjacanasta'

echo "== PNG previews: capibara + traje =="
gen_png look_vueltiao    '\capiframe' '\capibarakawaii\trajevueltiao'
gen_png look_banquero    '\capiframe' '\capibarakawaii\trajebanquero'
gen_png look_comerciante '\capiframe' '\capibarakawaii\trajecomerciante'
gen_png look_academico   '\capiframe' '\capibarakawaii\trajeacademico'
gen_png look_ahorrador   '\capiframe' '\capibarakawaii\trajeahorrador'

echo "== PNG previews: capibara en fondo =="
gen_png escena_neutro   '\escenaframe' '\fondoneutro\begin{scope}\capibarakawaii\end{scope}'
gen_png escena_banco    '\escenaframe' '\fondobanco\begin{scope}\capibarakawaii\trajebanquero\end{scope}'
gen_png escena_mercado  '\escenaframe' '\fondomercado\begin{scope}\capibarakawaii\trajecomerciante\end{scope}'
gen_png escena_finca    '\escenaframe' '\fondofinca\begin{scope}\capibarakawaii\trajevueltiao\end{scope}'

echo "== PNG previews: naranjas =="
gen_png dinero_naranjas '' '\naranjaen{-2.6}{-0.5}{1}\naranjapila\begin{scope}[shift={(4.2,-0.6)}]\naranjacanasta\end{scope}'

echo "== SVG CAPIDOLARES (moneda que crece) — bbox natural, apto SVGMobject =="
gen_svg capidolar_moneda  '' '\capidolarmoneda'
gen_svg capidolar_billete '' '\capidolarbillete'
gen_svg capidolar_pila    '' '\capidolarpila'
gen_svg capidolar_saco    '' '\capidolarsaco'
gen_svg naranja_precio    '' '\naranjaprecio'

echo "== PNG previews: capidolares =="
gen_png capidolar_moneda  '' '\capidolarmoneda'
gen_png capidolar_billete '' '\capidolarbillete'
gen_png capidolar_pila    '' '\capidolarpila'
gen_png capidolar_saco    '' '\capidolarsaco'
gen_png naranja_precio    '' '\naranjaprecio'
# crecimiento 1 -> muchas (tres torres) para ilustrar el interes compuesto
gen_png capidolar_crece   '' '\capipuck{-3.4}{0}\begin{scope}[shift={(0,0)}]\foreach\i in{0,1,2}{\capipuck{0}{\i*0.34}}\end{scope}\begin{scope}\foreach\i in{0,1,2,3,4,5}{\capipuck{3.4}{\i*0.34}}\end{scope}'

echo "DONE"
