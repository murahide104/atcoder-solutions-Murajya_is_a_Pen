a, b, c = map(int, input().split())

if c == 0:
    while True:
        if a == 0:
            print("Aoki")
            break
        a -= 1
        if b == 0:
            print("Takahashi")
            break
        b -= 1
else:
    while True:
        if b == 0:
            print("Takahashi")
            break
        b -= 1
        if a == 0:
            print("Aoki")
            break
        a -= 1