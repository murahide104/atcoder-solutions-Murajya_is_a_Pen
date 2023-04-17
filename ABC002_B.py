t_list = ["a","i","u","e","o"]
t = input()
for i in range(len(t_list)):
    t = t.replace(t_list[i], "")
print(t)