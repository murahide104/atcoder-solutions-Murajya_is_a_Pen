l = list(map(int, input().split()))
set_list = set()

for i in l:
    if 0 <= i - 4:
        set_list.add(4)
        i -= 4
        if i == 0:break
    if 0 <= i - 2:
        set_list.add(2)
        i -= 2
        if i == 0:break
    if 0 <= i - 1:
        set_list.add(1)
        i -= 0
        if i == 0:break
        
print(sum(list(set_list)))