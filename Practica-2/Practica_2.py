import pygame
pygame.init()

pantalla = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Práctica 2 - Saltos")

x, y = 300, 300
vel_y = 0
gravedad = 1
en_suelo = True
clock = pygame.time.Clock()
saltos = 0
saltamos = False
tiempo_tecla_presionada= 0
max_tiempo_tecla_presionada = 15

running = True
while running:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if en_suelo:#primer salto
                    vel_y = -15
                    en_suelo = False
                    saltos = 1
                    saltamos=True
                    tiempo_tecla_presionada = 0

                elif saltos < 2:#segundo salto
                    vel_y = -8
                    saltos += 1
                    saltamos=True
                    tiempo_tecla_presionada = 0

    teclas = pygame.key.get_pressed()

    if saltamos and teclas[pygame.K_SPACE] and tiempo_tecla_presionada < max_tiempo_tecla_presionada:
        vel_y -= 1 #sube un poco mas
        tiempo_tecla_presionada += 1
    else:
        saltando = False #sino cumple la condicion anterior, caera normal

    y += vel_y
    vel_y += gravedad

    if y >= 300:
        y = 300
        vel_y = 0
        en_suelo = True
        saltos = 0#reiniciamos el contador

    pantalla.fill((50, 50, 100))
    pygame.draw.rect(pantalla, (255, 255, 0), (x, y, 40, 40))
    pygame.draw.rect(pantalla, (100, 100, 50), (0, 341, 600,2))#Creamos el suelo
    pygame.display.update()

pygame.quit()
