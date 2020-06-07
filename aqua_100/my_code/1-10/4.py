N, M = map(int, input().split())
A = []
for i in range(N):
    line = list(map(int, input().split()))
    A.append(line)

t1 = 0
t2 = 0
max_score = 0
for i in range(M):
    for j in range(i + 1, M):
        score = 0
        for k in range(N):
            if A[k][i] > A[k][j]:
                score += A[k][i]
            else:
                score += A[k][j]
        if max_score < score:
            max_score = score
print(max_score)
