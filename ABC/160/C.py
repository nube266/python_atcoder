K, N = map(int, input().split())
A = list(map(int, input().split()))
L = []
for i, a in enumerate(A):
    if i == len(A) - 1:
        L.append(A[0] + (K - A[i]))
    else:
        L.append(A[i + 1] - A[i])
print(sum(L) - max(L))
