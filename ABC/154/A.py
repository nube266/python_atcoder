S, T = map(str, input().split())
A, B = map(int, input().split())
U = str(input())
if S == U:
    A -= 1
else:
    B -= 1
print("{0} {1}".format(A, B))