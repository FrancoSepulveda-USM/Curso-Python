from collections import Counter,defaultdict,namedtuple

'''Counter'''
lista  = [1,3,2,3,1,2,3,1,3,2,1,3,2,1,2,3,4,52,2,1,1,4,3,25,3,1]
print(Counter(lista))#Da la cantidad de aparaciones de cada valor unico en la lista.
#Se puede utilizar para saber cuantas palabras se repiten en strings
frase = "al pan pan y al vino vino"
print(Counter(frase.split()))
#Otros metodos de Counter
serie = Counter([1,1,1,1,1,1,2,3,2,3,2,3,2,3,2,4,2,3,4,2,4,1,2])
print(serie)
print(serie.most_common())#Entrega en tuplas ordenada de los valores que mas aparecen a los que menos(nro,#apariciones).
print(list(serie))

'''defaultidct'''
mi_dic = {"uno":"verde","dos":"azul"}
#print(mi_dic["tres"])
#Solucion
mi_dic = defaultdict(lambda:"Nuevo valor")
mi_dic["uno"] = "Verde"
print(mi_dic["dos"])
print(mi_dic)

'''namedtuple'''
PersonaTupla = namedtuple("Persona",["nombre","altura","peso"])
persona = PersonaTupla('Franco',1.79,87)
print(persona)
print(persona.nombre)
print(persona[0])
print(persona.altura)
print(persona[1])

lista = [1, 2, 3, 6, 7, 1, 2, 4, 5, 5, 5, 5, 3, 2, 6, 7]

