"""
- i*100点, D=難易度数
- 1 <= i <= D
- G点以上にしたい

bit全探索
    bit作成
    1か0か探索
        1：問題全て解く
        0：0~問題数-1まで解く

- Gを超えたらすぐbreak
"""

# D, G = map(int, input().split())
# pc = list(tuple(map(int, input().split())) for _ in range(D))
# min_slv = float("inf")

# for i in range(1 << D):
#     bit = format(i, f"0{D}b")
    
#     slv = 0
#     total = 0
    
#     # デバッグ
#     # print("----------")
#     # print(f"bit:{bit}")
    
    
#     # レベルが低い順にコンプリート得点を集計
#     for level in range(1, D+1):
#         # 1の時
#         if bit[level-1] == "1": # level: 1~D
#             p = pc[level-1][0]
#             c = pc[level-1][1]
#             total += p * level * 100 + c
#             slv += p
#             # このbitは終了
#             if G <= total: break
#     # コンプリート得点集計後、bit=0のレベルが高い順に全探索
#     else:
#         for rev_level in range(D, 0, -1):
#             # 0の時
#             if bit[rev_level-1] == "0":
#                 p = pc[rev_level-1][0]
                
#                 # そのレベルの問題数-1まで足していく
#                 for _ in range(1, p):
#                     total += rev_level*100
#                     slv += 1
#                     # 次の問題を解かない
#                     if G <= total: break
#                 # 下のレベルに進まない
#                 if G <= total: break
    
#     # bit=000・・の時、Gに達しない場合
#     if total < G: continue
    
#     # デバッグ
#     # print(f"total:{total}")
#     # print(f"slv:{slv}")
    
#     # 最小の問題数を更新
#     min_slv = min(slv, min_slv)

# print(min_slv)


"""
bit=format()を使わずに右シフト演算とアンド演算を用いて解いてみる
"""

D, G = map(int, input().split())
pc = list(tuple(map(int, input().split())) for _ in range(D))
min_slv = float("inf")

for i in range(1 << D):
    
    slv = 0
    total = 0
    
    # レベルが低い順にコンプリート得点を集計
    for level in range(1, D+1):
        # 1の時
        if (i >> level-1) & 1:   # level: 1~D
            p, c = pc[level-1]   # その難易度の p=問題数 c=コンプリートボーナス
            total += p * level * 100 + c
            slv += p
            
            if G <= total: break   # このbitを終了
    # コンプリート得点集計後、bit=0のレベルが高い順に全探索
    else:
        for level in reversed(range(1, D+1)): 
            if not ((i >> level-1) & 1):   # 0の時
                p = pc[level-1][0]   # その難易度の p=問題数
                
                # そのレベルの問題数-1まで足していく
                for _ in range(p-1):
                    total += level*100
                    slv += 1
                    
                    if G <= total: break   # 次の問題を解かない
                if G <= total: break   # 下のレベルに進まない
    
    # bit=000 and　解ける全ての問題を解いた -> Gに達しない場合
    if total < G: continue
    
    # 最小の問題数を更新
    min_slv = min(slv, min_slv)
    
print(min_slv)