# compile_quiet.ps1 — Compilación silenciosa en Windows (PowerShell).
# Equivalente nativo de compile_quiet.sh.
# Uso:
#   powershell -ExecutionPolicy Bypass -File .\compile_quiet.ps1 <ruta\archivo.tex> <nombre_salida> [dir_salida]
# Ej:
#   powershell -ExecutionPolicy Bypass -File .\compile_quiet.ps1 examples\ejemplo_guia.tex guia pdfs\examples

param(
  [Parameter(Mandatory = $true)][string]$FilePath,
  [Parameter(Mandatory = $true)][string]$OutputName,
  [string]$OutDir = "pdfs"
)

$ScriptDir = $PSScriptRoot
$AbsFile   = Join-Path $ScriptDir $FilePath
$AbsOut    = Join-Path $ScriptDir $OutDir
$Tmp       = Join-Path $ScriptDir ".build"        # carpeta temporal (ignorada por git)
$Log       = Join-Path $Tmp "latex_$OutputName.log"

New-Item -ItemType Directory -Force -Path $Tmp, $AbsOut | Out-Null

# TEXINPUTS: raíz del proyecto (recursivo //) para que \input{design/...} funcione.
$root = ($ScriptDir -replace '\\', '/')
$sep  = [System.IO.Path]::PathSeparator
$env:TEXINPUTS = "$root//$sep"

# Dos pasadas (TOC y referencias cruzadas)
foreach ($pass in 1, 2) {
  if ($pass -eq 2) {
    Copy-Item -Force (Join-Path $Tmp "$OutputName.toc") $ScriptDir -ErrorAction SilentlyContinue
  }
  $largs = @(
    "--interaction=nonstopmode",
    "--output-directory=$Tmp",
    "--jobname=$OutputName",
    "$AbsFile"
  )
  & lualatex @largs *> $Log
  if ($LASTEXITCODE -ne 0 -and $pass -eq 1) { break }
}
Remove-Item -Force (Join-Path $ScriptDir "$OutputName.toc") -ErrorAction SilentlyContinue

$Pdf = Join-Path $Tmp "$OutputName.pdf"
if (Test-Path $Pdf) {
  $logText = Get-Content $Log -Raw -ErrorAction SilentlyContinue
  $m = [regex]::Matches($logText, "Output written.*")
  $pagesStr = if ($m.Count -gt 0) { $m[$m.Count - 1].Value } else { "" }
  $warn = ([regex]::Matches($logText, "Warning:")).Count
  Write-Output "PDF OK | $pagesStr | Advertencias: $warn"

  $actionable = Get-Content $Log |
    Select-String "Warning:" |
    Where-Object { $_ -notmatch "microtype|Token|fontspec|Font|babel|polyglossia|fancyhdr" } |
    Select-Object -First 5
  if ($actionable) {
    Write-Output "Advertencias relevantes:"
    $actionable | ForEach-Object { Write-Output $_.Line }
  }

  Move-Item -Force $Pdf $AbsOut
  Write-Output "Guardado: $OutDir/$OutputName.pdf"
}
else {
  Write-Output "Error de compilacion en ${FilePath}:"
  Get-Content $Log -ErrorAction SilentlyContinue |
    Select-String -Pattern '^(!|l\.[0-9]|.*:[0-9]+: )' |
    Select-Object -First 20 |
    ForEach-Object { Write-Output $_.Line }
  Write-Output ""
  Write-Output "--- Ultimas 15 lineas del log ---"
  Get-Content $Log -Tail 15 -ErrorAction SilentlyContinue
  exit 1
}

# Limpiar auxiliares
foreach ($e in "aux", "log", "out", "toc", "fls", "fdb_latexmk", "nav", "snm", "vrb", "bbl", "blg") {
  Remove-Item -Force (Join-Path $Tmp "$OutputName.$e") -ErrorAction SilentlyContinue
}
