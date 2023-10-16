import math
from cmath import inf

pInf = math.inf

def minEdge(lEdges):
    min = pInf
    for edge in range(len(lEdges)):
        if lEdges[edge] < min and lEdges[edge] != 0:
            min = lEdges[edge]
            minEdge = edge
    return (minEdge, min)


def dijkstra(graf, initial):
    vistados = []
    vistados.append(minEdge(graf[initial])[0])
    lMin = []
    while len(vistados) < len(graf):
        for i in vistados:
            if minEdge(graf[i])[1] not in vistados:
                lMin.append(minEdge(graf[i]))
        if min(lMin[0]) not in vistados:
            vistados.append(min(lMin[0]))
        lMin = []

    return vistados


grafo = [
    [0, 5, pInf, 3, pInf],
    [pInf, 0, pInf, pInf, 1],
    [pInf, pInf, 0, pInf, pInf],
    [pInf, 1, 11, 0, 6],
    [pInf, pInf, 1, pInf, 0],
]
print(dijkstra(grafo, 0))
