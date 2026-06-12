# check.ps1 — Verifica el entorno en Windows (PowerShell).
# Uso:
#   powershell -ExecutionPolicy Bypass -File .\check.ps1

Write-Output "== Guias del Profe - verificacion de entorno (Windows) =="
$crit = 0

# lualatex (critico)
$lua = Get-Command lualatex -ErrorAction SilentlyContinue
if ($lua) {
  $v = (& lualatex --version 2>$null | Select-Object -First 1)
  Write-Output "  [ok]  lualatex: $v"
}
else {
  Write-Output "  [X]   lualatex NO encontrado -> instala MiKTeX o TeX Live (ver SETUP.md)"
  $crit = 1
}

# Fuentes (aviso)
try {
  Add-Type -AssemblyName System.Drawing -ErrorAction Stop
  $fams = (New-Object System.Drawing.Text.InstalledFontCollection).Families.Name
  foreach ($f in "Charter", "Inter") {
    if ($fams | Where-Object { $_ -like "*$f*" }) {
      Write-Output "  [ok]  fuente: $f"
    }
    else {
      Write-Output "  [!]   fuente no detectada: $f (instalala - ver SETUP.md)"
    }
  }
}
catch {
  Write-Output "  [!]   no pude listar fuentes; verificalo en Configuracion > Fuentes"
}

# poppler / pdftoppm (aviso - para la verificacion visual)
if (Get-Command pdftoppm -ErrorAction SilentlyContinue) {
  Write-Output "  [ok]  pdftoppm (poppler) disponible"
}
else {
  Write-Output "  [!]   pdftoppm no encontrado (opcional; 'scoop install poppler')"
}

Write-Output ""
if ($crit -eq 0) {
  Write-Output "Listo para compilar.  Prueba:"
  Write-Output "  powershell -ExecutionPolicy Bypass -File .\compile_quiet.ps1 examples\ejemplo_guia.tex prueba pdfs\examples"
}
else {
  Write-Output "Faltan dependencias criticas (ver arriba)."
}
exit $crit
