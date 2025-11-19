import os
from pathlib import Path
import shutil
from os import system

ancho = shutil.get_terminal_size().columns
ruta_principal = Path.home() / "Recetas"
categorias = []

def cantidad_recetas(ruta):#Indica la cantidad de recetas que ya estan dentro del sistema
    contador = 0
    print("Las recetas ya creadas son: ")
    for txt in Path(ruta).glob("**/*.txt"):
        contador+=1
        print(f"- {Path(txt).stem}")
    print(f"Existen {contador} recetas en total".center(ancho))

def opciones():
    opc = int(input("""Escoja entre estas 6 opciones
    1.- Leer receta
    2.- Crear receta nueva
    3.- Crear categoría nueva
    4.- Eliminar receta
    5.- Eliminar categoría
    6.- Salir\n""".center(ancho)))
    return opc

def recetas(): #Se encarga de gestionar toda la opcion 1, finalmente mostrando el contenido de la receta.
    mostrar_categorias()
    while True:
        opc_categoria = int(input("Indique el nro de categoría a la cual desea acceder\n"))
        if (opc_categoria-1) >= len(categorias): #Nro fuera de los límites de las categorías.
            print("Opción inválida")
        else:
            categoria = categorias[opc_categoria-1]
            nueva_ruta = ruta_principal / categoria
            break

    #Mostrar recetas
    rec = ver_recetas(nueva_ruta)#Lista con las recetas en la categoría
    if len(rec)==0:
        return print("No hay recetas disponibles")
    opc_receta = int(input("Cual receta desea escoger (Indique ingresando el nro)"))

    arch = Path(nueva_ruta,rec[opc_receta-1])

    system("cls")

    print(arch.read_text())#Muestra el contenido

def ver_recetas(ruta): #Ve las recetas que hay dentro de una categoria.
    rec = []
    contador = 1
    for txt in Path(ruta).glob("*.txt"):
        texto = str(txt)

        print(f"{contador}.- {Path(texto).stem}") #Imprimo las recetas sin la extension.

        rec.append(Path(texto)) #Las agrego con la extension txt

        contador+=1
    return rec

def eliminar_receta(): #Se encarga de gestionar toda la opcion 1, finalmente mostrando el contenido de la receta.
    mostrar_categorias()
    while True:
        opc_categoria = int(input("Indique el nro de categoría a la cual desea acceder\n"))
        if (opc_categoria-1) >= len(categorias): #Nro fuera de los límites de las categorías.
            print("Opción inválida")
        else:
            categoria = categorias[opc_categoria-1].capitalize()
            nueva_ruta = ruta_principal / categoria
            break

    #Mostrar recetas
    rec = ver_recetas(nueva_ruta)#Lista con las recetas en la categoría
    opc_receta = int(input("Cual receta desea escoger (Indique ingresando el nro)"))

    arch = Path(nueva_ruta,rec[opc_receta-1])

    system("cls")

    os.remove(arch)#Elimino el archivo

def escribir_archivo(ruta,cont):#Escribe en un archivo de ruta "ruta" el contenido indicado
    arch = open(ruta,"w")
    arch.write(cont)
    arch.close()

def crear_receta():
    mostrar_categorias()
    while True:
        opc_categoria = int(input("Indique la categoría donde desea incorporar la nueva receta\n"))
        if (opc_categoria-1) >= len(categorias): #Nro fuera de los límites de las categorías.
            print("Opción inválida")
        else:
            categoria = categorias[opc_categoria-1].capitalize()#Capitalize pues cada nivel empieza con letra mayuscula
            nueva_ruta = str(Path(ruta_principal,categoria))
            print(nueva_ruta)
            break

    nombre = input("Indique el nombre de la receta: ")
    nombre = nombre + ".txt" #Agrega la extensión
    nueva_ruta = str(Path(nueva_ruta ,nombre)) #Pathea la ruta correctamente
    contenido = input("""Contenido de la receta: """)

    escribir_archivo(nueva_ruta,contenido)

def mostrar_categorias():#Muestra las categorias ya existentes.
    # Mostrar las categorías
    print("Categorias disponibles")

    total = len(categorias)
    for num, cat in enumerate(categorias):
        print(f"{num + 1}.- {cat}")

def directorios():#Llena una lista con todos las categorías.
    for direct in ruta_principal.iterdir():
        categorias.append(Path(direct).stem.lower())

def cat_ya_existe(nombre):
    if str(nombre).lower() in categorias:
        return True #Ya existe
    return False#No existe

def crear_categoria():

    nombre = input("Ingrese el nombre de la nueva categoría: ")
    if nombre.lower() not in categorias:
        os.makedirs(Path(ruta_principal,nombre))
        categorias.append(nombre.lower())

def eliminar_categorias():

    while True:
        mostrar_categorias()
        opc = int(input("Cual desea eliminar: "))
        if opc<len(categorias):
            categoria = categorias[opc-1]
            categorias.pop(opc - 1)
            for txt in Path(ruta_principal, categoria).glob("*.txt"):
                print(txt)
                os.remove(txt)
            os.rmdir(Path(ruta_principal, categoria))
            break
        else:
            categoria = False


if __name__ == '__main__':
    directorios()#Inicializo las categorias.
    print("¡Bienvenido al administrador de recetas!".center(ancho))
    print(f"La ruta donde se encuentran las recetas es la siguiente -> {ruta_principal}")

    while True:
        cantidad_recetas(ruta_principal)

        opcion = opciones()
        match opcion:
            case 1:#Leer receta
                recetas()
            case 2:
                crear_receta()
            case 3:
                #crear categoria
                crear_categoria()
            case 4:
                eliminar_receta()
            case 5:
                eliminar_categorias()
            case 6:#Salir
                print("Gracias por preferirnos!")
                break
            case _:
                print("Ingrese una opción válida")

