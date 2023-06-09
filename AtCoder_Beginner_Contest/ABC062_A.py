l = [[1,3,5,7,8,10,12],[4,6,9,11],[2]]
a, b = map(int, input().split())

for i in range(3):
    if a in l[i]:
        if b in l[i]:
            print("Yes")
            break
        else:
            print("No")
            break