import math

n = int(input())
xy = list(tuple(map(int, input().split())) for _ in range(n))

max_dis = 0

for i in range(n):
    for j in range(i+1, n):
        xi, yi = xy[i]
        xj, yj = xy[j]
        dis = math.hypot(xi-xj, yi-yj)
        max_dis = max(dis, max_dis)

print(max_dis)