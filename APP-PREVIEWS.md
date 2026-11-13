# Animaciones copiadas de R-Zen

Se copiaron únicamente recursos de presentación: mandala giratorio, ilustración flotante, revelado, Color mágico, Por número, Cobra vida, dibujo libre y las tres animaciones de selección de puzzle (clásico, deslizar e intercambiar).

La lectura se hizo desde una copia local estable de `index.html`, mientras otro agente trabajaba en la app. No se modificaron archivos de la app ni se ejecutaron sus scripts, servidor, build o comandos Git. La copia temporal completa queda fuera de este repositorio; aquí solo se publican los fragmentos de presentación necesarios.

- `assets/app-previews.css`: reglas originales de presentación y 22 keyframes con sus curvas y duraciones.
- `assets/app-previews/`: seis imágenes originales, fragmentos HTML y hashes de procedencia.
- `assets/app-preview-layout.css`: encuadre y tamaños de la web, controles de preview y pausa.
- `assets/rzen-holiday.js`: pausa/reanudación, elección de los tres puzzles, suspensión fuera de pantalla y respeto a movimiento reducido.

Los botones de las tarjetas de la app y sus enlaces a partidas se eliminan. Las vistas son demostraciones visuales: no importan el runtime, las compras, el progreso ni los datos personales de la app.

Las ocho tarjetas de la web incluyen ahora también Revelar y Dibujo libre. Los controles de puzzle seleccionan únicamente qué animación se muestra. Los efectos se detienen fuera de pantalla, al ocultar la pestaña o al pulsar Pausar. El ajuste del sistema de movimiento reducido muestra vistas estáticas y conserva el arte a color.

## Comprobación

```sh
python scripts/build-rzen-page.py
python scripts/check-rzen-site.py
python scripts/check-app-previews.py
node --check assets/rzen-holiday.js
```

Para volver a importar, proporcionar explícitamente un snapshot estable y un directorio de assets de solo lectura a `scripts/import-app-previews.py`. El importador escribe únicamente en este repositorio. No se debe apuntar la salida ni iniciar procesos dentro del proyecto de la app.
