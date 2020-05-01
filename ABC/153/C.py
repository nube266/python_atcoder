N, K = map(int, input().split())
H = list(map(int, input().split()))
H.sort(reverse=1)
if N < K:
    K = N
for i in range(K):
    H[i] = 0
print(sum(H))
