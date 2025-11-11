import pygame

pygame.init()
pantalla = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Práctica 1 - Movimiento básico")

x, y = 300, 200
vel = 5
clock = pygame.time.Clock()
ancho, alto = 40, 40
running = True

while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        x -= vel
    if teclas[pygame.K_RIGHT]:
        x += vel
    if teclas[pygame.K_UP]:
        y -= vel
    if teclas[pygame.K_DOWN]:
        y += vel
    if teclas[pygame.K_LSHIFT]:
        print("Tecla shift presionada")

    #Aumentamos la velocidad a la derecha
    if teclas[pygame.K_RIGHT] and teclas[pygame.K_LSHIFT]:
        x += vel+2
    if teclas[pygame.K_RIGHT] and teclas[pygame.K_LSHIFT]:
        if pygame.KEYUP:
             x += vel
        print('Ambas teclas son presionadas')
    # Aumentamos la velocidad a la izquierda
    if teclas[pygame.K_LEFT] and teclas[pygame.K_LSHIFT]:
        x -= vel + 2
    if teclas[pygame.K_LEFT] and teclas[pygame.K_LSHIFT]:
        if pygame.KEYUP:
            x -= vel
        print('Ambas teclas son presionadas')
    # Aumentamos la velocidad hacia arriba
    if teclas[pygame.K_UP] and teclas[pygame.K_LSHIFT]:
        y -= vel + 2
    if teclas[pygame.K_UP] and teclas[pygame.K_LSHIFT]:
        if pygame.KEYUP:
            y -= vel
        print('Ambas teclas son presionadas')
    # Aumentamos la velocidad Hacia abajo
    if teclas[pygame.K_DOWN] and teclas[pygame.K_LSHIFT]:
        y += vel + 2
    if teclas[pygame.K_DOWN] and teclas[pygame.K_LSHIFT]:
        if pygame.K_DOWN:
            y += vel
        print('Ambas teclas son presionadas')
    #limites para que el cuadrado no se pase de la pantalla establecida
    if x < 0:
        x = 0
    if x + ancho > 600:
        x = 600 - ancho
    if y < 0:
        y = 0
    if y + alto > 400:
        y = 400 - alto

    pantalla.fill((30, 30, 30))
    pygame.draw.rect(pantalla, (250,250,250), (x, y, ancho, alto)) #Cambamos color del personaje
    #Creamos las paredes
    pygame.draw.rect(pantalla, ( 0,255, 0), (0, 398, 600,2))
    pygame.draw.rect(pantalla, (0, 255, 0), (0, 1, 2, 400))
    pygame.draw.rect(pantalla, (0, 255, 0), (0, -1, 600, 3))
    pygame.draw.rect(pantalla, (0, 255, 0), (598, 5, 1, 390))
    pygame.display.update()

pygame.quit()