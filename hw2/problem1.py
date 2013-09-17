#!/usr/bin/python
# Helps with the Vigenere cipher in problem 1

import re, string, itertools 
import letter
from frequency import printfreq

cipher = "\
XKJUROWMLLPXWZNPIMBVBQJCNOWXPCCHHVVFVSLLFVXHAZITYXOHULX\
QOJAXELXZXMYJAQFSTSRULHHUCDSKBXKNJQIDALLPQSLLUHIAQFPBPC\
IDSVCIHWHWEWTHBTXRLJNRSNCIHUVFFUXVOUKJLJSWMAQFVJWJSDYLJ\
OGJXDBOXAJULTUCPZMPLIWMLUBZXVOODYBAFDSKXGQFADSHXNXEHSAR\
UOJAQFPFKNDHSAAFVULLUWTAQFRUPWJRSZXGPFUTJQIYNRXNYNTWMHC\
"

print(cipher)
repsize = 3
mincount = 2

## Count repetitions
# make a set of possible repeat strings
repset = []
for i in range(0, len(cipher) - repsize): 
    rep = cipher[i:i+repsize]
    repset.append(rep)
repset = set(repset)
# then count each possible substring
for rep in repset:
    count = cipher.count(rep)
    if count >= mincount:
        ind = []
        # find all counts of rep
        for m in re.finditer(rep, cipher):
            ind.append(m.start())
        print("\n%s repeated %i times at" % (rep, count))
        print(ind)

# ask user for probable keysize
keysize = int(input("Judging from the indices of the repetitions, \
	the GCD is probably what? "))
print('')

# print cipher split into columns
rows = [cipher[i:i+keysize] for i in range(0, len(cipher), keysize)]
for row in rows:
    print(row)

# put every nth key into a column where n = keysize
columns = []
for i in range(keysize):
    columns.append([letter for letter in cipher[i::keysize]])

# print frequency counts of each column
for i in range(len(columns)):
    print("Column %i: %s" % (i, ''.join(columns[i])))
    printfreq(''.join(columns[i]))

# ask how much to shift each column
shifted = columns
for i in range(keysize):
    shift = int(input("Shift column[%i] by: " % i))
    for j in range(len(columns[i])):
        shifted[i][j] = letter.shift(columns[i][j], shift)
    print("Column %i shifted by %.02i: %s" % (i, shift, ''.join(shifted[i])))


# print the shifted result as columns
rows = []
for i in range(len(shifted[0])):
    line = ''
    for j in range(keysize):
        line += shifted[j][i]
    rows.append(line)

for row in rows:
    print(row)

## This prints out the final plaintext
# make columns into a single string each
shifted = [''.join(column) for column in shifted]

# join the nth character of every string
plain = ''
for i in range(len(shifted[0])):
    for string in shifted:
        plain += string[i]

print("plain is:")
print(plain)
