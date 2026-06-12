# Imágenes — generar el arte con NanoBanana (Antigravity / Gemini)

El design system permite poner imágenes con `\figura{archivo}{pie}`. Si el
archivo **no existe**, dibuja un **placeholder** automático — así el documento
compila aunque el arte aún no esté. El arte real se agrega después.

## Dónde viven las imágenes

```
assets/imgs/<unidad>/<archivo>.png      ← las imágenes
assets/imgs/<unidad>/PROMPTS.md         ← los prompts + la línea gráfica
```
`\figura{<unidad>/<archivo>.png}{pie de foto}` busca en `assets/imgs/`.

## Flujo para generar el arte

1. **Trabaja con placeholders primero.** Genera el documento con sus `\figura`;
   los huecos quedan marcados. No te bloquees por el arte.
2. **Escribe los prompts** en `assets/imgs/<unidad>/PROMPTS.md`, uno por imagen,
   siguiendo la **línea gráfica** (abajo).
3. **Genera con NanoBanana** (el modelo de imagen de Gemini) desde
   **Antigravity / Gemini CLI** o la app de Gemini. Guarda cada salida con el
   **mismo nombre** que espera el `\figura` correspondiente.
4. **Recompila.** El placeholder se reemplaza por la imagen real, sin tocar el
   `.tex`.

## Línea gráfica (para que todo se vea coherente)

- **Plano y editorial** (flat), estilo libro de texto / infografía limpia.
- **Color de la asignatura dominante** (el de `\setsubject`) + sus tints; **ámbar
  solo como acento**. Nada de degradados ruidosos ni sombras pesadas.
- **SIN texto incrustado** en la imagen (los rótulos van en LaTeX, en el pie o
  con anotaciones; así se pueden editar y traducir).
- Fondo limpio; composición centrada; relación de aspecto la que pida la `\figura`
  (p. ej. 16:7 para portadas de sección).

## Plantilla de prompt

```
Ilustración editorial plana de <qué>, estilo libro de texto.
Paleta: <color de asignatura> dominante + tints; acento ámbar puntual.
Composición limpia y centrada, sin texto, sin sombras pesadas, fondo claro.
Relación de aspecto <p. ej. 16:9>.
```

> **Regla:** el arte es opcional para que el documento exista. Genera el material
> con placeholders y, cuando quieras, súbele las imágenes con este flujo.
