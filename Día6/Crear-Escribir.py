
archivo = open("Prueba.txt","w")#Modo escritura
archivo.write("Hola\nmundo")
archivo.write("""Hola 
mundo\n""")
archivo.writelines(["Hola "," mundo"," Cruel"])
lista = ["Hola","mundo"]#Alternativa a writelines()
for p in lista:
    archivo.write(p+"\n")
archivo.close()


archivo = open("Directorio.py","w")
archivo.write("""import os
rut_actual = os.getcwd()
print(rut_actual)""")
archivo.close()

'''
registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]

registro = open("registro.txt", "a")
for item in registro_ultima_sesion:
    registro.writelines(item + '\t')

registro.close()
registro = open("registro.txt", "r")
print(registro.read())
'''
registro_ultima_sesion = ["Federico\t", "20/12/2021\t", "08:17:32 hs\t", "Sin errores de carga"]
archivo = open("registro1.txt","w")
archivo.writelines(registro_ultima_sesion)
archivo.close()
archivo = open("registro1.txt")
print(archivo.read())
archivo.close()