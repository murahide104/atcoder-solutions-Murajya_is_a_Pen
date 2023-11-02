n = int(input())
h = n // 60 + 21
m = n % 60

if m < 10:
    print("{}:0{}".format(h, m))
else:
    print("{}:{}".format(h, m))