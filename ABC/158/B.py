N, A, B = map(int, input().split())
res = N // (A + B) * A
amari = N % (A + B)
if amari >= A:
    amari = A
print(res + amari)
