from random import *
import shutil

intentos = {0: "Primer", 1:"Segundo", 2:"Tercer",3:"Cuarto",4:"Quinto",5:"Sexto",6:"Septimo",7:"Octavo"}

ancho = shutil.get_terminal_size().columns
print("Bienvenido al juego de adivinar el número!".center(ancho,"-"))
print("Escogeré un valor entre 1 y 100, debes adivinar cual valor es".center(ancho,"-"))
acierto = False

print(f"Ya pensé el número! Intenta Adivinarlo".center(ancho))
nro = randint(1,101)

for intento in range(8):
    if intento == 0:
        print("Tienes 8 try's para adivinar el número".center(ancho))

    usuario = int(input("Ingresa un valor entre 1 y 100: ").strip())
    if usuario > 100 or usuario < 0:
            print("Valor fuera de los límites válidos, elige un número entre 1 y 100")
    elif usuario > nro:
            print("El número escogido es mayor al que pensé")
    elif usuario < nro:
            print("El número escogido es menor al que pensé")
    else:
            print(f"Encontraste el número en el {intentos[intento]} intento! Felicidades!")
            acierto = True
            break
if not acierto:
    print(f"No lograste adivinarlo :(, el número secreto era {nro}")