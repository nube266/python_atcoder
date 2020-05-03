A, B, N = map(int, input().split())
if B > N:
    print(int(A*N/B))
else:
    work = A
    for x in range(B, N + 1, 1):
        if work < int(A*x/B)-A*int(x/B):
            work = int(A*x/B)-A*int(x/B)
    print(work)
