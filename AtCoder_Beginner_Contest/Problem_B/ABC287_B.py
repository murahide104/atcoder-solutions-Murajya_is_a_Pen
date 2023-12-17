n, m = map(int, input().split())
s = []
for i in range(n):
    s.append(input()[3:])
    
t = []
for i in range(m):
    t.append(input())

ans = 0
for x in s:
    if x in t:
        ans += 1

print(ans)