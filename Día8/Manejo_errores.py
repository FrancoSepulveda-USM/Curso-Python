def suma():
    n1 = int(input("Numero 1: "))
    n2 = int(input("Numero 2: "))
    print(n1+n2)

try:
    suma()
except:
    print("Algo no ha salido bien")
else:
    print("Todo salio bien")
finally:
    print("Eso fue todo")

try:
    suma()
except TypeError:
    print("Estas intentando combinar tipos distintos")
except ValueError:
    print("Ese no es numero")
else:
    print("Todo bien")


while True:
    try:
        numero = int(input("Dame un nro: "))
    except:
        print("Ese no es numero")
    else:
        print(f"Ingresaste el nro {numero}")
        break

print("Gracias")

