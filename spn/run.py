#!/usr/bin/python

from spn import *
from definitions import *

key = '89ac36b5'

x = 'fe26'
ct = spn_hex(x, pi_s, pi_p, key)

x2 = 'fe27'
ct = spn_hex(x2, pi_s, pi_p, key)