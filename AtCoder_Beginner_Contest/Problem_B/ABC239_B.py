x = input()

if x[0] == "-":
    if len(x) == 2:
        print(x)
    elif x[-1] == "0":
        print(f"-{x[1:-1]}")
    else:
        print(f"-{int(x[1:-1])+1}")
else:
    if len(x) == 1:
        print(0)
    else:
        print(x[:-1])