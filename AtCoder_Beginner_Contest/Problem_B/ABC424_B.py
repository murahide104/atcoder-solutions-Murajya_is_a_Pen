n, m, k = map(int, input().split())
n_l = [0] * (n+1)
m_l = [0] * (m+1)
ans = []
for i in range(k):
    a, b = map(int, input().split())
    n_l[a] += 1
    if n_l[a] == m:
        ans.append(a)

print(*ans)