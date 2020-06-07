S = str(input())
l = ["A", "C", "G", "T"]
ans = 0
for i in range(len(S)):
    cnt = 0
    for j in range(i, len(S)):
        if S[j] in l:
            cnt += 1
        else:
            break
    if ans < cnt:
        ans = cnt
print(ans)
