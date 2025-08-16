from collections import deque

grid = [
    [1, 1, 0, 1],
    [0, 1, 0, 1],
    [0, 1, 1, 1],
    [0, 0, 0, 1]
]

h = len(grid)
w = len(grid[0])
visited = [[False] * w for _ in range(h)]

queue = deque()
queue.append((0, 0, 0))  # y, x, 歩数0からスタート
visited[0][0] = True

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

while queue:
    y, x, dist = queue.popleft()
    
    # ゴールしたかcheck
    if y == h - 1 and x == w - 1:
        print(dist)
        break    
    
    for dy, dx in directions:
        ny = y + dy
        nx = x + dx
            
        # 範囲チェック
        if 0 <= ny < h and 0 <= nx < w:
            # 道か？ & 未訪問か？
            if grid[ny][nx] == 1 and not visited[ny][nx]:
                visited[ny][nx] = True
                queue.append((ny, nx, dist + 1))
