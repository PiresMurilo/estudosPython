def remove_repetidos(lista):
    lista2 = []
    for x in lista:
        if x not in lista2:
            lista2.append(x)
    lista3 = sorted(lista2)
    return lista3
