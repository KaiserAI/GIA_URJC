
a, b, c = map(int, input().strip().split())
suma = a + b + c

if a < 0 or b < 0 or c < 0:
    print("ERROR")
elif suma == 180:
    print("SI")
else:
    print("NO")