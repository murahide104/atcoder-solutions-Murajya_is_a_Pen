n, m, p = map(int, input().split())
day = m
cnt = 0

while True:
    if day <= n:
        cnt += 1
    else:
        break
    
    day += p


print(cnt)