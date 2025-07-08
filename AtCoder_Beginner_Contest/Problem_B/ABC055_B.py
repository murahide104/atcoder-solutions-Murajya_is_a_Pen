import math

n = int(input())

print(math.factorial(n) % (10**9+7))


# 毎計算ごとに割る方法
# MOD = 10**9 + 7

# def factorial_mod(n):
#     result = 1
#     for i in range(1, n+1):
#         result = (result * i) % MOD  # ←毎回modを取るのがポイント！
#     return result

# n = int(input())
# print(factorial_mod(n))