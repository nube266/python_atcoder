n = int(input())
sum = 0
for a in range(1, n + 1):
    if a % 3 == 0 or a % 5 == 0:
        continue
    sum += a
print(sum)
