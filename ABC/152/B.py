a, b = map(int, input().split())
s1 = ""
s2 = ""
for i in range(a):
    s1 += str(b)
for i in range(b):
    s2 += str(a)
print(s1) if s1 <= s2 else print(s2)
