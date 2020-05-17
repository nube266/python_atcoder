import math
A, B, H, M = map(int, input().split())

h2min = H * 60 + M
s_long = 1/2 * h2min
s_short = 6 * M
if s_long >= s_short:
    small = s_short
    big = s_long
else:
    small = s_long
    big = s_short
d1 = big - small
d2 = 360 - big + small
if d1 <= d2:
    d = d1
else:
    d = d2
c = math.sqrt(A ** 2 + B ** 2 - 2 * A * B * math.cos(math.radians(d)))
print(c)
