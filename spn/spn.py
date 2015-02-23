#!/usr/bin/python3

import sys

# converts a decimal int to n-bit binary string
def int_to_binstr(i, n):
    return bin(i)[2:].zfill(n)

# converts a hex string to n-bit binary string
def hex_to_binstr(h, n):
    return int_to_binstr(int(h, 16), n)

# permute a 16bit string
def permute_bits(string, p):
    return "".join( string[p[i]-1] for i in range(1,17) )
    
def spn_hex(hex, pi_s, pi_p, keystring, decrypt=False):
    print('-------------------------')
    print('Hex input: ' + hex)
    print('Hex key  : ' + keystring)
    # convert each char to 4-bit strings
    bitx = "".join([bin(int(char,16))[2:].zfill(4) for char in hex])
    bitkey = "".join([bin(int(char,16))[2:].zfill(4) for char in keystring])
    return spn(bitx, pi_s, pi_p, bitkey, decrypt)

# implementation of algorithm 3.1 from Stinson
def spn(x, pi_s, pi_p, keystring, decrypt=False):
    
    l = m = n_r = 4     # hardcode some values
    numRoundKeys = 5

    k = [None]      # fill first spot with placeholder
    # generate round keys
    for r in range(1, numRoundKeys+1):
        k.append(keystring[4*r-3-1:4*r-3-1+16])
        
    # the algorithm works for decrypting if we just invert the s-boxes,
    # and permuting all but the first/last round key, then reversing order
    if decrypt:
        print("Decryption mode on. We're going to invert the s-boxes, ")
        print("permute all but the first/last round key, and reverse")
        print("the round key order.")

        print("Original s_box: ")
        print([key for key in pi_s.keys()])
        print([val for val in pi_s.values()])
        pi_s = {pi_s[i] : i for i in pi_s.keys()}   # invert s-boxes

        for r in range(2, numRoundKeys):            # permute keys
            k[r] = permute_bits(k[r], pi_p)   
            
        temp = [None]                          # reverse round key order
        temp.extend(k[1:][::-1])
        k = temp

    print('Input binary : ' + x)
    print('Key in binary: ' + keystring)
    print('Round keys:') # print round keys
    for key in k[1:]:
        # this will print None once because it just acts as a placeholder
        print(key)

    # initialize arrays
    w = [''] * (n_r+3) 
    u = [''] * (n_r+3) 
    v = [''] * (n_r+3) 

    # ALGORITHM START
    w[0] = x
    for r in range(1, n_r-1+1):     # start rounds
        # printing some information
        print("\nRound: " + str(r))
        print("w[%i]   = %s" % (r-1, w[r-1]))
        print("k[%i]   = %s" % (r, k[r]))
        
        # Round 0
        print("Round: 0")
        print("xoring with Key[0]"
        # xor step
        u[r]  = int(w[r-1],2) ^ int(k[r],2)         # Round 0
        u[r] = int_to_binstr(u[r], 16)
        print("u[%i]   = %s" % (r, u[r]))

        # s-box step
        v[r] = ""
        for i in range( m):
            z = u[r][l*i:l*(i+1)]   # get next 4 bits
            z = int(z, 2)           # convert to decimal
            z = hex(z)[2:]          # convert to hex
            subbed = pi_s[z]        # substitute 
            subbed = hex_to_binstr(subbed, 4)   # convert back to binary
            v[r] += subbed
        print("v[%i]   = %s" % (r, v[r]))

        # permute step
        w[r] = permute_bits(v[r], pi_p)

    # last round xor step
    print("\nRound: %i" % n_r)
    print("k[%i] = %s" % (n_r, k[n_r]))
    u[n_r] = int(w[n_r-1], 2) ^ int(k[n_r], 2)
    # normally, there's a permute step here
    u[n_r] = int_to_binstr(u[n_r], 16)    # convert back to string
    print("u[%i] = %s" % (n_r, u[n_r]))

    # last round s-box step
    for i in range(m):
        z = u[n_r][l*i:l*(i+1)]   # get next 4 bits
        z = int(z, 2)           # convert to decimal
        z = hex(z)[2:]          # convert to hex
        subbed = pi_s[z]        # substitute 
        subbed = hex_to_binstr(subbed, 4)  # convert back to binary
        v[n_r] += subbed
    print("v[%i] = %s" % (n_r, v[n_r]))

    # post-rounds xor
    print("\nPost Rounds:")
    print("k[%i] = %s" % (n_r+1, k[n_r+1]))
    y = int(v[n_r], 2) ^ int(k[n_r+1], 2) 
    print("y    = %s" % int_to_binstr(y, 16))

    return int_to_binstr(y, 16)
    # ALGORITHM END

if __name__ == "__main__":
    if (len(sys.argv) < 5):
        print("Not enough args")
        sys.exit()
    
    a = sys.argv
    print(spn(a[1], a[2], a[3], a[4] ))
