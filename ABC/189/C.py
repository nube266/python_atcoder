N = int(input())
A = list(map(int, input().split()))

max_mikan = 1

for l in range(N):
    x = A[l]
    for r in range(l, N):
        if x > A[r]:
            x = A[r]
        mikan = x * (r - l + 1)
        if mikan > max_mikan:
            max_mikan = mikan
print(max_mikan)
