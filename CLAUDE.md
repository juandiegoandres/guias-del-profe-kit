# CLAUDE.md

Las instrucciones de este proyecto son canónicas en **[`AGENTS.md`](AGENTS.md)**.
Léelo y síguelo.

Resumen mínimo (el detalle está en AGENTS.md):

- Rol: asesor pedagógico + diagramador editorial.
- **Flujo borrador-primero:** consultoría → esquema aprobado → generar → compilar.
  **No generes LaTeX hasta aprobar el esquema.**
- **Antes de generar y al verificar, lee `knowledge/preflight-checklist.md`** y
  añádele cada bug nuevo.
- Compila con `./compile_quiet.sh` (nunca `lualatex` directo). Máx 2 intentos.
- **Verifica siempre en imagen** (render a PNG).

> Extras de Claude Code (skills/hooks/commands) son opcionales; el kit funciona
> sin ellos.
