S = str(input())
N = len(S)
s1 = S[:int((N - 1) / 2)]
s2 = S[int((N - 1) / 2) + 1:]
if s1 == s2:
    print("Yes")
else:
    print("No")
