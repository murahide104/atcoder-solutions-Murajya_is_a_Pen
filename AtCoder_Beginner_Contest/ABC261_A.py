l1, r1, l2, r2 = map(int, input().split())
red_list = []
blue_list = []

for i in range(l1,r1+1):
    red_list.append(i)
set_red = set(red_list)

for j in range(l2,r2+1):
    blue_list.append(j)
set_blue = set(blue_list)

if len(set_red & set_blue)-1 < 0:
    print(0)
else:
    print(len(set_red & set_blue)-1)
