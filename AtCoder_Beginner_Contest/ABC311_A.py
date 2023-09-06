n = int(input())
s = input()
cnt = 0
cnt_list = [0, 0, 0]

for i in range(n):
    cnt += 1
    if s[i] == "A":
        cnt_list[0] = 1
    elif s[i] == "B":
        cnt_list[1] = 1
    elif s[i] == "C":
        cnt_list[2] = 1
    if sum(cnt_list) == 3:
        break

print(cnt)
