N = list(map(int, input().split()))
A = list(map(int, input().split()))
B = []*N[0]
B = A[N[1]-1:N[2]]
A[N[1]-1:N[2]] = A[N[3]-1:N[4]]
A[N[3]-1:N[4]] = B
print(*A)