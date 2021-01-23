N = int(input())
S = []
for i in range(N):
    S.append(input())

table = [[0, 0]] * (N + 1)

table[0][0] = 1
table[0][1] = 1

for i in range(N):
    s = S[i]