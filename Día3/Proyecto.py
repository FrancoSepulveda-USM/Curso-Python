texto = input("Ingrese su texto: ").strip()# quita los espacios del final o inicio con strip
texto_minusculas = texto.lower()#Lo pasa a minusculas 
letras = input("Ingrese 3 letras: ").lower().split(" ")#Guarda cada letra en una lista, primero las pasa a minusculas.

print("Primer análisis \"Cuantas veces aparece cada letra en el texto?\"")
for let in letras:
    cant = texto_minusculas.count(let)
    print(f"La letra {let} aparece {cant} veces en el texto")
print("-"*15)

print("Segundo análisis \"Cuantas palabras hay a lo largo del texto\"")
print(len(texto.split(" ")))
print("-"*15)

print(f"""Tercer análisis \"Primera y ultima letra del texto\"
Primer letra: {texto[0]}
Última letra: {texto[-1]}""")
print("-"*15)

print(f"""Cuarto análisis \"Texto invertido\"""")
lista=texto.split(" ")
print("Texto: ",texto[::-1])#Invierte todas las letras del texto
lista.reverse()
texto_invertido = " ".join(lista) #Invierte el orden de las palabras del texto
print(f"Texto invertido: {texto_invertido}")
print("-"*15)

print("Quinto análisis \"Aparece la palabra Python?\"")
dicc = {True: "Si", False: "No"}
Esta_o_no = "Python" in texto_minusculas
print(dicc[Esta_o_no])
