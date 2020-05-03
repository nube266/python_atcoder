def chmin(a, b):
    if a > b:
        return b
    else:
        return a


N = int(input())
h = list(map(int, input().split()))

# dp[i]: i番目の足場への最小の移動コスト
dp = [float("inf")] * N * 10

for i in range(N):
    if i == 0:
        dp[0] = 0
    elif i == 1:
        dp[1] = abs(h[1] - h[0])
    else:
        dp[i] = chmin(abs(h[i] - h[i - 1]) + dp[i - 1],
                      abs(h[i] - h[i - 2]) + dp[i - 2])
print(dp[N - 1])
