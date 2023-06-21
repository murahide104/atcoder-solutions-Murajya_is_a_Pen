n = input()
for i in range(2):
    if n[i] == n[i+1] and n[i] == n[i+2]:
        print("Yes")
        exit(0)
else:
    print("Np")