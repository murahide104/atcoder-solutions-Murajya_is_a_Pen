import sys
from itertools import groupby,combinations,accumulate,permutations,chain
from bisect import bisect_right, bisect_left
from collections import Counter, deque
from functools import reduce
from collections import defaultdict
from math import gcd, sqrt, factorial  # 階乗
from heapq import heapify,heappop,heappush
sys.setrecursionlimit(10**7) #再帰関数の呼び出し制限
import copy
 
ip = lambda: input()
mi = lambda: map(int, ip().split())
li = lambda: list(mi())
Al = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
al = 'abcdefghijklmnopqrstuvwxyz'
####################################################################
####################################################################
n,m = mi()
s = []
for i in range(n):
    s.append(ip()[3:])
t = []
for i in range(m):
    t.append(ip())
s1 = set(s)
t1 = set(t)
ans = 0
for x in s:
    if x in t1:
        ans+=1
print(ans)
