n = int(input())
n_list = [input() for i in range(n)]
if n_list.count("For") > n//2:
    print("Yes")
else:
    print("No")