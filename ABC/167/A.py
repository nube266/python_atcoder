S = str(input())
T = str(input())
t = ""
for i in range(len(T) - 1):
    t += T[i]
print("Yes") if S == t else print("No")
