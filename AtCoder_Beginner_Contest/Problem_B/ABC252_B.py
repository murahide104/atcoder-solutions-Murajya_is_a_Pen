n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

max_a = max(a)
max_a_index = [i+1 for i, x in enumerate(a) if x == max_a]

for n in b:
    if n in max_a_index:
        print("Yes")
        break
else:
    print("No")