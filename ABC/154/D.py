import math
N, K = map(int, input().split())
P = list(map(int, input().split()))
Q = []
for p in P:
    Q.append(sum(range(1, p + 1)) / p)
max = 0
tmp = 0
for i in range(N - K + 1):
    if i == 0:
        for j in range(K):
            tmp += Q[j]
    else:
        tmp = tmp + Q[i + K - 1] - Q[i - 1]
    if max < tmp:
        max = tmp
print(max)
