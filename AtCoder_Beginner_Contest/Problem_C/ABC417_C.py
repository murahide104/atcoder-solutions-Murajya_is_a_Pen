"""
j-i = Ai + Aj は j-Aj = i+Ai
"""

n = int(input())
A = list(map(int, input().split()))

# Aリストのjを処理
A_j = []
for j in range(1, n+1):
    A_j.append(j - A[j-1])

A_i = []
for i in range(1, n+1):
    A_i.append(i + A[i-1])

counts = {}
for x in A_j:
    if x not in counts:
        counts[x] = 0
    counts[x] += 1

cnt = 0
for x in A_i:
    if x in counts: 
        cnt += counts[x]
    
print(cnt)