
numFoods, sizeBasket = map(int, input().strip().split())
foods = []
for i in range(numFoods):
    enter = input().split()
    foods.append(
        (int(enter[1]) / int(enter[2]), enter[0], int(enter[1]), int(enter[2]))
    )
foods.sort()
sol = False
idx = 0
vectSol = []
sum = 0
while not sol:
    if foods[idx][2] < sizeBasket:
        vectSol.append(foods[idx][3])
        sum += foods[idx][3]
        sizeBasket -= foods[idx][2]
        idx += 1
    else:
        num = foods[idx][2] / sizeBasket
        vectSol.append(foods[idx][3] * num)
        sum += foods[idx][3] * num
        sol = True
print(sum)
