
def sumFact(list):
    total = 0
    num = len(list)
    list.sort()
    for i in list:
        total = total + (i * num)
        num -= 1
    return total


n, m = map(int, input().strip().split())
listTimes = []
for i in range(0, n):
    a, t = map(int, input(). strip().split())
    listTimes.append(t)

tTime = sumFact(listTimes)
listE = []

for i in range(0, m):
    e = int(input())
    listE.append(e)

for i in listE:
    if i >= tTime:
        print("APROBADO")
    else:
        print("SUSPENSO")