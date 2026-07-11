# Notas de animación — Curiosidades: la química en la vida real (Química 9º)

Guion de **personaje + prop + fondo** por lámina, para que **ciencias-animador**
monte el video activo y fluido (Manim). Assets: ver `CREDITOS_curiosidades.md`.
Todos los `robot_*`, `cur_*`, `nuc_*`, `esc_*`, `bg_*`, `prop_*` están como SVG
(svg-src) y PDF (assets/imgs/quimica).

## El personaje: ROBOT CIENTÍFICO adaptable 🤖 (5 expresiones)

`robot_*` = mismo robot (DiceBear *bottts*, arte de Pablo Stanley) verde, con
**cara-pantalla que CAMBIA por escena**. Es un personaje **adaptable**: la misma
carrocería, distinta cara. Ya vienen **5 expresiones** listas:

| pose (`robot_…`) | cara (eyes/mouth) | cuándo usarla |
|---|---|---|
| `explica`     | ojos redondos + media sonrisa | narración normal, presentar |
| `senala`      | visor con dos puntos (atento)  | apuntar / dirigir la atención |
| `sorprendido` | ojos saltones + boca abierta   | dato asombroso (hierro, fisión) |
| `celebra`     | ojos felices + gran sonrisa    | cierres, logros |
| `sostiene`    | visor + boca-onda (techy)      | mostrar un aparato (batería, celular) |

**Variar aún más:** mismo `seed=Zap-lab-9` + `baseColor=7cb342`, cambiando
`eyes=` y `mouth=` en la API de DiceBear bottts (ver créditos) → nuevas
expresiones sin cambiar de robot. No tiene brazos → los props se colocan **al
lado** (el robot los "mira") y el animador los une si quiere.

### Kit de micro-animaciones del robot (reutilizar siempre)
- **Respira / idle:** escala 1.00↔1.02 en loop lento (nunca queda 100% quieto).
- **Cambio de cara:** transición entre `robot_*` por escena (crossfade rápido de la
  pantalla-cara) = el robot "reacciona".
- **Rebote (bob):** salto corto al aparecer o al enfatizar (squash&stretch suave).
- **Parpadeo / escaneo:** parpadeo de los ojos-LED o barrido de luz en el visor.
- **Antena:** menear la antena/cuernos al hablar; chispa en la antena al sorprenderse.
- **Mirar el objeto:** girar levemente hacia el prop que entra (dirige la atención).
- **Props "al lado":** ancla el prop junto al robot y hazlo entrar en arco (no
  aparición seca); el robot lo mira / lo señala con la pantalla.

## Puesta en escena por lámina (deck de 22 láminas)

| # | Lámina | Robot (cara) | Prop(s) que entran | Fondo | Micro-animación |
|---|---|---|---|---|---|
| 1 | Portada | asoma abajo-derecha | — | `esc_sol`+`bg_nube` arriba, `esc_colinas` abajo | título *fade+rise*; robot entra rebotando |
| 2 | Intro "no se queda en el lab" | centro-izq, idle | `prop_matraz` entra y sale; gota `cur_agua` | `bg_ciudad` tenue | robot mira el matraz; 4 temas en *stagger* |
| 3 | Sección Curiosidad 1 | mira los iones | `cur_atomo_fis` orbita | esmeralda pleno | átomo gira lento |
| 4 | "El hierro no se decide" | `sorprendido` (!) | chips Fe²⁺/Fe³⁺ que alternan | — | los chips 2+/3+ *parpadean* alternando; robot mira dudoso |
| 5 | Tabla fijo/multivalente | mini, esquina, idle | — | — | filas entran una a una; resaltar transición |
| 6 | Idea "hierro (II)/(III)" | fuera o pequeño | — | filete esmeralda | "(II)"/"(III)" hace *pop* |
| 7 | Sección Curiosidad 2 | idle | `cur_corazon` late | esmeralda pleno | corazón late |
| 8 | "Eres química con patas" | mira la lista | `cur_corazon` (late), `cur_energia` (chispa) | — | Na⁺/K⁺ viajan por una "neurona"; Ca²⁺ hace latir el corazón |
| 9 | Bebidas deportivas | + **bebida al lado** | `cur_bebida`, `cur_agua` (sudor) | `bg_sol` cálido | gotas de sudor caen; la bebida "rellena" iones |
| 10 | La batería del celular | + **batería al lado** | `cur_bateria`, `cur_celular` | — | iones Li⁺ (puntos) van y vuelven en la batería |
| 11 | **¿Cómo funciona una batería?** | señala el diagrama | diagrama de celda (ya en el PDF) | — | **animar el flujo:** iones⁺ migran por el electrolito → a la vez `e⁻` recorren el cable → el bombillo se enciende. Química→eléctrica con *morph* de etiqueta |
| 12 | **Recargable vs desechable** | idle, mira ambos lados | flecha "1 sentido" ✗ vs flecha circular ↻ | dividir pantalla | desechable: reacción avanza y se detiene (barra que se vacía). Recargable: flecha que **se invierte** al cargar |
| 13 | **Watts vs mAh** | idle | rayo/`cur_enchufe` (W rápido) · `cur_powerbank` (mAh) | — | W: rayo veloz llenando rápido. mAh: barra grande que dura; contraste velocidad vs tamaño |
| 14 | **Guardar energía lo cambió todo** | **celebra** (rebote alegre) | `cur_celular`, `cur_carro`, `cur_solar`, `cur_powerbank` | `bg_ciudad`+`esc_sol` | los 4 props desfilan; el sol "carga" el power bank; robot celebra (rebote) |
| 15 | Sección Curiosidad 3 | idle | `cur_sal` (salero) | esmeralda pleno | granos de sal caen |
| 16 | "Iones que usas sin saber" | mira cada ítem | `cur_sal`, `cur_pasta`, `cur_agua` (por ítem) | cocina/baño tenue | cada ítem revela su prop en *stagger* |
| 17 | Sección Curiosidad 4 | `sorprendido` | `nuc_atomo` (órbitas) | `esc_montanas`+`esc_sol` | átomo con órbitas gira; entra NÚCLEO |
| 18 | Idea "energía del NÚCLEO" | fuera o pequeño | `nuc_radiactivo` tenue | filete esmeralda | electrones se atenúan, núcleo brilla |
| 19 | Fisión (uranio-235) | `sorprendido` (!) | diagrama de fisión (ya en el PDF) | oscurecer un poco | **clímax:** 1 neutrón golpea → núcleo se **parte** → salen 2-3 neutrones → golpean otros → **efecto dominó** (reacción en cadena). Invertir tiempo aquí |
| 20 | "Del átomo al enchufe" | señala la central | `nuc_planta` (torre+vapor), `cur_energia` | `esc_colinas`+`bg_nube`+`esc_sol` | calor→vapor sube→turbina gira→rayo sale al enchufe |
| 21 | Lo bueno y lo malo | idle, mira la balanza | ✔ `cur_energia` · ✘ `nuc_residuos` (barril) | dividir pantalla | balanza: energía vs barril de residuos |
| 22 | En resumen (cierre) | **celebra** (rebote) | mini-desfile: `cur_agua`,`cur_bateria`,`cur_pasta`,`nuc_planta` | `esc_sol`+`bg_ciudad` | los props desfilan en fila; robot celebra; CTA |

## Reglas de oro para que se vea COOL y fluido
- **El robot nunca queda estático:** siempre respira o parpadea; rebota al enfatizar.
- **Un robot, mil reacciones:** cambia la cara por escena; la variedad viene del **prop que entra** y de **hacia
  dónde mira** el robot, no de cambiar de personaje.
- **Continuidad de color:** cada curiosidad usa un acento suave distinto sobre el
  esmeralda base (C1 ámbar, C2 azul-eléctrico para baterías / rojo-coral para el
  corazón, C3 azul agua, C4 gris-radiactivo). Esmeralda = identidad.
- **Baterías (C2):** el momento estrella es el **diagrama de celda animado** (lámina
  11): que se vea el ida-y-vuelta iones/electrones. Y el **contraste W vs mAh**
  (lámina 13): velocidad de llenado vs tamaño del depósito.
- **Fisión (lámina 19) = clímax visual:** dedícale tiempo al dominó de la reacción.
- **`esc_*` (siluetas) al fondo, tras el robot; `bg_*` (línea) para detalles** (sol,
  nubes) sin recargar.

---

## Gags / accesorios temáticos por escena (`gag_*`)

Cada curiosidad le pone al **personaje** (funciona igual con el robot o con la
lorelei humana de **pelo azul + gafas**) un **accesorio/gag** que hace un chiste
**alusivo por juego de palabras o guiño de ciencia** — tasteful, nada ofensivo ni
estereotipos. **Colocación:**

- **«sobre la cabeza»** = anclar el gag encima (del casco/pelo azul), un pelín más
  ancho que la cabeza; entra con **rebote** y se queda con **idle** suave. En la
  lorelei va **por encima del pelo**, sin tapar las gafas.
- **«al lado»** = entra en **arco** junto al personaje; el personaje lo **mira /
  señala** (dirige la atención). Los `?` **flotan** a los lados de la cabeza.

| Escena (lámina) | Gag(s) | Colocación | El chiste (entre líneas) |
|---|---|---|---|
| **4 · «El hierro no se decide»** (Fe²⁺/Fe³⁺) | `gag_casco_hierro` + 2×`gag_interrogacion` | casco **sobre la cabeza**; los `?` **flotan** a izq/der de la cabeza | Casco de caballero = **hierro** (Fe). El personaje se **encoge de hombros** entre los `?`: ¿2+ o 3+? *No se decide.* Sincroniza con la cara `sorprendido`/dudosa y con los chips 2+/3+ que parpadean alternando. |
| **9 · Bebidas deportivas** (electrolitos/sudor) | `gag_vincha` + `gag_munequera` + `cur_agua` (sudor) + `cur_bebida` | vincha **sobre la frente**; muñequera **al lado** (a la altura de la mano); gota de sudor cae de la sien; bebida entra **al lado** | Look de **deportista**: suda → pierde iones (Na⁺/K⁺) → la **bebida** los repone. La gota `cur_agua` cae y la bebida «rellena» los iones. |
| **10 · La batería del celular** (y 13-14, baterías) | `gag_conejo_pila` + `cur_energia` (rayo) | conejo **al lado**, saltando en arco; rayo sobre el conejo | Guiño al **conejito de las pilas** («sigue, y sigue…»): energía que no para. Acompaña al ida-y-vuelta de Li⁺ en la batería. |
| **15-16 · Sal / iones que usas sin saber** (cocina) | `gag_gorro_chef` + `cur_sal` (salero) | gorro de chef **sobre la cabeza**; salero **al lado** | Modo **cocinero**: la sal de mesa es **NaCl** (+ el yodo del salero yodado). El salero cae granos en *stagger* con cada ítem. |
| **16 · …y el baño** (flúor) | `gag_cepillo` | cepillo **al lado**, cerca de la boca | El **flúor** de la pasta: el cepillo (con pasta verde) entra por un lado, guiño «lávate los dientes con química». |
| **17-20 · Energía nuclear** (el chiste de «turbina») | `gag_gorro_helice` + `nuc_radiactivo` | hélice **sobre la cabeza**, **girando** como turbina; símbolo radiactivo tenue al lado | **Gorro de hélice** = la **TURBINA** que gira (chiste limpio, sin turbantes ni temas culturales). Clímax en lámina **20** «del átomo al enchufe»: calor→vapor→la hélice **gira** justo cuando gira la turbina real. |

### Reglas del gag (para que no distraiga)
- **Uno por escena** (o el par que forma un look, p. ej. vincha+muñequera). El gag
  **entra, hace la gracia y sale**; no compite con el contenido.
- **Recolorables:** los `gag_*` van en **currentColor** (Tabler/originales) o `#fff`
  (game-icons); recolóralos al acento de la curiosidad como el resto de props.
- **Sobre la cabeza:** deja respirar las **gafas** de la lorelei; el gag va por
  **encima del pelo azul**, nunca tapa la cara.
- **El de hélice gira**, el conejo **salta**, la vincha **rebota** con la cabeza:
  el gag hereda la micro-animación de su escena.
