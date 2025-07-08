a, b, x = map(int, input().split())

if a % x == 0:
    print((b//x +1) - (a//x +1 -1)) # 0も割り切れるという場合も含めて＋1
else:
    print((b//x +1) - (a//x +1))
    


# bまでのxの倍数からa未満のxの個数を引く
# print(b // x - (a - 1) // x)