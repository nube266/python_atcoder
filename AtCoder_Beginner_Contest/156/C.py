N = int(input())
X = list(map(float, input().split()))
P = round(sum(X) / N)
res = 0
for x in X:
    res += (int(x) - P) ** 2
print(res)
