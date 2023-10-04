

numCards, maxRisk = map(int, input().strip().split())
cards = []
for i in range(numCards):
    enter = input().split()
    cards.append((int(enter[1]) / int(enter[2]), enter[0], int(enter[1]), int(enter[2])))
cards.sort()
freeRisk = maxRisk
listSol = []
idx = 0
isEnd = False
while not isEnd:
    if cards[idx][2] < freeRisk:
       listSol.append(cards[idx][1])
       freeRisk -= cards[idx][2]
       idx += 1
    else:
        listSol.append(cards[idx][1])
        val = freeRisk / cards[idx][2]
        freeRisk -= val * cards[idx][2]
        isEnd = True

for action in listSol:
    print(action, end=' ')
