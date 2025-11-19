'''dicc = {"1": 1}
dicc.popitem()
lista = [1,2,3,4]
lista.insert(3,7)
print(lista)'''

precios_cafe = [("capuchino",1.5),("Expresso",1.2),("Moka",1.9)]
def cafe_mas_caro(lista_precios):

    precio_mayor = 0
    cafe_mas_caro = ""

    for cafe,precio in lista_precios:
        if precio>precio_mayor:
            precio_mayor = precio
            cafe_mas_caro = cafe
        else:
            pass

    return (cafe_mas_caro,precio_mayor) #retorna una tupla

print(cafe_mas_caro(precios_cafe))
cafe, precio = cafe_mas_caro(precios_cafe)
print(f"El cafe mas caro es {cafe} con el valor de {precio} pesos")

from random import shuffle

#crear palitos
palitos = ['-','--','---','----']

#mezclar palitos
def mezclar(lista):
    shuffle(lista)
    return lista

#pedirle intento
def probar_suerte():
    intento = ''
    while intento not in ['1','2','3','4']:
        intento = input("Elige el numero del 1 al 4: ")

    return int(intento)

#comprobar intento
def chequear_intento(lista,intento):
    if lista[intento-1] == '-':
        print("A lavar los platos")
    else:
        print("Te has salvado")
    print(f"te ha tocado {lista[intento-1]}")

palitos_mezclados = mezclar(palitos)
seleccion = probar_suerte()
chequear_intento(palitos_mezclados,seleccion)

def suma(**kwargss):
    total = 0
    for clave,valor in kwargss.items():
        print(f"{clave} = {valor}")
        total+=valor

    return total
print(suma(x=3,y=5,z=2))

def prueba(num1,num2,*args,**kwargss):
    print("El primer valor es",num1)
    print("El segundo valor es", num2)

    for arg in args:
        print(f"arg = {arg}")

    for clave,valor in kwargss.items():
        print(f"{clave} = {valor}")

prueba(15,30,100,200,300,400,x=3,y=5,z=2)

lista = [100,200,300,400]
dicc = {'x':3,'y':5,'z':2}

prueba(15,30,*lista,**dicc)








