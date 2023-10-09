
def updateComponentes(componentes, idOld, idNew):
    for i in range(len(componentes)):
        if componentes[i] == idOld:
            componentes[i] = idNew
    return componentes

def kruskal(numPositions, edges):
    componentes = list(range(numPositions))
    count = numPositions
    minCos = 0
    edges.sort()
    i = 0
    while count > 1 and len(edges) > i:
        distance, idPosition1, idPosition2 = edges[i]
        if componentes[idPosition1] != componentes[idPosition2]:
            count -= 1
            minCos += distance
            updateComponentes(componentes, componentes[idPosition1], componentes[idPosition2])
        i += 1
    return minCos


numPositions, numConecctions = map(int, input().strip().split())
edges = []
for _ in range(numConecctions):
    idPosition1, idPosition2, distance = map(int, input().strip().split())
    edges.append((distance, idPosition1, idPosition2))

minCost = kruskal(numPositions, edges)
if minCost % 5 != 0:
    minCost = (minCost // 5) + 1
else:
    minCost= minCost // 5
print(minCost)
