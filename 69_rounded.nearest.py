#program for rounder nearest

import decimal
decimal.getcontext().prec=1
decimal.getcontext().rounding=decimal.ROUND_HALF_EVEN
print(decimal.Decimal(10)/decimal.Decimal(4))

# output 2
