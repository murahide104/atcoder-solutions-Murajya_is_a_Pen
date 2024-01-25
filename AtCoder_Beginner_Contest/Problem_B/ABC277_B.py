mark = ["H", "D", "C", "S"]
num = ["A", "2", "3", "4", "5", "6", "7",
       "8", "9", "T", "J", "Q", "K"]
l = []

n = int(input())

for i in range(n):
    l.append(input())
    
    if l[i][0] in mark and l[i][1] in num:
        pass
    else:
        exit(print("No"))
else:
    if len(l) == len(set(l)):
        print("Yes")
    else:
        print("No")