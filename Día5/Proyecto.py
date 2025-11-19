from random import choice

palabras = ["madrid","automovil","helicoptero","computador","horoscopo"]

print("Se escogerá una palabra al azar....Tienes 6 vidas para adivinarla")

palabra = choice(palabras)
largo_palabra = len(palabra)

representacion = list("_"*largo_palabra)
#print(representacion)
intentos = 6
while intentos!=0:
    #Imprimir la palabra con guiones
    print(f"Cantidad de vidas {intentos}")
    print("PALABRA ACTUAL:")
    print(*representacion)


    indice = 0
    letra = input("Ingrese una letra: ")

    #encontrar los indices de la letra, si es que hay, si hay mas de una, retorna una lista.
    indices = [indice for indice,letras in enumerate(palabra) if letra==letras]
    if len(indices)==0 or indices[0]==-1: #No hay letra
        print("Letra no se encuentra dentro de la palabra")
        intentos-=1
        continue
    else:
        for ind in indices:
            representacion[ind] = letra

    if '_' not in representacion:
        print("Ganaste")
        break
