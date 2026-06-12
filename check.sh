#!/usr/bin/env bash
# Verifica que el entorno pueda compilar el kit.
# Uso: ./check.sh
set -u
crit=0

say(){ printf "%s\n" "$1"; }

say "== Guías del Profe — verificación de entorno =="

# lualatex (crítico)
if command -v lualatex >/dev/null 2>&1; then
  say "  [ok]  lualatex: $(lualatex --version 2>/dev/null | head -1)"
else
  say "  [X]   lualatex NO encontrado → instala TeX Live / MacTeX (ver SETUP.md)"
  crit=1
fi

# fuentes (aviso)
check_font(){
  if fc-list 2>/dev/null | grep -qi "$1"; then
    say "  [ok]  fuente: $1"
  else
    say "  [!]   fuente no detectada: $1 (instálala — ver SETUP.md)"
  fi
}
if command -v fc-list >/dev/null 2>&1; then
  check_font "Charter"
  check_font "Inter"
else
  say "  [!]   fc-list no disponible; no verifiqué fuentes (lualatex puede hallarlas igual)"
fi

# script de compilación
if [ -x ./compile_quiet.sh ]; then
  say "  [ok]  compile_quiet.sh ejecutable"
else
  say "  [!]   compile_quiet.sh no ejecutable → 'chmod +x compile_quiet.sh'"
fi

say ""
if [ "$crit" -eq 0 ]; then
  say "Listo para compilar."
else
  say "Faltan dependencias críticas (ver arriba)."
fi
exit "$crit"
