#!/usr/bin/python

import string

ciphertext = "UVWWVX YZAYZ AX BX CXUVWWVU DZERZZ ZY AFGBH HGZ FVIJD UBKKY FZTDVW"
ciphertext = ciphertext.upper();
print("Ciphertext: %s" % ciphertext)

# count total letters
total = 0
for char in ciphertext:
    if char.isalpha():
        total += 1
print("Total chars: %i" % total)

# count frequency
for letter in string.ascii_uppercase:
    count = ciphertext.count(letter)
    if count > 0:
        print("%s: %i (%0.2f%%)" % (letter, count, count/total * 100))

def rotate(letter, num):
    if not letter.isalpha():
        return letter

    letter = letter.upper()
    position = ord(letter) - ord('A') + num
    position = position % 26
    
    return chr(position + ord('A'))

# rot-N encryption check
def rotate_all():
    for i in range(0, 26):
        message = ""
        for char in ciphertext:
            message += rotate(char, i)
        
        print(message) 


def twowords():
    cipher = 'AX BX'
    cipherwords = cipher.split()
    validwords = ['OF',
            'TO',
            'IN',
            'IT',
            'IS',
            'BE',
            'AS',
            'AT',
            'SO',
            'WE',
            'HE',
            'BY',
            'OR',
            'ON',
            'DO',
            'IF']

    validwords = [word[::-1] for word in validwords]
    validwords.sort()
    validwords = [word[::-1] for word in validwords]
    for word in validwords:
        print(word)

def firstword():
    words = open("english.txt").read().splitlines()
    
    # strip words that aren't 6chars
#    for word in words:
#        if not len(word) == 6:
#            words.remove(word)

    # find words of the pattern UVWWVX
    for word in words:
        if len(word) == 6 and word[2] == word[3] and word[1] == word[4] and word[4] != word[5]:
            print(word)
        
def sixth():
    words = open("english.txt").read().splitlines()
    
    for word in words:
        if len(word) == 6 and word[1] == word[4] and word[1] == word[5] and word[1] == 'e':
            print(word)

sixth()
