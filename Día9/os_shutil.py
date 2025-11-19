import os
import shutil
from pathlib import Path
import send2trash

ruta_actual = Path(os.getcwd())#Obtengo la ruta actual en modo Path
ruta_principal = ruta_actual.parent#Obtengo la ruta sin el ultimo archivo
print(ruta_actual)
print(ruta_principal)
print(os.listdir())#Enlisto los archivos dentro de la carpeta actual

##mover un archivo a otra carpeta
#shutil.move("practica.txt",Path(ruta_principal,"Día8"))

#send2trash.send2trash("practica.txt")

print(os.walk(ruta_principal))#Es un generador
Variable = os.walk(ruta_principal)

'''
while True:
    try:
        print(next(Variable))
    except:
        break
'''

for carpeta,subcarpeta,archivo in os.walk(ruta_principal):
    print(f"En la carpeta {carpeta}")
    print(f"Las subcarpetas son: ")
    for sub in subcarpeta:
        print(f"\t{sub}")
    print(f"Los archivos son:")
    for arch in archivo:
        print(f"\t{arch}")
    print("\n")
