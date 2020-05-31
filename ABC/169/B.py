N = int(input())
A = list(map(int, input().split()))
res = 1
A.sort()
for i in range(N):
    res *= A[i]
    if res > (10 ** 18):
        print(-1)
        exit()
    elif res == 0:
        print(0)
        exit()
print(res)
