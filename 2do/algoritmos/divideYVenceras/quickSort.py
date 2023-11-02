def intercambiar(v, i, j):
    save = v[i]
    v[i] = v[j]
    v[j] = save
    return v


def pivote(v, ini, fin):
    p = v[ini]                            # Pone comoo pivote inicial el primer elemento del vector.
    i = ini + 1                           # Índice al inicio del vector.
    j = fin                               # Índice al final de este.
    hecho = False
    while not hecho:
        while i <= j and v[i] <= p:       # Coloca el índice i en un número mayor que el pivote.
            i += 1
        while i <= j and v[j] >= p:       # Coloca el j en un número menor que el pivote.
            j -= 1
        if j < i:                         # Si se cruzan los índices en el vector es que ya terminé.
            hecho = True                     
        else:
            v = intercambiar(v, i, j)    # Intercambia el elemento i con el j. 
    v = intercambiar(v, ini, j)          # Pone el pivote en el j para que a su izquierda queden los menores y a su derecha los mayores.
    return v, j


def quickSort(v, ini, fin):
    if ini < fin:
        [v, b] = pivote(v, ini, fin)    # Elige un pivote dentro de la función y devuelve el vector con los números menores al pivote a su izquierda y lo mayores a su derecha.
        v = quickSort(v, ini, b - 1)    # LLamada recursiva con el vector hasta el pivote.
        v = quickSort(v, b + 1, fin)    # Esta con el vector después del pivote.
    return v


vector = [1, 9, 5, 7, 3, 2, 2]
print(quickSort(vector, 0, len(vector) - 1))
