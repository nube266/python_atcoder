X = int(input())

m = 100
year = 0

while X > m:
    year += 1
    m += int(m * 0.01)

print(year)
