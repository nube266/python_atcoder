N, M = map(int, input().split())
H = list(map(int, input().split()))
A = []
B = []
for i in range(M):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

L = [1] * N
for i in range(M):
    if H[A[i] - 1] == H[B[i] - 1]:
        L[A[i] - 1] = 0
        L[B[i] - 1] = 0
    elif H[A[i] - 1] > H[B[i] - 1]:
        L[B[i] - 1] = 0
    else:
        L[A[i] - 1] = 0
print(sum(L))
