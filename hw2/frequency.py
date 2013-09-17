#!/usr/bin/python

import string, sys

# prints the frequency counts of each string
def printfreq(text):
    text = text.upper()
    for letter in string.ascii_uppercase:	# prints alphabetically
        count = text.count(letter)
        if count > 0:
            print("%s: %i (%.02f%%)" 
                    % (letter, count, count/countchars(text) * 100))

# count the number of alphabet chars in string
def countchars(text):
    count = 0
    for char in text:
        if char.isalpha():
            count += 1

    return count

if __name__ == "__main__":
    if len(sys.argv) > 1:
        text = ''.join(sys.argv[1:])
        print("Total alpha chars: %i" % len(''.join([c for c in text if c.isalpha()])))
        printfreq(text)

    else:
        print("Please specify a string.")
