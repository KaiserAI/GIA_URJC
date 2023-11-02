
diccTasks = {
    1: [50, 2],
    2: [10, 1],
    3: [15, 2],
    4: [30, 1]
}

listValues = list(diccTasks.values())
listValues.sort(reverse=True)
vectSol = []
lTakens = []

for i in range(len(listValues)):
    if listValues[i][1] not in lTakens:
        vectSol.append(listValues[i])
        lTakens.append(listValues[i][1])
    else:
        pass
vectSol.sort()
print(vectSol)
