#!/usr/bin/env python3
"""
Dr. Cuack — generador del personaje SVG del kit.

Compone la base del personaje (pato científico-matemático) con capas de
profesión y escribe un SVG autocontenido y animado por variante en `svg/`.

Uso:  python3 build.py            # regenera todos los SVG
      python3 build.py --list     # lista variantes

Los colores de acento vienen del design system del kit (design/preamble.tex):
  mat  #1E4078 (azul profundo)   cnat #106E50 (esmeralda)
  csoc #A54B2D (terracota)       eco  #463782 (índigo)
  alert #B45F0A (ámbar)
"""
import os, sys

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")

# ---------------------------------------------------------------- paleta
MAT   = "#1E4078"   # azul profundo
MATD  = "#16325F"
CNAT  = "#106E50"   # esmeralda
CSOC  = "#A54B2D"   # terracota
CSOCD = "#8C3D22"
ECO   = "#463782"   # índigo
ECOD  = "#392C6B"
AMBAR = "#E8930A"   # ámbar vivo (casco/chaleco)

LID   = "#F6C74A"   # color del párpado (amarillo de la cabeza)

# ---------------------------------------------------------------- plantilla
TEMPLATE = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"
     width="512" height="512" role="img" aria-labelledby="t d">
  <title id="t">Dr. Cuack — {title}</title>
  <desc id="d">{desc}</desc>
  <defs>
    <radialGradient id="gBody" gradientUnits="userSpaceOnUse" cx="226" cy="316" r="170">
      <stop offset="0%" stop-color="#FFE07A"/>
      <stop offset="55%" stop-color="#FFCF3F"/>
      <stop offset="100%" stop-color="#F0AE2B"/>
    </radialGradient>
    <radialGradient id="gHead" gradientUnits="userSpaceOnUse" cx="230" cy="120" r="210">
      <stop offset="0%" stop-color="#FFE38A"/>
      <stop offset="55%" stop-color="#FFD147"/>
      <stop offset="100%" stop-color="#F2B02C"/>
    </radialGradient>
    <linearGradient id="gBeak" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#FFBE55"/>
      <stop offset="100%" stop-color="#EE8E1E"/>
    </linearGradient>
    <linearGradient id="gFoot" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#F5AC42"/>
      <stop offset="100%" stop-color="#DE8B26"/>
    </linearGradient>
    <linearGradient id="gCoat" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#FFFFFF"/>
      <stop offset="100%" stop-color="#E8EEF5"/>
    </linearGradient>
    <clipPath id="clipEyeL"><ellipse cx="210" cy="150" rx="27" ry="32"/></clipPath>
    <clipPath id="clipEyeR"><ellipse cx="302" cy="150" rx="27" ry="32"/></clipPath>
  </defs>

  <style>
    #duck {{ animation: bob 4.2s ease-in-out infinite; }}
    #shadow {{ transform-box: view-box; transform-origin: 256px 480px;
              animation: shadowPulse 4.2s ease-in-out infinite; }}
    #head {{ transform-box: view-box; transform-origin: 256px 288px;
            animation: tilt 6.4s ease-in-out infinite; }}
    #hair path {{ transform-box: view-box; transform-origin: 254px 62px;
                 animation: sway 3.4s ease-in-out infinite; }}
    #hair path:nth-child(2) {{ animation-delay: .35s; }}
    #hair path:nth-child(3) {{ animation-delay: .7s; }}
    .lid {{ transform-box: fill-box; transform-origin: 50% 0%;
           transform: scaleY(0); animation: blink 5.6s infinite; }}
    @keyframes bob {{ 0%,100% {{ transform: translateY(0); }} 50% {{ transform: translateY(5px); }} }}
    @keyframes shadowPulse {{ 0%,100% {{ transform: scale(1); opacity:.12 }} 50% {{ transform: scale(1.06); opacity:.16 }} }}
    @keyframes tilt {{ 0%,100% {{ transform: rotate(0deg); }} 30% {{ transform: rotate(-1.3deg); }} 75% {{ transform: rotate(1.1deg); }} }}
    @keyframes sway {{ 0%,100% {{ transform: rotate(0deg); }} 50% {{ transform: rotate(3deg); }} }}
    @keyframes blink {{ 0%, 90.5%, 94.5%, 100% {{ transform: scaleY(0); }} 91.5%, 93.5% {{ transform: scaleY(1); }} }}
    /* clases opcionales: añadir en el elemento raíz del SVG */
    svg.talk #bill-lower, .talk #bill-lower {{ animation: talk .42s ease-in-out infinite; }}
    #bill-lower {{ transform-box: view-box; transform-origin: 256px 248px; }}
    @keyframes talk {{ 0%,100% {{ transform: translateY(0); }} 50% {{ transform: translateY(6px); }} }}
    .wave #arm-up {{ animation: wave 1.1s ease-in-out infinite; }}
    #arm-up {{ transform-box: view-box; transform-origin: 330px 320px; }}
    @keyframes wave {{ 0%,100% {{ transform: rotate(0deg); }} 50% {{ transform: rotate(-8deg); }} }}
{css_extra}
    @media (prefers-reduced-motion: reduce) {{ * {{ animation: none !important; }} }}
  </style>

  <ellipse id="shadow" cx="256" cy="480" rx="130" ry="15" fill="#1B2430" opacity="0.12"/>

  <g id="duck">
{behind}
    <!-- patas -->
    <g id="feet">
      <path d="M 172 474 C 168 446 186 430 210 430 C 234 430 250 446 246 474
               C 239 466 231 466 225 474 C 219 466 209 466 203 474 C 196 466 184 466 172 474 Z"
            fill="url(#gFoot)"/>
      <path d="M 266 474 C 262 446 278 430 302 430 C 326 430 344 446 340 474
               C 328 466 316 466 309 474 C 303 466 293 466 287 474 C 281 466 273 466 266 474 Z"
            fill="url(#gFoot)"/>
    </g>

    <!-- alas en reposo (detrás del cuerpo) -->
    <g id="wing-left">
      <path d="M 190 292 C 152 300 128 336 132 372 C 134 392 152 398 168 388
               C 192 372 204 336 204 304 Z" fill="{wing_fill}"/>{wing_left_extra}
    </g>
    <g id="wing-right">
      {wing_right}
    </g>

    <!-- cuerpo -->
    <g id="body">
      <path d="M 256 256 C 198 258 168 306 164 358 C 160 406 200 442 256 442
               C 312 442 352 406 348 358 C 344 306 314 258 256 256 Z" fill="url(#gBody)"/>
      <ellipse cx="256" cy="378" rx="62" ry="48" fill="#FFE9A8"/>
      <path d="M 176 388 C 188 426 220 440 256 440 C 292 440 324 426 336 388
               C 328 430 296 446 256 446 C 216 446 184 430 176 388 Z" fill="#DE9A1E" opacity="0.35"/>
    </g>
{clothing}
    <!-- cabeza -->
    <g id="head">
      <path d="M 256 56 C 184 56 150 114 150 184 C 150 250 194 294 256 294
               C 318 294 362 250 362 184 C 362 114 328 56 256 56 Z" fill="url(#gHead)"/>
      <ellipse cx="212" cy="108" rx="48" ry="34" fill="#FFFFFF" opacity="0.16"/>
{hair}
      <!-- mejillas -->
      <ellipse cx="172" cy="176" rx="13" ry="9" fill="#FFAC55" opacity="0.5"/>
      <ellipse cx="340" cy="176" rx="13" ry="9" fill="#FFAC55" opacity="0.5"/>

      <!-- ojos -->
      <g id="eye-left">
        <ellipse cx="210" cy="150" rx="27" ry="32" fill="#FFFFFF"/>
        <path d="M 183 150 A 27 32 0 0 1 237 150" fill="none" stroke="#D8D2C4" stroke-width="3" opacity=".6"/>
        <circle cx="215" cy="153" r="12.5" fill="#33261B"/>
        <circle cx="211" cy="148" r="4" fill="#FFFFFF"/>
        <circle cx="219" cy="158" r="2" fill="#FFFFFF" opacity="0.8"/>
        <g clip-path="url(#clipEyeL)"><ellipse class="lid" cx="210" cy="150" rx="28" ry="33" fill="{lid}"/></g>
      </g>
      <g id="eye-right">
        <ellipse cx="302" cy="150" rx="27" ry="32" fill="#FFFFFF"/>
        <path d="M 275 150 A 27 32 0 0 1 329 150" fill="none" stroke="#D8D2C4" stroke-width="3" opacity=".6"/>
        <circle cx="297" cy="153" r="12.5" fill="#33261B"/>
        <circle cx="293" cy="148" r="4" fill="#FFFFFF"/>
        <circle cx="301" cy="158" r="2" fill="#FFFFFF" opacity="0.8"/>
        <g clip-path="url(#clipEyeR)"><ellipse class="lid" cx="302" cy="150" rx="28" ry="33" fill="{lid}"/></g>
      </g>

      <!-- cejas -->
      <g fill="none" stroke="#8A6414" stroke-width="6" stroke-linecap="round">
        <path d="M 186 108 C 196 100 214 98 228 104"/>
        <path d="M 284 104 C 298 98 316 100 326 108"/>
      </g>

      <!-- pico -->
      <g id="beak" transform="translate(0 7)">
        <!-- mandíbula inferior: profunda, con sombra en el borde -->
        <path id="bill-lower" d="M 156 244 C 192 258 320 258 356 244
                 C 352 262 330 275 300 280 C 272 284 240 284 212 280
                 C 182 275 160 262 156 244 Z" fill="#DD831A"/>
        <path d="M 172 264 C 196 276 316 276 340 264 C 322 277 288 283 256 283
                 C 224 283 190 277 172 264 Z" fill="#C06E0C" opacity=".8"/>
        <!-- pico superior -->
        <path d="M 124 210 C 128 192 176 184 256 184 C 336 184 384 192 388 210
                 C 391 224 380 238 356 246 C 322 255 190 255 156 246
                 C 132 238 121 224 124 210 Z" fill="url(#gBeak)"/>
        <!-- boca: curva en S con comisuras hacia arriba -->
        <g fill="none" stroke="#A96409" stroke-width="4" stroke-linecap="round">
          <path d="M 140 220 C 150 234 176 243 212 247 C 241 250 271 250 300 247
                   C 336 243 362 234 372 220"/>
          <path d="M 141 221 Q 132 216 134 206"/>
          <path d="M 371 221 Q 380 216 378 206"/>
        </g>
        <!-- orificios nasales sobre el pico -->
        <g id="nostrils">
          <ellipse cx="233" cy="204" rx="6.5" ry="3.6" fill="#9E5605" transform="rotate(-16 233 204)"/>
          <ellipse cx="279" cy="204" rx="6.5" ry="3.6" fill="#9E5605" transform="rotate(16 279 204)"/>
          <path d="M 227 208 Q 233 211 240 207" fill="none" stroke="#FFD98F" stroke-width="2" opacity=".7"/>
          <path d="M 272 207 Q 279 211 285 208" fill="none" stroke="#FFD98F" stroke-width="2" opacity=".7"/>
        </g>
        <path d="M 152 203 C 170 194 208 189 250 188" fill="none" stroke="#FFE1A6" stroke-width="7" stroke-linecap="round" opacity="0.6"/>
      </g>

{glasses}{head_gear}    </g>
{props}{front}  </g>
</svg>
"""

GLASSES = """      <!-- gafas -->
      <g id="glasses" fill="none" stroke="#23303E" stroke-width="5">
        <circle cx="210" cy="150" r="34" fill="#AAD7FF" fill-opacity="0.14"/>
        <circle cx="302" cy="150" r="34" fill="#AAD7FF" fill-opacity="0.14"/>
        <path d="M 244 146 C 250 140 262 140 268 146"/>
        <path d="M 176 146 L 156 152"/>
        <path d="M 336 146 L 356 152"/>
        <path d="M 190 132 A 26 26 0 0 1 206 122" stroke="#FFFFFF" stroke-width="3" opacity=".65"/>
        <path d="M 282 132 A 26 26 0 0 1 298 122" stroke="#FFFFFF" stroke-width="3" opacity=".65"/>
      </g>
"""

SHADES = """      <!-- gafas oscuras -->
      <g id="shades">
        <rect x="177" y="127" width="64" height="46" rx="17" fill="#1B2430"/>
        <rect x="271" y="127" width="64" height="46" rx="17" fill="#1B2430"/>
        <path d="M 240 140 C 248 133 264 133 272 140" fill="none" stroke="#1B2430" stroke-width="6"/>
        <path d="M 178 144 L 158 150 M 334 144 L 354 150" stroke="#1B2430" stroke-width="6"/>
        <path d="M 190 140 L 206 134 M 284 140 L 300 134" stroke="#5C6B7E" stroke-width="4"
              stroke-linecap="round" opacity=".8"/>
      </g>
"""

HAIR = """      <!-- mechones -->
      <g id="hair" fill="none" stroke="#2F2A26" stroke-width="5" stroke-linecap="round">
        <path d="M 252 58 C 248 36 252 20 268 10"/>
        <path d="M 238 62 C 230 44 230 28 244 16"/>
        <path d="M 268 60 C 272 40 284 26 302 22"/>
      </g>
"""

WING_RIGHT_DOWN = """<path d="M 322 292 C 360 300 384 336 380 372 C 378 392 360 398 344 388
               C 320 372 308 336 308 304 Z" fill="{fill}"/>{extra}"""

# Ala derecha levantada (se dibuja en {props}, delante del cuerpo,
# por fuera de la cabeza para no taparla)
def arm_up(fill, hand=True):
    hand_svg = '\n      <ellipse cx="390" cy="256" rx="13" ry="11" fill="#F7C844" transform="rotate(-32 390 256)"/>' if hand else ""
    return f"""<path d="M 330 322 C 362 314 390 292 398 262 C 402 246 390 237 376 244
             C 352 256 332 284 324 316 Z" fill="{fill}"/>{hand_svg}"""

# Manitas amarillas sobre mangas (alas en reposo recoloreadas)
HAND_L = '\n      <ellipse cx="152" cy="376" rx="13" ry="11" fill="#F7C844" transform="rotate(24 152 376)"/>'
HAND_R = '\n      <ellipse cx="360" cy="376" rx="13" ry="11" fill="#F7C844" transform="rotate(-24 360 376)"/>'

# ------------------------------------------------------------ prendas

BATA = """    <!-- bata blanca -->
    <g id="coat">
      <path d="M 256 262 C 196 264 162 310 158 360 C 154 412 198 446 256 446
               C 314 446 358 412 354 360 C 350 310 316 264 256 262 Z" fill="url(#gCoat)"/>
      <path d="M 234 266 L 278 266 C 288 320 290 380 286 442 L 226 442 C 222 380 224 320 234 266 Z"
            fill="url(#gBody)"/>
      <ellipse cx="256" cy="394" rx="34" ry="46" fill="#FFE9A8"/>
      <path d="M 236 266 L 214 302 L 244 322 L 250 280 Z" fill="#FFFFFF" stroke="#D9E2EB" stroke-width="2.5"/>
      <path d="M 276 266 L 298 302 L 268 322 L 262 280 Z" fill="#FFFFFF" stroke="#D9E2EB" stroke-width="2.5"/>
      <path d="M 168 380 C 176 416 204 438 232 442 C 200 442 172 424 162 392 Z" fill="#C9D4E0" opacity=".7"/>
      <path d="M 344 380 C 336 416 308 438 280 442 C 312 442 340 424 350 392 Z" fill="#C9D4E0" opacity=".7"/>
    </g>
"""

POCKET_PENS = """    <g id="pocket">
      <rect x="192" y="356" width="36" height="28" rx="4" fill="#FFFFFF" stroke="#D9E2EB" stroke-width="2.5"/>
      <rect x="199" y="342" width="7" height="18" rx="2.5" fill="#1E4078"/>
      <rect x="210" y="344" width="7" height="16" rx="2.5" fill="#A54B2D"/>
    </g>
"""

ESTETOSCOPIO = """    <g id="estetoscopio" fill="none" stroke="#37474F" stroke-width="7" stroke-linecap="round">
      <path d="M 206 296 C 210 330 228 352 252 362"/>
      <path d="M 306 296 C 302 330 284 352 260 362"/>
      <path d="M 256 362 C 268 368 280 378 284 390"/>
      <circle cx="286" cy="398" r="13" fill="#90A4AE" stroke="#546E7A" stroke-width="3"/>
      <circle cx="286" cy="398" r="5.5" fill="#CFD8DC" stroke="none"/>
    </g>
    <g id="badge">
      <rect x="196" y="330" width="30" height="38" rx="4" fill="#FFFFFF" stroke="#C9D4E0" stroke-width="2.5"/>
      <rect x="206" y="336" width="10" height="26" rx="1.5" fill="#C62828"/>
      <rect x="198" y="344" width="26" height="10" rx="1.5" fill="#C62828"/>
    </g>
"""

def vest(color, dark, stripes="", vfill="url(#gBody)"):
    return f"""    <!-- chaleco -->
    <g id="vest">
      <path d="M 256 260 C 198 262 170 308 166 358 C 162 408 202 442 256 442
               C 310 442 350 408 346 358 C 342 308 314 262 256 260 Z" fill="{color}"/>
{stripes}      <path d="M 256 262 L 224 264 C 238 296 250 318 256 334 C 262 318 274 296 288 264 Z"
            fill="{vfill}"/>
      <path d="M 224 264 C 238 296 250 318 256 334 C 262 318 274 296 288 264"
            fill="none" stroke="{dark}" stroke-width="5"/>
      <path d="M 176 384 C 190 424 222 440 256 440 C 290 440 322 424 336 384
               C 330 428 296 446 256 446 C 216 446 182 428 176 384 Z" fill="{dark}"/>
    </g>
"""

BOWTIE = f"""    <g id="bowtie">
      <path d="M 254 302 L 228 289 C 224 288 222 291 223 295 L 223 311 C 222 315 224 318 228 317 L 254 304 Z" fill="{CSOC}"/>
      <path d="M 258 302 L 284 289 C 288 288 290 291 289 295 L 289 311 C 290 315 288 318 284 317 L 258 304 Z" fill="{CSOC}"/>
      <rect x="248" y="294" width="16" height="16" rx="5" fill="{CSOCD}"/>
    </g>
"""

CORBATA = f"""    <g id="corbata">
      <path d="M 230 290 L 256 300 L 238 314 Z" fill="#FDFBF4"/>
      <path d="M 282 290 L 256 300 L 274 314 Z" fill="#FDFBF4"/>
      <path d="M 256 300 L 242 316 L 252 382 L 256 390 L 260 382 L 270 316 Z" fill="{CSOC}"/>
      <path d="M 245 296 L 267 296 L 262 312 L 250 312 Z" fill="{CSOCD}"/>
    </g>
"""

HOODIE = f"""    <!-- hoodie -->
    <g id="hoodie">
      <path d="M 256 258 C 196 260 166 308 162 358 C 158 410 200 444 256 444
               C 312 444 354 410 350 358 C 346 308 316 260 256 258 Z" fill="{ECO}"/>
      <path d="M 214 380 L 298 380 C 304 380 308 384 306 390 L 300 414 C 299 418 296 420 292 420
               L 220 420 C 216 420 213 418 212 414 L 206 390 C 204 384 208 380 214 380 Z"
            fill="{ECOD}"/>
      <path d="M 220 384 L 232 416 M 292 384 L 280 416" stroke="{ECO}" stroke-width="4" fill="none"/>
      <path d="M 238 298 C 236 316 236 326 240 338" stroke="#CBC3EC" stroke-width="5" fill="none" stroke-linecap="round"/>
      <path d="M 274 298 C 276 316 276 326 272 338" stroke="#CBC3EC" stroke-width="5" fill="none" stroke-linecap="round"/>
      <rect x="236" y="336" width="8" height="10" rx="2" fill="#CBC3EC"/>
      <rect x="268" y="336" width="8" height="10" rx="2" fill="#CBC3EC"/>
      <path d="M 176 382 C 190 422 222 440 256 440 C 290 440 322 422 336 382
               C 330 426 296 444 256 444 C 216 444 182 426 176 382 Z" fill="{ECOD}"/>
    </g>
"""

HOOD_BEHIND = f"""    <!-- capucha detrás de la cabeza -->
    <ellipse cx="256" cy="258" rx="130" ry="68" fill="{ECOD}"/>
    <ellipse cx="256" cy="254" rx="122" ry="60" fill="{ECO}"/>
"""

# ------------------------------------------------------------ props / gear

GOGGLES = """      <g id="goggles">
        <path d="M 158 104 C 198 80 314 80 354 104" fill="none" stroke="#37474F" stroke-width="9"/>
        <rect x="196" y="66" width="120" height="42" rx="21" fill="#AEE3F7" fill-opacity=".85"
              stroke="#37474F" stroke-width="6"/>
        <path d="M 214 80 C 230 74 250 72 268 74" stroke="#FFFFFF" stroke-width="5"
              stroke-linecap="round" fill="none" opacity=".8"/>
      </g>
"""

FLASK = f"""    <g id="arm-up">
      {arm_up('{sleeve}')}
      <g id="flask" transform="translate(-12 28) rotate(-8 408 200)">
        <path d="M 399 152 L 399 180 L 380 214 Q 375 223 385 223 L 431 223 Q 441 223 436 214
                 L 417 180 L 417 152 Z" fill="#D2EBFA" fill-opacity=".55" stroke="#7FA8C9" stroke-width="3.5"
              stroke-linejoin="round"/>
        <path d="M 389 198 L 380 214 Q 375 223 385 223 L 431 223 Q 441 223 436 214 L 427 198 Z"
              fill="#17A673" fill-opacity=".9"/>
        <rect x="394" y="146" width="28" height="8" rx="4" fill="#7FA8C9"/>
        <circle class="bubble" cx="401" cy="212" r="3.4" fill="#BFF3DE"/>
        <circle class="bubble b2" cx="412" cy="216" r="2.6" fill="#BFF3DE"/>
        <circle class="bubble b3" cx="422" cy="211" r="3" fill="#BFF3DE"/>
      </g>
    </g>
"""

CSS_BUBBLES = """    .bubble { animation: rise 2.6s ease-in infinite; }
    .bubble.b2 { animation-delay: .9s; }
    .bubble.b3 { animation-delay: 1.7s; }
    @keyframes rise { 0% { transform: translateY(0); opacity: 0; }
      25% { opacity: .95; } 100% { transform: translateY(-40px); opacity: 0; } }
"""

CHALK_ARM = f"""    <g id="arm-up">
      {arm_up('url(#gBody)')}
      <rect x="388" y="234" width="9" height="26" rx="4" fill="#FDFDF8" stroke="#D8D5C8"
            stroke-width="1.5" transform="rotate(38 392 247)"/>
    </g>
"""

PIZARRA = f"""    <g id="pizarra" transform="rotate(-7 148 356)">
      <rect x="86" y="308" width="126" height="98" rx="8" fill="#6D4A2A"/>
      <rect x="95" y="317" width="108" height="80" rx="4" fill="#294F44"/>
      <text x="149" y="352" text-anchor="middle" font-family="'Comic Sans MS','Segoe Print','DejaVu Sans',sans-serif"
            font-size="19" fill="#F4F8F2">a²+b²=c²</text>
      <text x="120" y="384" text-anchor="middle" font-family="'Comic Sans MS','Segoe Print','DejaVu Sans',sans-serif"
            font-size="20" fill="#F4F8F2">π</text>
      <text x="172" y="386" text-anchor="middle" font-family="'Comic Sans MS','Segoe Print','DejaVu Sans',sans-serif"
            font-size="15" fill="#F4F8F2" opacity=".85">∞</text>
    </g>
"""

SYMBOLS = f"""    <g id="simbolos" font-family="Georgia,'DejaVu Serif',serif" font-weight="bold" fill="{MAT}">
      <text class="float" x="108" y="86" font-size="34" opacity=".75">π</text>
      <text class="float f2" x="396" y="118" font-size="28" opacity=".65">∑</text>
      <text class="float f3" x="386" y="58" font-size="26" opacity=".6">∞</text>
    </g>
"""

CSS_FLOAT = """    .float { animation: floaty 5.2s ease-in-out infinite; }
    .float.f2 { animation-delay: 1.2s; } .float.f3 { animation-delay: 2.4s; }
    @keyframes floaty { 0%,100% { transform: translateY(0); } 50% { transform: translateY(-9px); } }
"""

BIRRETE = f"""      <g id="birrete">
        <path d="M 196 88 C 200 72 312 72 316 88 L 316 106 C 288 97 224 97 196 106 Z" fill="{MATD}"/>
        <path d="M 256 30 L 372 64 L 256 98 L 140 64 Z" fill="{MAT}"/>
        <path d="M 140 64 L 256 98 L 256 108 L 140 74 Z" fill="{MATD}"/>
        <path d="M 372 64 L 256 98 L 256 108 L 372 74 Z" fill="#12294D"/>
        <circle cx="256" cy="64" r="5" fill="#D9A62E"/>
        <path d="M 256 64 C 296 60 336 64 352 72" fill="none" stroke="#D9A62E" stroke-width="4"/>
        <g id="tassel">
          <path d="M 352 72 L 354 108" stroke="#D9A62E" stroke-width="4"/>
          <path d="M 348 106 C 348 100 360 100 360 106 L 358 124 C 357 129 351 129 350 124 Z" fill="#EAB93D"/>
        </g>
      </g>
"""

CSS_TASSEL = """    #tassel { transform-box: view-box; transform-origin: 352px 72px;
      animation: pendulum 3.2s ease-in-out infinite; }
    @keyframes pendulum { 0%,100% { transform: rotate(0deg); } 50% { transform: rotate(7deg); } }
"""

LIBRO = f"""    <g id="libro">
      <path d="M 192 346 C 216 330 244 326 256 334 C 268 326 296 330 320 346
               L 320 398 C 296 384 268 382 256 390 C 244 382 216 384 192 398 Z" fill="{CSOC}"/>
      <path d="M 198 348 C 220 334 244 332 254 338 L 254 384 C 244 378 220 380 198 392 Z" fill="#FDFBF4"/>
      <path d="M 314 348 C 292 334 268 332 258 338 L 258 384 C 268 378 292 380 314 392 Z" fill="#FDFBF4"/>
      <path d="M 206 352 C 222 342 238 340 248 344 M 206 360 C 222 350 238 348 248 352
               M 206 368 C 222 358 238 356 248 360" stroke="#C9C2B4" stroke-width="2" fill="none"/>
      <path d="M 306 352 C 290 342 274 340 264 344 M 306 360 C 290 350 274 348 264 352
               M 306 368 C 290 358 274 356 264 360" stroke="#C9C2B4" stroke-width="2" fill="none"/>
      <path d="M 256 334 L 256 390" stroke="#8C3D22" stroke-width="3"/>
      <ellipse cx="196" cy="372" rx="13" ry="11" fill="#F7C844" transform="rotate(24 196 372)"/>
      <ellipse cx="316" cy="372" rx="13" ry="11" fill="#F7C844" transform="rotate(-24 316 372)"/>
    </g>
"""

CASCO = f"""      <g id="casco">
        <path d="M 170 100 C 172 50 340 50 342 100 L 344 108 C 296 94 216 94 168 108 Z" fill="{AMBAR}"/>
        <path d="M 170 100 C 171 62 240 52 256 52 C 240 52 196 64 188 102 Z" fill="#FFC24D"/>
        <path d="M 152 106 C 208 88 304 88 360 106 C 368 109 366 119 356 117
                 C 302 102 210 102 156 117 C 146 119 144 109 152 106 Z" fill="#C97C06"/>
      </g>
"""

def vstripes():
    return f"""      <path d="M 210 268 C 206 320 206 380 212 438 L 232 440 C 226 380 226 316 230 266 Z" fill="#CFD8DC"/>
      <path d="M 302 266 C 306 316 306 380 300 440 L 280 438 C 286 380 286 320 282 268 Z" fill="#CFD8DC"/>
"""

PLANO = f"""    <g id="plano" transform="rotate(-28 150 352)">
      <rect x="104" y="338" width="94" height="26" rx="13" fill="{MAT}"/>
      <ellipse cx="198" cy="351" rx="7" ry="13" fill="#DCE9FB"/>
      <ellipse cx="198" cy="351" rx="3" ry="6" fill="{MAT}"/>
      <rect x="134" y="338" width="18" height="26" fill="#DCE9FB"/>
    </g>
"""

FEDORA = f"""      <g id="fedora">
        <path d="M 138 106 C 148 90 196 82 256 82 C 316 82 364 90 374 106
                 C 382 117 370 126 354 121 C 302 108 210 108 158 121
                 C 142 126 130 117 138 106 Z" fill="#23303E"/>
        <path d="M 180 100 C 180 56 206 40 256 40 C 306 40 332 56 332 100
                 C 304 90 208 90 180 100 Z" fill="#2B3949"/>
        <path d="M 256 42 C 246 56 246 76 254 88" fill="none" stroke="#1B2430" stroke-width="4" opacity=".55"/>
        <path d="M 180 100 C 208 89 304 89 332 100 L 332 116 C 304 104 208 104 180 116 Z" fill="{CSOC}"/>
      </g>
"""

PALILLO = """      <path d="M 348 240 L 376 228" stroke="#F1E3C0" stroke-width="4.5" stroke-linecap="round"/>
"""

def pinstripes(color="#8A94A6"):
    return f"""      <g fill="none" stroke="{color}" stroke-width="2" opacity=".45">
        <path d="M 208 272 C 202 322 202 380 208 434"/>
        <path d="M 232 264 C 227 322 227 384 232 440"/>
        <path d="M 280 264 C 285 322 285 384 280 440"/>
        <path d="M 304 272 C 310 322 310 380 304 434"/>
      </g>
"""

AUDIFONOS = """      <g id="audifonos">
        <path d="M 162 128 C 170 60 342 60 350 128" fill="none" stroke="#263238" stroke-width="11"/>
        <rect x="140" y="122" width="30" height="52" rx="14" fill="#263238"/>
        <rect x="342" y="122" width="30" height="52" rx="14" fill="#263238"/>
        <rect x="147" y="130" width="16" height="36" rx="8" fill="#546E7A"/>
        <rect x="349" y="130" width="16" height="36" rx="8" fill="#546E7A"/>
      </g>
"""

LAPTOP = """    <g id="laptop">
      <rect x="204" y="326" width="104" height="74" rx="9" fill="#37474F" stroke="#263238" stroke-width="3"/>
      <text x="256" y="372" text-anchor="middle" font-family="Consolas,'DejaVu Sans Mono',monospace"
            font-size="26" font-weight="bold" fill="#8BE9A8">&lt;/&gt;</text>
      <path d="M 196 400 L 316 400 L 324 418 Q 325 422 319 422 L 193 422 Q 187 422 188 418 Z"
            fill="#455A64" stroke="#263238" stroke-width="2.5"/>
      <ellipse cx="204" cy="398" rx="14" ry="11" fill="#F7C844" transform="rotate(18 204 398)"/>
      <ellipse cx="308" cy="398" rx="14" ry="11" fill="#F7C844" transform="rotate(-18 308 398)"/>
    </g>
"""

# ---------------------------------------------------------------- variantes
V = {}

V["base"] = dict(
    title="científico matemático",
    desc="Pato amarillo con gafas redondas, mascota del kit Guías del Profe.",
    wing_fill="url(#gBody)",
)

V["cientifico"] = dict(
    title="científico",
    desc="Dr. Cuack con bata de laboratorio, gafas de seguridad y matraz burbujeante.",
    wing_fill="url(#gCoat)",
    wing_left_extra=HAND_L,
    wing_right="",  # el ala derecha va levantada con el matraz
    clothing=BATA + POCKET_PENS,
    head_gear=GOGGLES,
    props=FLASK.replace("{sleeve}", "url(#gCoat)"),
    css_extra=CSS_BUBBLES,
)

V["matematico"] = dict(
    title="matemático",
    desc="Dr. Cuack con chaleco, pajarita, tiza y pizarra con el teorema de Pitágoras.",
    wing_fill="url(#gBody)",
    wing_right="",
    clothing=vest(MAT, MATD) + BOWTIE,
    props=PIZARRA + CHALK_ARM,
    front=SYMBOLS,
    css_extra=CSS_FLOAT,
)

V["profesor"] = dict(
    title="profesor",
    desc="Dr. Cuack con birrete, corbata y libro abierto.",
    wing_fill="url(#gBody)",
    hair="",
    clothing=CORBATA,
    head_gear=BIRRETE,
    front=LIBRO,
    css_extra=CSS_TASSEL,
)

V["ingeniero"] = dict(
    title="ingeniero",
    desc="Dr. Cuack con casco de seguridad, chaleco reflectivo y plano enrollado.",
    wing_fill="url(#gBody)",
    hair="",
    clothing=vest(AMBAR, "#C97C06", vstripes()),
    head_gear=CASCO,
    props=PLANO,
)

V["medico"] = dict(
    title="médico",
    desc="Dr. Cuack con bata médica, estetoscopio y carné.",
    wing_fill="url(#gCoat)",
    wing_left_extra=HAND_L,
    wing_right_extra=HAND_R,
    clothing=BATA + ESTETOSCOPIO,
)

V["programador"] = dict(
    title="programador",
    desc="Dr. Cuack con hoodie, audífonos y laptop.",
    wing_fill=ECO,
    hair="",
    behind=HOOD_BEHIND,
    clothing=HOODIE,
    head_gear=AUDIFONOS,
    front=LAPTOP,
)

V["ganster"] = dict(
    title="gánster",
    desc="Dr. Cuack gánster: fedora, traje de rayas, gafas oscuras y palillo.",
    wing_fill="#2B3440",
    wing_left_extra=HAND_L,
    wing_right_extra=HAND_R,
    hair="",
    clothing=vest("#2B3440", "#222B38", pinstripes(), vfill="#F4F7FA") + CORBATA,
    glasses=SHADES,
    head_gear=FEDORA + PALILLO,
)

# ---------------------------------------------------------------- build

def build(name):
    v = V[name]
    wing_right = v.get("wing_right", None)
    if wing_right is None:
        wing_right = WING_RIGHT_DOWN.format(fill=v["wing_fill"],
                                            extra=v.get("wing_right_extra", ""))
    svg = TEMPLATE.format(
        title=v["title"],
        desc=v["desc"],
        wing_fill=v["wing_fill"],
        wing_left_extra=v.get("wing_left_extra", ""),
        wing_right=wing_right,
        behind=v.get("behind", ""),
        clothing=v.get("clothing", ""),
        hair=v.get("hair", HAIR),
        head_gear=v.get("head_gear", ""),
        props=v.get("props", ""),
        front=v.get("front", ""),
        css_extra=v.get("css_extra", ""),
        glasses=v.get("glasses", GLASSES),
        lid=LID,
    )
    out = os.path.join(OUT, f"dr-cuack-{name}.svg")
    with open(out, "w") as f:
        f.write(svg)
    return out

# ---------------------------------------------------------------- stickers

FLAMES = """    <g id="llamas">
      <path d="M 96 434 C 62 400 68 348 98 318 C 92 352 110 356 106 330
               C 126 350 128 392 112 416 C 118 410 126 402 128 392
               C 136 416 122 442 96 434 Z" fill="#F57C00"/>
      <path d="M 98 424 C 82 406 84 376 98 358 C 96 376 108 380 106 364
               C 116 378 116 402 106 416 Z" fill="#FFC107"/>
      <path d="M 416 434 C 450 400 444 348 414 318 C 420 352 402 356 406 330
               C 386 350 384 392 400 416 C 394 410 386 402 384 392
               C 376 416 390 442 416 434 Z" fill="#F57C00"/>
      <path d="M 414 424 C 430 406 428 376 414 358 C 416 376 404 380 406 364
               C 396 378 396 402 406 416 Z" fill="#FFC107"/>
    </g>
"""

SWEAT = """    <path d="M 366 88 C 376 106 384 120 384 132 A 16 16 0 1 1 352 132
             C 352 120 358 106 366 88 Z" fill="#7EC8F7" opacity=".95"/>
"""

def sparkle(x, y, s=1.0, fill="#FFD54F"):
    return (f'<path transform="translate({x} {y}) scale({s})" fill="{fill}" '
            f'd="M 0 -14 L 3.5 -3.5 L 14 0 L 3.5 3.5 L 0 14 L -3.5 3.5 L -14 0 L -3.5 -3.5 Z"/>')

SPARKLES = ("    <g id='chispas'>"
            + sparkle(92, 112) + sparkle(128, 66, .7) + sparkle(414, 96, 1.1)
            + sparkle(438, 152, .6) + sparkle(74, 190, .6) + "</g>\n")

STICKER_FILTERS = """    <filter id="diecut" x="-12%" y="-12%" width="124%" height="124%">
      <feMorphology in="SourceAlpha" operator="dilate" radius="11" result="grow"/>
      <feFlood flood-color="#FFFFFF"/>
      <feComposite in2="grow" operator="in" result="border"/>
      <feMerge><feMergeNode in="border"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <filter id="stickershadow" x="-16%" y="-16%" width="132%" height="132%">
      <feDropShadow dx="0" dy="7" stdDeviation="9" flood-color="#1B2430" flood-opacity="0.35"/>
    </filter>
"""

STICKER_CSS = """    .meme { font-family: 'Archivo Black','Arial Black','DejaVu Sans',sans-serif;
      font-weight: 900; fill: #FFFFFF; stroke: #1B2430; stroke-width: 9px;
      paint-order: stroke; stroke-linejoin: round; letter-spacing: .5px;
      text-anchor: middle; }
"""

# name → (variante, líneas arriba, líneas abajo, extras detrás, extras delante)
ST = {
    "esto-esta-bien":  ("base",        [], ["ESTO ESTÁ BIEN"], FLAMES, ""),
    "confia-en-mi":    ("ingeniero",   ["CONFÍA EN MÍ,"], ["SOY INGENIERO"], "", ""),
    "en-mi-maquina":   ("programador", [], ["FUNCIONA EN", "MI MÁQUINA"], "", SWEAT),
    "aqui-mando-yo":   ("ganster",     [], ["AQUÍ MANDO YO"], "", ""),
    "presiona-f":      ("profesor",    [], ["PRESIONA F"], "", ""),
    "matemagicas":     ("matematico",  [], ["MATEMÁGICAS"], SPARKLES, ""),
    "que-miras-bobo":  ("ganster",     [], ["¿QUÉ MIRAS,", "BOBO?"], "", ""),
    "receta-repasar":  ("medico",      [], ["RECETA:", "REPASAR"], "", ""),
    "eureka":          ("cientifico",  [], ["¡EUREKA!"], SPARKLES, ""),
}

def _fontsize(text, maxw=470, cap=48):
    est = 0.68  # ancho medio por carácter (em) en DejaVu Sans Bold mayúsculas
    return max(24, min(cap, int(maxw / (est * max(1, len(text))))))

def build_sticker(name):
    variant, top, bottom, behind, front = ST[name]
    src = open(os.path.join(OUT, f"dr-cuack-{variant}.svg")).read()
    defs = src[src.index("<defs>")+6 : src.index("</defs>")]
    style = src[src.index("<style>")+7 : src.index("</style>")]
    duck = src[src.index('<g id="duck">') : src.rindex("</svg>")]

    # escala y posición del personaje según el texto que lo rodea
    scale = 0.72 if (top and len(bottom) > 1) else (0.76 if (top or len(bottom) > 1) else 0.8)
    dy = 46 if top else 8
    tx = 256 * (1 - scale)

    texts = []
    y = 56
    for line in top:
        fs = _fontsize(line)
        texts.append(f'<text class="meme" x="256" y="{y}" font-size="{fs}">{line}</text>')
        y += fs + 8
    yb = 486 - sum(_fontsize(l) + 10 for l in bottom)
    for line in bottom:
        fs = _fontsize(line)
        yb += fs + 10
        texts.append(f'<text class="meme" x="256" y="{yb - 8}" font-size="{fs}">{line}</text>')

    body = "\n".join("      " + t for t in texts)
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"
     width="512" height="512" role="img" aria-label="Sticker Dr. Cuack: {name}">
  <defs>{defs}{STICKER_FILTERS}  </defs>
  <style>{style}{STICKER_CSS}  </style>
  <g filter="url(#stickershadow)">
    <g filter="url(#diecut)">
      <g transform="translate({tx:.0f} {dy}) scale({scale})">
{behind}{duck}{front}      </g>
{body}
    </g>
  </g>
</svg>
"""
    outdir = os.path.join(os.path.dirname(OUT), "stickers", "svg")
    os.makedirs(outdir, exist_ok=True)
    out = os.path.join(outdir, f"sticker-{name}.svg")
    with open(out, "w") as f:
        f.write(svg)
    return out

DEMO_HEAD = """<!doctype html>
<html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Dr. Cuack — demo del personaje</title>
<style>
  :root { color-scheme: light dark; }
  body { margin:0; font-family: Georgia, 'Times New Roman', serif;
         background:#F6F3EC; color:#2B2620; }
  body.dark { background:#1E2430; color:#EDE8DE; }
  header { text-align:center; padding:28px 16px 6px; }
  h1 { margin:0; font-size:1.9rem; }
  p.sub { margin:.4em 0 0; opacity:.75; }
  .controls { text-align:center; margin:14px 0 4px; }
  button { font:inherit; font-size:.9rem; padding:6px 14px; margin:0 4px;
           border:1.5px solid currentColor; border-radius:999px;
           background:transparent; color:inherit; cursor:pointer; }
  button.on { background:#1E4078; border-color:#1E4078; color:#fff; }
  .grid { display:grid; grid-template-columns:repeat(auto-fill,minmax(250px,1fr));
          gap:22px; max-width:1180px; margin:18px auto 48px; padding:0 20px; }
  .card { background:rgba(255,255,255,.55); border-radius:18px; padding:14px 10px 12px;
          text-align:center; box-shadow:0 3px 14px rgba(27,36,48,.10); }
  body.dark .card { background:rgba(255,255,255,.06); }
  .card svg { width:100%; height:auto; display:block; }
  .card h2 { font-size:1.02rem; margin:.4em 0 0; font-weight:600; }
</style></head><body>
<header>
  <h1>Dr. Cuack</h1>
  <p class="sub">Mascota del kit «Guías del Profe» — 8 variantes + stickers, SVG animado y autocontenido</p>
</header>
<div class="controls">
  <button id="b-talk">hablar</button>
  <button id="b-wave">saludar</button>
  <button id="b-dark">fondo oscuro</button>
</div>
<div class="grid">
"""

DEMO_TAIL = """</div>
<script>
  const toggle = (btn, cls) => {
    btn.classList.toggle('on');
    document.querySelectorAll('.card svg').forEach(s => s.classList.toggle(cls));
  };
  document.getElementById('b-talk').onclick = e => toggle(e.target, 'talk');
  document.getElementById('b-wave').onclick = e => toggle(e.target, 'wave');
  document.getElementById('b-dark').onclick = e => {
    e.target.classList.toggle('on'); document.body.classList.toggle('dark');
  };
</script>
</body></html>
"""

def build_demo():
    cards = []
    for name in V:
        svg = open(os.path.join(OUT, f"dr-cuack-{name}.svg")).read()
        svg = svg[svg.index("<svg"):]
        cards.append(f'<div class="card">{svg}<h2>{name}</h2></div>\n')
    stickers = []
    stdir = os.path.join(os.path.dirname(OUT), "stickers", "svg")
    for name in ST:
        svg = open(os.path.join(stdir, f"sticker-{name}.svg")).read()
        stickers.append(f'<div class="card">{svg}<h2>{name}</h2></div>\n')
    mid = ('</div>\n<header><h1>Stickers</h1>'
           '<p class="sub">Listos para WhatsApp/Telegram o para pegar en las guías</p></header>\n'
           '<div class="grid">\n')
    demo = os.path.join(os.path.dirname(OUT), "demo.html")
    with open(demo, "w") as f:
        f.write(DEMO_HEAD + "".join(cards) + mid + "".join(stickers) + DEMO_TAIL)
    return demo

if __name__ == "__main__":
    if "--list" in sys.argv:
        print("\n".join(V), "\n--- stickers ---")
        print("\n".join(ST))
        sys.exit(0)
    os.makedirs(OUT, exist_ok=True)
    for name in V:
        print("→", build(name))
    for name in ST:
        print("→", build_sticker(name))
    print("→", build_demo())
