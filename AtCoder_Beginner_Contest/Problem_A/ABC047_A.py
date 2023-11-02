L = list(map(int, input().split()))
L_max = L.pop(L.index(max(L)))
if L_max == sum(L):
    print("Yes")
else:
    print("No")