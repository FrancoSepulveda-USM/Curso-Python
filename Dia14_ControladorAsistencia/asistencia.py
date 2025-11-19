from cv2 import cv2
import face_recognition as fr
import os
import numpy
from datetime import datetime

'''
foto = fr.load_image_file('img.jpg') -> Carga la imagen
foto = cv2.cvtColor(foto, cv2.COLOR_BGR2RGB) -> Pasa la foto a rgb
cv2.imshow('TituloFoto',foto) -> Muestra la foto.
cv2.waitKey(0) -> Para que muestre la foto y no se cierre el programa antes.
cara_captura = fr.face_locations(imagen) -> Reconoce la cara de la imagen. (top, right, bottom, left)
cara_captura_codificada = fr.face_encodings(imagen, cara_captura) -> Codifica la cara para ser entendible por el pc.    
    transforma cada rostro en un vector numérico que representa las facciones de la cara
cara_captura_codificada = [vector_de_juan, vector_de_maria]
cara_captura = [ubicacion_juan, ubicacion_maria]
'''

# Crea BD
ruta = 'Empleados'
mis_imagenes = []
nombres_empleados = []
lista_empleados = os.listdir(ruta) # Entrega una lista con los nombres de los archivos en la ruta.

for nombre in lista_empleados:
    imagen_actual = cv2.imread(f'{ruta}/{nombre}') # Lee la imagen.
    mis_imagenes.append(imagen_actual)
    nombres_empleados.append(os.path.splitext(nombre)[0]) #Quita la extension jpg

print(nombres_empleados)

# Codifica las imagenes
def codificar(imagenes):
    lista_codificada = []
    for imagen in imagenes:
        imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
        codificado = fr.face_encodings(imagen)[0]
        lista_codificada.append(codificado)
    return lista_codificada


# Registrar ingresos
def registrar_ingresos(persona):
    f = open('registro.csv', 'r+')
    lista_datos = f.readlines()
    nombres_registro = []
    for linea in lista_datos:
        ingreso = linea.split(',')
        nombres_registro.append(ingreso[0])

    if persona not in nombres_registro:
        ahora = datetime.now()
        string_ahora = ahora.strftime('%H:%M:%S')
        f.writelines(f'\n{persona}, {string_ahora}')

lista_empleados_codificada = codificar(mis_imagenes)

''' Compara una imagen con las que están en las BD '''
# Captura imagen desde la camara
captura = cv2.VideoCapture(0, cv2.CAP_DSHOW)

exito, imagen = captura.read()# exito indica si se pudo leer la imagen. imagen contiene la foto capturada.

if not exito:
    print("No se ha podido tomar la captura")
else:
    # Reconoce la cara
    cara_captura = fr.face_locations(imagen)

    # Codifica la cara para ser entendible por el pc.
    cara_captura_codificada = fr.face_encodings(imagen, cara_captura)

    # Busco coincidencias -> Caraubic es la ubicacion de la cara de 'cara_captura'.
    for caracodif, caraubic in zip(cara_captura_codificada, cara_captura):
        coincidencias = fr.compare_faces(lista_empleados_codificada, caracodif)
        distancias = fr.face_distance(lista_empleados_codificada, caracodif)

        print(distancias)

        indice_coincidencia = numpy.argmin(distancias)

        # No hay coincidencias
        if distancias[indice_coincidencia] > 0.6:
            print("No coincide con ninguno de nuestros empleados")

        else:

            # Buscar el nombre del empleado encontrado
            nombre = nombres_empleados[indice_coincidencia]

            y1, x2, y2, x1 = caraubic
            cv2.rectangle(imagen, (x1, y1), (x2, y2), (0, 255, 0), 2) # Cuadro de la cara.
            cv2.rectangle(imagen, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(imagen, nombre, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 2555, 255), 2) # Escribe el nombre de la coincidencia.

            registrar_ingresos(nombre)

            cv2.imshow('Imagen web', imagen)

            cv2.waitKey(0)