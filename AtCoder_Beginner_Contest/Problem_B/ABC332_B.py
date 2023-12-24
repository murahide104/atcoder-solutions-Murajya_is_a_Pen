side = ["AB", "BC", "CD", "DE", "EA",
        "BA", "CB", "DC", "ED", "EA"]
diagonal = ["AC", "AD", "BD", "BE", "CE",
            "CA", "DA", "DB", "EB", "EC"]

s = input()
t = input()

if s in side and t in side:
    print("Yes")
elif s in diagonal and t in diagonal:
    print("Yes")
else:
    print("No")