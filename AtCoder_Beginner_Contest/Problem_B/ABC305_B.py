l_1 = []
for i in range(97, 123):
    l_1.append(chr(i))

s = input()

for i in s:
    if i in l_1:
        l_1.remove(i)

if not l_1:
    print("None")
else:
    print(l_1[0])