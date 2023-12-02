import numpy as np

h, w = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(h)]
B = np.transpose(A)

for row in B:
    print(*row)