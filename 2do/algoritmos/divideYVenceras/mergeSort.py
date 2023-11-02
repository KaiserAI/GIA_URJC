

def merge(v, lv, rv):
    i = j = k = 0
    while i < len(lv) and j < len(rv): # Comparo los elementos más a la izquierda de los arrays.
        if lv[i] < rv[j]:               # Si el más pequeño es el de la izquierda, al array original le pongo el de la izquierda.
            v[k] = lv[i]
            i += 1
        else:
            v[k] = rv[j]                # Lo mismo si es más pequeño el de la derecha.
            j += 1
        k += 1

    while i < len(lv):                  # Tmb tengo que pensar que me puedo quedar sin elementos en uno de los 2 arrays.
        v[k] = lv[i]                    # Así añado los que me quedan.
        i += 1
        k += 1
    while j < len(rv):                  # Lo mismo si me quedo sin elementos en el array de la izquierda (Añado todos los de la derecha).
        v[k] = rv[j]
        j += 1
        k += 1
    return v


def mergeSort(vector):
    leftVect = vector[:len(vector)//2]  # Divido el vector a la mitad.
    rightVect = vector[len(vector)//2:]
    if len(vector) > 1:
        mergeSort(leftVect)
        mergeSort(rightVect)
        vector = merge(vector, leftVect, rightVect)
    return vector

# Implementación de Juanjo aunque no va bien creo.
from math import inf


def merge(v, ini, med, fin):
    n1 = med - ini + 1
    n2 = fin - med
    l = [0] * (n1 + 1)
    r = [0] * (n2 + 1)
    for i in range(n1):
        l[i] = v[ini + i]
    l[n1] = inf
    for j in range(n2):
        r[j] = v[med + 1 + j]
    r[n2] = inf
    i = 0
    j = 0
    for k in range(ini, fin + 1):
        if l[i] < r[j]:
            v[k] = l[i]
            i += 1
        else:
            v[k] = r[j]
            j += 1
    return v


def mergeSort(v, ini, fin):
    if ini < fin:
        med = len(v) // 2
        v = mergeSort(v, ini, med)
        v = mergeSort(v, med + 1, fin)
        v = merge(v, ini, med, fin)
    return v


vector = [1, 8, 3, 7, 9, 7, 2]
print(mergeSort(vector, 0, len(vector) - 1))
