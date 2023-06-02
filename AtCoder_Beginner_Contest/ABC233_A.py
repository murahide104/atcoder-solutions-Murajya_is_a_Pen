x, y = map(int, input().split())
cnt = 0

while True:
    if x >= y:
        break
    x += 10
    cnt += 1

print(cnt)