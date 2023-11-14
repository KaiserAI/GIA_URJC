
def updateComponts(components, u, v):
    for i in range(len(components)):
        if components[i] == u:
            components[i] = v
    return components


def kruskel(numUni, roads):
    components = list(range(numUni))
    count = numUni
    mst = 0
    roads.sort()
    idx = 0
    while count > 1 and idx < len(roads):
        e, u, v = roads[idx]
        if components[u] != components[v]:
            mst += e
            count -= 1
            updateComponts(components, components[u], components[v])
        idx += 1
    return mst


numUni, numRoads = map(int, input().strip().split())
roads = []
for _ in range(numRoads):
    u, v, e = map(int, input().strip().split())
    roads.append((e, u, v))


mst = kruskel(numUni, roads)
print(mst)
