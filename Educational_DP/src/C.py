def chmax(a, b):
    if a > b:
        return a
    else:
        return b


N = int(input())
L = []
dp = [[0, 0, 0]] * N

for i in range(N):
    a, b, c = map(int, input().split())
    L.append([a, b, c])

print(dp)
