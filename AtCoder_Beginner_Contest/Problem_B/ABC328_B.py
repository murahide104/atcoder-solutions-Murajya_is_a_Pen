n = int(input())
l = list(input().split())

count = 0

for i in range(1, n+1):
    for j in range(int(l[i-1])):
        if len(set(str(i))) == 1 and len(set(str(j+1))) == 1:
            if set(str(i)) == set(str(j+1)):
                count += 1
            
print(count)