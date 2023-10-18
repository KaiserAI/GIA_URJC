import math
import copy

pInf = math.inf


def minEdge(lEdges):
    minVal = pInf
    minEdge = pInf
    for edge in range(len(lEdges)):
        if lEdges[edge] < minVal and lEdges[edge] != 0:
            minVal = lEdges[edge]
            minEdge = edge
    return (minEdge, minVal)


def dijkstra(graf, initial):
    grafCopy = copy.deepcopy(graf)
    visted = [initial]
    lMins = []
    while len(visted) < len(grafCopy):
        for i in visted:
            minEd = minEdge(grafCopy[i])
            if minEd[0] not in visted and minEd[0] != pInf:
                lMins.append((minEd, i))
        lMinsSort = sorted(lMins, key=lambda x: x[0][1])
        if lMinsSort[0][0][0] not in visted:
            visted.append(lMinsSort[0][0][0])
            grafCopy[lMinsSort[0][1]][lMins[0][0][0]] = pInf
        lMins = []

    return visted


grafo = [
    [0, 5, pInf, 3, pInf],
    [pInf, 0, pInf, pInf, 1],
    [pInf, pInf, 0, pInf, pInf],
    [pInf, 6, 11, 0, 6],
    [pInf, pInf, 1, pInf, 0],
]
print(dijkstra(grafo, 0))
