x, y, z = map(int, input().split())
y_cnt = z//3
x_cnt = z - y_cnt * 3
if x*3 < y:
    print(x * z)
else:
    print(y_cnt * y + x_cnt * x)