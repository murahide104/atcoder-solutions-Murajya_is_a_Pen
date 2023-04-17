import numpy as np
L_ = [list(map(str, input().split())) for _ in range(4)]

L = np.array(L_)
rotatede_L = np.rot90(L, k=2)
rotatede_L = '\n'.join([' '.join(map(str, row)) for row in rotatede_L])

print(rotatede_L)