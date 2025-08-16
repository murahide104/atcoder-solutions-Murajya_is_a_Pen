from collections import deque

r, c = map(int, input().split())
start_y, start_x = tuple(map(int, input().split()))
goal_y, goal_x = tuple(map(int, input().split()))
grid = [list(input()) for _ in range(r)]

visited = [[False] * c for _ in range(r)]

queue = deque()
queue.append((start_y-1, start_x-1, 0))  # y, x, 歩数0からスタート
visited[start_y-1][start_x-1] = True

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

while queue:
    y, x, dist = queue.popleft()
    
    # ゴールしたかcheck
    if y == goal_y-1 and x == goal_x-1:
        print(dist)
        break
    
    # 移動できるかcheckし、可能ならキューに追加
    for dy, dx in directions:
        ny = y + dy
        nx = x + dx
            
        # 範囲チェック
        if 0 <= ny < r and 0 <= nx < c:
            # 道か？ & 未訪問か？
            if grid[ny][nx] == "." and not visited[ny][nx]:
                visited[ny][nx] = True
                queue.append((ny, nx, dist + 1))