l = list(map(int, input().split()))
l_sorted = sorted(l)
if l_sorted[1] == l[1]:
    print("Yes")
else:
    print("No")