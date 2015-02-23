#!/usr/bin/python3

from spn import spn
from definitions import *

k = "00111010100101001101011000111111"
pt = "0010011010110111"
ct = spn(pt, pi_s, pi_p, k)
print("")
print("plaintext  = %s" % pt)
print("ciphertext = %s" % ct)
print("expected   = 1011110011010110")


