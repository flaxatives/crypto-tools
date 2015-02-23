#!/usr/bin/python

p = 2   # integers mod 2

""" 
extended GCD algorithm 

Polynomials are represented by arrays where index is
the exponent and coefficient is the value at the index
""" 
def extgcd(a, b):

    r = [None] * 2  # some variable initialization
    s = [None] * 2
    t = [None] * 2
    r[0] = a
    r[1] = b
    s[0] = [1]
    s[1] = [0]
    t[0] = [0]
    t[1] = [1]

    i = 1
    while not equalZero(r[i]):
        r.append([])
        s.append([])
        t.append([])

        q = quotient(r[i-1] , r[i])
        r[i+1] = subtract(r[i-1] , mult(q , r[i]))
        s[i+1] = subtract(s[i-1] , mult(q , s[i]))
        t[i+1] = subtract(t[i-1] , mult(q , t[i]))
        i += 1

    gcd = r[i-1]
    g = s[i-1]      # ag + bh = gcd
    h = t[i-1]
    a1 = [(-1) ** (i-1) * x % p for x in t[i]]  # gcd * a1 == a
    b1 = [(-1) ** i * x  % p for x in s[i]]     # gcd * b1 == b

    return normalize(gcd), \
            normalize(g), normalize(h), \
            normalize(a1), normalize(b1)


""" polynomial multiplication of a and b """
def mult(a, b):
    result = []

    for i in range(len(a)+len(b)):
        result.append(0)

    for i in range(len(a)):
        for j in range(len(b)):
            result[j+i] += a[i] * b[j]

    result =  result[:deg(result)+1]   # remove 0s at the end
    return [x % p for x in result]


""" polynomial quotient of a and b """
def quotient(a, b):
    a = normalize(a)
    b = normalize(b)
    q = [0]
    r = a
    d = deg(b)
    c = leadcoeff(b)

    while deg(r) >= d:
        s = [0] * (deg(r) - d + 1)
        s[deg(r) - d] = leadcoeff(r) // c

        q = add(q,s)
        r = subtract(r, mult(s,b))  # r - s*b
        r = r[:deg(r)+1]

    q = normalize(q)
    return [x % p for x in q]


""" simple polynomial addition """
def add(a, b):
    big = a
    small = b
    if len(small) > len(big):
        big, small = small, big
    
    while len(small) < len(big):
        small.append(0)

    polynomial = []
    for i in range(len(big)):
        polynomial.append(a[i] + b[i])

    return [x % p for x in polynomial]


""" Gets the leading coefficient of a polynomial """
def leadcoeff(a):
    return a[deg(a)]


""" checks if a polynomial is equal to 0 """
def equalZero(p):
    for coeff in p:
        if coeff != 0:
            return False

    return True


""" Polynomial a - b """
def subtract(a, b):
    b = [-x for x in b]
    return add(a, b)


""" Finds the degree of a polynomial """
def deg(a):
    if len(a) == 0 or equalZero(a):
        return -1

    degree = len(a) - 1
    while a[degree] == 0:
        degree -= 1

    return degree

""" get rid of 0s at the end """
def normalize(a):
    return a[:deg(a)+1]


""" make the array good for printing """
def prettify(a):
    str = ''
    for i, term in enumerate(a):
        if term != 0:
            if i == 0:
                str += '%d' % term
            elif i == 1:
                str += '%dx' % term
            else:
                str += '%dx^%d' % (term, i)
            str += ' + '
        
    return str.rstrip(' +')

