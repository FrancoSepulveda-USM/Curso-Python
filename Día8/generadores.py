#funcion normal
def mi_funcion():
    return 5

#generador
def mi_generador():
    yield 4 #va a retornar el 4 una vez se lo pida el programa

def mi_lista():
    lista = []
    for x in range(1,5):
        lista.append(x * 10)
    return lista

def mi_lista_generada():
    for x in range(1,5):
        yield x*10#va generando los valores 1 a la vez.

print(mi_funcion())
print(mi_generador())#No se le ha pedido el 4.

g = mi_generador()
print(next(g))
#print(next(g)) este dara error pues solo hay una vlor para retornar, el 4.

print(mi_lista())
print(mi_lista_generada())

ge = mi_lista_generada()
lista = []
while True:
    try:
        lista.append(next(ge))
    except:
        print("terminó")
        break

#otro ejemplo
def mi_generador():
    x=1
    yield x

    x += 1
    yield x

    x+=1
    yield x

    x*=100
    yield x

g = mi_generador()
print(next(g))
print(next(g))
print(next(g))
print(next(g))


def secuencia_infinita():
    num = 0
    while True:
        num += 1
        yield num


generador = secuencia_infinita()
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))