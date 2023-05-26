a, b, c, x = map(int, input().split())
if x <= a:
    print(float(1))
elif x > b:
    print(float(0))
else:
    print(c/(b-a))