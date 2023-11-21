n = int(input())
l = list(map(int, input().split()))

value_to_remove = max(l)
new_l = [x for x in l if x != value_to_remove]

print(max(new_l))