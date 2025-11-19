import os
from pathlib import Path, PosixPath
rut_actual = os.getcwd()
print(rut_actual)
ruta = PosixPath(rut_actual).parent
print(ruta)
for direc in ruta.iterdir():#Itera sobre las carpetas dentro de el directorio.
    print(direc) #Retorna solo el nombre de cada carpeta.
