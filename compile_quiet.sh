#!/bin/bash
# compile_quiet.sh — Compilación silenciosa (ahorra tokens de contexto)
# Uso: ./compile_quiet.sh <path/to/file.tex> <nombre_salida> [dir_salida]
# Ejemplo: ./compile_quiet.sh src/9/matematicas/guia_factorizacion.tex guia_factorizacion pdfs/9/matematicas

FILE_PATH=$1
OUTPUT_NAME=$2
OUT_DIR=${3:-pdfs}

if [ -z "$FILE_PATH" ] || [ -z "$OUTPUT_NAME" ]; then
    echo "Uso: ./compile_quiet.sh <path/to/file.tex> <nombre_salida> [dir_salida]"
    exit 1
fi

# Rutas absolutas para que funcione desde cualquier directorio de trabajo
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ABS_FILE="${SCRIPT_DIR}/${FILE_PATH}"
ABS_OUT="${SCRIPT_DIR}/${OUT_DIR}"
LOG="/tmp/latex_${OUTPUT_NAME}.log"

# TEXINPUTS incluye la raíz del proyecto para que \input{templates/...}
# funcione desde cualquier subdirectorio sin rutas relativas frágiles
# Incluye /tmp para que la 2ª pasada relea .toc/.aux generados allí
# (lualatex escribe en --output-directory pero \@input busca en TEXINPUTS).
export TEXINPUTS="${SCRIPT_DIR}//:/tmp:"

mkdir -p "$ABS_OUT"

# Dos pasadas (suficiente para TOC y referencias cruzadas)
for PASS in 1 2; do
    # Antes de la 2ª pasada, copia el .toc al CWD para que \@input lo relea.
    # (lualatex escribe en --output-directory=/tmp, pero \@input solo busca
    #  en el directorio de trabajo, donde "." está primero en la ruta.)
    if [ $PASS -eq 2 ]; then
        cp -f "/tmp/${OUTPUT_NAME}.toc" "${SCRIPT_DIR}/" 2>/dev/null
    fi
    lualatex \
        --interaction=nonstopmode \
        --output-directory="/tmp" \
        --jobname="$OUTPUT_NAME" \
        "$ABS_FILE" > "$LOG" 2>&1
    EXIT_CODE=$?
    if [ $EXIT_CODE -ne 0 ] && [ $PASS -eq 1 ]; then
        break
    fi
done
# Borra la copia temporal del .toc en el CWD
rm -f "${SCRIPT_DIR}/${OUTPUT_NAME}.toc"

# ── Resultado compacto ────────────────────────────────────────
if [ -f "/tmp/${OUTPUT_NAME}.pdf" ]; then
    PAGES=$(grep -o "Output written.*" "$LOG" | tail -1)
    WARN_COUNT=$(grep -c "Warning:" "$LOG" 2>/dev/null || echo 0)
    echo "PDF OK | $PAGES | Advertencias: $WARN_COUNT"

    # Solo advertencias accionables (ignorar ruido de fuentes y microtype)
    ACTIONABLE=$(grep "Warning:" "$LOG" \
        | grep -v -E "(microtype|Token|fontspec|Font|babel|polyglossia|fancyhdr)" \
        | head -5)
    [ -n "$ACTIONABLE" ] && echo "Advertencias relevantes:" && echo "$ACTIONABLE"

    mv "/tmp/${OUTPUT_NAME}.pdf" "${ABS_OUT}/"
    echo "Guardado: ${OUT_DIR}/${OUTPUT_NAME}.pdf"
else
    echo "Error de compilacion en ${FILE_PATH}:"
    grep -E "^(!|l\.[0-9]|.*:[0-9]+: )" "$LOG" | head -20
    echo ""
    echo "--- Ultimas 15 lineas del log ---"
    tail -15 "$LOG"
    exit 1
fi

# Limpiar todos los auxiliares de /tmp (guías, talleres, fichas, presentaciones)
rm -f "/tmp/${OUTPUT_NAME}.aux"  "/tmp/${OUTPUT_NAME}.log" \
      "/tmp/${OUTPUT_NAME}.out"  "/tmp/${OUTPUT_NAME}.toc" \
      "/tmp/${OUTPUT_NAME}.fls"  "/tmp/${OUTPUT_NAME}.fdb_latexmk" \
      "/tmp/${OUTPUT_NAME}.nav"  "/tmp/${OUTPUT_NAME}.snm" \
      "/tmp/${OUTPUT_NAME}.vrb"  "/tmp/${OUTPUT_NAME}.bbl" \
      "/tmp/${OUTPUT_NAME}.blg"
