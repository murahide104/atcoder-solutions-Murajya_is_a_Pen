def to_base_a(n: int, base: int) -> str:
    result = ""
    while 0 < n:
        result = str(n % base) + result
        n //= base
    return result
    

a = int(input())
n = int(input())

total = 0

for i in range(1, n+1):
    # i == 1桁の場合
    if i < 10:
        a_s = to_base_a(i, a)
        if a_s == a_s[::-1]: # 回文check
            total += i
        
        s_even = str(i) * 2 # 2桁回文を生成
        if n < int(s_even): continue
        
        a_s_even = to_base_a(int(s_even), a)
        if a_s_even == a_s_even[::-1]: # 回文check
            total += int(s_even)
    
    # i == 2桁以上の場合
    else:
        s_odd = str(i)[:-1] + str(i)[::-1] # 奇数回文を生成(121)
        if n < int(s_odd): break
        
        a_s_odd = to_base_a(int(s_odd), a)
        if a_s_odd == a_s_odd[::-1]:
            total += int(s_odd)
        
        
        # 偶数回文を生成
        s_even = str(i) + str(i)[::-1] # 偶数回文を生成(1221)
        if n < int(s_even): continue
        
        a_s_even = to_base_a(int(s_even), a)
        if a_s_even == a_s_even[::-1]:
            total += int(s_even)

print(total)