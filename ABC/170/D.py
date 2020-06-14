N = int(input())
A = list(map(int, input().split()))

A.sort()
L = []
pre_val = A[0]
count = 0
for a in A:
    if pre_val == a:
        count += 1
    else:
        temp = [pre_val, count]
        L.append(temp)
        count = 1
        pre_val = a
L.append([pre_val, count])

res = 0
for i in range(len(L)):
    flag = False
    if L[i][1] != 1:
        continue
    Ai = L[i][0]
    for j in range(i):
        Aj = L[j][0]
        if Ai % Aj == 0:
            flag = True
            break
    if flag is False:
        res += 1
print(res)
