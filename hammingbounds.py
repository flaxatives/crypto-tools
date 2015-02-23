import math

# gets all x <= 100 if (2x+1)^2 + 7 is 2^k
pow2 = [x for x in range(101) if ((2*x+1) ** 2 + 7) & ((2*x+1) ** 2 + 6) == 0]
# result == [0, 1, 2, 5, 90]
print(pow2)

# gets all x <= 30 if log_3(2n^2 + 1) is an integer
pow3 = [x for x in range(1, 31) if math.log((2*(x ** 2) + 1), 3) % 1 == 0]
print(pow3)