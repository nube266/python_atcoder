N = int(input())

D = []
for i in range(N):
    d1, d2 = map(int, input().split())
    D.append([d1, d2])

count = 0
for i in range(N):
    if D[i][0] == D[i][1]:
        count += 1
        if count == 3:
            break
    else:
        count = 0

print("Yes") if count == 3 else print("No")
