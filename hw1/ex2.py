#!/usr/bin/python

import string

ciphertext = "GYOMX NOGNG QUGNE TNMXM PLMZO MXYMK TMMJO XAXEN TKZZM QEBMF TZEQK JKZQE XYEXN MQLJK NOXAN HMTJE EFETX MICXE IJMFA MIHOY HMKYH WMKZR ZOXAG IONHO N"
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
        print("%s\t%i\t(%0.2f%%)" % (letter, count, count/total * 100))

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
