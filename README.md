# Guías del Profe — Kit

Un **kit para profesores** que convierte a un agente de IA de terminal (Claude
Code, Antigravity, OpenCode) en tu **diagramador y asesor pedagógico**: generas
guías, talleres, quizzes, exámenes, presentaciones y fichas en LaTeX con diseño
editorial consistente — **sin saber LaTeX**.

> **Se entrena con el uso.** Cada error que encuentras se guarda en
> `knowledge/preflight-checklist.md` para que el agente no lo repita. Entre más
> lo uses, mejor diagrama.

## Para quién

Profes que quieren material bonito y consistente sin pelear con la maquetación.
Hablas en español; el agente propone la estructura didáctica, espera tu visto
bueno y luego genera y compila.

## Empezar

1. **Requisitos e instalación:** ver [`SETUP.md`](SETUP.md) (TeX con `lualatex`
   + fuentes Charter e Inter). Verifica con `./check.sh`.
2. Abre este repo con tu agente (Claude Code / Antigravity / OpenCode). Leerá
   `AGENTS.md` automáticamente.
3. La primera vez te ofrecerá el onboarding *«¿quién eres y qué das?»*
   (ver `commands/setup.md`). Es opcional.
4. Pídele lo que necesitas: *«un taller de fracciones para 6.º, para imprimir»*.
   Te dará un esquema; apruébalo y lo genera.

## Cómo funciona (filosofía)

- **Borrador primero:** nunca genera LaTeX sin aprobar antes el esquema.
- **Semántica pura:** escribes el *qué* (definición, ejemplo, práctica…); el
  diseño vive en `design/` y es intercambiable.
- **Pre-flight de calidad:** antes de generar, el agente consulta el checklist de
  gotchas; al terminar, verifica el PDF en imagen.

## Estructura

```
AGENTS.md                 instrucciones canónicas (portable)
CLAUDE.md  GEMINI.md       adaptadores → AGENTS.md
SETUP.md  check.sh         requisitos y verificación de entorno
compile_quiet.sh           compilación (lualatex, 2 pasadas, log limpio)
design/                    design system (preamble.tex, beamer.tex)
knowledge/
  preflight-checklist.md   gotchas (se va engordando)
  vocabulario-v5.md        vocabulario semántico del design system
templates/                 plantillas por tipo de documento
commands/setup.md          onboarding del profe
examples/                  ejemplos de muestra
profile.example.md         plantilla del perfil (el real, profile.md, es local)
```

## Compatibilidad

| Herramienta | Lee | Notas |
|---|---|---|
| **Claude Code** | `CLAUDE.md` → `AGENTS.md` | Puede usar skills/hooks/commands (extras opcionales). |
| **OpenCode** | `AGENTS.md` | Núcleo completo. |
| **Antigravity** | `GEMINI.md` → `AGENTS.md` | Núcleo completo. |

## Licencia

[MIT](LICENSE) © 2026 Juan Diego Andrés Prada Ramírez. Úsalo, modifícalo y
compártelo libremente.
