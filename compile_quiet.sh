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

# Directorio de build AISLADO por ARCHIVO FUENTE (no por nombre de salida).
# Antes se compilaba en /tmp plano con --jobname=<nombre_salida>: dos documentos
# con el mismo nombre (p. ej. varios "guia_profe") compilados EN PARALELO se
# pisaban los auxiliares/PDF en /tmp y el PDF final salía con el tema equivocado
# (o corrupto). La llave es la ruta del .tex, así cada fuente tiene su sandbox
# y se puede compilar en paralelo sin colisión.  (preflight §0)
BUILD_DIR="/tmp/gdp-build/$(printf '%s' "$FILE_PATH" | tr '/ .' '___')"
rm -rf "$BUILD_DIR"
mkdir -p "$BUILD_DIR"
LOG="${BUILD_DIR}/latex.log"

# TEXINPUTS: primero el BUILD_DIR (para que la 2ª pasada relea el .toc/.aux
# que la 1ª escribió allí), luego la raíz del proyecto (para \input{design/...}
# y para resolver assets/imgs/... vía \graphicspath).
export TEXINPUTS="${BUILD_DIR}:${SCRIPT_DIR}//:"

mkdir -p "$ABS_OUT"

# Dos pasadas (suficiente para TOC y referencias cruzadas). El .toc queda en
# BUILD_DIR y \@input lo encuentra por TEXINPUTS: ya no hace falta copiarlo al CWD.
for PASS in 1 2; do
    lualatex \
        --interaction=nonstopmode \
        --output-directory="$BUILD_DIR" \
        --jobname="$OUTPUT_NAME" \
        "$ABS_FILE" > "$LOG" 2>&1
    EXIT_CODE=$?
    if [ $EXIT_CODE -ne 0 ] && [ $PASS -eq 1 ]; then
        break
    fi
done

# ── Resultado compacto ────────────────────────────────────────
if [ -f "${BUILD_DIR}/${OUTPUT_NAME}.pdf" ]; then
    PAGES=$(grep -o "Output written.*" "$LOG" | tail -1)
    WARN_COUNT=$(grep -c "Warning:" "$LOG" 2>/dev/null || echo 0)
    echo "PDF OK | $PAGES | Advertencias: $WARN_COUNT"

    # Solo advertencias accionables (ignorar ruido de fuentes y microtype)
    ACTIONABLE=$(grep "Warning:" "$LOG" \
        | grep -v -E "(microtype|Token|fontspec|Font|babel|polyglossia|fancyhdr)" \
        | head -5)
    [ -n "$ACTIONABLE" ] && echo "Advertencias relevantes:" && echo "$ACTIONABLE"

    mv "${BUILD_DIR}/${OUTPUT_NAME}.pdf" "${ABS_OUT}/"
    echo "Guardado: ${OUT_DIR}/${OUTPUT_NAME}.pdf"
else
    echo "Error de compilacion en ${FILE_PATH}:"
    grep -E "^(!|l\.[0-9]|.*:[0-9]+: )" "$LOG" | head -20
    echo ""
    echo "--- Ultimas 15 lineas del log ---"
    tail -15 "$LOG"
    # Deja el sandbox para depurar cuando falla.
    echo "(log completo: ${LOG})"
    exit 1
fi

# Limpieza: basta con borrar el sandbox aislado del archivo.
rm -rf "$BUILD_DIR"
