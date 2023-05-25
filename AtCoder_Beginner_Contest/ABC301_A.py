n = int(input())
s = input()

if s.count("T") == s.count("A"):
    t_cnt = 0
    a_cnt = 0
    for i in range(n):
        if s[i] == "T":
            t_cnt += 1
            if s.count("T") == t_cnt:
                print("T")
                break
        else:
            a_cnt += 1
            if s.count("A") == a_cnt:
                print("A")
                break
elif s.count("T") >= s.count("A"):
    print("T")
else:
    print("A")