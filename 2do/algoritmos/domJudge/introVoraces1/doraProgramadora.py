from copy import copy

listEmploy = list(map(int, input().strip().split()))
listEmployCopy = copy(listEmploy)
diccRep = {clave: 0 for clave in listEmploy}
listRep3 = []

for num in listEmploy:
    if num in listEmployCopy:
        diccRep[num] = diccRep[num] + 1
        listEmployCopy.remove(num)
    if diccRep[num] == 3:
        listRep3.append(num)
listRep3.sort()
for num in listRep3:
    print(num, end=' ')