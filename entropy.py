#!/usr/bin/python

import math

string = "\
 1 1 1 5 1\
 1 2 1 1\
 2 1 1\
 15 1 17 1 1 1 2 1\
 3 2 1\
 2 2\
 7 1 1 1 1 4 1 1 1 1 1\
 3 1\
 8 6 1 3 1 1 1\
 1 1 1\
 1 1 1 1 1\
 6 2 1 1 1 1 \
 1 1 2 1 1\
 1 1 1 1\
 4 1 1 1 1 1 1\
 11 5 1 1 1 1 1 1 1 1 1 1 6\
 1 1 1 1\
 1 1 1 1 1 1\
 1 1 1\
"

nums = string.split()
unique = list(set(nums)) 
sorted = sorted([int(num) for num in unique])
probs = [nums.count(str(c)) / 101 for c in sorted]

print("num:count:probability")
for char in sorted:
	print("%s: %i : %f" % (char, nums.count(str(char)), nums.count(str(char)) / 101.0))

# summands of the entropy sigma function
summands = [p * math.log(p, 2) for p in probs]
entropy = -1 * sum(summands)
print("Entropy: " + str(entropy))
