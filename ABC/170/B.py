X, Y = map(int, input().split())

for i in range(X + 1):
    j = X - i
    if Y == i * 4 + j * 2:
        print("Yes")
        exit()
print("No")
