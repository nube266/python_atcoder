"""
自分用のpythonの便利関数一覧
"""


def factorization(n):
    """
    素因数分解
    入力：整数n
    戻り値：素因数分解のリスト

    例
    入力：n=24
    戻り値：[[2, 3], [3, 1]] ← 2^3 + 3^1
    """
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5 // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])
    if temp != 1:
        arr.append([temp, 1])
    if arr == []:
        arr.append([n, 1])
    return arr


def euclidean(p, q):
    """
    ユーグリッドの互除法
    ２つの数の最大公約数を返す
    入力：整数p, 整数q
    戻り値：最大公約数

    例
    入力p=12, q=18
    戻り値：6
    """
    if p < q:
        p, q = q, p
    while(1):
        if p % q == 0:
            return q
        p, q = q, p % q


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


if __name__ == "__main__":
    pass
