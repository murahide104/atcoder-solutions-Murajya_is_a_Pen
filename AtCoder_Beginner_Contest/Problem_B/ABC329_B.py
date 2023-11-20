n = int(input())
l = list(map(int, input().split()))

value_to_remove = max(l)
print(value_to_remove)
new_l = [x for x in l if x != value_to_remove]
print(new_l)
print(max(new_l))