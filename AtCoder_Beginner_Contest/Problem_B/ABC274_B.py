h, w = map(int, input().split())
l = [list(input()) for _ in range(h)]

count = [0]*w

for i in range(h):
    for j in range(w):
        if l[i][j] == "#":
            count[j] += 1

print(*count)
