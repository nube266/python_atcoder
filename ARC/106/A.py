N = int(input())
if N % 3 == 0 or N % 5 == 0:
    print(-1)
    exit()
num1 = 5
cnt1 = 1
while N >= num1:
    num2 = 3
    cnt2 = 1
    while N >= num2:
        if N - num1 - num2 == 0:
            print("{0} {1}".format(cnt2, cnt1))
            exit()
        num2 = num2 * 3
        cnt2 = cnt2 + 1
    num1 = num1 * 5
    cnt1 = cnt1 + 1
print(-1)
