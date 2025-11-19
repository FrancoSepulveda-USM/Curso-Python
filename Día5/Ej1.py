def devolver_distintos(num1,num2,num3):
    suma = sum([num1,num2,num3])
    if suma > 15:
        return max(num1,num2,num3)
    elif suma < 10:
        return min(num1,num2,num3)
    else:
        lista = [num1,num2,num3]
        lista.sort()
        return lista[1]

print(devolver_distintos(3,5,4))