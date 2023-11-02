t = list(input())
n = int(input())
t_list = []

for i in range(len(t)):
    for j in range(len(t)):
        t_list.append(t[i]+t[j])

print(t_list[n-1])