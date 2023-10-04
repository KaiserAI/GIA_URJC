

def isResoluble(case, freeMoney):
    return case[1] <= freeMoney


nCases, maxMoney = map(int, input().strip().split())
cases = []
for i in range(nCases):
    materialsCost, money = map(int, input().strip().split())
    cases.append((materialsCost / money, materialsCost, money, i))
cases.sort()

listResoluble = []
benefice = 0
freeMoney = maxMoney
isEnd = False
idx = 0
while not isEnd:
    if isResoluble(cases[idx], freeMoney):
        listResoluble.append(cases[idx][3])
        freeMoney -= cases[idx][1]
        benefice += cases[idx][2]
        idx += 1
    else:
        listResoluble.append(cases[idx][3])
        valor = freeMoney / cases[idx][1]
        freeMoney -= valor * cases[idx][1]
        benefice += valor * cases[idx][2]
        isEnd = True

listResoluble.sort()
for i in range(len(listResoluble)):
    print(listResoluble[i], end=' ')
benefice = round(benefice)
print("\n", benefice)
