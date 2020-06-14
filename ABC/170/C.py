X, N = map(int, input().split())
P = list(map(int, input().split()))

min_val = -1
for i in range(-1000, 1000):
    if i in P:
        continue
    if abs(min_val - X) > abs(X - i):
        min_val = i
if len(P) == 0:
    print(X)
else:
    print(min_val)
