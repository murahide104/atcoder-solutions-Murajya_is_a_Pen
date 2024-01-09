h, w = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(h)]

#最小値探索
min_n = 100
for row in l:
    if min(row) < min_n:
        min_n = min(row)

count = 0

#最小値までの差を取り除く
for i in range(h):
    for j in range(w):
        if min_n < l[i][j]:
            count += l[i][j] - min_n

print(count)