N = int(input())
A = list(map(int, input().split()))
Q = int(input())
B = []
C = []
for i in range(Q):
    b, c = map(int, input().split())
    B.append(b)
    C.append(c)

A_new = {}
for a in A:
    if not a in A_new:
        A_new[a] = 1
    else:
        A_new[a] += 1

sum = 0
for i in range(0, 1):
    b = B[i]
    c = C[i]
    if b in A_new:
        n = A_new[b]
        A_new[b] = 0
        if c in A_new:
            A_new[c] += n
        else:
            A_new[c] = n
    key_list = A_new.keys()
    res = 0
    for k in key_list:
        res += A_new[k] * k
    print(res)
    sum = res


for i in range(1, Q):
    b = B[i]
    c = C[i]
    dif = 0
    if b in A_new:
        n = A_new[b]
        A_new[b] = 0
        if c in A_new:
            A_new[c] += n
        else:
            A_new[c] = n
        dif = c * n - b * n
    sum += dif
    print(sum)
