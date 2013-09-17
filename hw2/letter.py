#!/bin/python
# indexing starts at 0, monocase alphabet

import sys

# shift forward by a number
def shift(letter, shift):
    num = to_num(letter)
    shifted = (num + shift) % 26
    return to_char(shifted)

# return a number from a letter
def to_num(letter):
    letter = letter.lower()
    return ord(letter) - ord('a') 

# return a letter from a number
def to_char(num):
    num = int(num) % 26
    num = num + ord('a')
    return chr(num)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        for word in sys.argv[1:]:
            if word.isdigit():
                print("%i: %s" % (int(word), to_char(word)))
                continue
            
            for letter in word:
                if letter.isalpha():
                    print("%s: %i" % (letter, to_num(letter)))
    else:
        print("Put in a letter!")


