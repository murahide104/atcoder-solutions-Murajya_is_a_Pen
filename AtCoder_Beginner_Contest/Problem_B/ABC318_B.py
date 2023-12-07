l = [[0]*100 for _ in range(100)]

n = int(input())

for i in range(n):
    a, b, c, d = map(int, input().split())
    for j in range(a, b):
        for k in range(c, d):
            l[j][k] = 1

cnt = 0
for row in l:
    for e in row:
        if e == 1:
            cnt += 1

print(cnt)