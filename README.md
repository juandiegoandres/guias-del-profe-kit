<div align="center">

# 📚 Guías del Profe — Kit

**Convierte tu agente de IA de terminal en tu diagramador y asesor pedagógico.**
Genera guías, talleres, quizzes, exámenes, presentaciones y fichas en LaTeX con
diseño editorial consistente — **sin saber LaTeX**.

![License](https://img.shields.io/badge/licencia-MIT-1A8917)
![LaTeX](https://img.shields.io/badge/motor-lualatex-3D6117)
![Tools](https://img.shields.io/badge/funciona%20con-Claude%20Code%20·%20Antigravity%20·%20OpenCode-1E4078)

**🌐 Español · [English](README.en.md)**

</div>

---

## ✨ Lo que genera el agente

<table>
<tr>
<td width="50%" valign="top">
<img src="docs/img/ejemplo-guia.png" alt="Guía de aprendizaje" width="100%"/>
<br/><sub><b>Guía de aprendizaje</b> — teoría, ejemplos resueltos y práctica por niveles.</sub>
</td>
<td width="50%" valign="top">
<img src="docs/img/ejemplo-worksheet.png" alt="Worksheet recortable" width="100%"/>
<br/><sub><b>Worksheet recortable</b> — hoja con tablas y espacios para llenar a mano.</sub>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<img src="docs/img/ejemplo-quiz.png" alt="Quiz tipo ICFES" width="100%"/>
<br/><sub><b>Quiz tipo ICFES</b> — selección múltiple con burbujas + pregunta abierta.</sub>
</td>
<td width="50%" valign="top">
<img src="docs/img/ejemplo-beamer-portada.png" alt="Presentación — portada" width="100%"/>
<img src="docs/img/ejemplo-beamer-pregunta.png" alt="Presentación — pregunta" width="100%"/>
<br/><sub><b>Presentación Beamer 16:9</b> — una idea por lámina. Para clase o YouTube.</sub>
</td>
</tr>
</table>

> Todo sale del **mismo design system** (Charter + Inter Display, un color por
> asignatura). Cambias el tipo de documento, no la estética.

---

## 🔧 Cómo funciona

El agente nunca dispara LaTeX a ciegas: **propone, tú apruebas, genera, verifica.**

```mermaid
flowchart TD
  A["🧑‍🏫 Profe pide algo en español"] --> B["📋 El agente lee el preflight-checklist"]
  B --> C["✏️ Propone un esquema didáctico"]
  C --> D{"¿Apruebas el esquema?"}
  D -- "No · ajusta" --> C
  D -- "Sí" --> E["⚙️ Genera LaTeX semántico"]
  E --> F["🖨️ Compila con compile_quiet.sh"]
  F --> G["🔍 Verifica el PDF en imagen"]
  G --> H["✅ Material listo para imprimir"]
```

**Borrador primero** (no escribe LaTeX sin tu visto bueno) · **semántica pura**
(escribes el *qué*; el diseño vive aparte) · **pre-flight de calidad** (consulta
el checklist de errores antes de generar y verifica el PDF al terminar).

---

## 🧩 Una sola fuente, tres herramientas

`AGENTS.md` es el cerebro canónico; cada herramienta entra por su propia puerta.

```mermaid
flowchart TD
  CC["Claude Code"] -->|"CLAUDE.md"| X["📖 AGENTS.md<br/>instrucciones canónicas"]
  AG["Antigravity"] -->|"GEMINI.md"| X
  OC["OpenCode"] -->|"AGENTS.md"| X
  X --> DS["🎨 design system<br/>+ compile_quiet.sh"]
  X --> KN["🧠 knowledge/<br/>checklist + vocabulario"]
  X --> PR["👤 profile.md<br/>(perfil local del profe)"]
```

El núcleo (AGENTS.md + scripts + design system + checklist) funciona en las tres.
Skills/hooks de Claude Code son extras opcionales.

---

## 🚀 Empezar

1. **Requisitos:** TeX con `lualatex` + fuentes Charter e Inter. Detalle en
   [`SETUP.md`](SETUP.md). Verifica tu entorno:
   ```bash
   ./check.sh
   ```
2. Abre esta carpeta con tu agente (Claude Code / Antigravity / OpenCode):
   leerá `AGENTS.md` solo.
3. La primera vez te ofrece el onboarding *«¿quién eres y qué das?»* y guarda tu
   perfil local (`profile.md`, no se versiona).
4. Pídele lo que necesitas:
   > *«Un taller de fracciones equivalentes para 6.º, para imprimir en B/N.»*

   Te da un esquema → lo apruebas → lo genera y compila.

📖 **Guía completa:** instalación Mac/Windows en [`SETUP.md`](SETUP.md) · paso a
paso de uso y paquete de clase en [`USAGE.md`](USAGE.md).

---

## 🧠 Se entrena con el uso

Cada error que aparece se guarda en
[`knowledge/preflight-checklist.md`](knowledge/preflight-checklist.md) con el
formato **Regla · Síntoma · Causa · Fix**. El agente lo lee antes de generar, así
que **entre más lo usas, menos se equivoca.** Ya trae decenas de gotchas reales de
LaTeX/lualatex/Beamer.

---

## 📂 Estructura

```
AGENTS.md                  cerebro canónico (portable)
CLAUDE.md  GEMINI.md        adaptadores → AGENTS.md
SETUP.md                   instalación Mac/Windows + requisitos
USAGE.md                   paso a paso de uso + paquete de clase
WORKFLOW.md                flujo local del autor + cómo entrenar el kit
check.sh · check.ps1       verifica tu entorno (Mac·Linux · Windows)
compile_quiet.sh · .ps1    compilación (lualatex, 2 pasadas, log limpio)
design/                    design system (preamble.tex, beamer.tex)
knowledge/
  preflight-checklist.md   gotchas (se va engordando)
  vocabulario-v5.md        vocabulario semántico del design system
  imagenes-nanobanana.md   cómo generar el arte con NanoBanana (Gemini)
templates/                 plantillas a rellenar (guia, guia_profe, worksheet, quiz, beamer)
assets/imgs/               arte de los documentos (placeholders si falta)
commands/setup.md          onboarding del profe
examples/                  ejemplos que compilan (guía, worksheet, quiz, presentación)
profile.example.md         plantilla del perfil (el real, profile.md, es local)
```

> **Paquete de clase:** pídele *«el paquete de fracciones para 6.º»* y genera
> coherentes la **guía del estudiante, la guía del profe, la presentación, el
> taller y el quiz** en `material/<grado>/<asignatura>/<tema>/`, con sus PDF en
> `pdfs/` espejo. Detalle en [`USAGE.md`](USAGE.md).

---

## 📜 Licencia

[MIT](LICENSE) © 2026 Juan Diego Andrés Prada Ramírez · Instituto Técnico Santo
Tomás, Zapatoca. Úsalo, modifícalo y compártelo libremente.

<div align="center"><sub>Hecho para profes, por un profe 👨‍🏫</sub></div>
