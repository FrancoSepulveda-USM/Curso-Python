texto = "HOLA SOY FRANCO  O"
try:
    tex = texto.index(" O",5)
    print(tex)
except ValueError:
    print("No está")

tupla = ("E","S",4)
numeros = " ".join(map(str,tupla)) #El map(str,tuple) convierte en strings los valores de la tupla y los guarda en una lista, luego el join se hace a esa listq.
print(numeros)