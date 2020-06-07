def make_divisors(n):
    """
    約数を列挙
    入力：整数n
    戻り値：約数のリスト

    例
    入力：105
    戻り値：[1, 3, 5, 7, 15, 21, 35, 105]
    """
    lower_divisors, upper_divisors = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n // i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


n = int(input())
ans = 0
for i in range(1, n + 1, 2):
    if len(make_divisors(i)) == 8:
        ans += 1
print(ans)
