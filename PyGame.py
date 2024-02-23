import pygame               # Importamos la librería pygame
from random import randint  # Importamos la función randint

"""CLASE LADRILLO"""

class Brick:                                  # Definimos la clase para los ladrillos
    def __init__(self, x, y):                 # Inicializamos los atributos del objeto
        self.rect = pygame.Rect(x, y, 50, 50) # Genera el rectángulo del ladrillo en el juego
        self.image = brick                    # Se asigna la imagen del ladrillo 

    def draw(self, superf):
        superf.blit(self.image, self.rect)    # Dibuja la imagen ladrillo en superficie de destino

"""CLASE LADRILLO REFORZADO"""

class LadrilloReforzado:                      # Definimos la clase para los ladrillos reforzados
    def __init__(self, x, y):                 # Inicializamos los atributos del objeto
        self.rect = pygame.Rect(x, y, 55, 55) # Genera el rectángulo del ladrillo en el juego
        self.image = ladrilloR                # Se asigna la imagen del ladrillo reforzado
        self.golpes = 0

    def draw(self, surface):
        surface.blit(self.image, self.rect)   # Dibuja el ladrillo en la superficie de destino 

"""CLASE LADRILLO INDESTRUCTIBLE"""

class LadrilloIndestructible:                 # Definimos la clase para los ladrillos reforzados
    def __init__(self, x, y):                 # Inicializamos los atributos del objeto
        self.rect = pygame.Rect(x, y, 50, 50) # Genera el rectángulo del ladrillo en el juego
        self.image = ladrilloI                # Se asigna la imagen del ladrillo reforzado

    def draw(self, surface):
        surface.blit(self.image, self.rect)   # Dibuja el ladrillo en la superficie de destino

"""
INICIALZACIÓN DEL JUEGO

"""

pygame.init()                                 # Inicializamos pygame


"""MARCO Y FONDO"""
ventana = pygame.display.set_mode((1280,900)) # Inicialización de la superficie de dibujo
pygame.display.set_caption("Juego")
fondo = pygame.image.load("fondojuego.png")   # Crea el objeto fondo y carga la imágen dada


"""MUSICA DE FONDO"""
pygame.mixer.music.load('MUSICAMARIO.mp3')    # Cargamos el archivo de sonido
pygame.mixer.music.play(-1)                   # Reproducimos de forma infinita la musica.


"""BATE"""
bate = pygame.image.load("barraladrillo.png") # Crea el objeto bate con la imágen dada
baterect = bate.get_rect()                    # Obtengo el rectángulo del objeto 
baterect.move_ip(546,824)                     # Lo colocamos en la parte inferior de la pantalla


"""PELOTA"""
ball = pygame.image.load("LABOLA.png")        # Crea el objeto pelota con la imágen dada
ballrect = ball.get_rect()                    # Obtengo el rectángulo del objeto

speed_x = randint(5,8)                        # Valores de movimiento de pelota eje x
speed_y = randint(5,8)                        # Valores de movimiento de pelota eje y
speed = [speed_x,speed_y]                     # Cada ejecución, da velocidad distinta

ballrect.move_ip(400,524)                     # Pelota inicia en zona especificada


"""LADRILLOS"""
brick = pygame.image.load("ladrillo.png")     # Crea el objeto ladrillo con la imágen dada

def generate_bricks():
    bricks = []                               # Lista vacía que almacenará los ladrillos generados
    for row in range(5):                      # Bucle for para iterar sobre cada fila de ladrillos
        for column in range(21):              # Bucle iterador para columnas
            x = column * 60 + 15              # 60 es el espacio entre los ladrillos y 15 el margen del lado izq.
            y = row * 51 + 60                 # 51 es el espacio entre los ladrillos en columna y 60 el margen con la parte superior
            bricks.append(Brick(x, y))        # Crea objeto con coordenadas x e y , y las agrega a la lista
    return bricks                             # Devuelve los ladrillos generados

bricks = generate_bricks()                    # Asigno variable a la llamada de la función
bloques = pygame.sprite.Group()               # Crea grupo de sprites con los ladrillos


"""LADRILLO REFORZADO"""
ladrilloR = pygame.image.load("ladrillomario.png")              # Crea el objeto ladrilloR con la imágen dada

def generar_ladrillosR():                                   
    lista_ladrillosR = []                                       # Lista vacía que almacenará los ladrillos reforzados
    for fila in range(1):                                       # Bucle for para iterar sobre cada fila de ladrillos
        for columna in range(11):                               # Bucle for dentro del otro para iterar sobre cada columna de ladrillos
            x = columna * 240 + 13                              # 120 es el espacio entre los ladrillosy 13 el margen izq.
            y = fila * 51 + 312                                 # 51 es el espacio entre los ladrillos en columna y 312 el margen con la parte superior
            lista_ladrillosR.append(LadrilloReforzado(x, y))    # Crea objeto con coordenadas x e y , y las agrega a la lista
    return lista_ladrillosR                                     # Devuelve los ladrillos generados
 
ladrillo_reforzado = generar_ladrillosR()                       # Asigno variable a la llamada de la función
bloquesR = pygame.sprite.Group()                                # Crea grupo de sprites con los ladrillos

"""LADRILLO INDESTRUCTIBLE"""
ladrilloI = pygame.image.load("ladrillomario.png")              # Crea el objeto ladrilloR con la imágen dada

def generar_ladrillosR():                                   
    lista_ladrillosR = []                                       # Lista vacía que almacenará los ladrillos reforzados
    for fila in range(1):                                       # Bucle for para iterar sobre cada fila de ladrillos
        for columna in range(11):                               # Bucle for dentro del otro para iterar sobre cada columna de ladrillos
            x = columna * 240 + 13                              # 120 es el espacio entre los ladrillosy 13 el margen izq.
            y = fila * 51 + 312                                 # 51 es el espacio entre los ladrillos en columna y 312 el margen con la parte superior
            lista_ladrillosR.append(LadrilloReforzado(x, y))    # Crea objeto con coordenadas x e y , y las agrega a la lista
    return lista_ladrillosR                                     # Devuelve los ladrillos generados
 
ladrillo_reforzado = generar_ladrillosR()                       # Asigno variable a la llamada de la función
bloquesR = pygame.sprite.Group()                                # Crea grupo de sprites con los ladrillos


"""
BUCLE DEL JUEGO
"""


jugando = True                              # Variable jugando True

while jugando:                              # Iniciamos bucle principal del juego 

    ventana.blit(fondo, (0, 0))             # Establezco en la ventana el fondo de pantalla elegido.
    
    for event in pygame.event.get():        # Comprobamos si se ha pulsado el botón de cierre de la ventana
        if event.type == pygame.QUIT:       
            jugando = False                 # Jugando False y cierra


    """BATE"""
    ventana.blit(bate, baterect)                                        # Dibujo el bate

    keys = pygame.key.get_pressed()                                     # Compruebo si se ha pulsado alguna tecla
    if keys[pygame.K_LEFT]:                                             
        baterect = baterect.move(-12,0)                                  # Si se pulsa tecla izq., el bate se mueve en el eje x hacía la izquierda.

    if keys[pygame.K_RIGHT]:                                            # Si se pulsa dcha., el bate se mueve en el eje x hacía la derecha.
        baterect = baterect.move(12,0) 

    
    if keys[pygame.K_LEFT] and baterect.left < 0:                       # Bate pega parte izq. de pantalla, cancelamos con velocidad inversa
        baterect = baterect.move(12,0)
    
    if keys[pygame.K_RIGHT] and baterect.right > ventana.get_width():   # Bate pega parte dcha. de pantalla, cancelamos con velocidad inversa
        baterect = baterect.move(-12,0)

   
    """PELOTA"""
    ventana.blit(ball, ballrect)                                    # Dibujo la pelota

    ballrect = ballrect.move(speed)                                 # Muevo la pelota

    if baterect.colliderect(ballrect):                              # Si hay colisión, la velocidad será la inversa
        speed[1] = -speed[1]

    
    if ballrect.left < 0 or ballrect.right > ventana.get_width():   # Pelota pega parte izq. de pantalla, cancelamos con velocidad inversa
        speed[0] = -speed[0]

    if ballrect.top < 0 or ballrect.bottom > ventana.get_height():  # Pelota pega parte dcha. de pantalla, cancelamos con velocidad inversa
        speed[1] = -speed[1]

   
    """LADRILLOS COLISIÓN"""
    for brick in bricks:                        # Bucle para colisión de ladrillos
        if ballrect.colliderect(brick.rect):    # Si la pelota colisiona con un ladrillo
            speed[1] = -speed[1]                # Cambiar dirección vertical de la pelota
            bricks.remove(brick)                # Eliminar el ladrillo de la lista
            break
    
    for brick in bricks:                        # Dibujo de los ladrillos
        brick.draw(ventana)

    
    """LADRILLOS REFORZADOS COLISIÓN"""
    # Comprobación de colisión de la pelota con los ladrillos
    for ladrilloR in ladrillo_reforzado:                # Bucle colisión pelota con ladrillos                                    
        if ballrect.colliderect(ladrilloR.rect):        # Si la pelota colisiona con un ladrillo
            speed[1] = -speed[1]
            ladrilloR.golpes += 1                       # Cambiar dirección vertical de la pelota
            if ladrilloR.golpes >= 3:
                ladrillo_reforzado.remove(ladrilloR)    # Eliminar el ladrillo de la lista
                break

    for ladrilloR in ladrillo_reforzado:                # Dibujo de los ladrillos
        ladrilloR.draw(ventana)

    """GAME OVER Y CERRAR JUEGO"""
    fuente = pygame.font.Font(None, 80) 
    if ballrect.bottom > ventana.get_height():                      # Comprobar que si toca la parte inferior, game over
        texto = fuente.render("Game Over", True, (255, 0, 0))       # Color rojo
        texto_rect = texto.get_rect()
        texto_x = ventana.get_width() / 2 - texto_rect.width / 2    # Coordenadas x de game over
        texto_y = ventana.get_height() / 2 - texto_rect.height / 2  # Coordenadas y de game over
        ventana.blit(texto, [texto_x, texto_y])
        pygame.display.flip()
        pygame.time.delay(10000)                                    # Espera 10 segundos antes de salir
        jugando = False                                             # Cierra el juego

    
    """OTRAS PARTES DEL CODIGO"""
    pygame.display.flip()           # Todos los elementos del juego se vuelven a dibujar
    pygame.time.Clock().tick(60)    # Controlamos la tasa de refresco (FPS)

pygame.quit()                       # Cierro pygame