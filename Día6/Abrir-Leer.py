mi_archivo = open("Prueba.txt") #Asocia la variable al archivo
#print(mi_archivo) #No imprime lo que está dentro del archivo, muestra el objeto archivo y sus propiedades
                  #De esta forma lo abre en con modo 'r', o sea read

#print(mi_archivo.read()) '''Imprime el contenido del archivo, para eso lee por completo el archivo, por lo que el puntero queda al final del archivo, eso
# provoca que si despues de esto usas readline o read de nuevo, no imprimira nada pues ya se leyo por completo el archivo'''

#print(mi_archivo.readline())#Lee una sola linea, por lo que en este caso solo imprime la primera nomas
'''primera_linea = mi_archivo.readline() #Cada vez que se lee una linea con readline(), se lee la siguiente a la última leída
print(primera_linea)
primera_linea = mi_archivo.readline()
print(primera_linea)'''

#for linea in mi_archivo:#Recorre por linea
#    print(linea.rstrip())

lineas = mi_archivo.readlines()
print(lineas)





mi_archivo.close()#Siempre cerrar el archivo



