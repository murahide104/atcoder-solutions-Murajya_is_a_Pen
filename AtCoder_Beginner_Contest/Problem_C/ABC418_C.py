N, Q = map(int, input().split())
A = list(map(int, input().split()))

# 累積和準備
MAXV = 10**6
cnt = [0] * (MAXV +1)
prefix_count = [0] * (MAXV +1)
prefix_sum = [0] * (MAXV +1)

for a in A:
    cnt[a] += 1

for v in range(1, len(cnt)+1):
    prefix_count[v] = prefix_count[v-1] + cnt[v]
    prefix_sum[v] = prefix_sum[v-1] + cnt[v] * v


# 難易度毎に答え出力    
for _ in range(Q):
    B = int(input())

    if B == 1:
        print(1)
        continue
    
    ans = 0
    for k, v in count_dict.items():
        if k < B:
            ans += k*v
        else:
            ans += (B-1)*v
    ans += 1
    
    if ans <= a_sum:
        print(ans)
    else:
        print(-1)