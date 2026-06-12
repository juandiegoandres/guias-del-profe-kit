# SETUP — instalación y requisitos (Mac y Windows)

## ¿Qué necesitas?

| Requisito | Para qué | Mac | Windows |
|---|---|---|---|
| **TeX con `lualatex`** | compilar el LaTeX | MacTeX | MiKTeX o TeX Live |
| **Fuente Charter** | cuerpo de texto (serif) | **ya viene en macOS** | hay que instalarla |
| **Fuente Inter** (+ Inter Display) | títulos/etiquetas | instalar | instalar |
| **Poppler** (`pdftoppm`) | que el agente verifique el PDF en imagen | `brew install poppler` | con MiKTeX o Scoop |
| **Un agente de IA de terminal** | el que conversa contigo | Claude Code / Antigravity / OpenCode | igual |

---

## 🍎 macOS — paso a paso

1. **Instala MacTeX** (incluye `lualatex`):
   ```bash
   brew install --cask mactex-no-gui
   ```
   (o descarga MacTeX de https://tug.org/mactex/). Cierra y reabre la terminal.

2. **Fuente Charter:** ya viene con macOS — no haces nada. ✅

3. **Fuente Inter:** descárgala gratis en https://rsms.me/inter/ → abre el `.zip`
   → selecciona las fuentes **Inter** e **Inter Display** (Regular, SemiBold,
   Black) → doble clic → *Instalar*.

4. **Poppler** (para la verificación visual):
   ```bash
   brew install poppler
   ```

5. **Verifica** (desde la carpeta del kit):
   ```bash
   ./check.sh
   ```

---

## 🪟 Windows — paso a paso

> En Windows usa los scripts **`.ps1` (PowerShell nativo)** — no necesitas Git
> Bash. (Los `.sh` son para Mac/Linux; en Windows funcionan solo dentro de Git
> Bash/WSL, opcional.)

1. **Instala MiKTeX** (incluye `lualatex`): https://miktex.org/download →
   instálalo "para el usuario actual" → al primer uso, acepta que instale
   paquetes faltantes automáticamente.
   *(Alternativa: TeX Live.)*

2. **Fuente Charter** (Windows **no** la trae): descarga una versión de Charter
   (p. ej. *Bitstream Charter*, gratis) → clic derecho → **Instalar para todos
   los usuarios**. El nombre de la familia debe quedar como **"Charter"**.

3. **Fuente Inter:** descárgala en https://rsms.me/inter/ → instala **Inter** e
   **Inter Display** (Regular, SemiBold, Black): selecciona los `.ttf`/`.otf` →
   clic derecho → **Instalar para todos los usuarios**.

4. **Poppler** (`pdftoppm`, para la verificación visual): la forma fácil es
   [Scoop](https://scoop.sh) → `scoop install poppler`. *(Opcional: el agente
   puede verificar de otras formas; si no lo instalas, igual compila.)*

5. **Verifica** (en PowerShell, dentro de la carpeta del kit):
   ```powershell
   powershell -ExecutionPolicy Bypass -File .\check.ps1
   ```

---

## Conecta tu agente

Abre la carpeta del kit con tu herramienta; cada una lee su archivo, que apunta a
`AGENTS.md`:

| Herramienta | Lee |
|---|---|
| **Claude Code** | `CLAUDE.md` → `AGENTS.md` |
| **OpenCode** | `AGENTS.md` |
| **Antigravity / Gemini CLI** | `GEMINI.md` → `AGENTS.md` |

## Prueba que todo compila

**Mac / Linux:**
```bash
./compile_quiet.sh examples/ejemplo_guia.tex prueba pdfs/examples
```
**Windows (PowerShell):**
```powershell
powershell -ExecutionPolicy Bypass -File .\compile_quiet.ps1 examples\ejemplo_guia.tex prueba pdfs\examples
```
Debe terminar en `PDF OK`. El PDF queda en `pdfs/examples/prueba.pdf`.

## Si algo falla

- **`lualatex: command not found`** → no instalaste TeX o no reabriste la terminal.
- **`cannot find font "Charter"/"Inter"`** → falta instalar esa fuente (paso 2/3).
- **Windows:** usa los scripts `.ps1` con
  `powershell -ExecutionPolicy Bypass -File .\<script>.ps1`. Los `.sh` solo corren
  en Mac/Linux (o en Git Bash/WSL).
- Más errores comunes y sus arreglos: `knowledge/preflight-checklist.md`.
