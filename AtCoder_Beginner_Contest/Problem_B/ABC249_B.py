s = input()

u_check = True
l_check = True
unique_check = False

for char in s:
    if char.isupper():
        u_check = False
    if char.islower():
        l_check = False
    if s.count(char) != 1:
        unique_check = True

if u_check or l_check or unique_check:
    print("No")
else:
    print("Yes")
    