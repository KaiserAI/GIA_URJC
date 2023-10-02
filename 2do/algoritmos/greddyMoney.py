#Mi implementación:
def greddyMoney(dineroACambiar, valoresMonedas):
    dineroResidual = dineroACambiar
    index = 0
    cambioADevolver = []

    while dineroResidual > 0:
        if dineroResidual - valoresMonedas[index] >= 0:
            dineroResidual -= valoresMonedas[index]
            cambioADevolver.append(valoresMonedas[index])
        else:
            index += 1

    return cambioADevolver


#Implementación de Juanjo:
def inicializarSol(longitudLista):
    solInicial = [0]*longitudLista
    return solInicial


def esFactible(moneda, valores, M):
    return valores[moneda] <= M


def cambioVoraz(M, valores):
    cambio = inicializarSol(len(valores))
    moneda = 0
    while M > 0 and moneda < len(valores):
        while esFactible(moneda, valores, M):
            cambio[moneda] = cambio[moneda] + 1
            M -= valores[moneda]
        moneda = moneda + 1
    return cambio


valoresMonedas = [50, 20, 10, 5, 1] #Suponemos que nos dan los valores de las monedas ordenados de manera descendente.
dineroACambiar = 60
print(greddyMoney(dineroACambiar, valoresMonedas))
print(cambioVoraz(dineroACambiar, valoresMonedas)) #Aquí te da un array con la cantidad de monedas de cada tipo que se necesitan para devolver el cambio
