def letras_unicas(palabra):
    lista = list(palabra)
    lista_unicos = list(set(lista))
    lista_unicos.sort()
    return lista_unicos

print(letras_unicas("PythonnpPyhooon"))
