mod = 10 ** 9 + 7
N, K = map(int, input().split())
sum = 0
for i in range(K, N + 2):
    max = N * i - i * (i - 1) // 2
    min = i * (i - 1) // 2
    sum += max - min + 1
print(sum % mod)
