from collections import deque

q = int(input())
deq = deque()

for _ in range(q):
    query = list(map(int, input().split()))

    if query[0] == 1:
        query_num, c, x = query
        deq.append((x, c))
        
    else:
        k = query[1]
        total = 0

        while k > 0:
            val, cnt = deq.popleft()
            if cnt <= k:
                total += val * cnt
                k -= cnt
            else:
                total += val * k
                deq.appendleft((val, cnt - k))
                k = 0

        print(total)