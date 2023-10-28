l = list(map(int, input().split()))
set_list = set()
for i in l:
    if i == 1:
        set_list.add(1)
    elif i == 2:
        set_list.add(2)
    elif i == 3:
        set_list.update([1,2])
    elif i == 4:
        set_list.add(4)
    elif i == 5:
        set_list.update([1,4])
    elif i == 6:
        set_list.update([2,4])
    elif i == 7:
        set_list.update([1,2,4])

print(sum(list(set_list)))