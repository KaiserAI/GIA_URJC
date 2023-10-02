
numAspirantes = int(input())
alturaMinima = int(input())
listaAspirantes = list(map(int, input().strip().split()))

min = 0
may = 0
pueden = 0
for idxAspirante in range(0, numAspirantes):
    if listaAspirantes[idxAspirante] < listaAspirantes[min]:
        min = idxAspirante
    elif listaAspirantes[idxAspirante] > listaAspirantes[may]:
        may = idxAspirante
    if listaAspirantes[idxAspirante] >= alturaMinima:
        pueden += 1

print(min, may, pueden)