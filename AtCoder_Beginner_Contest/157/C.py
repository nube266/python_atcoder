N, M = map(int, input().split())
S = []
C = []
for i in range(M):
    s, c = map(int, input().split())
    S.append(s)
    C.append(str(c))

min = 10 ** (N - 1)
if min == 1:
    min = 0
max = 10 ** N

for i in range(min, max):
    st = str(i)
    flag = True
    for j in range(M):
        if st[S[j] - 1] != C[j]:
            flag = False
    if flag:
        print(i)
        exit()
print(-1)
