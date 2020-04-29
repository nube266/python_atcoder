N = int(input())
A = list(map(int, input().split()))
print("YES") if len(A) == len(list(set(A))) else print("NO")
