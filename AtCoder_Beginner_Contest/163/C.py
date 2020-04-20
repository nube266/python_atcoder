N = int(input())
A = list(map(int, input().split()))
res = [0] * N
for a in A:
    res[a - 1] += 1
for r in res:
    print(r)
