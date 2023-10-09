
numFoods, sizeBasket = map(int, input().strip().split())
foods = []
for i in range(numFoods):
    enter = input().split()
    foods.append((int(enter[2]) / int(enter[1]), enter[0], int(enter[1]), int(enter[2])))
foods.sort(reverse=True)
sol = False
idx = 0
sum = 0
while not sol and idx < len(foods):
    if foods[idx][2] > sizeBasket: 
        sum += foods[idx][3] * (sizeBasket / foods[idx][2])
        sol = True
    else:
        sum += foods[idx][3]
        sizeBasket -= foods[idx][2]
        idx += 1
print(f"{sum:.6f}")
