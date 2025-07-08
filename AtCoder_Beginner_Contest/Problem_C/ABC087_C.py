n = int(input())
a = [list(map(int, input().split())) for _ in range(2)]

max_reword = [[0]*n for _ in range(2)]
max_reword[0][0] = a[0][0]

x, y = (0, 0)

for i in range(n):
    x = i
    y = 0
    
    if i < n-1:
       max_reword[y][x+1] = max_reword[y][x] + a[y][x+1]
    
    if max_reword[y+1][x] < max_reword[y][x] + a[y+1][x]:
        max_reword[y+1][x] = max_reword[y][x] + a[y+1][x]
        y += 1
        for j in range(n-i-1):
            max_reword[y][x+1] = max_reword[y][x] + a[y][x+1]
            x += 1
    x += 1

print(max_reword[1][n-1])



# 累積和の模範解答
# n = int(input())
# a = [list(map(int, input().split())) for _ in range(2)]

# # 累積和
# top = [0] * (n + 1)
# bottom = [0] * (n + 1)

# for i in range(n):
#     top[i + 1] = top[i] + a[0][i]
#     bottom[i + 1] = bottom[i] + a[1][i]

# # 最大値を探す
# res = 0
# for i in range(n):
#     # i番目の列で降りると仮定
#     tmp = top[i + 1] + (bottom[n] - bottom[i])
#     res = max(res, tmp)

# print(res)