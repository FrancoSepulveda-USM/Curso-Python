from pathlib import Path
import os
from os import system
ruta = os.getcwd() #Obtiene la ruta.
print(ruta)

#Crear una ruta a partir de strings.
Ruta = Path("Franco","Sepúlveda")#Los fusiona y convierte en ruta relativa.
print(Ruta)
#El path acepta strings como objetos Path
Ruta = Path(ruta,"Franco","Sepúlveda")#Lo combiné con el path para tener la ruta absoluta.
print(Ruta)

#Metodo home para obtener la ruta a el directorio principal del usuario(o sea yo) actual
base = Path.home()
print(base)

#Cambiar el nombre base del archivo
Ruta2 = Ruta.with_name("Bello")
print(Ruta2)

#Ver los parientes del archivo, los que van antes.
print(Ruta2.parent.parent)
print(Ruta2)

#De esta forma se puede cambiar el nombre de algun elemento de la ruta sin cambiar el nombre del archivo finalfrom pathlib import Path
Ruta3 = Path("C:/Usuarios/Ejemplo/Documento.txt")
nueva_ruta = Ruta3.parent.with_name("ANTONIO") / Ruta3.name
#El uso de / Ruta3.name lo devuelve a la normalidad
print(nueva_ruta)  # Output: C:/Usuarios/ANTONIO/Documento.txt

#ENUMERAR
ruta_prin = Path.home() / "Documents" / "Comprobantes"
print(str(ruta_prin))
for pdf in Path(ruta_prin).glob("*.pdf"): #Devuelve todos los archivos .pdf en el directorio de la ruta "ruta_prin"
    print(pdf)

print("\n\n\n\n")
for pdf in Path(ruta_prin).glob("**/*.pdf"): #Devuelve todos los archivos .pdf en el directorio de la ruta "ruta_prin", incluyendo los que estan dentro de otros directorios dentro de ruta_principal
    print(pdf)

ruta_home = Path.home()
'''for txt in Path(ruta_home).glob("**/*.txt"): #Muestra todos los txt en la ruta_home y que hayan dentro de otros directorios
    print(txt)'''
system("cls")
print("Hola")