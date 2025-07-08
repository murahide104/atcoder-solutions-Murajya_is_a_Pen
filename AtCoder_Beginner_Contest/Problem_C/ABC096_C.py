h, w = map(int, input().split())

s = [list(input()) for _ in range(h)]

directions = [(0,-1), (1,0), (0,1), (-1,0)]

for i in range(h):
    for j in range(w):
        if s[i][j] == ".":
            continue
        for dx, dy in directions:
            ni = i + dx
            nj = j + dy
            if 0 <= ni < h and 0 <= nj < w:
                if s[ni][nj]=="#":
                    break
        else:
            print("No")
            exit()
else:
    print("Yes")
