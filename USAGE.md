# Cómo usar el kit — paso a paso

## ¿Qué es esto, en una frase?

Es un **conjunto de instrucciones + diseño + ejemplos** que tu agente de IA de
terminal lee, para que tú le pidas material en español («un taller de fracciones
para 6.º») y él te entregue un **PDF bien diagramado**, sin que toques LaTeX.

## ¿Cómo funciona?

Tú pides → el agente **propone un esquema** → tú apruebas → **genera el LaTeX** →
**compila** → **verifica el PDF** → te lo entrega. Nunca escribe LaTeX sin tu
visto bueno, y antes de generar consulta una lista de errores comunes para no
repetirlos.

---

## Paso a paso

1. **Instala los requisitos** (una sola vez): ver [`SETUP.md`](SETUP.md) y corre
   `./check.sh`.

2. **Abre la carpeta del kit con tu agente** (Claude Code / Antigravity /
   OpenCode). Lee `AGENTS.md` automáticamente.

3. **La primera vez:** te ofrece el onboarding *«¿quién eres y qué das?»* y guarda
   tu perfil en `profile.md` (local, no se sube). Así firma con tu nombre y usa
   tus grados/asignaturas por defecto.

4. **Pídele lo que necesitas**, en español y con contexto:
   > *«Una guía de la célula para 7.º de Ciencias, para imprimir en B/N.»*

5. **Revisa el esquema.** Te muestra título, secciones y ejercicios en texto
   plano. Dile *«ok»* o pide cambios. **No genera LaTeX hasta que apruebes.**

6. **Genera y compila.** Verás `PDF OK`. El PDF queda en una carpeta `pdfs/...`.

7. **Verifica y ajusta.** El agente revisa el PDF en imagen; si algo se ve raro,
   pídele el ajuste («el título está muy pegado», «agrega un ejemplo más»).

---

## 📦 Paquete de clase (varios documentos a la vez)

Para una clase no necesitas un solo archivo: a veces quieres **la guía, la
presentación, el taller y el quiz** del mismo tema. Pídelo así:

> *«Hazme el **paquete de clase** de fracciones equivalentes para 6.º de
> Matemáticas: guía, presentación, taller y quiz.»*

El agente genera **todos los documentos coherentes** (mismo tema, misma
asignatura/color, tu firma) en una estructura de carpetas ordenada:

```
material/
└── 6/                      ← grado
    └── matematicas/        ← asignatura
        └── fracciones/     ← tema
            ├── guia.tex
            ├── beamer.tex
            ├── quiz.tex
            └── worksheet.tex

pdfs/
└── 6/matematicas/fracciones/
    ├── guia.pdf
    ├── beamer.pdf
    ├── quiz.pdf
    └── worksheet.pdf
```

Así cada tema queda autocontenido y fácil de reutilizar el próximo año. Puedes
pedir solo algunos («solo guía y quiz») o agregar uno después («ahora súmale la
ficha de estudio»).

---

## Consejos

- **Sé concreto:** grado, asignatura, objetivo, tiempo, y si es para **imprimir
  (B/N)** o **pantalla (color)**.
- **Empieza por el esquema:** es más rápido corregir el plan que el PDF.
- **Cada error nuevo** que encuentres, pídele que lo anote en
  `knowledge/preflight-checklist.md` — así el kit no lo repite.
