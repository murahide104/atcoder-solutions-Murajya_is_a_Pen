n, m = map(int, input().split())
point = list(map(int, input().split()))
num = list(map(int, input().split()))
result = 0
for i in range(len(num)):
  result += point[num[i]-1]

print(result)