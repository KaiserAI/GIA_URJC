def intercambiar(v, i, j):
    save = v[i]
    v[i] = v[j]
    v[j] = save
    return v


def pivote(v, ini, fin):
    p = v[ini]                            # Pivote inicial
    i = ini + 1
    j = fin
    hecho = False
    while not hecho:
        while i <= j and v[i] <= p:
            i += 1
        while i <= j and v[j] >= p:
            j -= 1
        if j < i:
            hecho = True
        else:
            v = intercambiar(v, i, j)
    v = intercambiar(v, ini, j)
    return v, j


def quickSort(v, ini, fin):
    if ini < fin:
        [v, b] = pivote(v, ini, fin)
        v = quickSort(v, ini, b - 1)
        v = quickSort(v, b + 1, fin)
    return v


vector = [1, 9, 5, 7, 3, 2, 2]
print(quickSort(vector, 0, len(vector) - 1))
