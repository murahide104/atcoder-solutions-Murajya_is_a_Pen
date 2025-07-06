x = input()

zero_cnt = 0
for i in range(1, 4):
    if x[-i] == '0':
        zero_cnt += 1
    else:
        break

if zero_cnt == 0:
    print(float(x))
elif zero_cnt == 3:
    print(int(x[:-4]))
else:
    print(float(x[:-zero_cnt]))