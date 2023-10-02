
#Hecho por el profe
def isFeasible(almendras, nextCandIdx, freeWeight):
    return freeWeight - almendras[nextCandIdx][2] > 0


def greedyKnapSack(almendras, maxWeight):
    n = len(almendras)
    freeWeight = maxWeight
    isSol = False
    nextCandIdx = 0
    nutrition = 0
    while not isSol and nextCandIdx < n: #
        almendra = almendras[nextCandIdx]
        if isFeasible(almendras, nextCandIdx, freeWeight):
            freeWeight -= almendra[2]
            nutrition += almendra[1]
        else:
            valor = freeWeight / almendra[2]
            nutrition += (valor * almendra[2])
            isSol = True
        nextCandIdx += 1
    return nutrition

n, m = map(int, input().strip().split())
almendaras = []
for i in range(n):
    v, p = map(int, input().strip().split())
    almendaras.append((v/p, v, p, i))
almendaras.sort(reverse=True)

for i in range(m):
    mv, mp = map(int, input().strip().split())
    nutVal = greedyKnapSack(almendaras, mp)
    if nutVal >= mv:
        print("PUEDE")
    else:
        print("TOS")
