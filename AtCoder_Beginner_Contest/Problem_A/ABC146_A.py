s_l = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
s = input()

if s == "SUN":
    print(7)
else:
    print(s_l.index("SUN") - s_l.index(s))