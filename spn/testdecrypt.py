#!/usr/bin/python3

from spn import spn
from definitions import *

# decrypt using the same exact algorithm, except decrypt mode
k  = "00111010100101001101011000111111"
ct = "1011110011010110"
pt = spn(ct, pi_s, pi_p, k, decrypt=True)
print("")
print("ciphertext = %s" % ct)
print("plaintext  = %s" % pt)
print("expected   = 0010011010110111")


