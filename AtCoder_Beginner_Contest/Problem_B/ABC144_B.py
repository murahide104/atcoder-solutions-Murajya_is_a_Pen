n = int(input())


for i in range(1, 10):
    for j in range(1, 10):
        if i * j == n:
            exit(print("Yes"))
            
else:
    print("No")