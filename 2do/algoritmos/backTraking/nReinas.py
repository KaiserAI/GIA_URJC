def inicializarTablero(N):
    tablero = []
    for i in range(N):
        tablero.append([0]*N)
    return tablero


def imprimir(sol):
    N = len(sol)
    tablero = inicializarTablero(N)
    for f in range(N):
        tablero[f][sol[f]] = "\u2655"
        print(tablero[f])


def inicializarSol(n):
    return n*[-1]


def esSolucion(sol, fila):
    if fila == len(sol):
        return True


def damaEnColumna(sol, fila, col):
    encontrada = False
    f = 0
    while not encontrada and f < fila:
        encontrada = sol[f] == col
        f += 1
    return encontrada


def damaEnDiag1(sol, fila, col):
    encontrada = False
    f = 0
    while not encontrada and f < fila:
        encontrada = sol[f] - f == col - fila
        f += 1
    return encontrada


def damaEnDiag2(sol, fila, col):
    encontrada = False
    f = 0
    while not encontrada and f < fila:
        encontrada = sol[f] + f == col + fila
        f += 1
    return encontrada


def esFactible(sol, fila, col):
    return not (damaEnColumna(sol, fila, col) or damaEnDiag1(sol, fila, col) or damaEnDiag2(sol, fila, col))


def nReinasVA(sol, fila):
    N = len(sol)
    if fila == N:
        esSol = True
    else:
        esSol = False

    col = 0
    while not esSol and col < N:
        if esFactible(sol, fila, col):
            sol[fila] = col
            sol, esSol = nReinasVA(sol, fila + 1)
        col += 1
    if not esSol:
        sol[fila] = -1
    return sol, esSol


n = 4
sol = inicializarSol(n)
fila = 0
sol, esSol = nReinasVA(sol, fila)

if not esSol:
   print("No se ha encontrado solución.")
else:
    imprimir(sol)
