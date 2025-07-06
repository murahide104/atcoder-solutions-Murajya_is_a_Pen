import numpy as np

n = int(input())
l = np.array(list(map(int, input().split())))
count = 0

while True:
    for i in range(n):
        if l[i] % 2 != 0:
            print(count)
            exit()
    else:
        count += 1
        l = l // 2