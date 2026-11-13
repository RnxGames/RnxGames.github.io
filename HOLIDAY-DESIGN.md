# R-Zen 3.0.1 · Navidad 2026 / Año Nuevo 2027

La página comercial `r-zen.html` y su versión española `r-zen-es.html` contienen HTML completo. La navegación, los textos, los enlaces de descarga y los desplegables funcionan sin el runtime de plantillas anterior. JavaScript añade el tema persistente, el menú móvil, la muestra de música y la ampliación de capturas.

## Contenido verificado

- App local `ren-zen`, commit `753f1d08d6c586ba9cf87947440d4f46b9b30acf`: versión 3.0.1, galerías de puzzles con miniaturas y carga de imágenes visibles para reducir memoria y recargas.
- `RELEASE-NOTES-3.0.1.md`, `releases/3.0/LEEME.md` y `data/rzen-whatsnew.js`: Noches Noir, Día de Muertos, cartas coleccionables de Color mágico y carruseles de temporada.
- El repositorio de la web ya señalaba 3.0.1 como versión publicada en `rzen-update.json`, commit `0a7cb5b`.
- El diseño navideño pertenece a la web. No se anuncia contenido navideño inexistente en la app.
- Halloween queda en un desplegable de capítulos anteriores. `rzen-history.html` conserva la presentación estacional anterior, marcada como archivo y excluida de indexación para evitar títulos antiguos en búsquedas.
- La portada `index.html` incorpora una entrada a la edición navideña y referencias a 3.0.1.

## Editar y comprobar

Editar textos y estructura en `scripts/build-rzen-page.py`, estilos en `assets/rzen-holiday.css` e interacciones en `assets/rzen-holiday.js`.

```sh
python scripts/build-rzen-page.py
python scripts/check-rzen-site.py
node --check assets/rzen-holiday.js
git diff --check
python -m http.server 8123 --bind 127.0.0.1
```

Los HTML generados se versionan: GitHub Pages no necesita ejecutar Python. Al cambiar CSS/JS, actualizar el identificador de versión de sus URLs en el generador para invalidar las cachés.

Comprobaciones: HTML estático legible, idioma y canonical propios, hreflang recíproco, metadatos sociales, schema versión 3.0.1, archivos y anclas locales, texto alternativo y contraste mínimo 4,5:1 en los pares principales de texto y botones. Revisión en navegador a 320, 390, 768 y 1280 píxeles; menú, navegación por secciones, idioma, conservación del tema, música y diálogo de capturas con Escape y devolución de foco.

## Arte y assets

Generación con la herramienta integrada ImageGen, sin CLI ni llamadas de API propias. Los WebP están dentro del proyecto y la tarjeta social JPG mide 1200 × 630. Los banners `assets/v3/` son recursos existentes de la app. Las capturas `assets/v2/` son las imágenes reales conservadas de la web anterior; se presentan como vistas de la app, sin etiquetarlas como capturas de 3.0.1.

### Prompt final de la imagen nocturna

Use case: illustration-story. Asset type: wide premium website seasonal hero illustration for a relaxing coloring and jigsaw app, R-Zen. Primary request: a beautifully hand-painted winter holiday retreat, Christmas and New Year atmosphere. Scene: a cozy tiny cabin with warmly glowing arched windows beside a still alpine lake, snow-covered fir forest, elegant small Christmas tree with warm fairy lights, a few golden stars reflected in water, quiet snow, distant mountains. Style: sophisticated storybook gouache illustration with fine painterly texture and lush botanical detail, editorial art, calm and spacious, not childish, not photorealistic. Composition: wide landscape 3:2, cabin and illuminated tree in the right half, water and sky provide serene breathing space, foreground evergreen branches frame corners. Mood: midnight teal and blue with amber golden light, magical and restful. No text, numbers, typography, logos, UI, people, watermark. This is atmospheric website artwork, not a screenshot of app content.

### Prompt final de la variante diurna

Use case: lighting-weather. Edit this website holiday illustration to make its matching LIGHT MODE daytime variant. Preserve the composition, identical cabin, tree, lake, mountain and forest placement and painterly gouache style. Change only lighting, sky and palette: bright soft winter morning, pale ivory blue sky, sunlit creamy snow, natural deep evergreen pines, warm golden window and Christmas lights still gently glowing. Welcoming, airy and sophisticated, restrained festive red berries. No added objects, text, numbers, logos or watermark. Retain wide landscape framing.

Archivos finales: `assets/holiday/winter-night.webp`, `assets/holiday/winter-day.webp`, `assets/holiday/social-card.jpg`.
