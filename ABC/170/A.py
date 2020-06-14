l = list(map(int, input().split()))
for i, num in enumerate(l):
    if num == 0:
        print(i + 1)
