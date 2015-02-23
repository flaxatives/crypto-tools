#!/usr/bin/python

import numpy as np
import gcd

Nr = 10     # hardcoded for 128

""" 
AES Algorithm 128-bit 

Encrypts 16 bytes of plaintext using the 128-bit algorithm. Plaintext is given as
an array of bytes. Key is given as an array of bytes.
"""
def encrypt(message, key):
    # arrange into 4x4
    print("Arranging message to state:")
    state = makestate(message)
    for row in state:
        print([hex(word) for word in row])

    print("\nExpanding key:")
    words = keyexpand(key)
    for i in range(0, len(words), 4):
        print([hex(word) for word in words[i:i+4]])

    # initial round
    print("Adding round key: add state column to transposed key row")
    printState(state)
    state = addroundkey(state, words[0:4])
    for word in words[0:0+4]:
        print('%x' % word)
    printState(state)
    
    # 9 rounds
    for round in range(1, 10):
        print("\nSubbing bytes")
        for i in range(4):
            for j in range(4):
                state[i][j] = subbyte(state[i][j])    # subbytes
        printState(state)

        print("Shifting rows")
        state = shiftrows(state)            # shift rows
        printState(state)

        print("Mixing Columns")
        state = mixcolumns(state)           # mix columns
        printState(state)


        print("Adding round key: add state column to transposed key row")
        state = addroundkey(state, words[round:round+4])     # add round key
        for word in words[round:round+4]:
            print("%x" % word)
        printState(state)
        
    # final round
    print("\nSubbing bytes")
    for i in range(4):
        for j in range(4):
            state[i][j] = subbyte(state[i][j])    # subbytes
    printState(state)

    print("Shifting rows")
    state = shiftrows(state)                    # shift rows
    printState(state)

    print("Adding round key")
    state = addroundkey(state, words[10:10+4])   # add round key
    for word in words[10:10+4]:
        print("%x" % word)
    printState(state)

    print("\nFinal result")
    for i in range(4):
        print("%x %x %x %x" % (state[0][i], state[1][i], 
                state[2][i], state[3][i])) 


""" add roundkey """
def addroundkey(s, keys):
    result = ([[0,0,0,0],
               [0,0,0,0],
               [0,0,0,0],
               [0,0,0,0]])
    # transpose keys into a bytearray
    for i in range(4):
        result[0][i] = (keys[i] >> 8*3) & 0xff
        result[1][i] = (keys[i] >> 8*2) & 0xff
        result[2][i] = (keys[i] >> 8*1) & 0xff
        result[3][i] = (keys[i] >> 8*0) & 0xff

    for i in range(4):
        for j in range(4):
            result[i][j] = result[i][j] ^ s[i][j]

    return result
    

""" mix columns """
def mixcolumns(s):
    fixed = np.matrix([[2,3,1,1],
                       [1,2,3,1],
                       [1,1,2,3],
                       [3,1,1,2]])
    result = ([[0,0,0,0],
               [0,0,0,0],
               [0,0,0,0],
               [0,0,0,0]])

    # for each column, mult by the fixed matrix
    for i in range(4):
        col = np.matrix([s[0][i],
                         s[1][i],
                         s[2][i],
                         s[3][i]]).transpose()
        col = fixed * col
        result[0][i] = int(col[0])
        result[1][i] = int(col[1])
        result[2][i] = int(col[2])
        result[3][i] = int(col[3])
        
    return result

    
""" Shift rows """
def shiftrows(s):
    return [ [s[0][0], s[0][1], s[0][2], s[0][3]],
             [s[1][1], s[1][2], s[1][3], s[1][0]],
             [s[2][2], s[2][3], s[2][0], s[2][1]],
             [s[3][3], s[3][0], s[3][1], s[3][2]] ]


""" Turns a 16 byte array into a 4x4 byte array """
def makestate(message):
    state = []
    count = 0
    for i in range(4):
        state.append([])
        for j in range(4):
            state[i].append(0)
    for i in range(4):
        for j in range(4):
            state[j][i] = message[count]
            count += 1
    return state


""" 
AES 128-bit key expansion

Takes a key of 128 bits as an array of int bytes and expands it
to an array of 44 words
"""
def keyexpand(key):
    rcon = [0] * (Nr + 1)

    rcon[1] =  0x01000000
    rcon[2] =  0x02000000
    rcon[3] =  0x04000000
    rcon[4] =  0x08000000
    rcon[5] =  0x10000000
    rcon[6] =  0x20000000
    rcon[7] =  0x40000000
    rcon[8] =  0x80000000
    rcon[9] =  0x1b000000
    rcon[10] = 0x36000000

    words = []      # array of 44 words
    for i in range (0,4):
        words.append(concat_bytes(key[4*i], key[4*i+1], key[4*i+2], key[4*i+3]))

    for i in range(4,44):
        temp = words[i-1]
        if i % 4 == 0:
            temp = subword(rotword(temp)) ^ rcon[i//4]
        words.append(words[i-4] ^ temp)

    return words


""" Concats a sequence of int bytes and returns it as an int """
def concat_bytes(*bytes):
    word = 0
    for byte in bytes:
        word = (word << 8) ^ byte
    return word


""" Rotate 4 byte int to the left by a byte """
def rotword(word):
    b0 = (word >> 8*3) & 0xff       # grab leftmost byte
    word = (word << 8) & 0xffffff00 # shift to left by byte
    word = word ^ b0                # put b0 at the rightmost pos
    return word


""" Applies AES s-box to each byte of a 4byte int """
def subword(word):
    byte = [0] * 4
    byte[3] = word & 0xffA              # get 4 bytes
    byte[2] = (word >> 8) & 0xff
    byte[1] = (word >> 8*2) & 0xff
    byte[0] = (word >> 8*3) & 0xff

    for i in range(4):
        byte[i] = subbyte(byte[i])      # apply s-box to bytes

    return concat_bytes(byte[0], byte[1], byte[2], byte[3])


""" Applies AES s-box to a byte using extended gcd """
def subbyte(byte):
    # convert byte to polynomial, find inverse using extended gcd
    poly = [int(bit) for bit in bin(byte)[2:].zfill(8)]
    poly.reverse()
    rijndael_poly = [1, 1, 0, 1, 1, 0, 0, 0, 1]
    d, g, z, a1, b1 = gcd.extgcd(rijndael_poly, poly)

    # convert to column vector
    while len(z) < 8:
        z.append(0)
    z = np.matrix(z).transpose()
    a = np.matrix([1,1,0,0,0,1,1,0]).transpose()

    m = np.matrix([ [1,0,0,0,1,1,1,1], \
                    [1,1,0,0,0,1,1,1], \
                    [1,1,1,0,0,0,1,1], \
                    [1,1,1,1,0,0,0,1], \
                    [1,1,1,1,1,0,0,0], \
                    [0,1,1,1,1,1,0,0], \
                    [0,0,1,1,1,1,1,0], \
                    [0,0,0,1,1,1,1,1] ] )
    q = np.matrix([1,1,0,0,0,1,1,0]).transpose()
    product = (m * z) % 2
    product = product ^ q   # perform math!

    # convert back to int
    a = np.array(product.transpose())
    result = [x for x in a[0]]
    result.reverse()
    result = ''.join([str(bit) for bit in result])
    return int(result,2)


def printState(state):
    for row in state:
        print([hex(word) for word in row])
