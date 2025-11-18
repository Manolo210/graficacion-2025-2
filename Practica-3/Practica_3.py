import pygame
pygame.init()
pygame.mixer.init()#usamos este modulo

pygame.mixer.music.load("arcane.mp3")#Agregamos musica

pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1) #Repetir infinitamente

pantalla = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Práctica 3 - Disparos")


x, y = 50, 300
balas = []
clock = pygame.time.Clock()
running = True
velocidad_balas = 10

while running:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        keys = pygame.key.get_pressed()
        if event.type == pygame.KEYDOWN:
            if keys[pygame.K_LSHIFT] and keys[pygame.K_SPACE]:
                balas.append((pygame.Rect(x + 40, y + 15, 10, 5), velocidad_balas + 10, "derecha"))#Modificamo la velocidad de bala
            elif keys[pygame.K_UP] and keys[pygame.K_SPACE]:
                balas.append((pygame.Rect(x + 25, y - 5, 10, 5), velocidad_balas, "arriba"))
            elif keys[pygame.K_DOWN] and keys[pygame.K_SPACE]:
                balas.append((pygame.Rect(x + 25, y + 45, 10, 5), velocidad_balas, "abajo"))
            elif event.key == pygame.K_SPACE:
                 balas.append((pygame.Rect(x + 40, y + 15, 10, 5), velocidad_balas,"derecha"))
    #Mover balas
    for i in range(len(balas)):
        rect, vel, direccion = balas[i]
        if direccion == "derecha":
            rect.x += vel
        elif direccion == "arriba":
            rect.y -= vel #restar para subir
        elif direccion == "abajo":
            rect.y += vel #sumar para bajar
        balas[i] = (rect, vel, direccion)
#Para que no se pasen de la pantalla
    balas = [b for b in balas if 0 <= b[0].x <= 600 and 0 <= b[0].y <= 400]


    pantalla.fill((20, 20, 20))#borramos rastros de los fotogramas
    pygame.draw.rect(pantalla, (0, 255, 0), (x, y, 40, 40))
    for rect, vel, direccion in balas:
        pygame.draw.rect(pantalla, (255, 0, 0), rect)

    pygame.display.update()#Actualizamos pantalla

pygame.quit()
