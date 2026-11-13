"""Build crawlable English and Spanish holiday landing pages. No build dependencies."""
from pathlib import Path
from html import escape
import json

ROOT = Path(__file__).resolve().parent.parent
STORE = 'https://apps.apple.com/app/id6786930057'
COPY = {
 'en': {
  'title':'R-Zen 3.2 — Christmas update coming December 2026',
  'description':'R-Zen 3.2 arrives in December 2026 with a Christmas-themed update. Discover the next chapter, or download the current version 3.0.1 for iPhone and iPad.',
  'announcement':'R-Zen 3.2 · Coming December 2026', 'skip':'Skip to content',
  'nav':['Coming 3.2','Explore','Collections','FAQ'], 'download':'Download on the App Store', 'shortDownload':'Get R-Zen',
  'eyebrow':'Next release · Christmas & New Year',
  'hero':'A little color.<br>A little wonder.<br><em>A moment for you.</em>',
  'lede':'A new season of calm is on its way. R-Zen 3.2 arrives in December with a Christmas theme to welcome the holidays and the New Year.',
  'explore':'Discover R-Zen', 'heroNote':'Coming in December 2026 · Version 3.0.1 available now',
  'artTag':'A quieter kind of holiday.', 'artAlt':'Illustrated snowy lakeside cabin and Christmas tree, with warm golden lights among evergreen trees.',
  'versionNote':'Next release<br>December 2026',
  'trust':['No ads. No accounts.','Create offline','8 app languages','Optional one-time Premium'],
  'releaseEye':'Available now · R-Zen 3.0.1', 'releaseTitle':'New memories.<br>A smoother journey.',
  'releaseLede':'While we prepare the next chapter, enjoy R-Zen 3.0.1 today: smoother puzzle galleries, plus the collections and collectible cards introduced in 3.0.',
  'releaseLink':'Meet the collections ↓',
  'updates':[
   ['01 / 3.0.1','Less loading. More unwinding.','Puzzle galleries load pictures as they come into view, using less memory and helping prevent unexpected reloads on iPhone and iPad.'],
   ['02 / 3.0','Nights of Light and Memory','R-Zen 3.0 introduced Noir Nights and artwork inspired by Day of the Dead: mandalas, cozy illustrations, Magic Color, paint-by-number and animated creations.'],
   ['03 / 3.0','Your art becomes a keepsake','Finish a Magic Color canvas and keep it as a collectible card in your journal. A little reminder of the time you made for yourself.'],
   ['04 / 3.0','Your collections, together','Browse the updated seasonal carousels, with layouts refined for iPhone and iPad. Autumn or spring follows your hemisphere preference.']
  ],
  'collectionEye':'Included with Premium', 'collectionTitle':'Your Legacy library, all year round.',
  'collectionLede':'Explore the Legacy packs included with your Premium purchase: mandalas, designs to reveal and more sheets to paint by number.',
  'collectionNote':'Legacy packs · Optional downloads · Included with the one-time Premium unlock · Create offline after downloading',
  'modesEye':'Follow your mood', 'modesTitle':'Find your way to unwind.', 'modesLede':'A brush, a puzzle piece, a quiet moment. There is more than one way to feel at home.',
  'modes':[
   ['Mandalas','Let color find its rhythm. Fill intricate patterns at your own pace.','modes/mandala.webp','Lotus mandala coloring artwork from R-Zen'],
   ['Puzzles','Travel through beautiful places, one piece at a time. No timer. No rush.','modes/puzzle.webp','A landscape from the R-Zen puzzle collection'],
   ['Illustrations','Cozy scenes and little details, ready for your own palette.','modes/illustration.svg','A cozy café illustration to color in R-Zen'],
   ['Paint by Number','Follow the numbers and watch a picture come together.','modes/number.png','Paint-by-number artwork in R-Zen'],
   ['Magic Color','Brush across the canvas to reveal a full-color world underneath.','modes/magic.webp','A patchwork scene from Magic Color in R-Zen'],
   ['Comes Alive','Finish selected paint-by-number artworks and see them begin to move.','v25/koala-flowers-spring.webp','An example of seasonal R-Zen artwork']
  ],
  'journalEye':'Keep the feeling', 'journalTitle':'Little moments.<br>Lasting memories.',
  'journalText':'Write in your journal, revisit your completed creations and collect cards from your Magic Color canvases. Add original ambient music, and let the day soften around you.',
  'music':'A little sound of R-Zen', 'trackLabel':'Choose a music track', 'play':'Play music', 'diaryAlt':'The journal inside the R-Zen app',
  'galleryEye':'A look inside', 'galleryTitle':'Your calm, wherever you are.', 'galleryLede':'Explore a few views of R-Zen on iPhone and iPad. Tap an image for a closer look.',
  'gallery':['The world of puzzles','A space to color','Your creative library','Your journal'],
  'ritualEye':'Christmas 2026 → A fresh start in 2027', 'ritualTitle':'Less rush.<br><em>More little rituals.</em>',
  'ritualLede':'A quiet Christmas morning. A pause between celebrations. The first page of a new year. There is no perfect time to begin—just a moment that is yours.',
  'rituals':[['01','Pick something small','One color, one puzzle, one journal entry. Start wherever you feel like it.'],['02','Make yourself at home','Choose your music and take your time. There is nothing to keep up with.'],['03','Keep a little memory','Save your creation, return to it tomorrow, or begin something new.']],
  'downloadEye':'Your next quiet moment', 'downloadTitle':'Give yourself<br>a little room to breathe.',
  'downloadText':'Version 3.0.1 is available now. Start with a free selection across the main creative modes. Unlock more with an optional one-time Premium purchase. No subscriptions.',
  'downloadFine':'iPhone & iPad · 8 app languages · No ads or accounts',
  'historyTitle':'Earlier chapters · Halloween & the seasons', 'historyEye':'Previous update · R-Zen 2.8',
  'historyName':'Cozy Halloween', 'historyText':'A previous chapter, still part of R-Zen’s seasonal world. Enchanted Night is optional and never switches on automatically.',
  'historyBullets':['18 patterns, 18 illustrations, 18 paint-by-number scenes and 9 Comes Alive characters.','Optional palettes, journal stickers, frames and a gentle breathing pause.','Autumn Zen and Spring Zen remain earlier seasonal collections.'],
  'historyLink':'View the seasonal archive →',
  'faqEye':'A few things to know', 'faqTitle':'Make yourself comfortable.',
  'faqs':[
   ['Is R-Zen free?','R-Zen is free to download and includes a selection of content in the main modes. Premium is an optional one-time purchase, with no subscription. Prices are shown in the App Store and inside the app.'],
   ['Can I use it offline?','The included creative content works offline. Optional packs need an internet connection to download; once saved on your device, you can use them offline too. Purchases and external links also need a connection.'],
   ['What changed in version 3.0.1?','This update improves stability and memory use in puzzle galleries. The new collections and collectible journal cards were introduced in version 3.0.'],
   ['When is R-Zen 3.2 coming?','R-Zen 3.2 arrives in December 2026 with a Christmas-themed update. The exact date and full details will be shared closer to launch. Version 3.0.1 is available now.'],
   ['Which languages does the app support?','Spanish, English, Portuguese, French, Italian, Japanese, German and Vietnamese. This website is available in English and Spanish.']
  ],
  'footerMessage':'May your days be a little more colorful.', 'footerLinks':['Support & FAQ','Privacy','Terms of Use'], 'studio':'An independent app by RnxGames', 'rights':'All rights reserved.', 'close':'Close image', 'viewImage':'View image: ',
 },
 'es': {
  'title':'R-Zen 3.2 — La actualización navideña llega en diciembre de 2026',
  'description':'R-Zen 3.2 llegará en diciembre de 2026 con una actualización de temática navideña. Descubre el próximo capítulo o descarga la versión actual 3.0.1 para iPhone y iPad.',
  'announcement':'R-Zen 3.2 · Próximo lanzamiento: diciembre de 2026', 'skip':'Saltar al contenido',
  'nav':['Próxima 3.2','Explorar','Colecciones','Preguntas'], 'download':'Descárgala en la App Store', 'shortDownload':'Descargar R-Zen',
  'eyebrow':'Próximo lanzamiento · Navidad y Año Nuevo',
  'hero':'Un poco de color.<br>Un poco de magia.<br><em>Un momento para ti.</em>',
  'lede':'Una nueva temporada de calma está en camino. R-Zen 3.2 llegará en diciembre con una temática navideña para acompañarte durante las fiestas y el Año Nuevo.',
  'explore':'Descubre R-Zen', 'heroNote':'Llega en diciembre de 2026 · Versión 3.0.1 disponible ahora',
  'artTag':'Unas fiestas con más calma.', 'artAlt':'Ilustración de una cabaña nevada junto a un lago y un árbol de Navidad, con luces doradas entre abetos.',
  'versionNote':'Próximo lanzamiento<br>Diciembre de 2026',
  'trust':['Sin anuncios ni cuentas','Crea sin conexión','8 idiomas en la app','Premium opcional de pago único'],
  'releaseEye':'Disponible ahora · R-Zen 3.0.1', 'releaseTitle':'Nuevos recuerdos.<br>Un recorrido más fluido.',
  'releaseLede':'Mientras preparamos el próximo capítulo, disfruta de R-Zen 3.0.1: galerías de puzzles más fluidas y las colecciones y cartas coleccionables que llegaron con 3.0.',
  'releaseLink':'Conoce las colecciones ↓',
  'updates':[
   ['01 / 3.0.1','Menos carga. Más calma.','Las galerías de puzzles cargan las imágenes a medida que aparecen en pantalla: usan menos memoria y ayudan a evitar recargas inesperadas en iPhone y iPad.'],
   ['02 / 3.0','Noches de luz y memoria','R-Zen 3.0 presentó Noches Noir y obras inspiradas en Día de Muertos: mandalas, ilustraciones acogedoras, Color mágico, pintura por número y creaciones animadas.'],
   ['03 / 3.0','Tu arte se convierte en recuerdo','Termina un lienzo de Color mágico y consérvalo como carta coleccionable en tu diario. Un pequeño recuerdo del tiempo que te has dedicado.'],
   ['04 / 3.0','Tus colecciones, juntas','Explora los carruseles de temporada renovados, con ajustes para iPhone y iPad. Otoño o primavera siguen tu preferencia de hemisferio.']
  ],
  'collectionEye':'Incluidas con Premium', 'collectionTitle':'Tu colección Legacy, todo el año.',
  'collectionLede':'Explora los packs Legacy incluidos con tu compra Premium: mandalas, diseños para revelar y más láminas para pintar por número.',
  'collectionNote':'Packs Legacy · Descarga opcional · Incluidos con Premium de pago único · Crea sin conexión después de descargarlos',
  'modesEye':'Sigue tu inspiración', 'modesTitle':'Encuentra tu forma de desconectar.', 'modesLede':'Un pincel, una pieza, un momento de calma. Hay muchas formas de sentirte en tu espacio.',
  'modes':[
   ['Mandalas','Deja que el color encuentre su ritmo. Pinta los detalles a tu manera.','modes/mandala.webp','Un mandala de loto para colorear de R-Zen'],
   ['Puzzles','Viaja por lugares hermosos, pieza a pieza. Sin reloj. Sin prisa.','modes/puzzle.webp','Un paisaje de la colección de puzzles de R-Zen'],
   ['Ilustraciones','Escenas acogedoras y pequeños detalles, listos para tu propia paleta.','modes/illustration.svg','Una ilustración de un café acogedor para colorear en R-Zen'],
   ['Pintar por número','Sigue los números y descubre cómo toma forma una imagen.','modes/number.png','Una obra de pintura por número de R-Zen'],
   ['Color mágico','Pasa el pincel por el lienzo y revela un mundo a todo color.','modes/magic.webp','Una escena patchwork de Color mágico en R-Zen'],
   ['Cobra vida','Termina ciertas obras de pintura por número y verás cómo empiezan a moverse.','v25/koala-flowers-spring.webp','Un ejemplo del arte de temporada de R-Zen']
  ],
  'journalEye':'Conserva la sensación', 'journalTitle':'Pequeños momentos.<br>Recuerdos que se quedan.',
  'journalText':'Escribe en tu diario, vuelve a tus creaciones terminadas y colecciona las cartas de tus lienzos de Color mágico. Añade música ambiental original y deja que el día baje el ritmo.',
  'music':'Un poco del sonido de R-Zen', 'trackLabel':'Elegir una pista de música', 'play':'Reproducir música', 'diaryAlt':'El diario dentro de la app R-Zen',
  'galleryEye':'Una mirada al interior', 'galleryTitle':'Tu calma, donde estés.', 'galleryLede':'Explora algunas vistas de R-Zen en iPhone y iPad. Toca una imagen para verla más de cerca.',
  'gallery':['Un mundo de puzzles','Un espacio para colorear','Tu biblioteca creativa','Tu diario'],
  'ritualEye':'Navidad 2026 → Un nuevo comienzo en 2027', 'ritualTitle':'Menos prisas.<br><em>Más pequeños rituales.</em>',
  'ritualLede':'Una mañana tranquila de Navidad. Una pausa entre celebraciones. La primera página de un nuevo año. No hace falta un momento perfecto para empezar, solo uno que sea tuyo.',
  'rituals':[['01','Elige algo pequeño','Un color, un puzzle, unas líneas en el diario. Empieza por lo que te apetezca.'],['02','Haz tuyo el espacio','Elige tu música y tómate tu tiempo. No tienes que seguir el ritmo de nadie.'],['03','Guarda un recuerdo','Conserva tu creación, vuelve mañana o empieza algo nuevo.']],
  'downloadEye':'Tu próximo momento de calma', 'downloadTitle':'Regálate un espacio<br>para respirar.',
  'downloadText':'La versión 3.0.1 ya está disponible. Empieza con una selección gratuita en los principales modos creativos. Desbloquea más con Premium opcional de pago único. Sin suscripciones.',
  'downloadFine':'iPhone y iPad · 8 idiomas en la app · Sin anuncios ni cuentas',
  'historyTitle':'Capítulos anteriores · Halloween y las estaciones', 'historyEye':'Actualización anterior · R-Zen 2.8',
  'historyName':'Cozy Halloween', 'historyText':'Un capítulo anterior que sigue formando parte del mundo de temporada de R-Zen. Noche encantada es opcional y nunca se activa automáticamente.',
  'historyBullets':['18 patrones, 18 ilustraciones, 18 escenas por número y 9 personajes Cobra vida.','Paletas, stickers para el diario, marcos y una suave pausa de respiración opcionales.','Otoño Zen y Primavera Zen siguen como colecciones de temporadas anteriores.'],
  'historyLink':'Ver el archivo de temporadas →',
  'faqEye':'Algunas cosas que conviene saber', 'faqTitle':'Ponte a gusto.',
  'faqs':[
   ['¿R-Zen es gratis?','R-Zen es gratis para descargar e incluye una selección de contenido en los modos principales. Premium es una compra opcional de pago único, sin suscripción. El precio se muestra en la App Store y dentro de la app.'],
   ['¿Puedo usarla sin conexión?','El contenido creativo incluido funciona sin internet. Los packs opcionales necesitan conexión para descargarse; una vez guardados en tu dispositivo, también funcionan sin conexión. Las compras y los enlaces externos necesitan internet.'],
   ['¿Qué cambia en la versión 3.0.1?','Esta actualización mejora la estabilidad y el uso de memoria en las galerías de puzzles. Las nuevas colecciones y las cartas del diario llegaron con la versión 3.0.'],
   ['¿Cuándo llega R-Zen 3.2?','R-Zen 3.2 llegará en diciembre de 2026 con una actualización de temática navideña. La fecha exacta y todos los detalles se anunciarán más cerca del lanzamiento. La versión 3.0.1 ya está disponible.'],
   ['¿En qué idiomas está la app?','Español, inglés, portugués, francés, italiano, japonés, alemán y vietnamita. Esta web está disponible en inglés y español.']
  ],
  'footerMessage':'Que tus días tengan un poquito más de color.', 'footerLinks':['Ayuda y preguntas','Privacidad','Condiciones de uso'], 'studio':'Una app independiente de RnxGames', 'rights':'Todos los derechos reservados.', 'close':'Cerrar imagen', 'viewImage':'Ver imagen: ',
 }
}

APPLE = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M17 12c0-2 1.5-3.1 1.6-3.2-1-1.5-2.6-1.7-3.2-1.7-1.4-.1-2.7.8-3.4.8-.7 0-1.8-.8-3-.8C6.5 7.1 4 9 4 12.8c0 2.4.9 4.9 2 6.5.9 1.3 1.7 2.4 2.9 2.4s1.7-.8 3.2-.8 1.9.8 3.2.8 2.1-1.1 2.9-2.3c1-1.4 1.4-2.8 1.4-2.9-.1 0-2.6-1-2.6-4.5ZM14.8 5.5c.7-.9 1.2-2.1 1.1-3.3-1 .1-2.3.7-3 1.6-.6.7-1.2 1.9-1.1 3.1 1.1.1 2.3-.5 3-1.4Z"/></svg>'

PREVIEWS = json.loads((ROOT / 'assets/app-previews/markup.json').read_text(encoding='utf-8'))
LEGACY_CATALOG = json.loads((ROOT / 'assets/legacy-packs/catalog.json').read_text(encoding='utf-8'))
MODE_KEYS = ['traditional', 'puzzles', 'illustrations', 'by-number', 'magic-color', 'comes-alive', 'reveal', 'free']
COPY['en']['modes'].extend([
 ['Reveal', 'Brush gently across a hidden picture and uncover its colors.', '', ''],
 ['Free Drawing', 'Begin with a blank canvas and follow your own ideas, colors and brushstrokes.', '', '']
])
COPY['es']['modes'].extend([
 ['Revelar', 'Pasa suavemente el pincel por una imagen oculta y descubre sus colores.', '', ''],
 ['Dibujo libre', 'Empieza con un lienzo en blanco y sigue tus ideas, colores y pinceladas.', '', '']
])

def mode_cards(c, es):
 cards = []
 for i, ((title, description, _, _), key) in enumerate(zip(c['modes'], MODE_KEYS)):
  label = ('Vista animada de ' if es else 'Animated preview: ') + title
  controls = ''
  if key == 'puzzles':
   art = ''.join(PREVIEWS['puzzle-' + kind] for kind in ['classic','slide','swap'])
   controls = '<div class="app-puzzle-choices" role="group" aria-label="' + ('Tipo de puzzle' if es else 'Puzzle type') + '">'
   for kind, icon, name in zip(['classic','slide','swap'], ['◈','↕','⇄'], ['Clásico','Deslizar','Intercambiar'] if es else ['Classic','Slide','Swap']):
    controls += f'<button type="button" data-puzzle-choice="{kind}" aria-pressed="{str(kind == "classic").lower()}" aria-label="{name}" title="{name}"><span aria-hidden="true">{icon}</span><span class="preview-choice-label">{name}</span></button>'
   controls += '</div>'
  else:
   art = PREVIEWS[key]
  cards.append(f'<article class="mode" data-app-mode="{key}"><div class="mode-picture app-mode-preview" data-preview-active="true"><div class="app-preview-visual" role="img" aria-label="{escape(label)}"><div class="app-preview-content" aria-hidden="true">{art}</div></div>{controls}</div><span class="mode-index">0{i+1} / R-ZEN</span><h3>{escape(title)}</h3><p>{escape(description)}</p></article>')
 return ''.join(cards)

def collection_cards(es):
 lang = 'es' if es else 'en'
 cards = []
 for i, pack in enumerate(LEGACY_CATALOG['packs']):
  title = pack['title'][lang]
  samples = ''.join(f'<img src="./assets/legacy-packs/{sample["src"]}" width="{sample["width"]}" height="{sample["height"]}" alt="{escape(title)} — {"ejemplo" if es else "example"} {n+1}" loading="lazy" decoding="async">' for n, sample in enumerate(pack['samples']))
  if pack['cover']:
   cover = f'<div class="collection-cover"><img class="pack-cover-image" src="./assets/legacy-packs/{pack["cover"]}" width="1000" height="563" alt="{escape(title)}" loading="lazy" decoding="async"></div>'
   examples = f'<details class="pack-examples"><summary>{"Ver algunos diseños" if es else "Preview a few designs"}</summary><div class="pack-example-grid">{samples}</div></details>'
  else:
   cover = f'<div class="collection-cover pack-samples {pack["slug"]}">{samples}</div>'
   examples = ''
  tags = ''.join(f'<span>{escape(tag)}</span>' for tag in pack['tags'][lang])
  cards.append(f'<article class="collection-card{" collection-featured" if i == 0 else ""}" data-pack-id="{pack["id"]}">{cover}<div class="collection-body"><div class="eyebrow">{escape(pack["tagline"][lang])}</div><h3>{escape(title)}</h3><p>{escape(pack["description"][lang])}</p><div class="chips">{tags}</div>{examples}</div></article>')
 return ''.join(cards)

def build(lang):
 c = COPY[lang]
 es = lang == 'es'
 filename = 'r-zen-es.html' if es else 'r-zen.html'
 other = 'r-zen.html' if es else 'r-zen-es.html'
 canonical = 'https://rnxgames.com/' + filename
 def button(label=None, classes=''):
  return f'<a class="button {classes}" href="{STORE}" target="_blank" rel="noopener" data-download>{APPLE}{escape(label or c["download"])}</a>'
 updates = ''.join(f'<article class="release-row"><span>{escape(n)}</span><div><h3>{escape(h)}</h3><p>{escape(p)}</p></div></article>' for n,h,p in c['updates'])
 collections = collection_cards(es)
 modes = mode_cards(c, es)
 gallery = ''.join(f'<figure><a class="screenshot-button" style="display:block" href="./assets/v2/full/{image}.jpg" data-screenshot aria-label="{escape(c["viewImage"]+caption)}"><img src="./assets/v2/{image}.jpg" width="{w}" height="{h}" alt="{escape(caption)}" loading="lazy" decoding="async"></a><figcaption>{escape(caption)}</figcaption></figure>' for image,caption,w,h in zip(['iphone-canada','ipad-mandalas','iphone-packs','ipad-diary'],c['gallery'],[460,640,460,640],[996,853,996,853]))
 rituals = ''.join(f'<article class="ritual-step"><b>{n}</b><div><h3>{escape(h)}</h3><p>{escape(p)}</p></div></article>' for n,h,p in c['rituals'])
 faqs = ''.join(f'<details><summary>{escape(q)}</summary><p>{escape(a)}</p></details>' for q,a in c['faqs'])
 schema = {'@context':'https://schema.org','@type':'SoftwareApplication','name':'R-Zen Experience','softwareVersion':'3.0.1','operatingSystem':'iOS','applicationCategory':'LifestyleApplication','description':('Un espacio para mandalas, puzzles, pintura por número, Color mágico y tu diario en iPhone y iPad.' if es else 'A calm space for mandalas, puzzles, paint by number, Magic Color and your journal on iPhone and iPad.'),'url':canonical,'downloadUrl':STORE,'image':'https://rnxgames.com/assets/logo.png','inLanguage':['es','en','pt','fr','it','ja','de','vi']}
 content = f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(c['title'])}</title>
<meta name="description" content="{escape(c['description'])}">
<link rel="canonical" href="{canonical}">
<link rel="alternate" hreflang="en" href="https://rnxgames.com/r-zen.html">
<link rel="alternate" hreflang="es" href="https://rnxgames.com/r-zen-es.html">
<link rel="alternate" hreflang="x-default" href="https://rnxgames.com/r-zen.html">
<meta property="og:type" content="website"><meta property="og:title" content="{escape(c['title'])}">
<meta property="og:description" content="{escape(c['description'])}"><meta property="og:url" content="{canonical}">
<meta property="og:locale" content="{'es_ES' if es else 'en_US'}">
<meta property="og:image" content="https://rnxgames.com/assets/holiday/social-card.jpg">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{escape(c['artAlt'])}">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{escape(c['title'])}">
<meta name="twitter:description" content="{escape(c['description'])}"><meta name="twitter:image" content="https://rnxgames.com/assets/holiday/social-card.jpg">
<meta name="theme-color" content="#f7f5ee"><link rel="icon" href="./assets/logo.png"><link rel="apple-touch-icon" href="./assets/logo.png"><link rel="manifest" href="./site.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<script>try{{const t=localStorage.getItem('rzen-web-theme');if(t==='dark'||t==='light')document.documentElement.dataset.theme=t;}}catch{{}}</script>
<link rel="stylesheet" href="./assets/rzen-holiday.css?v=20261113-legacy">
<link rel="stylesheet" href="./assets/app-previews.css?v=20261113-legacy">
<link rel="stylesheet" href="./assets/app-preview-layout.css?v=20261113-legacy">
<script src="./assets/rzen-holiday.js?v=20261113-legacy" defer></script>
<script type="application/ld+json">{json.dumps(schema,ensure_ascii=False)}</script>
<noscript><style>@media(max-width:899px){{.nav-links{{position:static;display:flex;flex-wrap:wrap;padding:12px 0;border:0}}.nav{{flex-wrap:wrap}}}}.tools{{margin-left:auto}}</style></noscript>
</head>
<body>
<a class="skip" href="#main">{c['skip']}</a>
<div class="announcement"><a href="#next-release">✦ &nbsp; {c['announcement']} &nbsp; ✦</a></div>
<header class="site-header"><div class="wrap nav">
<a class="brand" href="./index.html"><img src="./assets/logo.png" width="42" height="42" alt=""><span><strong>R-Zen</strong><small>Experience</small></span></a>
<nav class="nav-links" id="navigation" aria-label="{'Navegación principal' if es else 'Main navigation'}">{''.join(f'<a href="#{anchor}">{label}</a>' for anchor,label in zip(['next-release','explore','collections','faq'],c['nav']))}</nav>
<div class="tools"><a class="lang" href="./{other}" data-language lang="{'en' if es else 'es'}" hreflang="{'en' if es else 'es'}" aria-label="{'Read in English' if es else 'Leer en español'}">{'EN' if es else 'ES'}</a>
<button class="icon-button" type="button" data-theme-toggle hidden aria-label="{'Cambiar tema' if es else 'Switch theme'}"><svg data-moon viewBox="0 0 24 24" aria-hidden="true"><path d="M20 15A8 8 0 0 1 9 4a8 8 0 1 0 11 11Z"/></svg></button>
<button class="icon-button menu-button" data-menu-toggle type="button" hidden aria-label="{'Menú' if es else 'Menu'}" aria-expanded="false" aria-controls="navigation"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg></button></div>
{button(c['shortDownload'],'small')}</div></header>
<main id="main">
<section class="hero" id="home" aria-labelledby="hero-title"><div class="wrap">
<div class="hero-grid"><div class="hero-copy"><div class="eyebrow">{c['eyebrow']}</div><h1 id="hero-title">{c['hero']}</h1><p>{c['lede']}</p><div class="hero-actions"><a class="button" href="#next-release">{'Descubre lo que viene' if es else 'Discover what’s coming'} <span aria-hidden="true">↓</span></a>{button('Descargar 3.0.1' if es else 'Download 3.0.1','secondary')}</div><p class="hero-note">{c['heroNote']}</p></div>
<div class="hero-art"><div class="hero-scene" role="img" aria-label="{escape(c['artAlt'])}"></div><div class="ornament" aria-hidden="true"><svg viewBox="0 0 80 130"><path d="M40 0v52m-7 0h14v9H33z"/><circle cx="40" cy="88" r="27"/><ellipse cx="40" cy="88" rx="12" ry="27"/><path d="M15 80h50M14 95h52M40 60v55M29 121h22"/><path d="m40 71 3 10 10 1-8 6 2 10-7-6-8 6 3-10-8-6 10-1Z"/></svg></div><div class="art-tag">{c['artTag']}</div><div class="version-tag"><b>3.2</b><span>{c['versionNote']}</span></div></div></div>
<div class="trust">{''.join(f'<div><span aria-hidden="true">{icon}</span>{escape(label)}</div>' for icon,label in zip(['✧','↟','◎','◇'],c['trust']))}</div></div></section>
<section class="section launch-section" id="next-release" aria-labelledby="launch-title"><div class="wrap launch-panel"><div class="launch-date"><span>{'PRÓXIMO LANZAMIENTO' if es else 'NEXT RELEASE'}</span><strong>3.2</strong><time datetime="2026-12">{'Diciembre de 2026' if es else 'December 2026'}</time></div><div class="launch-copy"><div class="eyebrow">{'Navidad y Año Nuevo' if es else 'Christmas & New Year'}</div><h2 id="launch-title">{'La Navidad llega a R-Zen.' if es else 'Christmas is coming to R-Zen.'}</h2><p>{'La próxima actualización traerá una temática navideña para llenar tus momentos de calma de espíritu festivo. Compartiremos la fecha exacta y todas las novedades más cerca del lanzamiento.' if es else 'The next update brings a Christmas theme to fill your quiet moments with a little holiday spirit. We’ll share the exact date and all the new details closer to launch.'}</p><a class="launch-current" href="#whats-new">{'Mientras tanto, descubre la versión 3.0.1 disponible ahora' if es else 'Meanwhile, explore version 3.0.1, available now'} <span aria-hidden="true">↓</span></a></div></div></section>
<section class="section" id="whats-new"><div class="wrap release"><div class="release-intro"><div class="eyebrow">{c['releaseEye']}</div><h2>{c['releaseTitle']}</h2><p>{c['releaseLede']}</p><a class="button secondary small" href="#collections">{c['releaseLink']}</a></div><div class="release-list">{updates}</div></div></section>
<section class="section collections" id="collections"><div class="wrap"><div class="section-head center"><div class="eyebrow">{c['collectionEye']}</div><h2>{c['collectionTitle']}</h2><p>{c['collectionLede']}</p></div><div class="collection-stats" aria-label="{'Biblioteca Legacy' if es else 'Legacy library'}"><div><strong>{len(LEGACY_CATALOG['packs'])}</strong><span>{'packs Legacy' if es else 'Legacy packs'}</span></div><div><strong>{sum(p['count'] for p in LEGACY_CATALOG['packs'])}</strong><span>{'diseños para descubrir' if es else 'designs to explore'}</span></div><div><strong>Premium</strong><span>{'Una compra, más formas de crear' if es else 'One purchase, more ways to create'}</span></div></div><div class="collection-grid">{collections}</div><p class="collection-note">{c['collectionNote']}</p></div></section>
<section class="section" id="explore"><div class="wrap"><div class="section-head"><div class="eyebrow">{c['modesEye']}</div><h2>{c['modesTitle']}</h2><p>{c['modesLede']}</p></div><div class="app-preview-toolbar"><button class="button secondary small" type="button" data-preview-motion aria-pressed="false" hidden>{'Pausar animaciones' if es else 'Pause animations'}</button></div><div class="modes-grid">{modes}</div>
<article class="journal"><div class="journal-art" aria-hidden="true"><img src="./assets/v25/bunny-pie-autumn.webp" width="400" height="500" alt="" loading="lazy" decoding="async"><img src="./assets/v25/koala-flowers-spring.webp" width="400" height="500" alt="" loading="lazy" decoding="async"></div><div><div class="eyebrow">{c['journalEye']}</div><h3>{c['journalTitle']}</h3><p>{c['journalText']}</p><div class="player"><button type="button" data-play aria-label="{c['play']}" aria-pressed="false">▶</button><span>{c['music']}</span><label class="sr-only" for="track">{c['trackLabel']}</label><select id="track" data-track><option value="./assets/song-1.mp3">Soft Focus</option><option value="./assets/song-2.mp3">Whispering Bamboo</option></select></div><audio preload="none" src="./assets/song-1.mp3"></audio><p class="fine" data-audio-status role="status"></p></div></article></div></section>
<section class="section" id="gallery" style="padding-top:0"><div class="wrap"><div class="section-head center"><div class="eyebrow">{c['galleryEye']}</div><h2>{c['galleryTitle']}</h2><p>{c['galleryLede']}</p></div><div class="gallery">{gallery}</div></div></section>
<section class="section ritual" id="new-year"><div class="wrap ritual-grid"><div><div class="eyebrow">{c['ritualEye']}</div><h2>{c['ritualTitle']}</h2><p>{c['ritualLede']}</p></div><div class="ritual-steps">{rituals}</div></div></section>
<section class="section" id="download"><div class="wrap download-panel"><div class="eyebrow">{c['downloadEye']}</div><h2>{c['downloadTitle']}</h2><p>{c['downloadText']}</p>{button()}<p class="fine">{c['downloadFine']}</p></div></section>
<section class="section history"><div class="wrap"><details><summary>{c['historyTitle']}</summary><div class="history-content"><img src="./assets/rzen-halloween-hero.webp" width="1200" height="800" alt="Cozy Halloween" loading="lazy" decoding="async"><div><div class="eyebrow">{c['historyEye']}</div><h3>{c['historyName']}</h3><p>{c['historyText']}</p><ul>{''.join(f'<li>{escape(x)}</li>' for x in c['historyBullets'])}</ul><a href="./rzen-history.html" class="button secondary small">{c['historyLink']}</a></div></div></details></div></section>
<section class="section" id="faq" style="padding-top:0"><div class="wrap"><div class="section-head center"><div class="eyebrow">{c['faqEye']}</div><h2>{c['faqTitle']}</h2></div><div class="faq">{faqs}</div></div></section>
</main>
<footer class="footer" id="contact"><div class="wrap"><div class="footer-top"><div><a class="brand" href="./index.html"><img src="./assets/logo.png" width="42" height="42" alt=""><span><strong>R-Zen</strong><small>Experience</small></span></a><p class="footer-message">{c['footerMessage']}</p></div><div class="footer-links">{''.join(f'<a href="./{path}">{label}</a>' for path,label in zip(['support.html','privacy-policy.html','terms-of-use.html'],c['footerLinks']))}<a href="mailto:xnerzogames@gmail.com">xnerzogames@gmail.com</a></div></div><div class="footer-bottom"><span>© 2026 R-Zen Experience. {c['rights']}</span><a href="./index.html">{c['studio']} ↗</a><span><a href="https://instagram.com/rnxgamesstudio/" rel="noopener" target="_blank">Instagram</a> · <a href="https://x.com/_rnxgames_" rel="noopener" target="_blank">X</a> · <a href="https://tiktok.com/@_rnxgames_" rel="noopener" target="_blank">TikTok</a></span></div></div></footer>
<dialog class="lightbox" id="screenshot-dialog" aria-label="{'Vista ampliada de R-Zen' if es else 'Enlarged R-Zen screenshot'}"><form method="dialog"><button>{c['close']} ×</button></form><img alt=""></dialog>
</body></html>
'''
 (ROOT / filename).write_text(content, encoding='utf-8')

if __name__ == '__main__':
 for language in COPY: build(language)
