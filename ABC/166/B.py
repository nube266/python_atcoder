N, K = map(int, input().split())
l = [1] * N
for i in range(K):
    d = int(input())
    A = list(map(int, input().split()))
    for a in A:
        l[a - 1] = 0
print(sum(l))
