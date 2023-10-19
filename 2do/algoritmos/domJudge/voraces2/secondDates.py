

def sumAges(list):
    sumAge = 0
    for i in range(len(list)):
        sumAge += list[i][0]
    return sumAge


def showList(list):                            
    for i in range(len(list)):
        if i == len(list) - 1:
            print(list[i][1], end='\n')
        else:
            print(list[i][1], end=' ')


numPart, sizeGroup = map(int, input().strip().split())
listPart = []
for i in range(numPart):
    name, age = map(str, input().strip().split())
    listPart.append((int(age), name))
listPart.sort()
listOld = listPart[sizeGroup:]
listYoung = listPart[:sizeGroup]
listOld2 = listPart[len(listPart) - sizeGroup :]
listYoung2 = listPart[: len(listPart) - sizeGroup]


if (sumAges(listOld) - sumAges(listYoung)) > (sumAges(listOld2) - sumAges(listYoung2)):
    showList(listYoung)
    showList(listOld)
else:
    showList(listYoung2)
    showList(listOld2)
