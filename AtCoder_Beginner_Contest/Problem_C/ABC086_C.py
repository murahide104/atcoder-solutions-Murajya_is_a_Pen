n = int(input())

prev_t = 0
prev_x = 0
prev_y = 0

for i in range(n):
    t, x, y = map(int, input().split())

    dist = abs(x-prev_x) + abs(y-prev_y)    # マンハッタン距離
    dt = t-prev_t
    
    if dist <= dt:
        if (dist % 2) == (dt % 2):
            prev_t = t
            prev_x = x
            prev_y = y
            continue
    
    print("No")
    exit()

else:
    print("Yes")