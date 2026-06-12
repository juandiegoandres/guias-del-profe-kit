# WORKFLOW — cómo trabajo con el kit

Guía rápida para el día a día (para el autor y quien mantenga el kit).

## Las dos carpetas

| Carpeta | Rol |
|---|---|
| `guias-del-profe` (la vieja) | **Bodega / archivo:** proyectos grandes que ya existen (libro, unidades, videos). No es git. Úsala para retomar eso. |
| `guias-del-profe-kit` (esta) | **Mesa de trabajo de ahora + lo que comparto** en GitHub. Aquí hago el material nuevo. |

> El **design system canónico es el de este kit**. Si cambias el diseño, hazlo
> aquí (no en la carpeta vieja) para que la mejora se publique sola.

## Día a día

1. Abro **`guias-del-profe-kit`** con mi agente (Claude Code / Antigravity / OpenCode).
2. Le pido el material. Lo genera en **`material/<grado>/<asignatura>/<tema>/`** y
   los PDF en **`pdfs/...`**.
3. Lo imprimo / uso. **Eso es privado.**

### Qué es privado vs. qué se comparte

| **Privado (NO se sube — ya en `.gitignore`)** | **Se versiona y sube (mejora el kit)** |
|---|---|
| `material/` (mis documentos) | `design/`, `templates/`, `knowledge/` |
| `pdfs/`, `.build/` | `examples/`, docs (`*.md`) |
| `profile.md` (mi perfil) | `compile_quiet.sh` / `.ps1`, `check.*` |

## Cómo lo entreno 🔁

Cuando aparece un error nuevo, o mejoro una plantilla / el design:

```bash
cd ~/Sites/guias-del-profe-kit
git add knowledge/ templates/ design/        # solo lo compartible
git commit -m "nuevo gotcha: <lo que sea>"
git push
```

Mi material privado **no entra** en el commit (está ignorado). Solo viaja la
mejora → el kit aprende y le sirve a otros profes.

## La sección de plantillas (templates/)

Es el **menú de puntos de partida**. Hoy: `guia`, `guia_profe`, `worksheet`,
`quiz`, `beamer`. El agente **siempre parte de aquí**, no maqueta desde cero.

**Para agregar una plantilla nueva** (p. ej. ficha, examen, infografía):
1. Crea `templates/<tipo>.tex` (que compile con placeholders `<...>`).
2. Si entra en el paquete de clase, añádela al flujo en `AGENTS.md`.
3. `git add templates/ AGENTS.md && git commit && git push`.

## Regla mental rápida

- **Material nuevo** → en el kit (`material/`, privado).
- **Proyectos viejos grandes** → en `guias-del-profe`.
- **Mejora del kit** (gotcha, plantilla, diseño) → commit + push aquí.
