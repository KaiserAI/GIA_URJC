import sys


def binarySearch(v, ini, end, search, iteration):
    if ini <= end:
        med = (ini + end) // 2
        if search == v[med]:
            return med, iteration
        elif search < v[med]:
            return binarySearch(v, ini, med - 1, search, iteration+1)
        else:
            return binarySearch(v, med + 1, end, search, iteration+1)
    return -1


nRooms, nAttempts, idPenny = map(int, input().strip().split())
lRooms = list(map(int, input().strip().split()))
room, iteration = binarySearch(lRooms, 0, len(lRooms) - 1, idPenny, 1)
if iteration > nAttempts:
    sys.stdout.buffer.write("¿Donde esta Penny?".encode('utf-8'))
else:
    print(f'Penny esta en la habitacion {room}, se han requerido {iteration} saltos')
