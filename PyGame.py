import pygame, os
import sys
from pygame import gfxdraw
from random import randint ##

# Inicialización de Pygame
pygame.init()

# Inicialización de la superficie de dibujo
ventana = pygame.display.set_mode((1280,900))
pygame.display.set_caption("Juego")

# Crea el objeto pelota
ball = pygame.image.load("LABOLA.png")

# Obtengo el rectángulo del objeto anterior
ballrect = ball.get_rect()

# Inicializo los valores con los que se van a mover la pelota

speed_x = randint(3,6)
speed_y = randint(3,6)

speed = [speed_x,speed_y] # En cada ejecución la pelota tiene una velocidad distinta

# Pongo la pelota en el origen de coordenadas
ballrect.move_ip(0,0)

# Crea el objeto bate, y obtengo su rectángulo
bate = pygame.image.load("barraladrillo.png")
baterect = bate.get_rect()

# Crea el objeto ladrillo y obtengo su rectangulo
brick = pygame.image.load("ladrillomario.png")
brickrect = brick.get_rect()


GREEN = (0,255,0)
"""LADRILLO"""
# Definimos la clase ladrillo.

"""class Bloque(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("ladrillomario.png")
        self.rect = self.image.get_rect(topleft=(x, y))"""

"""class Ladrillo(pygame.sprite.Sprite):
    def __init__(self, x, y):       # Contructor de la clase ladrillo.
        self.x = x
        self.y = y
        
    def update(self):
        pygame.draw.rect(ventana, GREEN, (self.x, self.y, 60,20))
        self.rect = pygame.Rect(self.x, self.y, 60,20)
#         super() .__init__(self)                 # Herencia de otra clase."""

# # Inicialización de otros objetos MIRAR ESTO!!!!!
#         self.image = pygame.image.load("ladrillo.png")
#         #os.path.join("resources", "images", "ladrillo.png")
#         self.rect = self.image.get_rect(x = x, y = y)
#         self.puntos = puntos(x = 560, y = 860)
"""..."""

# Pongo el bate en la parte inferior de la pantalla
baterect.move_ip(546,824)                                #MODIFICAR PARA CENTRAR 546

#Ejercicio 2: Aceleración de la pelota cada cierto golpes con la barra
#Creamos un contador de colisiones entre la pelota y la barra
cont_golpes = 0

fuente = pygame.font.Font(None, 80) 
"""LADRILLO"""
bloques = pygame.sprite.Group()  
"""."""
# Bucle principal del juego
jugando = True
while jugando:
    
    # Comprobamos los eventos

    # Comprobamos si se ha pulsado el botón de cierre de la ventana
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False

    # Compruebo si se ha pulsado alguna tecla
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        baterect = baterect.move(-6,0)
    if keys[pygame.K_RIGHT]:
        baterect = baterect.move(6,0)

    # Compruebo si hay colisión
    if baterect.colliderect(ballrect):
        speed[1] = -speed[1]
        cont_golpes += 1

    # Al llegar el contador a 5 golpes y al tocar el borde la velocidad de la pelota se suma 2
    if cont_golpes == 5 and ballrect.top < 0:
        speed = [speed_x +2 ,speed_y +2 ]

    # Muevo la pelota
    ballrect = ballrect.move(speed)

    # Compruebo si la pelota llega a los límites de la ventana
    if ballrect.left < 0 or ballrect.right > ventana.get_width():
        speed[0] = -speed[0]
            
    if ballrect.top < 0 or ballrect.bottom > ventana.get_height():
        speed[1] = -speed[1]

    # Cuando el bate pegue en la parte izquierda de la ventana, contrarrestamos la velocidad del bate.
    if keys[pygame.K_LEFT] and baterect.left < 0:
        baterect = baterect.move(6,0)
    # Cuando el bate pegue en la parte derecha de la ventana, contrarrestamos la velocidad del bate.
    if keys[pygame.K_RIGHT] and baterect.right > ventana.get_width():
        baterect = baterect.move(-6,0)

    """GAME OVER Y CERRAR JUEGO"""
    # Compruebo si la pelota toca la parte inferior y si es asi, game over en la pantalla.
    if ballrect.bottom > ventana.get_height():
        texto = fuente.render("Game Over", True, (255, 0, 0))
        texto_rect = texto.get_rect()
        texto_x = ventana.get_width() / 2 - texto_rect.width / 2
        texto_y = ventana.get_height() / 2 - texto_rect.height / 2
        ventana.blit(texto, [texto_x, texto_y])
        pygame.display.flip()
        pygame.time.delay(10000)  # Espera 10 segundos antes de salir
        jugando = False #Esto hace que el juego se cierre asi no vuelve a iniciar
    """..."""

    # Se pinta la ventana con un color
    # Esto borra los posibles elementos que teníamos anteriormente
    ventana.fill((124, 192, 201))

    # Dibujo la pelota
    ventana.blit(ball, ballrect)

    # Dibujo el bate
    ventana.blit(bate, baterect)

    # Dibujo los bloques
    bloques.draw(ventana)

    # Actualizo los bloques (por si necesitan actualización)
    bloques.update()

    # Todos los elementos del juego se vuelven a dibujar
    pygame.display.flip()

    # Controlamos la frecuencia de refresco (FPS)
    pygame.time.Clock().tick(60)

pygame.quit()