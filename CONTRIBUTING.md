# Cómo aportar 🤝

¡Gracias por sumar! Este kit **mejora con el uso**: entre más profes lo usan y
comparten lo que aprenden, mejor diagrama. No necesitas ser programador para
aportar.

## La forma más valiosa: añadir un *gotcha*

Cada vez que el agente cometa un error de LaTeX y lo arreglen, **anótenlo** en
[`knowledge/preflight-checklist.md`](knowledge/preflight-checklist.md). Así nadie
vuelve a tropezar con lo mismo. Usa el formato:

```
- **<Regla en imperativo>.** · Síntoma: <qué se ve mal>. · Causa: <por qué>. ·
  Fix: <solución concreta, con snippet si aplica>.
```

Ponlo en la sección que corresponda (fuentes, tablas, TikZ, contenido…).

## Aportar un ejemplo

1. Crea el `.tex` en `examples/` (mira los que ya están como referencia).
2. **Debe compilar limpio:**
   ```bash
   ./compile_quiet.sh examples/tu_ejemplo.tex prueba pdfs/examples      # Mac/Linux
   # Windows: powershell -ExecutionPolicy Bypass -File .\compile_quiet.ps1 examples\tu_ejemplo.tex prueba pdfs\examples
   ```
3. (Opcional) Añade una captura en `docs/img/` y enséñala en el README.

## Mejorar una plantilla

Las plantillas viven en `templates/`. Manténlas **mínimas y que compilen** con
sus placeholders `<...>`. Si añades una nueva, agrégala también al flujo de
*paquete de clase* en `AGENTS.md`.

## Reglas de estilo (importante)

- **Semántica pura:** usa el vocabulario del design system
  ([`knowledge/vocabulario-v5.md`](knowledge/vocabulario-v5.md)); no maquetes con
  `\vspace`/color/`minipage`. El diseño vive en `design/`.
- **Multiplataforma:** si tocas un script, mantén `.sh` (Mac/Linux) y `.ps1`
  (Windows) **equivalentes**.
- **No subas** PDFs ni tu `profile.md` ni `material/` (ya están en `.gitignore`).

## Proceso (Git)

1. Haz *fork* y crea una rama: `git checkout -b mi-aporte`.
2. Commits claros en español. Cierra el mensaje con:
   ```
   Co-Authored-By: Tu Nombre <tu@correo>
   ```
3. Abre un *Pull Request* describiendo qué aportas y por qué.

## ¿Dudas o ideas?

Abre un *Issue* contando tu caso (qué enseñas, qué te gustaría generar). Las
mejores plantillas salen de necesidades reales del aula. 💡
