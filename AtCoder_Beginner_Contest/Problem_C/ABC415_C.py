t = int(input())   # テストケースの数

# ケースごとにYesNo判定
for _ in range(t):
    n = int(input())   # 薬品の種類
    s = input()   # 薬品の状態
    s = "0" + s

    ok = [0] * (1 << n)
    ok[0] = 1

    for i in range(1 << n):
        if not ok[i]:
            continue
        
        for j in range(n):   # 薬品1=(j=0)
            # すでに入っているならpass
            if i & (1 << j):
                continue
            # 組み合わせた時に危険でない場合、okに追加
            next_point = i | (1 << j)
            if s[next_point] == "0":
                ok[next_point] = 1
        
    print("Yes" if ok[-1] == 1 else "No")


























"""
TLE
再帰関数を用いて
"""
# def dfs(path, visited):
#     # 危険な状態だったら終了
#     for i in range(len(n_out)):
#         check = []
#         for j in range(1, len(visited)):
#             if visited[j] == True:
#                 check.append(j)
#         if n_out[i] == check:
#             return False
        
#     # すべての点を通ったら終了
#     if len(path) == len(visited)-1:
#         return True

#     for next_point in range(1, n+1):  # 1〜9の点
#         if not visited[next_point]:
#             # まだ訪れてないなら進む
#             visited[next_point] = True
#             if dfs(path + [next_point], visited):
#                 return True
#             visited[next_point] = False  # 戻ってきたときに訪問状態をリセット（バックトラック）
            
#     return False



# t = int(input())   # テストケースの数

# # ケースごとにYesNo判定
# for i in range(t):
#     n = int(input())   # 薬品の種類
#     s = input()   # 薬品の状態
    
#     # 危険な状態を用意　[[1,2], [3]...]
#     out = [i+1 for i, value in enumerate(s) if value == "1"]
#     n_out = [[] for _ in range(len(out))]
    
#     for j in range(len(out)):
#         out[j] = bin(out[j])[::-1][:-2]
#         for k in range(len(out[j])):
#             if out[j][k] == "1":
#                 n_out[j].append(k+1)
    
#     # YesNo判定
#     for j in range(1, n+1):
#         visited = [False]*(n+1)
#         visited[j] = True
    
#         found = dfs([j], visited)
    
#         if found:
#             print("Yes")
#             break
#     else:
#         print("No")