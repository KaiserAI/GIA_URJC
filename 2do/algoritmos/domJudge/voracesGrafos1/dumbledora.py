
def updateComponentes(componentes, idOld, idNew):
    for i in range(len(componentes)):
        if componentes[i] == idOld:
            componentes[i] = idNew
    return componentes


def updateCostPerRoom(costPerRoom, c, h1, h2):
    costPerRoom[h1] += c
    costPerRoom[h2] += c


def kruskal(numRooms, rooms):
    componentes = list(range(numRooms))
    count = numRooms
    mst = 0
    rooms.sort()
    i = 0
    costPerRoom = [0]*numRooms
    while count > 1 and len(rooms) > i:
        c, h1, h2 = rooms[i]
        if componentes[h1] != componentes[h2]:
            count -= 1
            mst += c
            updateCostPerRoom(costPerRoom, c, h1, h2)
            updateComponentes(componentes, componentes[h1], componentes[h2])
        i += 1
    return mst, costPerRoom

numRooms, numHalls = map(int, input().strip().split())
rooms = []
for _ in range(numHalls):
    h1, h2, c = map(int, input().strip().split())
    rooms.append((c, h1, h2))

mst, listCost = kruskal(numRooms, rooms)
print(f'Coste total: {mst}')
for i in range(numRooms):
    print(f'H{i}: {listCost[i]}')
    
