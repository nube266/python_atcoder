N, M = map(int, input().split())
s1, s2 = 0, 0
for i in range(1, N):
    s1 += i
for i in range(1, M):
    s2 += i
print(s1 + s2)
