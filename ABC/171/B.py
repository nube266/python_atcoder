N, K = map(int, input().split())
P = list(map(int, input().split()))
P.sort()
res = 0
for i in range(K):
    res += P[i]
print(res)
