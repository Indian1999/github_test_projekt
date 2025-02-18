def sum_rek(lista):
    if len(lista) == 0:
        return 0
    if len(lista) == 1:
        return lista[0]
    return lista[0] + sum_rek(lista[1:])

print(sum_rek([1,2,3,4,5,6,7,8,9,10]))