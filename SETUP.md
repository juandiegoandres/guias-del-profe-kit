# SETUP — requisitos e instalación

## 1. TeX con `lualatex`

Necesitas una distribución TeX que incluya **lualatex** y los paquetes usuales.

- **macOS:** [MacTeX](https://tug.org/mactex/) (`brew install --cask mactex`), o
  BasicTeX + paquetes.
- **Windows:** [TeX Live](https://tug.org/texlive/) o MiKTeX.
- **Linux:** `sudo apt install texlive-full` (o el equivalente de tu distro).

Comprueba: `lualatex --version`.

## 2. Fuentes

El design system usa **Charter** (cuerpo serif) e **Inter / Inter Display**
(títulos). Deben estar instaladas en el sistema (lualatex las busca con fontspec).

- **Charter:** suele venir con TeX (XCharter) o instálala como fuente del sistema.
- **Inter / Inter Display:** descarga gratis en
  [rsms.me/inter](https://rsms.me/inter/) e instálalas (incluye *Inter Display*,
  *Inter Display SemiBold*, *Inter Display Black*).

> Si una fuente falta, lualatex falla con «cannot find font». Instálala y reintenta.

## 3. Verifica el entorno

```bash
./check.sh
```
Te dice si faltan `lualatex` o las fuentes.

## 4. Conecta tu agente

Abre esta carpeta con tu herramienta. Cada una lee su archivo y este apunta a
`AGENTS.md`:

- **Claude Code** → `CLAUDE.md`
- **OpenCode** → `AGENTS.md`
- **Antigravity / Gemini CLI** → `GEMINI.md`

## 5. Primera vez

El agente te ofrecerá el onboarding (`commands/setup.md`) para crear tu
`profile.md` local (nombre, colegio, grados, asignaturas, impresión/pantalla,
marca). Ese archivo **no se versiona** (está en `.gitignore`); es tuyo.

## Probar que todo compila

Cuando haya un ejemplo en `examples/`, pruébalo:
```bash
./compile_quiet.sh examples/<archivo>.tex prueba /tmp
```
Debe decir `PDF OK`.
