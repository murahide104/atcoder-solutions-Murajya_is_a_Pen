l = list(map(int, input().split()))
if len(set(l)) == 2 and l.count(l[0]) in [2, 3] :
    print("Yes")
else:
    print("No")