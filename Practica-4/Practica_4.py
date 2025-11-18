import pygame
import random

pygame.init()

pantalla = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Práctica 4 - Colisiones")

# Inicializacion de variables
vel = 5
ancho, alto = 40, 40
x, y = 300, 200 #Posicion inicial del jugador
jugador = pygame.Rect(x, y, ancho, alto) #El rect para colisiones y posicion

balas = []
aleatoriox = random.randint(0, 600 - 40)#Posicion x del enemigo
aleatorioy = random.randint(0, 400 - 40)#Posicion y del enemigo
enemigos = [pygame.Rect(aleatoriox, aleatorioy, 40, 40)]
contador_puntos = 0#Contamos los puntos de tiros al enemigo
clock = pygame.time.Clock()
running = True

fuente= pygame.font.SysFont("Consolas", 20)#Contador en pantalla
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            #Usamos jugador.x y jugador.y, que se actualizan mas abajo
            balas.append(pygame.Rect(jugador.x + 40, jugador.y + 15, 10, 5))#Las balas se dispararan dependiendo de la posicion del jugador

    teclas = pygame.key.get_pressed()
    velocidad_actual = vel

    if teclas[pygame.K_LSHIFT]:
        velocidad_actual = vel + 5#Boost de velocidad
    #movimiento de jugador
    if teclas[pygame.K_LEFT]:
        x -= velocidad_actual
    if teclas[pygame.K_RIGHT]:
        x += velocidad_actual
    if teclas[pygame.K_UP]:
        y -= velocidad_actual
    if teclas[pygame.K_DOWN]:
        y += velocidad_actual
    #Limite para que el jugador no salga de la pantalla
    if x < 0:
        x = 0
    if x + ancho > 600:
        x = 600 - ancho
    if y < 0:
        y = 0
    if y + alto > 400:
        y = 400 - alto

    jugador.x = x
    jugador.y = y

#################
    for b in balas:
        b.x += 10
    balas = [b for b in balas if b.x < 600] #para que no pase de la pantalla
    #colision de las balas al enemigo
    for b in balas[:]:
        for e in enemigos[:]:
            if b.colliderect(e):
                balas.remove(b)#Bala desaparace
                enemigos.remove(e)#Enemigo desaparece
                contador_puntos += 1#Se suma un punto en el contador
                print("contador de puntos: ", contador_puntos)#imprirmir en consola

                ###posicion nuevo del enemigo que puede ser en cualquier parte de la pantalla
                nuevox = random.randint(0, 600 - 40)
                nuevoy = random.randint(0, 400 - 40)
                enemigos.append(pygame.Rect(nuevox, nuevoy, 40, 40))


    pantalla.fill((0, 0, 0))#borramos rastros anteriores del fotograma
    pygame.draw.rect(pantalla, (2, 250, 250), (x, y, ancho, alto))

    for b in balas:
        pygame.draw.rect(pantalla, (255, 255, 0), b)
    for e in enemigos:
        pygame.draw.rect(pantalla, (255, 0, 0), e)

    texto_puntos = fuente.render("Puntos: " + str(contador_puntos), True, (255, 255, 255))

    # Dibujar el texto en la pantalla: (Superficie de texto, Posición X, Posición Y)
    pantalla.blit(texto_puntos, (5,5))
    pygame.display.update()

pygame.quit()
