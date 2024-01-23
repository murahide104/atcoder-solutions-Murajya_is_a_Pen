a, b, c, d, e, f, x = map(int, input().split())

cnt_t = 0
bt_check_t = False
run_cnt_t = 0
bt_cnt_t = 0

cnt_a = 0
bt_check_a = False
run_cnt_a = 0
bt_cnt_a = 0

for i in range(x):
    #高橋くん
    if bt_check_t:
        bt_cnt_t += 1
        if bt_cnt_t == c:
            bt_cnt_t = 0
            bt_check_t = False
    else:
        cnt_t += b
        run_cnt_t += 1
        if run_cnt_t == a:
            run_cnt_t = 0
            bt_check_t = True
    
    #青木くん
    if bt_check_a:
        bt_cnt_a += 1
        if bt_cnt_a == f:
            bt_cnt_a = 0
            bt_check_a = False
    else:
        cnt_a += e
        run_cnt_a += 1
        if run_cnt_a == d:
            run_cnt_a = 0
            bt_check_a = True

if cnt_t > cnt_a:
    print("Takahashi")
elif cnt_t < cnt_a:
    print("Aoki")
else:
    print("Draw")