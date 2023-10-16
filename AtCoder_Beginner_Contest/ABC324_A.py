n = int(input())
set_l = set(list(map(int, input().split())))
if len(set_l) == 1:
    print("Yes")
else:
    print("No")