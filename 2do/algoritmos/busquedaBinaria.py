def binarySearch(arr, ini, fin, buscando):
    if ini > fin:
        return -ini
    else:
        medio = (ini + fin) // 2                                        # k
        if buscando == arr[medio]:
            return medio
        elif buscando < arr[medio]:
            return binarySearch(arr, ini, medio - 1, buscando)          # El elemento que busco está abajo de la mitad.
        else:
            return binarySearch(arr, medio + 1, fin, buscando)          # El elemento que busco está encima de la mitad.




if __name__ == '__main__':
    arr = [1, 3, 5, 7, 8, 10, 12, 15]
    ini = 0                                                             # i
    fin = len(arr) - 1                                                  # j

    buscando = 10                                                       # x
    posicion = binarySearch(arr, ini, fin, buscando)

    if posicion >= 0:
        print("Elemento buscado", buscando, "está en la posicion", posicion)
    else:
        print("Elemento buscado no está en el array.")
