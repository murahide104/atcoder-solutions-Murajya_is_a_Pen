"""
n = 文字列の数
k = k個の単語を組み合わせる
x = x番目の文字列を求める
"""

import itertools

n, k, x = map(int, input().split())
s = [input() for _ in range(n)]

box = sorted("".join(t) for t in itertools.product(s, repeat=k))

print(box[x-1])