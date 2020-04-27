N = int(input())
d = {}
for i in range(N):
    s = str(input())
    if not s in d:
        d[s] = 1
    else:
        d[s] = d[s] + 1
max = 0
res = []
for key in d:
    num = d[key]
    if num < max:
        continue
    elif num == max:
        res.append(key)
    else:
        max = num
        res = [key]
res.sort()
for r in res:
    print(r)
