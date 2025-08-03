grid = [list(input()) for _ in range(10)]

# 次に進む方向リスト
next = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def dfs(i, j):
    # 範囲外、海、到達済みの場合return
    if i < 0 or i >= 10 or j < 0 or j >= 10:
        return
    if grid[i][j] == "x" or visited[i][j]:
        return
    
    # 記録
    visited[i][j] = True
    
    # 次のマスに移動
    for dx, dy in next:
        dfs(i + dx, j + dy)

for i in range(10):
    for j in range(10):
        
        if grid[i][j] == "x":
            grid[i][j] = "o"
            visited = [[False]*10 for _ in range(10)]

            cnt = 0
            for k in range(10):
                for l in range(10):
                    if (grid[k][l] == "o") and (not visited[k][l]):
                        cnt += 1
                        dfs(k,l)
            
            grid[i][j] = "x"
        
            if cnt == 1:
                print("YES")
                exit()
else:
    print("NO")