N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort(reverse=True)
limit = 1 / 4 / M * sum(A)
for i in range(0, M):
    if(A[i] < limit):
        print("No")
        exit()
print("Yes")
