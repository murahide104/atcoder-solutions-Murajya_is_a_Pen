h, w = map(int, input().split())
l = [list(list(input())) for _ in range(h)]
cnt = 0

for i in range(h):
    for j in range(w):
        if l[i][j] == "#":
            cnt += 1

print(cnt)