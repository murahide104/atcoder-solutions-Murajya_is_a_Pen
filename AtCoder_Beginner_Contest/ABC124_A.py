a, b = map(int, input().split())
total = 0
if a > b :
    total += a
    a -= 1
else:
    total += b
    b -= 1

total += max(a, b)
print(total)