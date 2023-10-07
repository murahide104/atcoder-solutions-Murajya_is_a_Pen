import numpy as np

a = [list(map(int, input().split())) for _ in range(2)]
a_ = np.array(a)

print(a_[0][0]*a_[1][1]-a_[0][1]*a_[1][0])