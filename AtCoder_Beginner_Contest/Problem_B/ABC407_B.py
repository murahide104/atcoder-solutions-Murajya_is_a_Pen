x, y = map(int, input().split())

cnt = 0
for i in range(1, 7):
    for j in range(1, 7):
        if x <= i + j:
            cnt += 1
        elif y <= abs(i-j):
            cnt += 1

print(cnt/36)