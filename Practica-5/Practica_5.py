import pygame
pygame.init()

pantalla = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Práctica 5 - Sprites y fondo")

fondo = pygame.image.load("fondo.png")
fondo = pygame.transform.scale(fondo, (800, 800))

sprite_original = pygame.image.load("personaje.png")
sprite = pygame.transform.scale(sprite_original, (80, 80))
sprites = [sprite, sprite, sprite, sprite]

frame = 0
x = 50
y = 800 - 130 - 110
clock = pygame.time.Clock()
running = True

scroll_x = 0
#salto
vel_y = 0
en_suelo = True
gravedad = 1
#disparos
balas = []

while running:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    moving = False

    if keys[pygame.K_RIGHT]:
        x += 5
        frame = (frame + 1) % len(sprites)
        scroll_x -= 5
        moving = True

    if keys[pygame.K_LEFT]:
        x -= 5
        frame = (frame + 1) % len(sprites)
        scroll_x += 5
        moving = True

    if keys[pygame.K_SPACE] and en_suelo:
        vel_y = -18
        en_suelo = False

    vel_y += gravedad
    y += vel_y

    if y >= 800 - 130 - 110:#suelo
        y = 800 - 130 - 110
        vel_y = 0
        en_suelo = True

    #disparos con z
    if keys[pygame.K_y]:
        balas.append(pygame.Rect(x + 70, y + 30, 10, 5))

    for b in balas:
        b.x += 10
        pygame.draw.rect(pantalla, (255, 255, 0), b)

    balas = [b for b in balas if b.x < 800]

    if scroll_x <= -800:
        scroll_x = 0
    if scroll_x >= 800:
        scroll_x = 0

    pantalla.blit(fondo, (scroll_x, 0))
    pantalla.blit(fondo, (scroll_x + 800, 0))

    if moving:
        y_offset = (frame % 6) - 3
    else:
        y_offset = 0

    pantalla.blit(sprites[frame], (x, y + y_offset))

    pygame.display.update()

pygame.quit()

