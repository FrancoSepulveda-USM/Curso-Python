import pygame
import random
import math
#Inicializo pygame para poder acceder a sus funcionalidades.
pygame.init()


#Crear la pantalla
pantalla = pygame.display.set_mode((800,600))#Esto muestra por poco tiempo una pantalla cuando se ejecuta el programa y no hay mas codigo debajo.
'''Establecer el tamaño de la pantalla con una tupla de argumento (alto,ancho) 
en pixeles'''

#Titulo, icono y fondo de pantalla
pygame.display.set_caption("Invasion espacial")
icono = pygame.image.load("ovni.png")
pygame.display.set_icon(icono)
fondo = pygame.image.load("Fondo.jpg")

puntaje = 0

#Crear Jugador y enemigo
img_jugador = pygame.image.load("cohete.png")
'''Coordenadas iniciales del jugador en pantalla'''
jugador_x = 368
jugador_y = 500
jugador_x_cambia = 0
jugador_y_cambia = 0

'''Coordenadas iniciales enemigo en pantalla (solo 1 enemigo)
enemigo_x = random.randint(0,136)
enemigo_y = random.randint(50,200)
enemigo_x_cambia = 0.6#Para movimiento del eneemigo
enemigo_y_cambia = 50
img_enemigo = pygame.image.load("enemigo.png")'''
#Varios enemigos
enemigo_x = []
enemigo_y = []
enemigo_x_cambia = []#Para movimiento del eneemigo
enemigo_y_cambia = []
img_enemigo = []
cant_enemigos = 8
for en in range(cant_enemigos):
    img_enemigo.append(pygame.image.load("enemigo.png"))
    enemigo_x.append(random.randint(0, 736))
    enemigo_y.append(random.randint(50, 200))
    enemigo_x_cambia.append(0.6)  # Para movimiento del eneemigo
    enemigo_y_cambia.append(50)


#Crear bala, la bala no debe cmabiar su eje x
img_bala = pygame.image.load("bala.png")
bala_x = 0
bala_y = 500#altura de nave
bala_x_cambia = 0
bala_y_cambia = 0.6
'''Funcionalidad de poner que la bala este visible o invisible, que solo este visible cuando se ejcute el disparo'''
bala_visible = False

#Posicionar al jugador
def jugador(x,y):
    pantalla.blit(img_jugador,(x,y))

#Posicionar enemigo
'''1 enemigo'''
def enemigo(x,y):
    pantalla.blit(img_enemigo,(x,y))
def enemigos(x,y,ene):
    pantalla.blit(img_enemigo[ene],(x,y))

#Posicionar bala
def disparar_bala(x,y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_bala,(x+16,y+10))#Para que aparezcan en el medio de la nave

#Funcion degectar colisiones
def hay_colision(x1,y1,x2,y2):
    distancia = math.sqrt(math.pow(x1-x2,2) + math.pow(y2-y1,2))
    if distancia<27:
        return True
    else:
        return False

#Loop del juego
'''La pantalla se muestra todo el tiempo que dure el programa, entonces lo conveniente
es hacer un while en donde cuando presionen la x de la esquina superior derecha de la pantalla
termine el while y por tanto teermine el programa'''
ejecutando = True
while ejecutando:
    # Cambiar fonde de pantalla en formato RGB (rojo,verde,azul)
    '''pantalla.fill((205, 144, 228))'''
    #Poner imagen de fondo de pantalla, se carga en cada iteracion del juego.
    pantalla.blit(fondo,(0,0))


    #jugador_x+=0.1#De esta forma se mueve hacia la derecha

    for evento in pygame.event.get():#Dejo que el programador realice eventos con la pantalla mostrada.

        # Si presiono la x de la esquina superioir derecha de la pantalla termina el juego
        if evento.type == pygame.QUIT:
            ejecutando = False

        '''Movimiento controlado de jugador'''
        #Evento presionar flechas
        if evento.type == pygame.KEYDOWN:#KEYDOWN ES TECLA PRESIONADA, NO IMPORTA CUAL, o sea entra cuando se presiona una tecla.

            #Flecha izquierda
            if evento.key == pygame.K_LEFT:
                #print("Flecha izquierda presionada")
                jugador_x_cambia = -0.6

            #Felcha derecha
            if evento.key == pygame.K_RIGHT:
                #print("Flecha derecha presionada")
                jugador_x_cambia = 0.6

            #Tecla espacio, cambiar solo cuando bala_visible sea False
            if evento.key == pygame.K_SPACE:
                if not bala_visible:
                    bala_x = jugador_x
                    disparar_bala(bala_x,bala_y)
                '''Si apreto espacio y bala_visible es True, eso genera un error,
                ya que estoy lanzando la bala varias veces en un mismo lanzamiento'''

        # Evento soltar tecla
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                #print("Flecha soltada")
                jugador_x_cambia = 0#Para que deje de moverse una vez se suelta


    #modificar ubicacion del jugador
    jugador_x += jugador_x_cambia
    #mantener dentro de bordes
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 800-64:#ancho menos tamaño objeto
        jugador_x = 800-64

    # modificar ubicacion del  enemigo
    '''Varios enemigos'''
    for e in range(cant_enemigos):
        #movimiento
        enemigo_x[e] += enemigo_x_cambia[e]

        #limites
        if enemigo_x[e] <= 0:
            enemigo_x_cambia[e] = 0.6
            enemigo_y[e] += enemigo_y_cambia[e]
        elif enemigo_x[e] >= 800 - 64:
            enemigo_x_cambia[e] = -0.6  # cuando toca los limites cambia de sentido
            enemigo_y[e] += enemigo_y_cambia[e]

        #colision
        colision = hay_colision(enemigo_x[e], enemigo_y[e], bala_x, bala_y)
        if colision:
            bala_y = 500
            bala_visible = False
            puntaje += 1
            # reinicio enemigo
            enemigo_x[e] = random.randint(0, 136)
            enemigo_y[e] = random.randint(50, 200)
        #Ponerlo en pantalla
        enemigos(enemigo_x[e], enemigo_y[e],e)

    '''1 enemigo
    enemigo_x += enemigo_x_cambia
    # mantener dentro de bordes
    if enemigo_x <= 0:
        enemigo_x_cambia = 0.6
        enemigo_y+= enemigo_y_cambia
    elif enemigo_x >= 800 - 64:
        enemigo_x_cambia = -0.6 #cuando toca los limites cambia de sentido
        enemigo_y+=enemigo_y_cambia
    '''

    #movimiento bala
    '''La reinicio cuando sale de pantalla'''
    if bala_y <= -64:
        bala_y = 500
        bala_visible = False


    if bala_visible:
        disparar_bala(bala_x,bala_y)
        bala_y-=bala_y_cambia
        '''errores: Dispara solo una bala(debo reiniciar la posicion de la bala) y esta se mueve con el jugador(creo que es porque se le pasa
        jugador_x como argumento y este cambia en cada loop)'''

    #colision
    '''1 enemigo
    colision = hay_colision(enemigo_x,enemigo_y,bala_x,bala_y)
    if colision:
        bala_y = 500
        bala_visible = False
        puntaje+=1
        # reinicio enemigo
        enemigo_x = random.randint(0, 136)
        enemigo_y = random.randint(50, 200)
    '''

    #Posicionar a los objetos en la pantlla mediante llamar a la funcion.
    jugador(jugador_x,jugador_y)
    #1 jugador-> enemigo(enemigo_x, enemigo_y)

    #actualizar pantalla para que se vea el fondo y el objeto movido
    pygame.display.update()

    #Para hacer efectivo el cambio de color, debo actualizar el display