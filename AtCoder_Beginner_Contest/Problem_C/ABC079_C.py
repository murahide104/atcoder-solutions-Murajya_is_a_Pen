# abcd = list(map(int, input()))
# ops = []


# for i in range(1 << 3):
#     bit = format(i, '03b')
#     ops = bit.replace("1", "+").replace("0", "-")
#     # 1行にできる
#     # ops = format(i, '03b').replace('1', '+').replace('0', '-')
    
    
#     total = abcd[0]
#     for j in range(3):
#         if ops[j] == "+":
#             total += abcd[j+1]
#         else:
#             total -= abcd[j+1]
#     else:
#         if total == 7:
#             print(abcd[0], end="")
#             for k in range(3):
#                 print(ops[k]+ str(abcd[k+1]), end="")
#             print("=7")
#             exit()

"""
bit=format() 使わずに解く
"""

abcd = list(map(int, input()))

# op全パターン探索
for i in range(1 << 3):
    total = abcd[0]
    
    # 計算
    for j in range(3):
        if (i >> j) & 1:
            total += abcd[j+1]
        else:
            total -= abcd[j+1]
    
    # =7 発見後の処理
    if total == 7:
        ops = format(i, "03b").replace("1", "+").replace("0", "-")[::-1]
        print(abcd[0], end="")
        for k in range(3):
            print(ops[k]+ str(abcd[k+1]), end="")
        print("=7")
        exit()