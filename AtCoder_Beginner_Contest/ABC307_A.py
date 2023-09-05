n = int(input())
l = list(map(int, input().split()))

l2 = []
cnt = 0
total = 0

for i in range(n*7):
    total += l[i]
    cnt += 1
    if cnt == 7:
        l2.append(total)
        total = 0
        cnt = 0

print(*l2)