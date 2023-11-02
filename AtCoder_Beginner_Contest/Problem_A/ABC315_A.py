t = list(input())
l = ["a", "e", "i", "o", "u"]
new_t = [char for char in t if char not in l]
print(*new_t, sep="")