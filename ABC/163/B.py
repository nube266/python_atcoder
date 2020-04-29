n, m = map(int, input().split())
A = input().split()
sum = 0
for a in A:
    sum += int(a)
if n >= sum:
    print(n - sum)
else:
    print("-1")
