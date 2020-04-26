A, B = map(float, input().split())
ori8_min = A / 0.08
ori8_max = (A + 1) / 0.08
ori10_min = B / 0.1
ori10_max = (B + 1) / 0.1
for i in range(10001):
    if ori10_min <= i < ori10_max and ori8_min <= i < ori8_max:
        print(i)
        exit()
print(-1)
