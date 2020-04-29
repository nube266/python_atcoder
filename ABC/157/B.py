A1 = list(map(int, input().split()))
A2 = list(map(int, input().split()))
A3 = list(map(int, input().split()))
A = A1 + A2 + A3
N = int(input())
for i in range(N):
    b = int(input())
    A = [0 if i == b else i for i in A]
if A[0] == A[4] == A[8] == 0 or A[2] == A[4] == A[6]:
    print("Yes")
    exit()
for i in range(3):
    if A[i*3] == A[i*3 + 1] == A[i*3 + 2] == 0:
        print("Yes")
        exit()
    if A[i] == A[3 + i] == A[6 + i] == 0:
        print("Yes")
        exit()
print("No")
