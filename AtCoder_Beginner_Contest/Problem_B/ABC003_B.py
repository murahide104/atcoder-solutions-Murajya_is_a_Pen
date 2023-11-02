s = input()
t = input()
at_list = ["a","t","c","o","d","e","r","@"]

cnt_s = s.count("@")
index_list = [-1]
for i in range(cnt_s):
    index_list.append(s.find("@", index_list[-1]+1))
    if t[index_list[-1]] in at_list:
        x = t[index_list[-1]]
        s = s[:index_list[-1]]+x+s[index_list[-1]+1:]
    else:
        print("You will lose")
        exit(0)

cnt_t = t.count("@")
index_list = [-1]
for i in range(cnt_t):
    index_list.append(t.find("@", index_list[-1]+1))
    if s[index_list[-1]] in at_list:
        x = s[index_list[-1]]
        t = t[:index_list[-1]]+x+t[index_list[-1]+1:]
    else:
        print("You will lose")
        exit(0)

if s == t:
    print("You can win")
else:
    print("You will lose")