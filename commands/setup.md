# Onboarding — «¿quién eres y qué das?»

Instrucción para el agente. Córrela en el primer uso (o cuando el profe pida
`setup`). Es **opcional** y **idempotente** (re-correrla actualiza el perfil).

## Qué hacer

1. Saluda breve y explica que vas a personalizar el kit con 4–5 preguntas.
2. Pregunta (en pocas tandas, no una por una):
   - **Nombre** (cómo firmar los documentos).
   - **Colegio / institución** y ciudad.
   - **Grados** que da y **asignaturas** (mapea a `mat` / `cnat` / `csoc` / `eco`).
   - **Salida por defecto:** impresión B/N (`\printmodetrue`) o pantalla a color
     (`\printmodefalse`).
   - **Marca / sitio** (opcional) y cualquier **preferencia** (estilo de
     ejercicios, tono, contexto local…).
3. Escribe las respuestas en **`profile.md`** (en la raíz del repo) con el mismo
   formato que `profile.example.md`. Ese archivo es **local** (está en
   `.gitignore`); no lo subas.
4. Confirma con un resumen de una línea y pregunta en qué trabajamos hoy.

## Reglas

- Si el profe quiere saltarlo, respeta y sigue sin perfil (usa valores neutros).
- No inventes datos: si no responde algo, déjalo en blanco en `profile.md`.
- En sesiones siguientes, **lee `profile.md` al inicio** y úsalo (no vuelvas a
  preguntar lo que ya está).

## Cómo conectarlo por herramienta (opcional)

- **Claude Code:** se puede exponer como skill/slash-command (`/setup`).
- **OpenCode / Antigravity:** basta con que el profe diga «corre el setup» y el
  agente siga este archivo.
