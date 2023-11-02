L = list(map(int, input().split()))
if L.count(L[0]) == 3:
    print(L[0])
else:
    for i in range(len(L)):
        if L.count(L[i]) == 1:
            print(L[i])
            break