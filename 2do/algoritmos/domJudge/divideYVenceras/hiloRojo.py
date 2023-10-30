

def binarySearch(data, search, star, end):
    if star > end:
        return -1
    else:
        mid = (star + end) // 2
        if search == data[mid]:
            return mid
        else:
            if search > data[mid]:
                return binarySearch(data, search, mid + 1, end)
            else:
                return binarySearch(data, search, star, mid - 1)



n = int(input().strip())
data1 = list(map(int, input().strip().split()))
m = int(input().strip())
data2 = list(map(int, input().strip().split()))
k = int(input().strip())
for _ in range(k):
    q1, q2 = map(int, input().strip().split())
    p1 = binarySearch(data1, q1, 0, n - 1)
    p2 = binarySearch(data2, q2, 0, m - 1)
    if p1 >= 0 and p2 >= 0:
        print(str(p1) + " " + str(p2))
    else:
        print("SIN DESTINO")
      
