import pygame
import os
pygame.init()

ANCHO, ALTO = 640, 480
VENTANA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Animación Direccional con carpetas")

def cargar_frames(ruta_carpeta, tam=(64, 64)):
    frames = []
    for archivo in sorted(os.listdir(ruta_carpeta)):
        if archivo.endswith(".png"):
            img = pygame.image.load(os.path.join(ruta_carpeta, archivo)).convert_alpha()
            img = pygame.transform.scale(img, tam)
            frames.append(img)
    return frames

base = "assets/images/characters/direcciones"

animaciones = {
    "arriba": cargar_frames(os.path.join(base, "atras"), tam=(80, 80)),
    "abajo": cargar_frames(os.path.join(base, "enfrente"), tam=(80, 80)),
    "izquierda": cargar_frames(os.path.join(base, "izquierda"), tam=(80, 80)),
    "derecha": cargar_frames(os.path.join(base, "derecha"), tam=(80, 80)),
    "quieto": cargar_frames(os.path.join(base, "quieto"), tam=(80, 80))
}

x, y = ANCHO//2,ALTO // 2
velocidad = 3
direccion = "quieto"
direccion_anterior = direccion

frame_index = 0
ultimo_tiempo= pygame.time.get_ticks()
tiempo_animacion =150
reloj =pygame.time.Clock()

ejecutando = True
while ejecutando:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecutando = False

    teclas = pygame.key.get_pressed()
    moviendo = False

    #detectar movimiento
    if teclas[pygame.K_UP]:
        y -= velocidad
        direccion = "arriba"
        moviendo = True
    elif teclas[pygame.K_DOWN]:
        y += velocidad
        direccion = "abajo"
        moviendo = True
    elif teclas[pygame.K_LEFT]:
        x -= velocidad
        direccion = "izquierda"
        moviendo = True
    elif teclas[pygame.K_RIGHT]:
        x += velocidad
        direccion = "derecha"
        moviendo = True
    else:
        direccion = "quieto"

    if direccion != direccion_anterior:
        frame_index = 0
        direccion_anterior = direccion

    ahora = pygame.time.get_ticks()
    if ahora - ultimo_tiempo > tiempo_animacion:
        frame_index = (frame_index + 1) % len(animaciones[direccion])
        ultimo_tiempo = ahora

    VENTANA.fill((90, 150, 255))
    VENTANA.blit(animaciones[direccion][frame_index], (x, y))
    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
