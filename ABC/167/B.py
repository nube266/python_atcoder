A, B, C, K = map(int, input().split())
res = 0
count = 0
for i in range(A):
    if count >= K:
        print(res)
        exit()
    res += 1
    count += 1

for i in range(B):
    if count >= K:
        print(res)
        exit()
    count += 1

for i in range(C):
    if count >= K:
        print(res)
        exit()
    res -= 1
    count += 1
