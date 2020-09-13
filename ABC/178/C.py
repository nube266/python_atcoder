p = 10 ** 9 + 7


def func(a, n):
    bi = str(format(n, "b"))
    res = 1
    for i in range(len(bi)):
        res = (res * res) % p
        if bi[i] == "1":
            res = (res * a) % p
    return res


N = int(input())
n = func(10, N)
no_0 = func(9, N)
no_9 = func(9, N)
no_09 = func(8, N)
ans = (n - no_0 - no_9 + no_09)
if ans < 0:
    ans += p
if ans < 0:
    ans += p
print(ans)
