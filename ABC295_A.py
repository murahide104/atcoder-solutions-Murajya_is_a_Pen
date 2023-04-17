n = int(input())
input_set = set(input().split())
sumple_set = {"and", "not", "that", "the", "you"}
if len(input_set & sumple_set) >= 1:
    print("Yes")
else:print("No")