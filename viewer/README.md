# Biblioteca / visor de recursos del kit

Un visor web **estático y sin dependencias** para navegar todo el material
creado en `guias-del-profe-kit`: guías del profe, talleres, beamers, iconos,
imágenes libres (con su licencia) y librerías TikZ.

## Uso

```bash
cd viewer
npm run index     # recorre el repo y genera public/resources.json + miniaturas
npm run serve     # sirve en http://localhost:4173
# o de un tirón:
npm start
```

Abre <http://localhost:4173>. Filtra por **sección, asignatura, grado o tipo**,
busca por texto, y haz clic en una tarjeta para abrir el PDF/imagen (los PDF se
ven embebidos con el visor nativo del navegador; el botón «Abrir en pestaña»
usa la ruta real del repo vía `/repo/...`).

## Cómo funciona

- **`indexer.mjs`** recorre `pdfs/`, `material/`, `assets/imgs/`, `tikzlib/` y
  `design/tema-*.tex`; clasifica cada recurso (grado · asignatura · serie · tipo),
  lee las licencias de los `assets/imgs/*/CREDITOS.md`, genera una miniatura
  (`pdftoppm` para PDF, `sips` para raster, `rsvg-convert` para SVG) y escribe
  `public/resources.json`. Si falta alguna herramienta, ese recurso queda sin
  miniatura (se muestra un marcador).
- **`serve.mjs`** es un servidor estático mínimo: sirve `public/` y expone la
  raíz del repo en `/repo/` para abrir los archivos reales.
- **`public/`** es la UI (HTML/CSS/JS vanilla), con tema claro/oscuro y acentos
  por asignatura (mate azul, ciencias esmeralda, economía dorado).

## Notas

- `material/` y `pdfs/` están en `.gitignore` (son salida generada); el visor
  los lee del disco. Por eso `public/resources.json` y `public/thumbs/` también
  se ignoran: **corre `npm run index` tras compilar material nuevo**.
- Cero paquetes de npm: usa solo Node y las herramientas de línea de comandos
  ya presentes en el entorno del kit.

## Ideas a futuro

- Reemplazar el visor nativo por **PDF.js** embebido para navegación de páginas
  y resaltado (hoy se usa el visor nativo del navegador, que ya es PDF.js en
  Firefox) — el `<iframe>` está aislado en `openModal()`, es un cambio local.
- Botón de descarga en lote por serie; export del índice a CSV.
