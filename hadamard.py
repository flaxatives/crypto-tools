import numpy as np
import math
from scipy.linalg import hadamard as had

# define generating matrix
g = [bin(x)[2:].zfill(4) for x in range(0,16)]  # string array of 0-15 in binary
g = [[int(bit) for bit in bits] for bits in g]  # array of arrays of bits
g = np.transpose(np.matrix(g))                  # transpose

#s = np.matrix('-1,1,-1,1,-1,-1,1,-1,1,1,-1,1,1,-1,1,-1')
#result = s * had(16)
#print(result)


def enc(n):
    droppedbit = int(bin(n)[2:].zfill(5)[0])
    nbin4 = bin(n)[2:].zfill(5)[1:]     # remove high bit
    xvector = np.matrix([int(x) for x in nbin4])     # convert to array of ints
    y = (xvector * g) % 2
    y = [yi for yi in np.array(y)[0]]
    z = [(-1) ** yi for yi in y]
    if (droppedbit == 1):
        z = [zi * -1 for zi in z]
    return z
    
#def dec(n):
#    productvector = n * had(16)[0]
#    maximum = max([abs(x) for x in productvector])
#    position = 0
#    for i in range(len(productvector)):
#        if abs(productvector[i]) == max:
#            position = i
    