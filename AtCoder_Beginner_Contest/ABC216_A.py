x, y = map(int, input().split("."))
if y <= 2:
    print(str(x)+"-")
elif 3 <= y <= 6:
    print(x)
else:
    print(str(x)+"+")