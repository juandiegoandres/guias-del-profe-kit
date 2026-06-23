# Estilo ZapiaLab — adaptar guías al centro de interés de programación

> Léelo cuando el profe pida material para **ZapiaLab** ("Programación en la Era de los
> Agentes de IA"). No cambia el design system: lo **configura** y fija el tono.

ZapiaLab forma adolescentes (cero código) como **arquitectos/auditores/hackers** que usan la IA
como copiloto, no como muleta. El pensum vive en `~/Sites/zapialab/pensum-zapialab/` (Módulo 0 +
6 semanas) y ahora también como MOOC en juandiegoandres.com. Una guía impresa de ZapiaLab es el
complemento físico de una lección del MOOC.

## Configuración del documento
- **Asignatura/color:** usa `\setsubject{eco}` (índigo) como acento de "tecnología/lógica", o el
  que el profe prefiera. Mantén un solo color por documento.
- **Modo:** casi siempre `\printmodetrue` (los chicos imprimen y rayan). Pantalla solo si es para proyectar.
- **Metadatos:** título de la semana, "ZapiaLab" como institución/marca, y el nivel (adolescentes).

## Tono (obligatorio en ZapiaLab)
- **Hacker, motivador, directo**, técnico pero accesible. Nada acartonado.
- Frase-columna del programa: *"La IA amplifica a quien entiende el sistema; al que no, lo reemplaza."*
- **Regla del semáforo** siempre visible en la guía: 🔴 prohibido LLM · 🟡 IA solo tutora de errores ·
  🟢 IA copiloto. Indica la regla de la semana arriba, como un sello/alerta (usa el bloque de alerta ámbar).

## Bilingüe con intención
- Incluye una caja **🔤 Tech English** con el vocabulario técnico de la guía (term inglés → uso).
- Los *prompts* de ejemplo a la IA van **en inglés** (es la habilidad real). El resto, en español.

## Evaluación
- Los criterios evalúan **diseño lógico**, no memorización de sintaxis. Refléjalo en los enunciados
  ("¿tu lógica funcionaría con cualquier lista?") y en las notas pedagógicas de la `guia_profe`.

## Paquete típico de una semana ZapiaLab
`guia.tex` (estudiante) + `guia_profe.tex` (secuencia de los 90 min, errores comunes, soluciones) +
opcional `worksheet.tex` (laboratorio imprimible). El video lo hacen mate-animador/videotutorialista;
aquí solo lo imprimible. Aprueba el esquema del conjunto antes de generar.
