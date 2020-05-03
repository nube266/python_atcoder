def chmin(a, b):
    if a > b:
        return b
    else:
        return a


N, K = map(int, input().split())
h = list(map(int, input().split()))

dp = [float("inf")] * N

for i in range(N):
    if i == 0:
        dp[0] = 0
        continue
    for j in range(1, K + 1):
        if i - j < 0:
            break
        dp[i] = chmin(dp[i], abs(h[i] - h[i - j]) + dp[i - j])
print(dp[N - 1])
