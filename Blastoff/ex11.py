def intersection(lista1, lista2):
    inter = [x for x in range(1,12) if x in lista1 and x in lista2]
    return inter


lista1 = [1,2,3,4]
lista2 = [1,2,5,8]


print(intersection(lista1,lista2))