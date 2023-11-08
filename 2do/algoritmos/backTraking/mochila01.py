import copy


def inicializarDatos():
    datos = {}
    datos["N"] = 4
    datos["W"] = 8
    datos["Peso"] = [2, 3, 4, 5]
    datos["Valor"] = [3, 5, 6, 10]
    return datos


def inicializarSolucion(datos):
    sol = {}
    sol["Objetos"] = [0] * datos["N"]
    sol["Peso"] = 0
    sol["Valor"] = 0
    return sol

def esSolucion(sol, datos):
    return sol["Peso"] + min(datos["Peso"]) <= datos["W"]


def mejor(sol1, sol2):
    if sol1["Valor"] > sol2["Valor"]:
        mejor = copy.deepcopy(sol1)
    else:
        mejor = copy.deepcopy(sol2)
    return mejor


def asignar(sol, i, datos):
    sol["Objetos"][i] += 1
    sol["Valor"] += datos["Valor"][i]
    sol["Peso"] += datos["Peso"][i]
    return sol


def borrar(sol, i, datos):
    sol["Objetos"][i] -= 1
    sol["Valor"] -= datos["Valor"][i]
    sol["Peso"] -= datos["Peso"][i]
    return sol

def mochilaVA(sol, mejorSol, datos, k):  # k es la posición por la que voy
    if esSolucion(sol, datos):
        mejorSol = mejor(sol, mejorSol)
    else:
        for i in range(k, datos["N"]):
            sol = asignar(sol, i, datos)            # Meter un nodo.
            mejorSol = mochilaVA(sol, mejorSol, datos, i + 1)
            sol = borrar(sol, i, datos)             # Borro el nodo para meter el otro.
    return mejorSol


datos = inicializarDatos()
sol = inicializarSolucion(datos)
mejorSol = inicializarSolucion(datos)
mejorSol = mochilaVA(sol, mejorSol, datos, 0)
print(mejorSol)
