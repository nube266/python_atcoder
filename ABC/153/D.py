H = int(input())
count = 0
while H > 0:
    H = H // 2
    count += 1
res = 0
a = 1
for i in range(1, count + 1):
    res += a
    a *= 2
print(res)
