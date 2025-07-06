import math

total = 0
p1, p2 = 0, 0

n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    total += math.sqrt((p1-x)**2 + (p2-y)**2)
    p1, p2 = x, y
else:
    total += math.sqrt((p1-0)**2 + (p2-0)**2)

print(total)