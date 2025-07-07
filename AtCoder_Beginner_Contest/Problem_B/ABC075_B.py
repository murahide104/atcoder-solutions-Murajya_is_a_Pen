h, w = map(int, input().split())
grid = [list(input()) for _ in range(h)]
cnt_grid = [[""]*w for _ in range(h)]

directions = [(-1,-1), (0,-1), (1,-1),
              (-1,0),          (1,0),
              (-1,1),  (0,1),  (1,1)]

for i in range(h):
    for j in range(w):
        count = 0
        if grid[i][j] == ".":
            for dx, dy in directions:
                ni = i + dx
                nj = j + dy
                if 0 <= ni < h and 0<= nj < w and grid[ni][nj] == "#":
                    count += 1
            cnt_grid[i][j] = str(count)
        else:
            cnt_grid[i][j] = "#"
            
for row in cnt_grid:
    print("".join(row))
