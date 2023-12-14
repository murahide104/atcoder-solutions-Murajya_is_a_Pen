n = int(input())

cost = 10**10
flag = 0

for i in range(n):
    a, p, x = map(int, input().split())
    if x <= a: continue
    if p < cost:
        flag = 1
        cost = p
        
print(cost if flag else -1)