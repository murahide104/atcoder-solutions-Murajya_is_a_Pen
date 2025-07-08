n = int(input())
s = input()

east = [0] * (n+1)
west = [0] * (n+1)

reversed_s = s[::-1]

# 累積和を求める
for i in range(n):
    if reversed_s[i] == "E":
        east[i+1] = east[i] + 1
    else:
        east[i+1] = east[i]

    if s[i] == "W":
        west[i+1] = west[i] + 1
    else:
        west[i+1] = west[i]
else:
    east.reverse()

# 最小値を求める
res = 999999
for i in range(n):
    temp = west[i] + east[i+1]
    res = min(res, temp)

print(res)



# n = int(input())
# s = input()

# east = [0] * (n+1)
# west = [0] * (n+1)

# # 累積和を求める
# for i in range(n):
#     west[i+1] = west[i] + (1 if s[i] == "W" else 0)

# for i in range(n-1, -1, -1):
#     east[i] = east[i+1] + (1 if s[i] == "E" else 0)

# # 最小値を求める
# res = float('inf')
# for i in range(n):
#     res = min(res, (west[i] + east[i+1]))

# print(res)