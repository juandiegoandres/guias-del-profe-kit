# Assets · Física 8° — Termodinámica (Eje 1)

Todos los assets son de **licencia libre compatible** (Dominio Público, CC BY, MIT).
**NINGUNO es CC BY-SA.** Verificado vía API de Wikimedia Commons / repos oficiales.

## Retratos de científicos (`assets/imgs/fisica/`)

| Archivo | Personaje | Licencia | Autor / origen | Nota |
|---|---|---|---|---|
| `celsius.jpg` | Anders Celsius (1701–1744) | **Dominio Público** | Óleo de Olof Arenius | Retrato limpio, 923×1050. |
| `fahrenheit.jpg` | D. G. Fahrenheit (1686–1736) | **Dominio Público** | Grabado anónimo de época | *No existe retrato auténtico verificado de Fahrenheit.* Esta es una lámina de época sobre termometría (un hombre midiendo con termómetro sobre un hornillo), la que usa Wikipedia. Úsese como "estampa de época", no como retrato. 580×600. |
| `kelvin.jpg` | William Thomson, Lord Kelvin (1824–1907) | **Dominio Público** | Foto Dickinson (London) | Retrato limpio, 939×1176. |
| `joule.jpg` | James Prescott Joule (1818–1889) | **Dominio Público** | Grabado de C. H. Jeens | Retrato limpio, 338×354 (pequeño; suficiente para columna). |

Fuente de todas: Wikimedia Commons. Verificación de licencia PD por `extmetadata.LicenseShortName = "Public domain"`.

### Pendientes (para Ejes 2 y 3, cuando toque)
Anotados para bajar después (todos serán PD, s. XVII–XIX):
`Sadi Carnot`, `Robert Boyle`, `Jacques Charles`, `Joseph Louis Gay-Lussac`.

## Íconos animables en Manim (`assets/svg-src/fisica/`)

SVG **path-based**, verificados sin `<text>/<image>/<filter>` → importan en `SVGMobject`.

| Archivo | Ícono | Fuente | Licencia | Uso sugerido |
|---|---|---|---|---|
| `tw-termometro.svg` | Termómetro (bulbo rojo) | Twemoji | **CC BY 4.0** | 1.1, 1.2 medición |
| `tw-fuego.svg` | Llama/fuego | Twemoji | **CC BY 4.0** | fuente de calor (1.4, 1.6, 1.7) |
| `tw-olla.svg` | Olla con comida | Twemoji | **CC BY 4.0** | calor específico, convección |
| `tw-sol.svg` | Sol | Twemoji | **CC BY 4.0** | radiación (1.7) |
| `tw-copo-nieve.svg` | Copo de nieve (frío) | Twemoji | **CC BY 4.0** | baja T / azul-frío |
| `tw-cuchara.svg` | Cuchara | Twemoji | **CC BY 4.0** | conducción (1.6) |
| `tw-taza-caliente.svg` | Taza caliente (café) | Twemoji | **CC BY 4.0** | calor vs temperatura (1.3), 2ª ley |
| `tw-hielo.svg` | Cubo de hielo | Twemoji | **CC BY 4.0** | frío / equilibrio térmico |
| `tb-termometro.svg` | Termómetro (línea) | Tabler | **MIT** | alternativa monolínea recolorable |
| `tb-flama.svg` | Llama (línea) | Tabler | **MIT** | alternativa monolínea |
| `tb-sol.svg` | Sol (línea) | Tabler | **MIT** | alternativa monolínea |
| `tb-copo-nieve.svg` | Copo (línea) | Tabler | **MIT** | alternativa monolínea |
| `tb-molecula.svg` | Molécula/átomo | Tabler | **MIT** | partícula base |

**Recolorear Tabler** (usan `currentColor`): `sed 's/currentColor/#106E50/g' in.svg`.
Twemoji ya vienen a todo color (fill), listos para `SVGMobject`.

### Assets compuestos que arma el animador (marcados, no incluidos aquí)
- **Caja de partículas** con velocidad parametrizable por T (usar `tb-molecula.svg` como partícula base o círculos Manim). Reutilizable en 1.1, 3.2 y leyes de gases.
- **Termómetro con columna que sube**: base `tw-termometro.svg` / `tb-termometro.svg` + rectángulo animable de mercurio.
- **Flecha de calor caliente→frío** (un solo sentido): flecha Manim roja→azul entre `tw-fuego`/`tw-taza-caliente` y `tw-hielo`/`tw-copo-nieve`.
- **Anillo + esfera** (dilatación, 1.5): primitivas de Manim (Annulus + Circle), no hay ícono.
</content>
</invoke>

## Añadido para Video 1.1 (Temperatura)

| Archivo | Personaje | Licencia | Autor / origen | Nota |
|---|---|---|---|---|
| `galileo.jpg` | Galileo Galilei (1564–1642) | **Dominio Público** | Óleo de Justus Sustermans, 1636 (Wikimedia Commons) | Retrato clásico. 500×635. PD por antigüedad (autor m. 1681, obra s. XVII). |

---

## Añadido para EJES 2 y 3 (máquinas térmicas + gases ideales)

### Retratos de científicos (`assets/imgs/fisica/`) — todos Dominio Público

| Archivo | Personaje | Licencia | Autor / origen | Nota |
|---|---|---|---|---|
| `boyle.jpg` | Robert Boyle (1627–1691) | **Dominio Público** | Retrato de época (Wikimedia, `Robert_Boyle_0001.jpg`) | Ley de Boyle (3.3). 523×663. PD por antigüedad. |
| `charles.jpg` | Jacques A. C. Charles (1746–1823) | **Dominio Público** | Grabado de época (Wikimedia) | Ley de Charles (3.4); pionero del vuelo en globo (1783). 586×802. |
| `gaylussac.jpg` | Joseph L. Gay-Lussac (1778–1850) | **Dominio Público** | Retrato de época (Wikimedia, `Gaylussac.jpg`) | Ley de Gay-Lussac (3.5). 1876×2335. |
| `carnot.jpg` | Sadi Carnot (1796–1832) | **Dominio Público** | Litografía s. XIX (Wikimedia, `Carnot-2.jpg`), **recortada a busto** | Eficiencia / límite de Carnot (2.6). Original 1696×3257 de cuerpo entero; recortado al 46 % superior (busto). PD por antigüedad. |

Verificación PD por `extmetadata.LicenseShortName = "Public domain"` vía API de Wikimedia Commons.
Científicos citados **sin retrato** (se nombran con ícono en el guion): Torricelli (3.1), Bernoulli (3.2),
Clapeyron (3.7), Rumford (2.1), Mayer/Joule (2.2), Clausius/Kelvin (2.3), Otto (2.4), Perkins (2.5).

### Íconos animables en Manim (`assets/svg-src/fisica/`) — verificados path-based (sin `<text>/<image>/<filter>/<use>`)

| Archivo | Ícono | Fuente | Licencia | Uso sugerido |
|---|---|---|---|---|
| `tw-jeringa.svg` | Jeringa | Twemoji (jdecked) | **CC BY 4.0** | Boyle (3.3), compresión |
| `tb-globo-aerostatico.svg` | Globo aerostático | Tabler | **MIT** | Charles (3.4), globo |
| `tb-motor.svg` | Motor | Tabler | **MIT** | motor de combustión (2.4) |
| `tb-nevera.svg` | Nevera/refrigerador | Tabler | **MIT** | refrigeración (2.5) |
| `tb-manometro.svg` | Manómetro (gauge) | Tabler | **MIT** | presión (3.1, 3.2, 3.5) |
| `tb-aerosol.svg` | Aerosol (spray) | Tabler | **MIT** | Gay-Lussac (3.5) |
| `gi-neumatico.svg` | Neumático/rueda | game-icons (Delapouite) | **CC BY 3.0** | Gay-Lussac (3.5), llantas |
| `fis-piston.svg` | Pistón + cilindro | **Autoría del kit** | **CC0** | 1ª ley (2.2), motor (2.4). Geométrico, recolorable con `currentColor`. |

**NINGÚN asset es CC BY-SA.** Tabler = MIT, Twemoji = CC BY 4.0, game-icons = CC BY 3.0 (atribuir a
Delapouite / game-icons.net), `fis-piston.svg` = CC0 (dominio del kit).

### Assets compuestos que arma el animador (marcados, no incluidos aquí) — Ejes 2 y 3
- **Caja de partículas** (ya en `videotutoriales-ciencias/escenas/fisica_1_1_temperatura.py`) reparametrizada:
  velocidad ↔ T, densidad ↔ V, frecuencia de choques ↔ P. Sirve en 3.1, 3.2, Boyle/Charles/Gay-Lussac.
- **Pistón con Q y flecha de trabajo W**: base `fis-piston.svg` + flecha roja de calor (`tw-fuego`) entrando y
  flecha de W saliendo (1ª ley 2.2, motor 2.4).
- **Motor de 4 tiempos**: `tb-motor.svg`/`fis-piston.svg` + válvulas y bujía como primitivas de Manim; 4 viñetas.
- **Ciclo de la nevera**: `tb-nevera.svg` + serpentines frío (azul) / caliente (rojo) + compresor (2.5).
- **Gráficas de leyes** (P–V hipérbola, V–T recta al cero absoluto, P–T recta): **mate-animador** o `Axes` nativos.
- **Barra de energía** entra vs trabajo útil vs calor perdido (eficiencia 2.6): mate-animador o `Rectangle`s.

## Iconos Font Awesome Free 6 (video 1.1 rev. 2, `videotutoriales-ciencias/assets/svg/fisica/`)

Font Awesome Free — iconos **CC BY 4.0** (https://fontawesome.com/license/free). Path-based, importan en `SVGMobject`.

| Archivo | Icono FA | Licencia | Uso |
|---|---|---|---|
| `fa-termometro.svg` | `temperature-empty` | **CC BY 4.0** | Carcasa moderna del termometro (1.1) + columna mercurio nativa |
| `fa-banera.svg` | `bath` | **CC BY 4.0** | Analogia chispa vs. bañera (1.1 calor vs. temperatura) |
| `fa-copo.svg` | `snowflake` | **CC BY 4.0** | Curiosidad del agua/hielo (1.1 cierre) |
| `fa-botella.svg` | `bottle-water` | **CC BY 4.0** | Gaseosas nevera / equilibrio termico (1.1) |
