from decimal import Decimal
import math
a, b = map(str, input().split())
print(math.floor(Decimal(a) * Decimal(b)))
