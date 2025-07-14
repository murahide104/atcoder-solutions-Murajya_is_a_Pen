k, s = map(int, input().split())

count = 0

for i in range(k+1):
    if s < i: break
    for j in range(k+1):
        if s < i + j: break
        if s - (i + j)  <= k:
            count += 1

print(count)