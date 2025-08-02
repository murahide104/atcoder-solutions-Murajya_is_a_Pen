# n, q = map(int, input().split())
# a = list(map(int, input().split()))

# painted = [0]*n

# for i in range(q):
#     if painted[a[i]-1]:
#         painted[a[i]-1] = 0
#     else:
#         painted[a[i]-1] = 1
    
#     cnt = 0
#     start = False
#     for j in range(n):
#         if (painted[j] == 1) and (not start):
#             start = True
#             cnt += 1
#         elif painted[j] == 0:
#             start = False

#     print(cnt)


"""
色を塗り替えたところの前後だけ見る
"""

n, q = map(int, input().split())
a = list(map(int, input().split()))

painted = [0]*(n+2) # パッディング (0とnは常に白)(2番目 i=2)

cnt = 0
for i in range(q):
    if painted[a[i]]:   # 黒 to 白 
        painted[a[i]] = 0   # to白
        # 両橋黒 +1
        if (painted[a[i]-1]  == 1) and (painted[a[i]+1] == 1):
            cnt += 1
        # 両橋白　-1
        if (painted[a[i]-1]  == 0) and (painted[a[i]+1] == 0):
            cnt -= 1
    else:   # 白 to 黒
        painted[a[i]] = 1   # to黒
        
        # 両橋白 ＋1
        if (painted[a[i]-1]  == 0) and (painted[a[i]+1] == 0):
            cnt += 1
        # 両橋黒 -1
        if (painted[a[i]-1]  == 1) and (painted[a[i]+1] == 1):
            cnt -= 1
            
    print(cnt)