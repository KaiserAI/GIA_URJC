
def crearRelPesoValor(dicc):
    listRel = []
    pesos = list(dicc.keys())
    valores = list(dicc.values())
    for idx in range(0, len(dicc.keys())):
        listRel.append(round(valores[idx] / pesos[idx], 1))
    return listRel


def crearDiccSort(diccObjetos):
    valores = list(diccObjetos.keys())
    pesos = list(diccObjetos.values())
    diccSorted = {}
    relPesoValor = crearRelPesoValor(diccObjetos)
    for idx in range(0, len(relPesoValor)):

        diccSorted[relPesoValor[idx]] = [valores[idx], pesos[idx]]
    sortedDictWithValues = dict(sorted(diccSorted.items(), reverse=True))
    return sortedDictWithValues


def fraccionar(peso, pesoRestante):
    for num in range(9, 1, -1):
        if peso * (num/10) <= pesoRestante:
            return num/10
    else:
         return 0


def crearSol(diccSort, pesoMax):
    vectorSol = {}
    pesoRestante = pesoMax
    for i in diccSort:
        if diccSort[i][1] < pesoRestante:
            vectorSol[i] = 1
            pesoRestante -= diccSort[i][1]
        else:
            objectPorcent = fraccionar(diccSort[i][1], pesoRestante)
            vectorSol[i] = objectPorcent
            pesoRestante -= diccSort[i][1] * objectPorcent
    return vectorSol


diccObjetos = {10: 20,
               20: 30,
               30: 66,
               40: 40,
               50: 60}
pesoMax = 100

diccSort = crearDiccSort(diccObjetos)
vectorSol = crearSol(diccSort, pesoMax)
