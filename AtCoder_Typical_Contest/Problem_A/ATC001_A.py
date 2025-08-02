import sys
sys.setrecursionlimit(10**7)

h, w = map(int, input().split())
maze = [list(input()) for _ in range(h)]
visited = [[False]*w for _ in range(h)]

next = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def dfs(x, y):
    # 引き返し条件
    if x < 0 or x >= w or y < 0 or y >= h:   # 範囲外
        return False
    if maze[y][x] == "#":   # 壁
        return False
    if visited[y][x] == True:   # 到達済み
        return False
    
    # ゴールしたか確認
    if maze[y][x] == "g":
        return True

    # 到達記録
    visited[y][x] = True
    
    # 次のマスに移動
    for dx, dy in next:
        if dfs(x + dx, y + dy):
            return True
    
    return False
        
found = False
# sを探し探索開始
for i in range(h):
    for j in range(w):
        if maze[i][j] == "s":
            found = dfs(j, i)
            break
    if found: break

print("Yes" if found else "No")