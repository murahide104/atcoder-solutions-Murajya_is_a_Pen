a, b = map(int, input().split())
if a == 1:
    print(1)
else:
    if a <= b:
        print(a)
    else:
        print(a-1)