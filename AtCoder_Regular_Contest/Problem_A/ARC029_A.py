# # 時間がかかるお肉から焼いていく

# n = int(input())
# t = [int(input()) for _ in range(n)]
# t.sort(reverse=True)

# grill_A = 0
# grill_B = 0

# for i in range(n):
#     if i == 0:
#         grill_A = t[i]
#         continue
    
#     if grill_A < grill_B:
#         grill_A += t[i]
#     else:
#         grill_B += t[i]
    
# print(max(grill_A, grill_B))

"""
bit全探索で解く
"""

n = int(input())
t = [int(input()) for _ in range(n)]

ans = float('inf')

for i in range(1 << n):
    grill_A = 0
    grill_B = 0
    for j in range(n):
        if (i >> j) & 1:
            grill_A += t[j]
        else:
            grill_B += t[j]

    ans = min(ans, max(grill_A, grill_B))
    
print(ans)