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
ballrect.move_ip(400,524)

# Crea el objeto bate, y obtengo su rectángulo
bate = pygame.image.load("barraladrillo.png")
baterect = bate.get_rect()

# Crea el objeto ladrillo 
brick = pygame.image.load("ladrillo.png")

"""LADRILLOS"""
# Definimos la clase para los ladrillos
class Brick:
    def __init__(self, x, y):                   # El método __init__ se utiliza para inicializar los atributos de un objeto
        self.rect = pygame.Rect(x, y, 50, 50)   # Se crea un rectángulo para representar el ladrillo en el juego, se especifican coordenadas(x,y), y el ancho y altura del rectángulo(50, 50)
        self.image = brick                      # Se asigna la imagen del ladrillo 

    def draw(self, surface):
        surface.blit(self.image, self.rect)     # Para dibujar la imagen del ladrillo(self.image), en la superficie de destino(surface) en la posición especificada por el rectángulo del ladrillo(self.rect)

# Función para generar ladrillos
def generate_bricks():
    bricks = []                   # Lista vacía que almacenará los ladrillos generados
    for row in range(5):          # Bucle for para iterar sobre cada fila de ladrillos
        for column in range(21):  # Bucle for dentro del otro para iterar sobre cada columna de ladrillos
            x = column * 60 + 15  # Esto calcula la coordenada x de cada ladrillo en función de la columna en la que se encuentre (El 60 es para el espacio horizontal entre los ladrillos y el 15 es para dejar margen en el lado izquierdo)
            y = row * 51 + 60     # Esto calcula la coordenada y de cada ladrillo en función de la fila en la que se encuentre (El 51 para el espacio vertical entre los ladrillos y el 60 es para dejar margen en la parte superior)
            bricks.append(Brick(x, y)) # Se crea el objeto Brick usando las coordenadas (x, y) calculadas y lo agrega a la lista bricks
    return bricks                 # Devuelve los ladrillos generados 

bricks = generate_bricks()
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
    """LADRILLOS"""
    # Comprobación de colisión de la pelota con los ladrillos
    for brick in bricks:
        if ballrect.colliderect(brick.rect):
            speed[1] = -speed[1] # Cambiar dirección vertical de la pelota
            bricks.remove(brick) # Eliminar el ladrillo de la lista
            break
    """..."""
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
    """LADRILLOS"""
    # Dibujo de los ladrillos
    for brick in bricks:
        brick.draw(ventana)
    """..."""
    # Todos los elementos del juego se vuelven a dibujar
    pygame.display.flip()

    # Controlamos la frecuencia de refresco (FPS)
    pygame.time.Clock().tick(60)


pygame.quit()