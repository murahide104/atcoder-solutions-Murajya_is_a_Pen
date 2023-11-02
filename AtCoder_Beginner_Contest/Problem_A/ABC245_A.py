a, b, c, d = map(int, input().split())
a_time = a * 60 + b
c_time = c * 60 + d

if a_time <= c_time:
    print("Takahashi")
elif a_time == c_time:
    print("Takahashi")
else:
    print("Aoki")