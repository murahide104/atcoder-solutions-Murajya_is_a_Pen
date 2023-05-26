l = list(map(int, input().split()))
l_familly = ["F", "M", "T"]
while True:
    for i in range(3):
        if l[i+1] > l[0]:
            print(l_familly[i])
            exit(0)
        l[0] -= l[i+1]