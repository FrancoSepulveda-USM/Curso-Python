'''dicc = {"Clave 1":2,"Clave 2":5}
for item in dicc.items():
    print(item)

for key, value in dicc.items():
    print(key,value)
'''
'''while input("Sigo o no sigo? (S/N)") == "S":
    print("OK")
    continue
    print("SIGO")
else:
    print("NO SIGO")

while True:
    print(2)
    break

l = list(range(2500,2586))
print(l)
'''
nombres = ["Franco","Antonio","Sepýlveda"]
numeros = [3,4,1,5]
dicc = {"a":1,"b":2,"c":3}
combinacion = zip(nombres,numeros,dicc)
print(list(combinacion))

for nombre,numero,letra in combinacion:
    print(f"{nombre} {numero} {letra}")


palabra = "Hola"
lista = [letra*3 if letra == "H" else letra*4 if letra == "o"  else letra *5 for letra in palabra]
print(lista)


cliente = {"nombre": "Franco",
           "edad": 21,
           "ocupacion": "Estudiante"}
pelicula = {"titulo": "Matrix",
            "ficha_tecnica": {"protagonista": "Keanu Reeves",
                              "director":"Lana y Lilly Wachowski"}}
elementos = [cliente,pelicula,"libros"]

for e in elementos:
    match e:
        case {"nombre": nombre,
           "edad": edad,
           "ocupacion": ocupacion}:#En caso de que e sea un diccionario con esa estructura.
            print("Es un cliente")
            print(nombre,edad,ocupacion)
        case {"titulo": titulo,
            "ficha_tecnica": {"protagonista": protagonista,
                              "director":director}}:
            print("Es una pelicula")
            print(titulo,protagonista,director)
        case _:
            print("No se que es")





















