# Créditos y licencias — imágenes e iconos de genética

## Imágenes libres (Wikimedia Commons)

| Archivo | Contenido | Archivo Commons | Autor | Licencia |
|---|---|---|---|---|
| `mendel.jpg` | Retrato de Gregor Mendel (1822–1884) | `File:Gregor_Mendel_2.jpg` | Autor desconocido (s. XIX) | **Dominio público** |
| `arveja_botanica.jpg` | Lámina botánica de *Pisum sativum* | `File:Illustration_Pisum_sativum0.jpg` | O. W. Thomé, *Flora von Deutschland* (1885) | **Dominio público** |

Licencia PD verificada con la API de Commons (`extmetadata.LicenseShortName = "Public domain"`).
Descargadas a ~700 px con `curl` desde `Special:FilePath`. Se prefirió
`Gregor_Mendel_2.jpg` (PD) sobre `Gregor_Mendel_oval.jpg` (CC BY 4.0) para
mantener todo en dominio público.

## Iconos vectoriales

Iconos vectoriales reutilizados de bibliotecas de **licencia libre**. Se
descargaron con `curl`, se recolorearon (`currentColor` → esmeralda `#106E50`
para fondo claro y `#FFFFFF` para fondo esmeralda) y se convirtieron a PDF
vectorial con `rsvg-convert` (librsvg).

| Archivo (PDF) | Fuente original (SVG) | Autor / colección | Licencia |
|---|---|---|---|
| `dna.pdf`, `dna-w.pdf` | tabler-icons `dna.svg` | Tabler Icons (Paweł Kuna) | MIT |
| `dna-2.pdf` | tabler-icons `dna-2.svg` | Tabler Icons | MIT |
| `plant.pdf`, `plant-2.pdf` | tabler-icons `plant.svg` / `plant-2.svg` | Tabler Icons | MIT |
| `leaf.pdf` | tabler-icons `leaf.svg` | Tabler Icons | MIT |
| `flask.pdf` | tabler-icons `flask.svg` | Tabler Icons | MIT |
| `flower.pdf` | tabler-icons `flower.svg` | Tabler Icons | MIT |
| `microscope.pdf` | tabler-icons `microscope.svg` | Tabler Icons | MIT |

- **Colección:** Tabler Icons — https://tabler.io/icons — licencia **MIT**
  (uso libre, comercial y educativo; basta conservar el aviso de licencia).
- **SVG originales sin recolorear:** `assets/svg-src/genetica/`.
- **Reconversión:** `sed 's/currentColor/#106E50/g' src.svg | rsvg-convert -f pdf -w 400 -h 400 -o out.pdf`

> Nota editorial: se eligieron iconos de línea (Tabler) en vez de clip-art
> coloreado (p. ej. una arveja de Openclipart) porque encajan con la estética
> plana y minimalista del design system. Cumplen la regla de «reusar recursos
> libres» (licencia MIT). Si en el futuro se quiere una ilustración coloreada de
> arveja/vaina, Openclipart (CC0) y Wikimedia Commons (PD) son buenas fuentes.
