def mayuscula(texto):
    print(texto.upper())

def minuscula(texto):
    print(texto.lower())

#Para por argumento funciones
def una_func(funcion):
    return funcion#Se dirige a la funcion pasada como parametro

def seg_func(funcion,texto):
    return funcion(texto)

#Funciones dentro de funciones
def cambiar_letras(tipo):

    def mayus(texto):
        print(texto.upper())

    def minus(texto):
        print(texto.lower())

    if tipo == 'may':
        return mayus
    elif tipo == 'min':
        return minus
#Forma bruta
'''
print('hola')
mayuscula("holaa")
print('adios')
#La otra opcion sería poner el hola y adios dentro de las funciones, pero eso implicaria que al llamar a la funcion siempre se imprima ese hola y adios.
'''

mi_funcion = mayuscula
mi_funcion("hola")

''' Practica de pasar funciones como argumentos
una_func(mayuscula("probando"))
seg_func(minuscula,"FRANCO")
'''

operacion = cambiar_letras("may")#operacion es la funcion pero con parametro may
operacion("palabra")
menor  = cambiar_letras('min')
menor("MAYUSUCLAS")

'''Al tener ya la funcion con el tipo may, al darle palabras, identificara 
que es may, por tanto retornará la palabra con mayusuclas
Esto es posible porque las funciones se comportan como objetos'''


#DECORADORES
def decorar_saludo(funcion):#recibe la funcion que sera decorada

    '''
    Defino una funcion dentro que se encarga de imprimir antes y despues cosas.
    Luego llama a la funcion principal.
    Finalmente retorna otra_funcion para que sea llamada la funcion definida dentrocde decorar_saludo.
    '''
    def otra_funcion(palabra):
        print("Hola")
        funcion(palabra)
        print("adios")

    return otra_funcion

'''
Hacer esto sigue con el mismo problema de que la funcion si o si se imprimira con hola y adios impresos.
@decorar_saludo
def mayuscula(texto):
    print(texto.upper())
'''
#Probando la funcion con decoracion

mayuscula("python")#Normal

#decorada
mayuscula_decorada = decorar_saludo(mayuscula)
mayuscula_decorada("hiphop")
