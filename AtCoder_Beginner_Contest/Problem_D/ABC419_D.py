n, m = map(int, input().split())
s = list(input())
t = list(input())

check = [False] * (n + 1)

for _ in range(m):
    l, r = map(int, input().split())
    
    check[l-1] ^= True
    check[r] ^= True

ans = []

parity = False
for i in range(n):
    parity ^= check[i]
    ans.append(t[i] if parity else s[i])

print("".join(ans))