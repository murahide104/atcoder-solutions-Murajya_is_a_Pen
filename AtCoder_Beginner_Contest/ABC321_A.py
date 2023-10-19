x = input()
n = 10
for i in range(len(x)):
    if n <= int(x[i]):
        exit(print("No"))
    n = int(x[i])
else:
    print("Yes")
