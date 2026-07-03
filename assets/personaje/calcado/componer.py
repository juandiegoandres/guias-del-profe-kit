#!/usr/bin/env python3
"""
Compone variantes de profesión, stickers meme y emojis sobre el arte calcado.

Toma svg/dr-cuack-base.svg (calcado de Nanobanana, viewBox 1024) y le
superpone accesorios vectoriales dibujados en el mismo estilo plano
(contorno navy #0B1838, colores planos del design system del kit).

Uso:  python3 componer.py          # regenera svg/ (variantes), stickers/, emoji/ y demo.html
"""
import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
from export_png import render  # noqa: E402


def leer_duck_static(variant):
    """Contenido de <g id="duck"> del calco, sin ids (para reutilizar varias veces
    en un mismo SVG sin colisiones)."""
    src = open(os.path.join(HERE, "svg", f"dr-cuack-{variant}.svg")).read()
    i = src.index('<g id="duck">')
    return re.sub(r'\sid="[^"]*"', "", src[i:src.rindex("</svg>")])


# Transform que lleva la cabeza REAL del calco (ojos en ~388.5/634.5,362.5 del
# viewBox 1024) a coincidir con las posiciones de ojo usadas por los overlays
# de emoji (170/342, 246 en el lienzo ~512).
REAL_HEAD_SCALE = 0.6992
REAL_HEAD_TX = -101.6
REAL_HEAD_TY = -7.5


def real_head():
    """Recorte de la cabeza real (calcada) del pato, encuadrada como una cara
    de emoji. Se usa como base de todos los emojis en vez de redibujarla."""
    duck = leer_duck_static("base")
    return (f'<clipPath id="emojiFaceClip"><ellipse cx="256" cy="222" rx="232" ry="178"/></clipPath>'
            f'<g clip-path="url(#emojiFaceClip)">'
            f'<g transform="translate({REAL_HEAD_TX} {REAL_HEAD_TY}) scale({REAL_HEAD_SCALE})">{duck}</g>'
            f'</g>')

NAVY   = "#0B1838"
YELLOW = "#FBD213"
CREMA  = "#FBE993"
ORANGE = "#FB7A12"
ORANGED= "#E9860D"
BOCA   = "#D8502E"
MAT    = "#1E4078"   # azul profundo (design system)
MATD   = "#152E58"
CNAT   = "#17A673"   # esmeralda viva
CSOC   = "#A54B2D"   # terracota
AMBAR  = "#E8930A"   # ámbar
AMBARD = "#C97C06"
ECO    = "#463782"   # índigo
ECOD   = "#392C6B"
GRIS   = "#2B3440"
COAT   = "#F4F7FA"
CELESTE= "#7EC8F7"

SW = 13  # grosor de contorno a escala 1024


def g(inner, **attrs):
    a = " ".join(f'{k.replace("_","-")}="{v}"' for k, v in attrs.items())
    return f"<g {a}>{inner}</g>"


# ------------------------------------------------------------------ accesorios

GAFAS_NERD = f"""
  <g id="gafas-nerd">
    <rect x="316" y="300" width="150" height="126" rx="32" fill="#BFE3F4" fill-opacity="0.25"/>
    <rect x="558" y="300" width="150" height="126" rx="32" fill="#BFE3F4" fill-opacity="0.25"/>
    <rect x="316" y="300" width="150" height="126" rx="32" fill="none" stroke="{NAVY}" stroke-width="26"/>
    <rect x="558" y="300" width="150" height="126" rx="32" fill="none" stroke="{NAVY}" stroke-width="26"/>
    <rect x="458" y="342" width="110" height="26" rx="13" fill="{NAVY}"/>
    <path d="M 310 356 L 272 346 M 714 356 L 752 346" stroke="{NAVY}" stroke-width="24" stroke-linecap="round"/>
    <path d="M 352 344 L 384 324 M 594 344 L 626 324" stroke="#FFFFFF" stroke-width="12"
          stroke-linecap="round" opacity="0.6"/>
  </g>
"""

GAFAS_SOL = f"""
  <g id="gafas-sol">
    <rect x="306" y="296" width="164" height="126" rx="34" fill="#101820" stroke="{NAVY}" stroke-width="{SW}"/>
    <rect x="554" y="296" width="164" height="126" rx="34" fill="#101820" stroke="{NAVY}" stroke-width="{SW}"/>
    <rect x="462" y="338" width="100" height="26" rx="13" fill="{NAVY}"/>
    <path d="M 308 352 L 270 342 M 716 352 L 754 342" stroke="{NAVY}" stroke-width="24" stroke-linecap="round"/>
    <path d="M 346 344 L 382 320 M 594 344 L 630 320" stroke="#5C6B7E" stroke-width="13"
          stroke-linecap="round" opacity="0.9"/>
  </g>
"""

def panel_izq(fill, extra=""):
    return f"""
    <path d="M 500 590 C 442 586 386 576 352 562 C 294 646 272 772 296 872
             C 356 902 456 910 502 902 C 484 792 484 682 500 590 Z"
          fill="{fill}" stroke="{NAVY}" stroke-width="{SW}"/>{extra}"""

def panel_der(fill, extra=""):
    return f"""
    <path d="M 524 590 C 582 586 638 576 672 562 C 730 646 752 772 728 872
             C 668 902 568 910 522 902 C 540 792 540 682 524 590 Z"
          fill="{fill}" stroke="{NAVY}" stroke-width="{SW}"/>{extra}"""

def solapas(fill):
    return f"""
    <path d="M 500 588 L 418 570 L 478 664 Z" fill="{fill}" stroke="{NAVY}" stroke-width="{SW}" stroke-linejoin="round"/>
    <path d="M 524 588 L 606 570 L 546 664 Z" fill="{fill}" stroke="{NAVY}" stroke-width="{SW}" stroke-linejoin="round"/>"""

BATA = panel_izq(COAT) + panel_der(COAT) + solapas(COAT)

BOLSILLO = f"""
    <rect x="338" y="740" width="76" height="62" rx="10" fill="#FFFFFF" stroke="{NAVY}" stroke-width="{SW}"/>
    <rect x="352" y="712" width="16" height="40" rx="6" fill="{MAT}" stroke="{NAVY}" stroke-width="7"/>
    <rect x="376" y="716" width="16" height="36" rx="6" fill="{CSOC}" stroke="{NAVY}" stroke-width="7"/>"""

MATRAZ = f"""
  <style>
    .bubble {{ transform-box: fill-box; transform-origin: 50% 50%;
      animation: bubbleRise 2.4s ease-in infinite; }}
    .bubble.b2 {{ animation-delay: .8s; }}
    .bubble.b3 {{ animation-delay: 1.6s; }}
    @keyframes bubbleRise {{ 0% {{ transform: translateY(0) scale(1); opacity: 0; }}
      20% {{ opacity: .95; }} 100% {{ transform: translateY(-46px) scale(.7); opacity: 0; }} }}
    @media (prefers-reduced-motion: reduce) {{ .bubble {{ animation: none; opacity: .8; }} }}
  </style>
  <g id="matraz">
    <path d="M 802 556 L 802 612 L 756 696 Q 746 714 766 714 L 890 714 Q 910 714 900 696
             L 854 612 L 854 556 Z" fill="#C9E8F4" fill-opacity="0.55" stroke="{NAVY}" stroke-width="{SW}"
          stroke-linejoin="round"/>
    <path d="M 774 664 L 756 696 Q 746 714 766 714 L 890 714 Q 910 714 900 696 L 882 664 Z"
          fill="{CNAT}" stroke="{NAVY}" stroke-width="{SW}" stroke-linejoin="round"/>
    <rect x="790" y="540" width="76" height="24" rx="12" fill="#9DBAD0" stroke="{NAVY}" stroke-width="{SW}"/>
    <circle class="bubble b1" cx="800" cy="690" r="9" fill="#BFF3DE"/>
    <circle class="bubble b2" cx="836" cy="698" r="7" fill="#BFF3DE"/>
    <circle class="bubble b3" cx="862" cy="688" r="8" fill="#BFF3DE"/>
  </g>
"""

PIZARRA = f"""
  <g id="pizarra" transform="rotate(-6 260 700)">
    <rect x="136" y="596" width="252" height="192" rx="14" fill="#6D4A2A" stroke="{NAVY}" stroke-width="{SW}"/>
    <rect x="158" y="618" width="208" height="148" rx="8" fill="#2F5147" stroke="{NAVY}" stroke-width="8"/>
    <text x="262" y="682" text-anchor="middle" font-family="'Comic Sans MS','Segoe Print','DejaVu Sans',sans-serif"
          font-size="38" fill="#F4F8F2">a²+b²=c²</text>
    <text x="216" y="742" text-anchor="middle" font-family="'Comic Sans MS','Segoe Print','DejaVu Sans',sans-serif"
          font-size="40" fill="#F4F8F2">π</text>
    <text x="308" y="744" text-anchor="middle" font-family="'Comic Sans MS','Segoe Print','DejaVu Sans',sans-serif"
          font-size="32" fill="#F4F8F2" opacity=".85">∞</text>
  </g>
"""

TIZA = f"""
    <rect x="776" y="616" width="26" height="72" rx="12" fill="#FDFDF8" stroke="{NAVY}"
          stroke-width="11" transform="rotate(34 789 652)"/>"""

SIMBOLOS = f"""
  <g id="simbolos" font-family="Georgia,'DejaVu Serif',serif" font-weight="bold" fill="{MAT}">
    <text x="140" y="230" font-size="72" opacity=".75">π</text>
    <text x="856" y="280" font-size="60" opacity=".65">∑</text>
    <text x="836" y="140" font-size="54" opacity=".6">∞</text>
  </g>
"""

BIRRETE = f"""
  <g id="birrete">
    <path d="M 396 214 C 420 192 604 192 628 214 L 628 268 C 560 246 464 246 396 268 Z"
          fill="{MATD}" stroke="{NAVY}" stroke-width="{SW}"/>
    <path d="M 512 58 L 784 142 L 512 226 L 240 142 Z" fill="{MAT}" stroke="{NAVY}"
          stroke-width="{SW}" stroke-linejoin="round"/>
    <path d="M 240 142 L 512 226 L 512 252 L 240 168 Z" fill="{MATD}" stroke="{NAVY}"
          stroke-width="{SW}" stroke-linejoin="round"/>
    <path d="M 784 142 L 512 226 L 512 252 L 784 168 Z" fill="#12294D" stroke="{NAVY}"
          stroke-width="{SW}" stroke-linejoin="round"/>
    <circle cx="512" cy="142" r="12" fill="#EAB93D" stroke="{NAVY}" stroke-width="8"/>
    <path d="M 512 142 C 600 136 690 146 724 162 L 724 238" fill="none" stroke="#EAB93D" stroke-width="11"/>
    <path d="M 706 234 C 706 222 742 222 742 234 L 736 278 C 733 290 715 290 712 278 Z"
          fill="#EAB93D" stroke="{NAVY}" stroke-width="9"/>
  </g>
"""

LIBRO = f"""
  <g id="libro">
    <path d="M 368 690 C 418 658 480 652 512 668 C 544 652 606 658 656 690
             L 656 796 C 606 766 544 764 512 780 C 480 764 418 766 368 796 Z"
          fill="{CSOC}" stroke="{NAVY}" stroke-width="{SW}" stroke-linejoin="round"/>
    <path d="M 382 694 C 424 668 478 664 506 678 L 506 764 C 478 754 424 758 382 780 Z" fill="#FDFBF4"/>
    <path d="M 642 694 C 600 668 546 664 518 678 L 518 764 C 546 754 600 758 642 780 Z" fill="#FDFBF4"/>
    <path d="M 398 700 C 428 684 462 680 490 688 M 398 716 C 428 700 462 696 490 704
             M 398 732 C 428 716 462 712 490 720" stroke="#C9C2B4" stroke-width="7" fill="none"/>
    <path d="M 626 700 C 596 684 562 680 534 688 M 626 716 C 596 700 562 696 534 704
             M 626 732 C 596 716 562 712 534 720" stroke="#C9C2B4" stroke-width="7" fill="none"/>
    <path d="M 512 668 L 512 780" stroke="{NAVY}" stroke-width="9"/>
  </g>
"""

CASCO = f"""
  <g id="casco">
    <path d="M 330 212 C 336 92 688 92 694 212 L 696 222 C 580 194 444 194 328 222 Z"
          fill="{AMBAR}" stroke="{NAVY}" stroke-width="{SW}" stroke-linejoin="round"/>
    <path d="M 468 108 C 482 100 542 100 556 108 L 552 152 L 472 152 Z" fill="{AMBARD}"
          stroke="{NAVY}" stroke-width="10" stroke-linejoin="round"/>
    <path d="M 296 224 C 420 192 604 192 728 224 C 750 230 744 258 718 252
             C 600 224 424 224 306 252 C 280 258 274 230 296 224 Z"
          fill="{AMBARD}" stroke="{NAVY}" stroke-width="{SW}" stroke-linejoin="round"/>
  </g>
"""

def franja(x):
    return f"""
    <path d="M {x} 600 C {x-6} 690 {x-6} 790 {x} 884" stroke="#CFD8DC" stroke-width="34" fill="none"/>
    <path d="M {x} 600 C {x-6} 690 {x-6} 790 {x} 884" stroke="#9FB2BC" stroke-width="8" fill="none" opacity=".6"/>"""

CHALECO_ING = (panel_izq(AMBAR, franja(370)) + panel_der(AMBAR, franja(654)) + solapas(AMBAR))

ESTETO = f"""
  <g id="estetoscopio" fill="none" stroke="{NAVY}" stroke-width="16" stroke-linecap="round">
    <path d="M 436 600 C 446 678 474 728 512 744"/>
    <path d="M 588 600 C 578 678 550 728 512 744"/>
    <path d="M 512 744 C 524 766 544 782 560 790"/>
    <circle cx="576" cy="806" r="28" fill="#8FA6B8" stroke-width="{SW}"/>
    <circle cx="576" cy="806" r="11" fill="#CFD8DC" stroke="none"/>
  </g>
  <g id="cruz">
    <rect x="344" y="688" width="66" height="66" rx="10" fill="#FFFFFF" stroke="{NAVY}" stroke-width="{SW}"/>
    <path d="M 368 704 h 18 v 16 h 16 v 18 h -16 v 16 h -18 v -16 h -16 v -18 h 16 Z" fill="#D64545"/>
  </g>
"""

HOODIE = (panel_izq(ECO) + panel_der(ECO) + f"""
    <path d="M 472 596 C 468 640 470 668 478 694 M 552 596 C 556 640 554 668 546 694"
          stroke="#CBC3EC" stroke-width="11" fill="none" stroke-linecap="round"/>
    <rect x="466" y="688" width="18" height="22" rx="6" fill="#CBC3EC"/>
    <rect x="540" y="688" width="18" height="22" rx="6" fill="#CBC3EC"/>""")

AUDIFONOS = f"""
  <g id="audifonos">
    <path d="M 314 320 C 322 124 702 124 710 320" fill="none" stroke="{NAVY}" stroke-width="34"/>
    <path d="M 314 320 C 322 124 702 124 710 320" fill="none" stroke="#455A64" stroke-width="16"/>
    <rect x="258" y="292" width="74" height="152" rx="36" fill="#16325F" stroke="{NAVY}" stroke-width="{SW}"/>
    <rect x="692" y="292" width="74" height="152" rx="36" fill="#16325F" stroke="{NAVY}" stroke-width="{SW}"/>
    <rect x="276" y="312" width="38" height="112" rx="19" fill="#455A64"/>
    <rect x="710" y="312" width="38" height="112" rx="19" fill="#455A64"/>
  </g>
"""

LAPTOP = f"""
  <g id="laptop">
    <rect x="366" y="638" width="292" height="186" rx="18" fill="#26323C" stroke="{NAVY}" stroke-width="{SW}"/>
    <text x="512" y="752" text-anchor="middle" font-family="Consolas,'DejaVu Sans Mono',monospace"
          font-size="64" font-weight="bold" fill="#8BE9A8">&lt;/&gt;</text>
    <path d="M 348 824 L 676 824 L 700 868 Q 706 882 686 882 L 338 882 Q 318 882 324 868 Z"
          fill="#455A64" stroke="{NAVY}" stroke-width="{SW}" stroke-linejoin="round"/>
  </g>
"""

CAMISA_V = f"""
    <path d="M 512 585 L 428 570 C 468 652 490 722 512 748 C 534 722 556 652 596 570 Z"
          fill="#FFFFFF" stroke="{NAVY}" stroke-width="{SW}" stroke-linejoin="round"/>
    <path d="M 486 598 L 538 598 L 526 642 L 498 642 Z" fill="{CSOC}" stroke="{NAVY}" stroke-width="11" stroke-linejoin="round"/>
    <path d="M 498 642 L 526 642 L 548 768 L 512 812 L 476 768 Z" fill="{CSOC}" stroke="{NAVY}" stroke-width="11" stroke-linejoin="round"/>"""

def pinstripes(xs):
    return "".join(f"""
    <path d="M {x} 604 C {x-8} 700 {x-8} 796 {x} 880" stroke="#7C8794" stroke-width="5" fill="none" opacity=".65"/>"""
                   for x in xs)

TRAJE = (panel_izq(GRIS, pinstripes((330, 380, 430))) +
         panel_der(GRIS, pinstripes((594, 644, 694))) + CAMISA_V + solapas(GRIS))

FEDORA = f"""
  <g id="fedora">
    <path d="M 270 202 C 300 160 380 142 512 142 C 644 142 724 160 754 202
             C 774 220 760 246 728 238 C 610 206 414 206 296 238 C 264 246 250 220 270 202 Z"
          fill="#23303E" stroke="{NAVY}" stroke-width="{SW}" stroke-linejoin="round"/>
    <path d="M 352 178 C 352 70 402 42 512 42 C 622 42 672 70 672 178
             C 608 150 416 150 352 178 Z" fill="#2B3949" stroke="{NAVY}" stroke-width="{SW}"/>
    <path d="M 512 46 C 500 76 500 118 510 148" fill="none" stroke="{NAVY}" stroke-width="9" opacity=".6"/>
    <path d="M 352 178 C 416 148 608 148 672 178 L 672 218 C 608 186 416 186 352 218 Z"
          fill="{CSOC}" stroke="{NAVY}" stroke-width="{SW}"/>
  </g>
"""

PALILLO = f"""
    <path d="M 606 502 L 684 478" stroke="#EFE2C0" stroke-width="13" stroke-linecap="round"/>"""

MILLOS = "#2447A0"
MILLOSD = "#1A3578"

CAMISETA_MILLOS = f"""
  <g id="camiseta">
    <path d="M 512 588 C 448 584 390 574 352 562 C 294 646 272 772 296 872
             C 380 906 644 906 728 872 C 752 772 730 646 672 562
             C 634 574 576 584 512 588 Z" fill="{MILLOS}" stroke="{NAVY}" stroke-width="{SW}"/>
    <path d="M 342 596 C 320 668 312 762 322 848 M 682 596 C 704 668 712 762 702 848"
          stroke="#FFFFFF" stroke-width="16" fill="none" opacity=".9"/>
    <path d="M 512 588 L 446 570 C 468 612 488 630 512 640 C 536 630 556 612 578 570 Z"
          fill="#FFFFFF" stroke="{NAVY}" stroke-width="{SW}" stroke-linejoin="round"/>
    <path transform="translate(392 668) scale(1.15)" fill="#FFFFFF" stroke="{NAVY}" stroke-width="7"
          d="M 0 -22 L 6 -7 L 22 -7 L 9 3 L 14 19 L 0 9 L -14 19 L -9 3 L -22 -7 L -6 -7 Z"/>
    <text x="580" y="810" text-anchor="middle" font-family="'Arial Black','DejaVu Sans',sans-serif"
          font-weight="900" font-size="110" fill="#FFFFFF" stroke="{NAVY}" stroke-width="8"
          paint-order="stroke">10</text>
  </g>
"""

BIGOTE_BARBA = f"""
  <g id="barba">
    <path d="M 360 468 C 366 566 430 618 512 618 C 594 618 658 566 664 468
             C 654 540 600 574 512 574 C 424 574 370 540 360 468 Z"
          fill="#5F452F" stroke="{NAVY}" stroke-width="11" stroke-linejoin="round"/>
    <path d="M 448 594 C 452 584 462 580 470 584 M 540 588 C 548 582 558 584 562 592"
          stroke="{NAVY}" stroke-width="6" fill="none" opacity=".5"/>
    <path d="M 512 414 C 486 390 444 390 420 410 C 406 424 414 442 434 440
             C 462 436 488 428 512 426 C 536 428 562 436 590 440
             C 610 442 618 424 604 410 C 580 390 538 390 512 414 Z"
          fill="#5F452F" stroke="{NAVY}" stroke-width="11" stroke-linejoin="round"/>
  </g>
"""

BALON = f"""
  <g id="balon">
    <circle cx="790" cy="858" r="64" fill="#FFFFFF" stroke="{NAVY}" stroke-width="{SW}"/>
    <path d="M 790 828 L 816 848 L 806 878 L 774 878 L 764 848 Z" fill="{NAVY}"/>
    <path d="M 790 828 L 790 800 M 816 848 L 844 840 M 806 878 L 822 902 M 774 878 L 758 902
             M 764 848 L 736 840" stroke="{NAVY}" stroke-width="9"/>
  </g>
"""

# ------------------------------------------------------------------ variantes

V = {
    "base":        [],
    "cientifico":  [BATA, BOLSILLO, GAFAS_NERD, MATRAZ],
    "matematico":  [GAFAS_NERD, PIZARRA, TIZA, SIMBOLOS],
    "profesor":    [BIRRETE, LIBRO],
    "ingeniero":   [CHALECO_ING, CASCO],
    "medico":      [BATA, ESTETO],
    "programador": [HOODIE, GAFAS_NERD, AUDIFONOS, LAPTOP],
    "ganster":     [TRAJE, FEDORA, GAFAS_SOL, PALILLO],
    "millos":      [CAMISETA_MILLOS, BIGOTE_BARBA, BALON],
}

# ------------------------------------------------------------------ stickers

FLAMES = f"""
  <g id="llamas">
    <path d="M 192 868 C 124 800 136 696 196 636 C 184 704 220 712 212 660
             C 252 700 256 784 224 832 C 236 820 252 804 256 784
             C 272 832 244 884 192 868 Z" fill="#F57C00" stroke="{NAVY}" stroke-width="11" stroke-linejoin="round"/>
    <path d="M 196 848 C 164 812 168 752 196 716 C 192 752 216 760 212 728
             C 232 756 232 804 212 832 Z" fill="#FFC107"/>
    <path d="M 832 868 C 900 800 888 696 828 636 C 840 704 804 712 812 660
             C 772 700 768 784 800 832 C 788 820 772 804 768 784
             C 752 832 780 884 832 868 Z" fill="#F57C00" stroke="{NAVY}" stroke-width="11" stroke-linejoin="round"/>
    <path d="M 828 848 C 860 812 856 752 828 716 C 832 752 808 760 812 728
             C 792 756 792 804 812 832 Z" fill="#FFC107"/>
  </g>
"""

SWEAT = f"""
    <path d="M 732 176 C 752 212 768 240 768 264 A 32 32 0 1 1 704 264
             C 704 240 716 212 732 176 Z" fill="{CELESTE}" stroke="{NAVY}" stroke-width="11"/>"""

def spark(x, y, s=1.0):
    return (f'<path transform="translate({x} {y}) scale({s})" fill="#FFD54F" stroke="{NAVY}" stroke-width="6" '
            f'd="M 0 -30 L 8 -8 L 30 0 L 8 8 L 0 30 L -8 8 L -30 0 L -8 -8 Z"/>')

SPARKLES = "<g>" + spark(170, 240) + spark(250, 130, .65) + spark(846, 200, 1.05) + spark(880, 320, .55) + "</g>"

TAP_TEMPLE = f"""
  <g id="tap-temple">
    <path d="M 660 470 C 700 420 738 366 748 320 C 752 300 736 288 722 300
             C 700 320 674 372 654 424 Z" fill="{YELLOW}" stroke="{NAVY}" stroke-width="{SW}"
          stroke-linejoin="round"/>
    <ellipse cx="742" cy="308" rx="34" ry="30" fill="{YELLOW}" stroke="{NAVY}" stroke-width="{SW}"/>
    <path d="M 730 296 L 738 282 M 744 292 L 750 276 M 756 300 L 766 288"
          stroke="{NAVY}" stroke-width="7" stroke-linecap="round" opacity=".55"/>
  </g>
"""

FIST_RAISED = f"""
  <g id="fist-raised">
    <path d="M 652 420 C 676 366 700 300 716 250" stroke="{YELLOW}" stroke-width="72"
          stroke-linecap="round"/>
    <path d="M 652 420 C 676 366 700 300 716 250" stroke="{NAVY}" stroke-width="{SW}"
          fill="none" stroke-linecap="round"/>
    <circle cx="726" cy="212" r="64" fill="{YELLOW}" stroke="{NAVY}" stroke-width="{SW}"/>
    <path d="M 686 186 L 686 152 M 712 176 L 714 138 M 738 178 L 744 142 M 762 190 L 772 158"
          stroke="{NAVY}" stroke-width="9" stroke-linecap="round"/>
    <path d="M 692 224 C 704 232 716 234 728 232 M 700 244 C 712 250 722 250 732 246"
          stroke="{NAVY}" stroke-width="6" fill="none" opacity=".55"/>
    <path d="M 640 150 L 660 176 M 676 116 L 690 148 M 720 100 L 726 134"
          stroke="{NAVY}" stroke-width="7" stroke-linecap="round" opacity=".5"/>
  </g>
"""

ARROW_UP = f"""
  <g id="arrow-up">
    <path d="M 700 900 L 700 480 L 640 480 L 760 320 L 880 480 L 820 480 L 820 900 Z"
          fill="{CNAT}" stroke="{NAVY}" stroke-width="{SW}" stroke-linejoin="round"/>
  </g>
"""

ST = {
    "esto-esta-bien": ("base",        [], ["ESTO ESTÁ BIEN"], FLAMES, ""),
    "confia-en-mi":   ("ingeniero",   ["CONFÍA EN MÍ,"], ["SOY INGENIERO"], "", ""),
    "en-mi-maquina":  ("programador", [], ["FUNCIONA EN", "MI MÁQUINA"], "", SWEAT),
    "aqui-mando-yo":  ("ganster",     [], ["AQUÍ MANDO YO"], "", ""),
    "presiona-f":     ("profesor",    [], ["PRESIONA F"], "", ""),
    "matemagicas":    ("matematico",  [], ["MATEMÁGICAS"], SPARKLES, ""),
    "que-miras-bobo": ("ganster",     [], ["¿QUÉ MIRAS,", "BOBO?"], "", ""),
    "receta-repasar": ("medico",      [], ["RECETA:", "REPASAR"], "", ""),
    "eureka":         ("cientifico",  [], ["¡EUREKA!"], SPARKLES, ""),
    "roll-safe":      ("base",        [], ["SI NO HAY EXAMEN,", "NO TOCA ESTUDIAR"], "", TAP_TEMPLE),
    "success-kid":    ("base",        [], ["ENTREGUÉ LA GUÍA", "A TIEMPO"], "", FIST_RAISED),
    "stonks":         ("ganster",     [], ["NOTAS: STONKS"], ARROW_UP, ""),
}

STICKER_DEFS = f"""
    <filter id="diecut" x="-12%" y="-12%" width="124%" height="124%">
      <feMorphology in="SourceAlpha" operator="dilate" radius="22" result="grow"/>
      <feFlood flood-color="#FFFFFF"/>
      <feComposite in2="grow" operator="in" result="border"/>
      <feMerge><feMergeNode in="border"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <filter id="stickershadow" x="-16%" y="-16%" width="132%" height="132%">
      <feDropShadow dx="0" dy="14" stdDeviation="18" flood-color="#1B2430" flood-opacity="0.35"/>
    </filter>
"""

MEME_CSS = """  <style>
    .meme { font-family: 'Archivo Black','Arial Black','DejaVu Sans',sans-serif;
      font-weight: 900; fill: #FFFFFF; stroke: #1B2430; stroke-width: 18px;
      paint-order: stroke; stroke-linejoin: round; letter-spacing: 1px; text-anchor: middle; }
  </style>
"""


def _fontsize(text, maxw=940, cap=96):
    return max(48, min(cap, int(maxw / (0.68 * max(1, len(text))))))


def leer_duck(variant):
    src = open(os.path.join(HERE, "svg", f"dr-cuack-{variant}.svg")).read()
    i = src.index('<g id="duck">')
    return src[i:src.rindex("</svg>")]


def build_variant(name):
    base = open(os.path.join(HERE, "svg", "dr-cuack-base.svg")).read()
    if name == "base":
        return os.path.join(HERE, "svg", "dr-cuack-base.svg")
    extras = "\n".join(V[name])
    s = base.replace("dr-cuack-base (calcado)", f"dr-cuack-{name} (calcado)")
    s = s.replace("  </g>\n</svg>", extras + "\n  </g>\n</svg>")
    out = os.path.join(HERE, "svg", f"dr-cuack-{name}.svg")
    with open(out, "w") as f:
        f.write(s)
    return out


def build_sticker(name):
    variant, top, bottom, behind, front = ST[name]
    duck = leer_duck(variant)
    scale = 0.72 if (top and len(bottom) > 1) else (0.74 if (top or len(bottom) > 1) else 0.78)
    dy = 100 if top else 20
    tx = 1024 * (1 - scale) / 2
    texts, y = [], 112
    for line in top:
        fs = _fontsize(line)
        texts.append(f'<text class="meme" x="512" y="{y}" font-size="{fs}">{line}</text>')
        y += fs + 16
    yb = 972 - sum(_fontsize(l) + 20 for l in bottom)
    for line in bottom:
        fs = _fontsize(line)
        yb += fs + 20
        texts.append(f'<text class="meme" x="512" y="{yb - 16}" font-size="{fs}">{line}</text>')
    body = "\n      ".join(texts)
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024"
     role="img" aria-label="Sticker Dr. Cuack: {name}">
  <defs>{STICKER_DEFS}  </defs>
{MEME_CSS}  <g filter="url(#stickershadow)">
    <g filter="url(#diecut)">
      <g transform="translate({tx:.0f} {dy}) scale({scale})">
{behind}{duck}{front}      </g>
      {body}
    </g>
  </g>
</svg>
"""
    outdir = os.path.join(HERE, "stickers", "svg")
    os.makedirs(outdir, exist_ok=True)
    out = os.path.join(outdir, f"sticker-{name}.svg")
    with open(out, "w") as f:
        f.write(svg)
    return out


# ------------------------------------------------------------------ emojis

def cabeza(ojos, boca, extras="", rubor=False):
    blush = (f'<ellipse cx="118" cy="300" rx="26" ry="16" fill="#FFAFA3"/>'
             f'<ellipse cx="394" cy="300" rx="26" ry="16" fill="#FFAFA3"/>') if rubor else ""
    return f"""  <g id="cara">
    {real_head()}
    {blush}
{ojos}
{boca}
{extras}  </g>"""

# Parches del color de la cabeza para tapar el ojo/pico real del calco cuando
# la expresion necesita una forma distinta (si se deja vacio, se conserva la
# cara real tal cual).
TAPA_OJOS = f'<ellipse cx="170" cy="246" rx="34" ry="42" fill="{YELLOW}"/><ellipse cx="342" cy="246" rx="34" ry="42" fill="{YELLOW}"/>'
TAPA_OJO_IZQ = f'<ellipse cx="170" cy="246" rx="34" ry="42" fill="{YELLOW}"/>'
TAPA_OJO_DER = f'<ellipse cx="342" cy="246" rx="34" ry="42" fill="{YELLOW}"/>'
TAPA_BOCA = f'<ellipse cx="256" cy="322" rx="94" ry="68" fill="{YELLOW}"/>'

OJOS_NORMAL = ""  # se conserva la mirada real del calco

OJOS_FELICES = TAPA_OJOS + f"""    <g fill="none" stroke="{NAVY}" stroke-width="18" stroke-linecap="round">
      <path d="M 136 250 C 148 226 192 226 204 250"/>
      <path d="M 308 250 C 320 226 364 226 376 250"/>
    </g>"""

OJOS_TRISTES = TAPA_OJOS + f"""    <g fill="none" stroke="{NAVY}" stroke-width="18" stroke-linecap="round">
      <path d="M 136 240 C 148 262 192 262 204 240"/>
      <path d="M 308 240 C 320 262 364 262 376 240"/>
    </g>"""

def ojos_corazon():
    hz = f'M 0 14 C -34 -18 -14 -44 0 -26 C 14 -44 34 -18 0 14 Z'
    return (TAPA_OJOS + f'<g fill="#E8536F" stroke="{NAVY}" stroke-width="11" stroke-linejoin="round">'
            f'<path transform="translate(170 246) scale(1.9)" d="{hz}"/>'
            f'<path transform="translate(342 246) scale(1.9)" d="{hz}"/></g>')

OJOS_SORPRESA = TAPA_OJOS + f"""    <g>
      <circle cx="170" cy="246" r="46" fill="#FFF" stroke="{NAVY}" stroke-width="11"/>
      <circle cx="342" cy="246" r="46" fill="#FFF" stroke="{NAVY}" stroke-width="11"/>
      <circle cx="170" cy="252" r="16" fill="{NAVY}"/><circle cx="342" cy="252" r="16" fill="{NAVY}"/>
    </g>"""

BOCA_SONRISA = TAPA_BOCA + f"""    <g>
      <path d="M 176 322 C 178 302 212 290 256 290 C 300 290 334 302 336 322
               C 338 346 310 360 256 360 C 202 360 174 346 176 322 Z"
            fill="{ORANGE}" stroke="{NAVY}" stroke-width="13"/>
      <ellipse cx="256" cy="336" rx="52" ry="12" fill="{ORANGED}"/>
      <path d="M 210 354 C 226 384 286 384 302 354 C 298 388 278 404 256 404
               C 234 404 214 388 210 354 Z" fill="{BOCA}" stroke="{NAVY}" stroke-width="12" stroke-linejoin="round"/>
    </g>"""

BOCA_RISA = TAPA_BOCA + f"""    <g>
      <path d="M 176 318 C 178 298 212 286 256 286 C 300 286 334 298 336 318
               C 338 340 310 352 256 352 C 202 352 174 340 176 318 Z"
            fill="{ORANGE}" stroke="{NAVY}" stroke-width="13"/>
      <path d="M 196 348 C 212 398 300 398 316 348 C 314 408 286 434 256 434
               C 226 434 198 408 196 348 Z" fill="{BOCA}" stroke="{NAVY}" stroke-width="12" stroke-linejoin="round"/>
      <path d="M 222 404 C 244 418 268 418 290 404 C 280 424 232 424 222 404 Z" fill="#F07B62"/>
    </g>"""

BOCA_CERRADA = TAPA_BOCA + f"""    <g>
      <path d="M 176 322 C 178 302 212 290 256 290 C 300 290 334 302 336 322
               C 338 346 310 360 256 360 C 202 360 174 346 176 322 Z"
            fill="{ORANGE}" stroke="{NAVY}" stroke-width="13"/>
      <ellipse cx="256" cy="336" rx="52" ry="12" fill="{ORANGED}"/>
    </g>"""

BOCA_FRUNCIDA = BOCA_CERRADA + f"""    <path d="M 216 388 C 236 372 276 372 296 388" fill="none"
          stroke="{NAVY}" stroke-width="13" stroke-linecap="round"/>"""

BOCA_O = TAPA_BOCA + f"""    <g>
      <path d="M 186 316 C 190 298 218 288 256 288 C 294 288 322 298 326 316
               C 328 334 306 344 256 344 C 206 344 184 334 186 316 Z"
            fill="{ORANGE}" stroke="{NAVY}" stroke-width="13"/>
      <ellipse cx="256" cy="386" rx="34" ry="42" fill="{BOCA}" stroke="{NAVY}" stroke-width="12"/>
    </g>"""

GAFAS_NERD_E = f"""    <g transform="translate(-108 -12) scale(0.711)">{GAFAS_NERD}</g>"""
GAFAS_SOL_E = f"""    <g transform="translate(-108 -12) scale(0.711)">{GAFAS_SOL}</g>"""

CEJAS_ENOJO = f"""    <g stroke="{NAVY}" stroke-width="17" stroke-linecap="round" fill="none">
      <path d="M 126 178 L 204 206"/><path d="M 386 178 L 308 206"/>
    </g>"""

CEJAS_ALTAS = f"""    <g stroke="{NAVY}" stroke-width="14" stroke-linecap="round" fill="none">
      <path d="M 134 168 C 148 152 190 148 206 160"/>
      <path d="M 306 160 C 322 148 364 152 378 168"/>
    </g>"""

LAGRIMAS_RISA = f"""    <path d="M 88 260 C 104 286 112 306 110 322 A 24 24 0 1 1 62 318 C 62 302 72 282 88 260 Z"
          fill="{CELESTE}" stroke="{NAVY}" stroke-width="10"/>
    <path d="M 424 260 C 440 286 448 306 446 322 A 24 24 0 1 1 398 318 C 398 302 408 282 424 260 Z"
          fill="{CELESTE}" stroke="{NAVY}" stroke-width="10"/>"""

LLANTO = f"""    <path d="M 148 288 C 142 356 142 420 150 470 L 194 470 C 190 420 192 356 196 292 Z"
          fill="{CELESTE}" opacity=".9"/>
    <path d="M 316 292 C 320 356 322 420 318 470 L 362 470 C 370 420 370 356 364 288 Z"
          fill="{CELESTE}" opacity=".9"/>"""

CORAZONES = f"""    <g fill="#E8536F" stroke="{NAVY}" stroke-width="8" stroke-linejoin="round">
      <path transform="translate(74 130) scale(1.1)" d="M 0 14 C -34 -18 -14 -44 0 -26 C 14 -44 34 -18 0 14 Z"/>
      <path transform="translate(444 150) scale(.8)" d="M 0 14 C -34 -18 -14 -44 0 -26 C 14 -44 34 -18 0 14 Z"/>
    </g>"""

ZZZ = f"""    <g font-family="'Arial Black','DejaVu Sans',sans-serif" font-weight="900" fill="{MAT}">
      <text x="392" y="120" font-size="56">Z</text>
      <text x="444" y="82" font-size="42">z</text>
      <text x="478" y="52" font-size="30">z</text>
    </g>"""

ENOJO_MARCA = f"""    <g stroke="#D64545" stroke-width="12" stroke-linecap="round" fill="none">
      <path d="M 428 96 C 440 108 440 122 430 134"/>
      <path d="M 452 88 C 466 102 466 120 454 134"/>
    </g>"""

GORRO_FIESTA = f"""    <g transform="rotate(14 256 60)">
      <path d="M 256 -12 L 322 116 C 280 138 232 138 190 116 Z" fill="{ECO}" stroke="{NAVY}"
            stroke-width="12" stroke-linejoin="round"/>
      <circle cx="256" cy="-12" r="17" fill="#FFD54F" stroke="{NAVY}" stroke-width="9"/>
      <circle cx="238" cy="72" r="9" fill="#FFD54F"/><circle cx="276" cy="46" r="8" fill="#F07B62"/>
      <circle cx="262" cy="100" r="8" fill="#8BE9A8"/>
    </g>"""

CONFETI = f"""    <g>
      <rect x="76" y="120" width="18" height="18" rx="4" fill="#F07B62" transform="rotate(24 85 129)"/>
      <rect x="436" y="150" width="16" height="16" rx="4" fill="#8BE9A8" transform="rotate(-18 444 158)"/>
      <circle cx="120" cy="80" r="9" fill="{CELESTE}"/>
      <circle cx="410" cy="86" r="8" fill="#FFD54F"/>
      <rect x="66" y="240" width="14" height="14" rx="3" fill="#FFD54F" transform="rotate(40 73 247)"/>
    </g>"""

GUINO = TAPA_OJO_DER + f"""    <path d="M 308 246 C 320 228 364 228 376 246" fill="none" stroke="{NAVY}"
          stroke-width="18" stroke-linecap="round"/>"""

MANO_BARBILLA = f"""    <ellipse cx="300" cy="452" rx="58" ry="34" fill="{YELLOW}" stroke="{NAVY}"
          stroke-width="12" transform="rotate(-14 300 452)"/>
    <path d="M 268 444 L 268 466 M 292 440 L 292 468 M 316 440 L 316 466"
          stroke="{NAVY}" stroke-width="8" opacity=".5" transform="rotate(-14 300 452)"/>"""

CEJA_PENSANDO = f"""    <g stroke="{NAVY}" stroke-width="14" stroke-linecap="round" fill="none">
      <path d="M 138 186 C 154 176 188 178 202 188"/>
      <path d="M 302 162 C 318 148 358 150 374 164"/>
    </g>"""

EXPLOSION = f"""    <style>
      .burst-outer {{ transform-box: fill-box; transform-origin: 50% 50%;
        animation: burstPulse 0.9s ease-in-out infinite; }}
      .burst-inner {{ transform-box: fill-box; transform-origin: 50% 50%;
        animation: burstPulse 0.9s ease-in-out infinite reverse; }}
      @keyframes burstPulse {{ 0%,100% {{ transform: scale(1) rotate(0deg); }}
        50% {{ transform: scale(1.14) rotate(7deg); }} }}
      .spark1 {{ transform-box: fill-box; transform-origin: 50% 50%;
        animation: spark1fly 1.3s ease-out infinite; }}
      .spark2 {{ transform-box: fill-box; transform-origin: 50% 50%;
        animation: spark2fly 1.3s ease-out .35s infinite; }}
      .spark3 {{ transform-box: fill-box; transform-origin: 50% 50%;
        animation: spark3fly 1.3s ease-out .7s infinite; }}
      @keyframes spark1fly {{ 0% {{ transform: translate(0,0) scale(1); opacity: 1; }}
        100% {{ transform: translate(-20px,-14px) scale(.3); opacity: 0; }} }}
      @keyframes spark2fly {{ 0% {{ transform: translate(0,0) scale(1); opacity: 1; }}
        100% {{ transform: translate(22px,-8px) scale(.3); opacity: 0; }} }}
      @keyframes spark3fly {{ 0% {{ transform: translate(0,0) scale(1); opacity: 1; }}
        100% {{ transform: translate(18px,16px) scale(.3); opacity: 0; }} }}
      @media (prefers-reduced-motion: reduce) {{
        .burst-outer, .burst-inner, .spark1, .spark2, .spark3 {{ animation: none; }} }}
    </style>
    <g>
      <path class="burst-outer" fill="{ORANGE}" stroke="{NAVY}" stroke-width="11" stroke-linejoin="round"
            d="M 256 -24 L 288 32 L 352 6 L 340 68 L 408 78 L 356 116 L 396 160 L 330 158
               L 336 216 L 276 178 L 256 236 L 236 178 L 176 216 L 182 158 L 116 160
               L 156 116 L 104 78 L 172 68 L 160 6 L 224 32 Z"/>
      <path class="burst-inner" fill="#FFD54F" d="M 256 22 L 276 58 L 318 44 L 310 84 L 352 92 L 318 114 L 342 142
               L 300 140 L 302 176 L 266 152 L 256 188 L 246 152 L 210 176 L 212 140
               L 170 142 L 194 114 L 160 92 L 202 84 L 194 44 L 236 58 Z"/>
      <circle class="spark1" cx="96" cy="60" r="11" fill="{ORANGE}"/>
      <circle class="spark2" cx="422" cy="48" r="9" fill="{ORANGE}"/>
      <circle class="spark3" cx="448" cy="120" r="7" fill="#FFD54F"/>
    </g>"""

MANO_SALUDO = f"""    <g transform="rotate(-28 350 170)">
      <rect x="288" y="142" width="128" height="58" rx="29" fill="{YELLOW}" stroke="{NAVY}" stroke-width="13"/>
      <path d="M 318 152 L 318 192 M 344 148 L 344 196 M 370 148 L 370 196"
            stroke="{NAVY}" stroke-width="8" opacity=".55"/>
    </g>"""

CEJAS_FIRMES = f"""    <g stroke="{NAVY}" stroke-width="15" stroke-linecap="round" fill="none">
      <path d="M 136 182 L 204 190"/><path d="M 308 190 L 376 182"/>
    </g>"""

OJOS_CANSADOS = TAPA_OJOS + f"""    <g>
      <ellipse cx="170" cy="254" rx="34" ry="38" fill="{NAVY}"/>
      <ellipse cx="342" cy="254" rx="34" ry="38" fill="{NAVY}"/>
      <circle cx="160" cy="244" r="9" fill="#FFFFFF"/>
      <circle cx="332" cy="244" r="9" fill="#FFFFFF"/>
      <path d="M 132 226 C 146 214 194 214 208 226 C 194 220 146 220 132 226 Z"
            fill="{YELLOW}"/>
      <path d="M 304 226 C 318 214 366 214 380 226 C 366 220 318 220 304 226 Z"
            fill="{YELLOW}"/>
      <path d="M 130 300 C 146 312 194 312 210 300" fill="none" stroke="{NAVY}"
            stroke-width="6" opacity=".3" stroke-linecap="round"/>
      <path d="M 302 300 C 318 312 366 312 382 300" fill="none" stroke="{NAVY}"
            stroke-width="6" opacity=".3" stroke-linecap="round"/>
    </g>"""

BOCA_SERIA = TAPA_BOCA + f"""    <g>
      <path d="M 176 322 C 178 302 212 290 256 290 C 300 290 334 302 336 322
               C 338 346 310 360 256 360 C 202 360 174 346 176 322 Z"
            fill="{ORANGE}" stroke="{NAVY}" stroke-width="13"/>
      <path d="M 216 334 L 296 334" stroke="{NAVY}" stroke-width="7" stroke-linecap="round"/>
    </g>"""

# Referencia: la escena de "Resacón en Las Vegas" donde a Alan se le superponen
# operaciones matemáticas flotando frente a la cara mientras cuenta cartas.
_CUENTAS = [
    (66, 78, "10+9-8+7", 26, -9, 0.0),
    (368, 64, "=13", 30, 7, 0.5),
    (430, 168, "-8", 30, 11, 1.1),
    (44, 190, "7×3", 27, -7, 1.7),
    (398, 268, "÷2", 26, -9, 0.3),
    (70, 320, "then...", 22, 4, 2.2),
    (150, 46, "∑", 32, -3, 1.4),
    (386, 372, "=21", 26, 8, 2.6),
]

def _cuentas_css():
    rules = ["""    <style>
      .eqf { opacity: 0; animation: eqFade 3.6s ease-in-out infinite; }"""]
    for i in range(len(_CUENTAS)):
        rules.append(f"      .eqf.e{i} {{ animation-delay: {(_CUENTAS[i][5]):.2f}s; }}")
    rules.append("""      @keyframes eqFade { 0%, 100% { opacity: 0; transform: translateY(6px); }
        45%, 55% { opacity: .8; transform: translateY(-4px); } }
      @media (prefers-reduced-motion: reduce) { .eqf { animation: none; opacity: .55; } }
    </style>""")
    return "\n".join(rules)

def _cuentas_texts():
    out = []
    for i, (x, y, txt, size, rot, _delay) in enumerate(_CUENTAS):
        out.append(f'<text class="eqf e{i}" x="{x}" y="{y}" transform="rotate({rot} {x} {y})" '
                    f'font-family="Georgia,\'DejaVu Serif\',serif" font-weight="bold" '
                    f'font-size="{size}" fill="{MAT}" text-anchor="middle">{txt}</text>')
    return "\n      ".join(out)

CUENTAS_OVERLAY = _cuentas_css() + '\n    <g>\n      ' + _cuentas_texts() + "\n    </g>"

EMOJIS = {
    "feliz":       cabeza(OJOS_NORMAL, BOCA_SONRISA, rubor=True),
    "risa":        cabeza(OJOS_FELICES, BOCA_RISA, LAGRIMAS_RISA),
    "amor":        cabeza(ojos_corazon(), BOCA_SONRISA, CORAZONES, rubor=True),
    "cool":        cabeza("", BOCA_SONRISA, GAFAS_SOL_E),
    "nerd":        cabeza(OJOS_NORMAL, BOCA_SONRISA, GAFAS_NERD_E),
    "triste":      cabeza(OJOS_TRISTES, BOCA_FRUNCIDA, f'<path d="M 352 300 C 366 326 372 344 370 358 A 22 22 0 1 1 326 354 C 326 340 336 322 352 300 Z" fill="{CELESTE}" stroke="{NAVY}" stroke-width="10"/>'),
    "llorando":    cabeza(OJOS_TRISTES, BOCA_O, LLANTO),
    "enojado":     cabeza(OJOS_NORMAL, BOCA_FRUNCIDA, CEJAS_ENOJO + ENOJO_MARCA),
    "sorprendido": cabeza(OJOS_SORPRESA, BOCA_O, CEJAS_ALTAS),
    "guino":       cabeza(GUINO, BOCA_SONRISA, rubor=True),
    "dormido":     cabeza(OJOS_TRISTES, BOCA_CERRADA, ZZZ),
    "fiesta":      cabeza(OJOS_FELICES, BOCA_RISA, GORRO_FIESTA + CONFETI, rubor=True),
    "pensando":    cabeza(OJOS_NORMAL, BOCA_CERRADA, CEJA_PENSANDO + MANO_BARBILLA),
    "explotado":   cabeza(OJOS_SORPRESA, BOCA_O, EXPLOSION),
    "saludo":      cabeza(OJOS_NORMAL, BOCA_CERRADA, CEJAS_FIRMES + MANO_SALUDO),
    "cuentas":     cabeza(OJOS_CANSADOS, BOCA_SERIA, CUENTAS_OVERLAY),
}


def build_emoji(name):
    body = EMOJIS[name]
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="-10 -30 532 542" width="512" height="512"
     role="img" aria-label="Emoji Dr. Cuack: {name}">
{body}
</svg>
"""
    outdir = os.path.join(HERE, "emoji", "svg")
    os.makedirs(outdir, exist_ok=True)
    out = os.path.join(outdir, f"emoji-{name}.svg")
    with open(out, "w") as f:
        f.write(svg)
    return out


# ------------------------------------------------------------------ memes (formatos famosos)


MEME_SIZE = {}  # nombre -> (w, h) real, para exportar PNG sin deformar

MEME_DEFS = f"""
    <filter id="grayout">
      <feColorMatrix type="matrix" values="0.33 0.33 0.33 0 0  0.33 0.33 0.33 0 0
        0.33 0.33 0.33 0 0  0 0 0 0.55 0"/>
    </filter>
    <filter id="memeshadow" x="-16%" y="-16%" width="132%" height="132%">
      <feDropShadow dx="0" dy="10" stdDeviation="14" flood-color="#1B2430" flood-opacity="0.3"/>
    </filter>
"""

CAPTION_CSS = f"""  <style>
    .cap {{ font-family: Georgia, 'DejaVu Serif', serif; font-weight: 700; fill: {NAVY};
      dominant-baseline: middle; }}
  </style>
"""


def _wrap_lines(text, maxchars=17):
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if len(trial) > maxchars and cur:
            lines.append(cur)
            cur = w
        else:
            cur = trial
    if cur:
        lines.append(cur)
    return lines


def _caption_lines(x, y0, lines, size=44, lh=54, anchor="start"):
    out = []
    for i, line in enumerate(lines):
        out.append(f'<text class="cap" x="{x}" y="{y0 + i * lh}" font-size="{size}" '
                    f'text-anchor="{anchor}">{line}</text>')
    return "\n      ".join(out)


def build_drake(name, variant_reject, variant_approve, texto_reject, texto_approve):
    """Formato 'Drake': dos paneles, arriba rechaza, abajo aprueba."""
    W, PH = 900, 520
    duck_r = leer_duck_static(variant_reject)
    duck_a = leer_duck_static(variant_approve)
    lines_r = _wrap_lines(texto_reject, 13)
    lines_a = _wrap_lines(texto_approve, 13)
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {PH * 2}" width="{W}" height="{PH * 2}"
     role="img" aria-label="Meme Dr. Cuack (formato Drake): {name}">
  <defs>{MEME_DEFS}  </defs>
{CAPTION_CSS}  <g filter="url(#memeshadow)">
    <rect x="0" y="0" width="{W}" height="{PH * 2}" rx="26" fill="#FFFFFF" stroke="{NAVY}" stroke-width="10"/>
    <line x1="0" y1="{PH}" x2="{W}" y2="{PH}" stroke="{NAVY}" stroke-width="8"/>
    <line x1="480" y1="14" x2="480" y2="{PH - 14}" stroke="{NAVY}" stroke-width="6" opacity=".5"/>
    <line x1="480" y1="{PH + 14}" x2="480" y2="{PH * 2 - 14}" stroke="{NAVY}" stroke-width="6" opacity=".5"/>

    <g transform="translate(40 30) scale(0.44)" filter="url(#grayout)">{duck_r}</g>
    <circle cx="120" cy="86" r="46" fill="#E14848" stroke="{NAVY}" stroke-width="8"/>
    <path d="M 100 66 L 140 106 M 140 66 L 100 106" stroke="#FFFFFF" stroke-width="12" stroke-linecap="round"/>
    {_caption_lines(516, 220 - (len(lines_r) - 1) * 27, lines_r, size=38)}

    <g transform="translate(40 {PH + 6}) scale(0.44)">{duck_a}</g>
    <circle cx="120" cy="{PH + 86}" r="46" fill="#1FA65A" stroke="{NAVY}" stroke-width="8"/>
    <path d="M {100} {PH + 90} L {116} {PH + 106} L {144} {PH + 66}" fill="none"
          stroke="#FFFFFF" stroke-width="12" stroke-linecap="round" stroke-linejoin="round"/>
    {_caption_lines(516, PH + 220 - (len(lines_a) - 1) * 27, lines_a, size=38)}
  </g>
</svg>
"""
    outdir = os.path.join(HERE, "memes", "svg")
    os.makedirs(outdir, exist_ok=True)
    out = os.path.join(outdir, f"meme-{name}.svg")
    with open(out, "w") as f:
        f.write(svg)
    MEME_SIZE[name] = (W, PH * 2)
    return out


def _brain(cx, cy, r, fill, glow=False, rainbow=False):
    grad_id = f"brainglow{cx}{cy}"
    defs = ""
    if rainbow:
        defs = f"""<radialGradient id="{grad_id}" cx="50%" cy="45%" r="60%">
          <stop offset="0%" stop-color="#FFD54F"/><stop offset="35%" stop-color="#F07B62"/>
          <stop offset="65%" stop-color="#8B5FBF"/><stop offset="100%" stop-color="#4FA8E8"/>
        </radialGradient>"""
        fill = f"url(#{grad_id})"
    glow_ring = (f'<circle cx="{cx}" cy="{cy}" r="{r + 34}" fill="none" stroke="{fill if not rainbow else "#FFD54F"}" '
                 f'stroke-width="10" opacity=".45"/>'
                 f'<circle cx="{cx}" cy="{cy}" r="{r + 58}" fill="none" stroke="{fill if not rainbow else "#8B5FBF"}" '
                 f'stroke-width="8" opacity=".25"/>') if glow else ""
    return f"""<defs>{defs}</defs>
    {glow_ring}
    <path transform="translate({cx} {cy}) scale({r / 90})"
          d="M -70 -10 C -78 -46 -46 -70 -14 -64 C -4 -76 18 -76 28 -64
             C 62 -70 82 -42 74 -12 C 88 -2 88 20 76 30 C 82 52 66 74 40 74
             C 34 84 16 90 0 84 C -16 90 -34 84 -40 74 C -66 74 -82 52 -76 30
             C -88 20 -88 -2 -74 -12 Z"
          fill="{fill}" stroke="{NAVY}" stroke-width="9" stroke-linejoin="round"/>
    <path transform="translate({cx} {cy}) scale({r / 90})"
          d="M -30 -50 C -20 -40 -20 -24 -32 -16 M 6 -58 C 14 -46 12 -30 0 -20
             M -50 10 C -38 4 -26 8 -22 20 M 30 6 C 40 0 52 6 54 18"
          fill="none" stroke="{NAVY}" stroke-width="6" opacity=".55" stroke-linecap="round"/>
"""


def build_expanding_brain(name, etapas):
    """etapas: lista de 4 (texto, duck_extra_svg, brain_kwargs)."""
    W, PH = 1120, 420
    H = PH * len(etapas)
    panels = []
    for idx, (texto, extra, bkw) in enumerate(etapas):
        y0 = idx * PH
        lines = _wrap_lines(texto, 19)
        brain = _brain(150, y0 + PH / 2, 92, **bkw)
        panels.append(f"""
    <line x1="0" y1="{y0}" x2="{W}" y2="{y0}" stroke="{NAVY}" stroke-width="6" opacity=".35"/>
    <g>{brain}</g>
    <g transform="translate(320 {y0 + 20}) scale(0.36)">{extra}</g>
    {_caption_lines(620, y0 + PH / 2 - (len(lines) - 1) * 27, lines, size=38, lh=48)}""")
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}"
     role="img" aria-label="Meme Dr. Cuack (cerebro galáctico): {name}">
  <defs>{MEME_DEFS}  </defs>
{CAPTION_CSS}  <g filter="url(#memeshadow)">
    <rect x="0" y="0" width="{W}" height="{H}" rx="26" fill="#FFFFFF" stroke="{NAVY}" stroke-width="10"/>
    {"".join(panels)}
  </g>
</svg>
"""
    outdir = os.path.join(HERE, "memes", "svg")
    os.makedirs(outdir, exist_ok=True)
    out = os.path.join(outdir, f"meme-{name}.svg")
    with open(out, "w") as f:
        f.write(svg)
    MEME_SIZE[name] = (W, H)
    return out


MESA = f"""
  <g id="mesa">
    <rect x="0" y="720" width="1024" height="220" fill="#8C5A32" stroke="{NAVY}" stroke-width="{SW}"/>
    <rect x="0" y="720" width="1024" height="34" fill="#A9734A" stroke="{NAVY}" stroke-width="{SW}"/>
    <path d="M 90 754 L 90 936 M 934 754 L 934 936" stroke="{NAVY}" stroke-width="16" opacity=".4"/>
  </g>
"""


def build_change_my_mind(name, variant, texto):
    W, H = 1024, 1024
    duck = leer_duck_static(variant)
    lines = _wrap_lines(texto, 22)
    lh = 60
    sign_h = 60 + len(lines) * lh + 40
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}"
     role="img" aria-label="Meme Dr. Cuack (cámbiame de opinión): {name}">
  <defs>{MEME_DEFS}  </defs>
{CAPTION_CSS}  <g filter="url(#memeshadow)">
    <rect x="0" y="0" width="{W}" height="{H}" rx="26" fill="#EFEAE0" stroke="{NAVY}" stroke-width="10"/>
    <g transform="translate(232 40) scale(0.72)">{duck}</g>
    {MESA}
    <g transform="translate(300 610)">
      <path d="M -20 -20 L 240 -50 L 500 -20 L 480 20 L 240 -6 L 0 20 Z" fill="#B9C2CC"
            stroke="{NAVY}" stroke-width="9" stroke-linejoin="round"/>
      <rect x="-30" y="20" width="500" height="{sign_h}" rx="14" fill="#FFFFFF" stroke="{NAVY}" stroke-width="11"/>
      {_caption_lines(220, 20 + 60, lines, size=40, lh=lh, anchor="middle")}
    </g>
  </g>
</svg>
"""
    outdir = os.path.join(HERE, "memes", "svg")
    os.makedirs(outdir, exist_ok=True)
    out = os.path.join(outdir, f"meme-{name}.svg")
    with open(out, "w") as f:
        f.write(svg)
    MEME_SIZE[name] = (W, H)
    return out


MEMES_DRAKE = {
    "drake-guias": dict(variant_reject="base", variant_approve="matematico",
                        texto_reject="Enseñar todo de memoria",
                        texto_approve="Usar guías con Dr. Cuack"),
}

def _brain_duck(*overlays):
    return leer_duck_static("base") + "".join(overlays)


MEMES_BRAIN = {
    "cerebro-galactico": [
        ("Copiar el tablero", _brain_duck(), dict(fill="#9AA0A8")),
        ("Hacer un resumen", _brain_duck(GAFAS_NERD), dict(fill="#F0C24B", glow=True)),
        ("Usar guías con Dr. Cuack", _brain_duck(GAFAS_NERD, BIRRETE), dict(fill="#F0913F", glow=True)),
        ("Ser Dr. Cuack", _brain_duck(GAFAS_NERD, BIRRETE, SPARKLES), dict(fill="#FFD54F", glow=True, rainbow=True)),
    ],
}

MEMES_TABLE = {
    "cambiame-de-opinion": dict(variant="profesor",
                                texto="Los patos con gafas enseñan mejor. Cámbiame de opinión."),
}


def build_demo():
    def card(path, name):
        svg = open(path).read()
        svg = svg[svg.index("<svg"):]
        return f'<div class="card">{svg}<h2>{name}</h2></div>\n'
    secs = []
    secs.append("<header><h1>Dr. Cuack — calcado</h1><p class='sub'>variantes · stickers · emojis</p></header>")
    secs.append('<div class="grid">')
    for name in V:
        secs.append(card(os.path.join(HERE, "svg", f"dr-cuack-{name}.svg"), name))
    secs.append('</div><header><h1>Stickers</h1></header><div class="grid">')
    for name in ST:
        secs.append(card(os.path.join(HERE, "stickers", "svg", f"sticker-{name}.svg"), name))
    secs.append('</div><header><h1>Emojis</h1></header><div class="grid emoji">')
    for name in EMOJIS:
        secs.append(card(os.path.join(HERE, "emoji", "svg", f"emoji-{name}.svg"), name))
    secs.append('</div><header><h1>Memes</h1></header><div class="grid memes">')
    for name in list(MEMES_DRAKE) + list(MEMES_BRAIN) + list(MEMES_TABLE):
        secs.append(card(os.path.join(HERE, "memes", "svg", f"meme-{name}.svg"), name))
    secs.append("</div>")
    html = """<!doctype html><html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Dr. Cuack — calcado</title>
<style>
  body { margin:0; font-family: Georgia, serif; background:#F6F3EC; color:#2B2620; }
  header { text-align:center; padding:26px 16px 4px; }
  h1 { margin:0; font-size:1.8rem; } p.sub { margin:.3em 0 0; opacity:.7; }
  .grid { display:grid; grid-template-columns:repeat(auto-fill,minmax(240px,1fr));
          gap:20px; max-width:1150px; margin:18px auto 40px; padding:0 20px; }
  .grid.emoji { grid-template-columns:repeat(auto-fill,minmax(170px,1fr)); }
  .grid.memes { grid-template-columns:repeat(auto-fill,minmax(320px,1fr)); }
  .card { background:rgba(255,255,255,.6); border-radius:16px; padding:12px 8px 10px;
          text-align:center; box-shadow:0 3px 12px rgba(27,36,48,.10); }
  .card svg { width:100%; height:auto; display:block; }
  .card h2 { font-size:.95rem; margin:.35em 0 0; font-weight:600; }
</style></head><body>
""" + "".join(secs) + "</body></html>\n"
    out = os.path.join(HERE, "demo.html")
    with open(out, "w") as f:
        f.write(html)
    return out


if __name__ == "__main__":
    outs = []
    for name in V:
        outs.append(build_variant(name))
    for name in ST:
        outs.append(build_sticker(name))
    for name in EMOJIS:
        outs.append(build_emoji(name))
    for name, kw in MEMES_DRAKE.items():
        outs.append(build_drake(name, **kw))
    for name, etapas in MEMES_BRAIN.items():
        outs.append(build_expanding_brain(name, etapas))
    for name, kw in MEMES_TABLE.items():
        outs.append(build_change_my_mind(name, **kw))
    outs.append(build_demo())
    for o in outs:
        print("→", os.path.relpath(o, HERE))
    if "--png" in sys.argv:
        for name in V:
            render(os.path.join(HERE, "svg", f"dr-cuack-{name}.svg"),
                   os.path.join(HERE, "png", f"dr-cuack-{name}.png"), 1024)
        os.makedirs(os.path.join(HERE, "stickers", "png"), exist_ok=True)
        for name in ST:
            render(os.path.join(HERE, "stickers", "svg", f"sticker-{name}.svg"),
                   os.path.join(HERE, "stickers", "png", f"sticker-{name}.png"), 1024)
        os.makedirs(os.path.join(HERE, "memes", "png"), exist_ok=True)
        for name in list(MEMES_DRAKE) + list(MEMES_BRAIN) + list(MEMES_TABLE):
            w, h = MEME_SIZE[name]
            scale = 1024 / max(w, h)
            render(os.path.join(HERE, "memes", "svg", f"meme-{name}.svg"),
                   os.path.join(HERE, "memes", "png", f"meme-{name}.png"),
                   round(w * scale), round(h * scale))
        os.makedirs(os.path.join(HERE, "emoji", "png"), exist_ok=True)
        for name in EMOJIS:
            render(os.path.join(HERE, "emoji", "svg", f"emoji-{name}.svg"),
                   os.path.join(HERE, "emoji", "png", f"emoji-{name}.png"), 512)
        print("PNG exportados")
