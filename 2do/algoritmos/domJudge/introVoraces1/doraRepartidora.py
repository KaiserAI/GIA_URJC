from copy import copy


def sumFact(list):
    total = 0
    num = len(list)
    list.sort()
    for i in list:
        total = total + (i * num)
        num -= 1
    return total


numClients = int(input())
num = copy(numClients)
listTime = []
tTime = 0
for i in range(0, numClients):
    id, time = map(int, input().strip().split())
    listTime.append(time)

tTime = sumFact(listTime)
print(tTime)