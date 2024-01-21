m, d = map(int, input().split())
y1, m1, d1 = map(int, input().split())

if d == d1:
    if m == m1:
        print(y1+1, 1, 1)
    else:
        print(y1, m1+1, 1)
else:
    print(y1, m1, d1+1)