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


def dijkstra(graf, initial):                                        # Este dijkstra lo que me da son los nodos que recorro (en orden) para recorrer todo el grafo en la mínima distancia.
    grafCopy = copy.deepcopy(graf)
    visted = [initial]
    lMins = []
    while len(visted) < len(grafCopy):
        for i in visted:
            minEd = minEdge(grafCopy[i])                            #  Devuelve el nodo que menos distancia requiere para alcanzarlo y la propia distancia.
            if minEd[0] not in visted and minEd[0] != pInf:         #  Si no he visitado ese nodo lo agrego a una lista de posibles conexiones.
                lMins.append((minEd, i))
        lMinsSort = sorted(lMins, key=lambda x: x[0][1])            #  Una vez haya visto todas las posibles conexiones me quedo con la que menos distancia tenga,
        if lMinsSort[0][0][0] not in visted:
            visted.append(lMinsSort[0][0][0])
            grafCopy[lMinsSort[0][1]][lMins[0][0][0]] = pInf        #  A esta que cogí le asigno infinito para evitar cogerla de nuevo.
        lMins = []
    return visted


grafo = [
    [0, 5, pInf, 3, pInf],
    [pInf, 0, pInf, pInf, 1],
    [pInf, pInf, 0, pInf, pInf],
    [pInf, 1, 11, 0, 6],
    [pInf, pInf, 1, pInf, 0],
]
print(dijkstra(grafo, 0))


######################################################Implementación del profe##########################################

def selectMinDistance(distance, visited):                  # Este me da la mínima distancia desde un nodo inicial al resto.
    minDist = float("inf")
    bestItem = 0
    for i in range(1, len(distance)):
        if not visited[i] and distance[i] < minDist:
            minDist = distance[i]
            bestItem = i
    return bestItem


def dijkstraP(g, origin):
    n = len(g) - 1
    distance = [float("Inf")] * (n+1)
    visited = [False] * (n+1)

    distance[origin] = 0
    visited[origin] = True

    for start, end, weight in g[origin]:
        distance[end] = weight
    for _ in range(2, len(g)):
        nextNode = selectMinDistance(distance, visited)
        visited[nextNode] = True
        for star, end, weight in g[nextNode]:
            distance[end] = min(distance[end], distance[nextNode]+weight)
    return distance


grafo2 = [
    [],
    [(1, 2, 5), (1, 4, 3)],
    [(2, 5, 1)],
    [],
    [(4, 2, 1), (4, 3, 11), (4, 5, 6)],
    [(5, 3, 1)]
]
print(dijkstraP(grafo2, 1))
