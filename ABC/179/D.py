N, K = map(int, input().split())

S = []

for i in range(K):
    l, r = map(int, input().split())
    for j in range(l, r + 1):
        S.append(j)

dp = [0] * N * 10

dp[1] = 1

for i in range(1, N + 1):
    if dp[i] == 0:
        continue
    for s in S:
        if i + s <= N + 1:
            dp[i + s] = (dp[i + s] + dp[i]) % 998244353

print(dp[N])
