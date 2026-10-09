# Luma (@3dluma.cba) - contexto para Claude

Este archivo se lee solo al abrir una sesión en este repo. Todo lo que está acá lo armó otra sesión de Claude con el dueño. No hace falta que el dueño lo repita.

## Quién es el dueño y cómo hablarle
- Fabri. Tiene "Luma": lámparas y accesorios de deco impresos en 3D, Córdoba, Argentina.
- Instagram: @3dluma.cba. Web: https://lumacba.netlify.app/
- Se abruma con respuestas largas. Respondé corto, simple, en español rioplatense (voseo), sin emojis. Una sola pregunta por vez.
- No es técnico. Los pasos que tenga que hacer él, explicalos uno por uno.

## Marca
- Colores: amarillo #FFD60A, negro #0B0B0B, crema #FFF1B8, blanco.
- Fuente: Bricolage Grotesque 800 (archivo en fuentes/bric800.ttf). Google Fonts está bloqueado en el sandbox, usá el archivo local.
- Estilo: casual, cálido, con movimiento, stickers tipo die-cut con borde blanco. Pocas palabras en pantalla.
- Producto estrella: lámpara de mesa con pantalla cilíndrica amarilla de textura tejida y patas de madera (trípode). Foto real: fotos/lampara-real-foto.png (720x1280). Recortes: recursos/lamp_core.png, lamp_outline.png, tex.png.
- Otros objetos que se muestran: maceta, florero, colgante, portavelas, esfera (recursos/objetos).
- Cuando haya más fotos reales del dueño, usarlas siempre por encima de ilustraciones.

## Publicar en Instagram (lo más importante)
Se publica con el conector Windsor.ai (cuenta de Instagram ya conectada; buscá el id con get_connectors, conector `instagram`).
1. Generar la imagen en 1080x1920, guardar como JPEG (calidad ~90, menos de 8 MB) en `publicar/` con nombre `AAAA-MM-DD-tema.jpg`.
2. Hacer commit y push al branch main de este repo (el repo es público a propósito: Instagram necesita una URL pública).
3. URL pública: `https://raw.githubusercontent.com/<usuario>/<repo>/main/publicar/<archivo>.jpg`. Si Instagram la rechaza, probar `https://cdn.jsdelivr.net/gh/<usuario>/<repo>@main/publicar/<archivo>.jpg`. Comprobar antes con curl que devuelve 200 y content-type image/jpeg.
4. `mcp__Windsor_ai__list_actions` para ver el esquema exacto, y después `execute_action` con connector `instagram`, action `create_story`, params `{"image_url": "<URL>"}`.
- Otras acciones: create_image_post (aspecto entre 4:5 y 1.91:1, con caption), create_carousel_post (2 a 10 imágenes), create_video_post (Reels MP4, 3 s a 15 min), create_comment, reply_to_comment, hide/unhide/delete_comment.
- Historias por API: imagen JPEG o video MP4/MOV de 3 a 60 s, 9:16. NO se pueden poner stickers interactivos (encuesta, pregunta), música, enlaces ni colaboraciones. Eso lo hace el dueño a mano. Para pedir interacción, escribir en la imagen algo como "respondé con tu número" (la gente responde por mensaje directo).
- Windsor pide confirmación del usuario antes de acciones de escritura. El dueño autorizó expresamente que se publiquen historias en @3dluma.cba desde este repo. Solo historias; para posts de feed o Reels, preguntarle antes.

## Cómo se generaron las imágenes y videos (herramientas/)
- Se dibuja en HTML/SVG, se captura con Playwright + Chromium (`executable_path='/opt/pw-browsers/chromium'`), y los videos se arman con ffmpeg (libx264, yuv420p, crf 18, 30 fps, 1080x1920).
- Los scripts son de otro sandbox: tienen rutas viejas (por ejemplo `os.chdir('/tmp/...')`). Cambiá las rutas a las de este repo antes de correrlos.
- herramientas/historias-estaticas/build.py: historias con la foto real. herramientas/animaciones/: 5 videos animados (anim1 a anim5, cada uno con su ranimN.py). herramientas/logo/: stickers y logo.
- Recortar la lámpara de una foto: rembg solo detecta la pantalla; patas, zócalo y cable se completan con polígonos a mano (cv2). Por eso conviene reutilizar recursos/lamp_core.png.
- historias-hechas/: ejemplos de lo ya creado para mantener el mismo estilo.

## Qué ya se publicó o se mostró (no repetir)
- Ya subida: "tu rincón merece esta luz" (foto de la lámpara con texto grande). No volver a hacerla.
- El resto de historias en historias-hechas/ no están confirmadas como publicadas. Antes de elegir tema, mirar las últimas publicaciones con Windsor (get_data de instagram, medios recientes) y evitar repetir lo de los últimos 14 días.

## Estado de la cuenta (a 8-oct-2026)
- 1.280 seguidores, 30 publicaciones, unos 98 seguidores nuevos en 30 días.
- Los picos de seguidores vinieron de días puntuales (9-10 y 23-24 de septiembre), con mucho alcance.
- Objetivo del dueño: crecer entre 1.000 y 2.000 seguidores en 2 semanas (hay un plan armado en un documento aparte; ser realista con él). Las historias casi no reciben votos ni respuestas, por eso conviene pedir interacción simple.
- Fecha clave: Día de la Madre en Argentina, domingo 18 de octubre de 2026.

## Rutina diaria deseada
El dueño quiere despertarse y ver una historia nueva ya publicada. Cada día:
1. Elegir tema según el día (sugerencia, ajustable): lunes producto, martes "¿cuál te llevás?", miércoles proceso de impresión, jueves idea de regalo / Día de la Madre, viernes novedad u oferta, sábado detrás de escena, domingo inspiración de rincón.
2. Generar la imagen, subirla a publicar/, publicarla como historia.
3. Dejar al dueño un resumen de una línea: qué se publicó y a qué hora.
- No inventar precios, descuentos, stock ni plazos de entrega. Si hace falta un dato, preguntárselo al dueño o no mencionarlo.
- Si algo falla (URL, permisos, Windsor), no insistir: dejar la imagen lista en publicar/ y avisar en una línea qué falló.

## Historias diarias automáticas (orden del dueño, vigente)
Cada día se publican TRES historias en @3dluma.cba, todas con autorización permanente del dueño (no pedir confirmación). Solo aplica a estas historias; cualquier otra publicación (feed, Reels, respuestas, comentarios) sí requiere su confirmación.

1. 8:00 (hora Argentina): "buen <día>". Script: herramientas/historia-diaria/diaria.py. Ej.: buen viernes, buen sábado. Diseño: fondo amarillo, lámpara con estrella, frase corta abajo, "luma" chiquito arriba.
2. 15:04: historia para que respondan (cambia cada día). Script: herramientas/historia-diaria/tarde_noche.py tarde. Son 5 variantes que rotan: "¿cuál te llevás?", "¿de qué color?", "¿la querés?", "¿qué rincón te falta?", "¿prendida o apagada?".
3. 20:17: historia de ambiente de noche (cambia cada día). Script: herramientas/historia-diaria/tarde_noche.py noche. Son 5 variantes: "ya es de noche. ¿la prendés?", "fin del día.", "apagá la luz grande.", "buenas noches.", "luz cálida para cerrar el día.".

Formato común: fondo amarillo (mañana y tarde) o negro con brillo amarillo (noche), "luma" chiquito arriba, texto grande y una línea de respuesta abajo. Nada de links, precios, promociones, ni "lámparas 3D".

Cómo se hace cada una (igual para las tres, cambiando el comando y la hora):
1. Generar el PNG con el script. Ejemplos desde la raíz del repo:
   python3 herramientas/historia-diaria/diaria.py publicar/AAAA-MM-DD-manana.png AAAA-MM-DD
   python3 herramientas/historia-diaria/tarde_noche.py tarde publicar/AAAA-MM-DD-tarde.png AAAA-MM-DD
   python3 herramientas/historia-diaria/tarde_noche.py noche publicar/AAAA-MM-DD-noche.png AAAA-MM-DD
   Después convertir a JPEG 1080x1920 con Pillow, borrar el PNG y el SVG.
2. Commit y push al branch main. URL: https://raw.githubusercontent.com/fabriscar/Luma-CBA/main/publicar/<archivo>.jpg (verificar 200).
3. Windsor: connector `instagram`, account 17841439121158917, action `create_story`, params `{"image_url": "<URL>"}`.
4. Si algo falla, no insistir ni publicar otra cosa: dejar el archivo en publicar/ y anotar el error en el commit.
