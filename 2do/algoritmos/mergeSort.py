

def merge(v, lv, rv):
    i = j = k = 0
    while i < len(lv) and j < len(rv): # Comparo los elementos más a la izquierda de los arrays.
        if lv[i] < rv[j]:               # Si el más pequeño es el de la izquierda, al array original le pongo el de la izquierda.
            v[k] = lv[i]
            i += 1
        else:
            v[k] = lv[j]                # Lo mismo si es más pequeño el de la izquierda.
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
