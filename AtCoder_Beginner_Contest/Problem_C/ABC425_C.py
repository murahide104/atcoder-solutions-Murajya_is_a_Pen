n, q = map(int, input().split())
A = list(map(int, input().split()))

B = A + A
pref = [0] * (2*n+1)
for i in range(2*n):
    pref[i+1] = pref[i] + B[i]

shift = 0
out = []

for _ in range(q):
    query = list(map(int, input().split()))
    
    if query[0] == 1:
        c = query[1]
        shift = (shift + c) % n

    else:
        l, r = query[1:]
        start = shift + (l-1)
        length = r - l + 1
        ans = pref[start+length] - pref[start]
        out.append(str(ans))

print("\n".join(out))