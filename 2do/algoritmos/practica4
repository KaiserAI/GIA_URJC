

################################################### 8 ##################################################################
def potencia(base, expo):
    if expo == 0:
        result = 1
    elif expo == 1:
        result = base
    elif expo % 2 == 0:
        aux = potencia(base, expo // 2)
        result = aux * aux
    else:
        result = base * potencia(base, expo - 1)
    return result


#print(potencia(2, 3))


################################################### 9 ##################################################################
def sumMaxCentral(v, ini, mitad, fin):
    suma = 0
    sumaMaxD = 0
    for i in range(mitad, ini - 1, -1):
        suma += v[i]
        if suma > sumaMaxD:
            sumaMaxD = suma
    suma = 0
    sumaMaxI = 0
    for i in range(mitad + 1, fin + 1):
        suma += v[i]
        if suma > sumaMaxI:
            sumaMaxI = suma
    return sumaMaxD + sumaMaxI

def sumMax(v, ini, fin):
    if ini > fin:
        result = 0
    elif ini == fin:
        result = v[ini]
    else:
        mitad = (ini + fin) // 2
        sumMaxI = sumMax(v, ini, mitad)
        sumMaxD = sumMax(v, mitad + 1, fin)
        sumMaxC = sumMaxCentral(v, ini, mitad, fin)
        result = max(sumMaxI, sumMaxD, sumMaxC)
    return result

vect = [-2, 11, -4, 13, -5,- 2]
print(sumMax(vect, 0, len(vect) - 1))
