import copy


def esSolucion(lab, f, c):
    return f == len(lab)-1 and c == len(lab[0])-1


def esMejor(s1, s2):
    n = len(s1)-1
    m = len(s1[0])-1
    return s1[n][m] < s2[n][m]


def esFactible(lab, f, c):
    return 0 <= f < len(lab) and 0 <= c < len(lab[0]) and lab[f][c] == 0


def laberintoVa(lab, mejorSol, f, c, k):
    if esSolucion(lab, f, c):
        if esMejor(lab, mejorSol):
            mejorSol = copy.deepcopy(lab)
    else:
        desp = [[0,1], [1,0], [0,-1], [-1,0]]
        for d in desp:
            newF = f+d[0]
            newC = c+d[0]
            if esFactible(lab, newF, newC):
                lab[newF][newC] = k
                mejorSol = laberintoVa(lab, newF, newC, k+1)
                lab[newF][newC] = 0
    return mejorSol
