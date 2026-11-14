# Colecciones Legacy incluidas con Premium

La sección de Premium muestra cinco packs Legacy de contenido permanente: Estelar (95), Extra Número (59), Zodíaco (13), Zodíaco Pixel (13) y Zodíaco Chibi (13). Total: 193 diseños, sin contar dos veces las obras que tienen modos Colorear y Revelar.

Las cinco tarjetas avanzan automáticamente cada seis segundos y vuelven a la primera al terminar. El avance se pausa mientras el ratón está encima, hay foco de teclado dentro, la pestaña está oculta o el carrusel está fuera de vista. Tocar, arrastrar o usar los controles lo pausa hasta pulsar Reanudar carrusel. Con movimiento reducido, el avance automático queda desactivado. Conserva desplazamiento táctil nativo, arrastre con ratón, flechas, puntos de selección e indicador de posición. El contenedor admite flechas de teclado, Inicio y Fin. Al cambiar de tamaño conserva el pack seleccionado. Sin JavaScript, se mantiene el desplazamiento horizontal nativo; los controles mejorados se muestran al inicializarse el script.

Selección contrastada con el registro real de la app, leído sin modificarla, y con los cinco manifiestos publicados en `RnxGames/rzen-packs`, ref `3f1c599e78e80ab71ea52644f4b648fe3edf7dfe`. Sus contenidos coinciden con las cantidades mostradas. `assets/legacy-packs/catalog.json` conserva los IDs, modos, cantidades y referencias necesarias para generar las tarjetas.

Día de Muertos y Noches Noir no se incluyen porque el registro actual los sitúa en Nuevos. Halloween, aunque figura como Legacy en ese registro, se conserva en el archivo histórico por ser temático de temporada y por el criterio editorial solicitado. Las menciones históricas a la actualización 3.0 permanecen como historial de lanzamiento.

Se copiaron tres portadas existentes de la app a este sitio. Las muestras de arte proceden de los packs; las de Pixel y Chibi se presentan por separado para distinguir ambos estilos. La preparación y optimización de las imágenes se hizo únicamente en el repositorio de la web.

```sh
python scripts/build-rzen-page.py
python scripts/check-rzen-site.py
python scripts/check-legacy-packs.py
```
