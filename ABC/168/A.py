a = int(input())
# a, b = map(int, input().split())
l1 = [0,
      1,
      6,
      8
      ]
if a % 10 in l1:
    print("pon")
elif a % 10 == 3:
    print("bon")
else:
    print("hon")
