import os
import zipfile



'''Con zipfile
#Comprimir dentro de archivo descomprimido
mi_zip = zipfile.ZipFile("archivo_comprimido.zip",'w')
mi_zip.write("mi_texto_A.txt")
mi_zip.write("mi_texto_B.txt")
mi_zip.close()
#Descomprimir
descomprimir = zipfile.ZipFile("archivo_comprimido.zip",'r')
#descomprimir.extractall()descomprime todos
#descomprimir.extract("mi_texto_A.txt")
'''

import shutil
import os
from pathlib import Path
'''con shutil'''
'''Creo el archivo comprimido
ruta_actual = Path(os.getcwd(),"Comprimir")
archivo_destino = "archivo_comprimido2"
shutil.make_archive(archivo_destino,'zip',ruta_actual)'''

#Descomprimo el archivo en una carpeta de nombre "Descomprimido"
ruta_actual = Path(os.getcwd(),"Descomprimido/")
print(os.getcwd())
shutil.unpack_archive("archivo_comprimido2.zip",ruta_actual,'zip')

