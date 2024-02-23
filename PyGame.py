import pygame, os
import sys
from pygame import gfxdraw
from random import randint ##

# Inicialización de Pygame
pygame.init()

"""MARCO Y FONDO"""
ventana = pygame.display.set_mode((1280,900)) # Inicialización de la superficie de dibujo
pygame.display.set_caption("Juego")
fondo = pygame.image.load("fondojuego.png")   #Crea el objeto fondo

"""MUSICA DE FONDO"""
pygame.mixer.music.load('MUSICAMARIO.mp3')      #Cargamos el archivo de sonido.
pygame.mixer.music.play(-1)                     #Reproducimos de forma infinita la musica.


"""BATE"""
bate = pygame.image.load("barraladrillo.png") # Crea el objeto bate
baterect = bate.get_rect()                    # Obtengo el rectángulo del objeto anterior
baterect.move_ip(546,824)                     # Pongo el bate en la parte inferior de la pantalla

"""PELOTA"""
ball = pygame.image.load("LABOLA.png") # Crea el objeto pelota
ballrect = ball.get_rect()             # Obtengo el rectángulo del objeto anterior

speed_x = randint(5,8)    # Inicializo los valores con los que se va a mover la pelota en el eje x
speed_y = randint(5,8)    # Inicializo los valores con los que se va a mover la pelota en el eje y
speed = [speed_x,speed_y] # En cada ejecución la pelota tiene una velocidad distinta

ballrect.move_ip(400,524) # Pongo la pelota en la posición de inicio preestablecida.


"""LADRILLOS"""
brick = pygame.image.load("ladrillo.png") # Crea el objeto ladrillo

#Definimos la clase para los ladrillos
class Brick:
    def __init__(self, x, y):                   # El método __init__ se utiliza para inicializar los atributos de un objeto
        self.rect = pygame.Rect(x, y, 50, 50)   # Se crea un rectángulo para representar el ladrillo en el juego, se especifican coordenadas(x,y), y el ancho y altura del rectángulo(50, 50)
        self.image = brick                      # Se asigna la imagen del ladrillo 

    def draw(self, surface):
        surface.blit(self.image, self.rect)     # Para dibujar la imagen del ladrillo(self.image), en la superficie de destino(surface) en la posición especificada por el rectángulo del ladrillo(self.rect)

# Función para generar ladrillos
def generate_bricks():
    bricks = []                         # Lista vacía que almacenará los ladrillos generados
    for row in range(5):                # Bucle for para iterar sobre cada fila de ladrillos
        for column in range(21):        # Bucle for dentro del otro para iterar sobre cada columna de ladrillos
            x = column * 60 + 15        # Esto calcula la coordenada x de cada ladrillo en función de la columna en la que se encuentre (El 60 es para el espacio horizontal entre los ladrillos y el 15 es para dejar margen en el lado izquierdo)
            y = row * 51 + 60           # Esto calcula la coordenada y de cada ladrillo en función de la fila en la que se encuentre (El 51 para el espacio vertical entre los ladrillos y el 60 es para dejar margen en la parte superior)
            bricks.append(Brick(x, y))  # Se crea el objeto Brick usando las coordenadas (x, y) calculadas y lo agrega a la lista bricks
    return bricks                       # Devuelve los ladrillos generados
 

bricks = generate_bricks()
bloques = pygame.sprite.Group()  


"""LADRILLO REFORZADO"""

ladrilloR = pygame.image.load("ladrillomario.png") # Crea el objeto ladrillo

# Definimos la clase ladrillo reforzado
class LadrilloReforzado:
    def __init__(self, x, y):                   # El método __init__ se utiliza para inicializar los atributos de un objeto
        self.rect = pygame.Rect(x, y, 55, 55)   # Se crea un rectángulo para representar el ladrillo en el juego, se especifican coordenadas(x,y), y el ancho y altura del rectángulo(50, 50)
        self.image = ladrilloR                     # Se asigna la imagen del ladrillo 
        self.golpes = 2

    def golpear(self):
        self.golpes -= 1
        if self.golpes <= 0:
            self.eliminar()
        else:
            # Cambiar de color u otras acciones si es necesario
            pass

    def eliminar(self):
        # Eliminar el ladrillo de la lista o el grupo
        bloquesR.remove(self)

    def draw(self, surface):
        surface.blit(self.image, self.rect)     # Para dibujar la imagen del ladrillo(self.image), en la superficie de destino(surface) en la posición especificada por el rectángulo del ladrillo(self.rect)

# Función para generar ladrillos
def generar_ladrillosR():
    lista_ladrillosR = []                         # Lista vacía que almacenará los ladrillos generados
    for fila in range(1):                # Bucle for para iterar sobre cada fila de ladrillos
        for columna in range(11):        # Bucle for dentro del otro para iterar sobre cada columna de ladrillos
            x = columna * 120 + 13        # Esto calcula la coordenada x de cada ladrillo en función de la columna en la que se encuentre (El 60 es para el espacio horizontal entre los ladrillos y el 15 es para dejar margen en el lado izquierdo)
            y = fila * 51 + 312          # Esto calcula la coordenada y de cada ladrillo en función de la fila en la que se encuentre (El 51 para el espacio vertical entre los ladrillos y el 60 es para dejar margen en la parte superior)
            lista_ladrillosR.append(LadrilloReforzado(x, y))  # Se crea el objeto Brick usando las coordenadas (x, y) calculadas y lo agrega a la lista bricks
    return lista_ladrillosR                       # Devuelve los ladrillos generados
 

ladrillo_reforzado = generar_ladrillosR()
bloquesR = pygame.sprite.Group()


"""BUCLE DEL JUEGO"""
# Bucle principal del juego
jugando = True
while jugando:

    ventana.blit(fondo, (0, 0)) # Establezco en la ventana el fondo de pantalla elegido.
    
    for event in pygame.event.get(): # Comprobamos si se ha pulsado el botón de cierre de la ventana
        if event.type == pygame.QUIT:
            jugando = False


    """BATE"""
    ventana.blit(bate, baterect)    # Dibujo el bate

    keys = pygame.key.get_pressed() # Compruebo si se ha pulsado alguna tecla
    if keys[pygame.K_LEFT]:
        baterect = baterect.move(-7,0) # Si se ha pulsado la tecla de dirección izquierda, el bate se mueve en el eje x hacía la izquierda.

    if keys[pygame.K_RIGHT]:           # Si se ha pulsado la tecla de dirección derecha, el bate se mueve en el eje x hacía la derecha.
        baterect = baterect.move(7,0) 

    
    if keys[pygame.K_LEFT] and baterect.left < 0: # Cuando el bate pegue en la parte izquierda de la ventana, contrarrestamos la velocidad del bate.
        baterect = baterect.move(7,0)
    
    if keys[pygame.K_RIGHT] and baterect.right > ventana.get_width(): # Cuando el bate pegue en la parte derecha de la ventana, contrarrestamos la velocidad del bate.
        baterect = baterect.move(-7,0)

   
    """PELOTA"""
    ventana.blit(ball, ballrect)    # Dibujo la pelota

    ballrect = ballrect.move(speed) # Muevo la pelota

    if baterect.colliderect(ballrect): # Compruebo si hay colisión, si la hay, la velocidad de la pelota será la contraria al colisionar.
        speed[1] = -speed[1]

    
    if ballrect.left < 0 or ballrect.right > ventana.get_width():  # Si la pelota llega a los límites de la ventana en el eje x, cambia a la velocidad x contraria 
        speed[0] = -speed[0]

    if ballrect.top < 0 or ballrect.bottom > ventana.get_height(): # Si la pelota llega a los límites de la ventana en el eje y, cambia a la velocidad y contraria
        speed[1] = -speed[1]

   
    """LADRILLOS COLISIÓN"""
    # Comprobación de colisión de la pelota con los ladrillos
    for brick in bricks:
        if ballrect.colliderect(brick.rect):    # Si la pelota colisiona con un ladrillo
            speed[1] = -speed[1]                # Cambiar dirección vertical de la pelota
            bricks.remove(brick)                # Eliminar el ladrillo de la lista
            break
    
    for brick in bricks:                        # Dibujo de los ladrillos
        brick.draw(ventana)

    
    """LADRILLOS REFORZADOS COLISIÓN"""
    # Comprobación de colisión de la pelota con los ladrillos
    for ladrilloR in ladrillo_reforzado:
        cont = 0
        if ballrect.colliderect(ladrilloR.rect):    # Si la pelota colisiona con un ladrillo
            cont += 1
            speed[1] = -speed[1]                # Cambiar dirección vertical de la pelota
            if cont == 2:
                ladrillo_reforzado.remove(ladrilloR)                # Eliminar el ladrillo de la lista
                break

    for ladrilloR in ladrillo_reforzado:                        # Dibujo de los ladrillos
        ladrilloR.draw(ventana)

    """GAME OVER Y CERRAR JUEGO"""
    fuente = pygame.font.Font(None, 80) 
    if ballrect.bottom > ventana.get_height():                      # Compruebo si la pelota toca la parte inferior y si es asi, game over en la pantalla.
        texto = fuente.render("Game Over", True, (255, 0, 0))
        texto_rect = texto.get_rect()
        texto_x = ventana.get_width() / 2 - texto_rect.width / 2
        texto_y = ventana.get_height() / 2 - texto_rect.height / 2
        ventana.blit(texto, [texto_x, texto_y])
        pygame.display.flip()
        pygame.time.delay(10000)                                    # Espera 10 segundos antes de salir
        jugando = False                                             #Esto hace que el juego se cierre asi no vuelve a inicia

    
    """OTRAS PARTES DEL CODIGO"""
    pygame.display.flip()           # Todos los elementos del juego se vuelven a dibujar
    pygame.time.Clock().tick(60)    # Controlamos la tasa de refresco (FPS)

pygame.quit()