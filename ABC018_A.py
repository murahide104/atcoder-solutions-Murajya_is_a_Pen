n_list = [int(input()) for _ in range(3)]
sorted_n_list = sorted(n_list, reverse=True)
for i in range(3):
    print(sorted_n_list.index(n_list[i])+1)