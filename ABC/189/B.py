from decimal import Decimal

N, X = map(int, input().split())

alco = Decimal(0.0)

for n in range(N):
    v, p = map(int, input().split())
    alco += Decimal(v) * Decimal(p) / Decimal("100")
    if alco > Decimal(X):
        print(n + 1)
        exit()
print(-1)
