#!/usr/bin/python
import numpy as np

# generates a string hankel matrix, returns as a 2d list
def hankel(string, m):
	h = [[None for _ in range(m)] for _ in range(m)]	# make empty matrix
	
	# fill the matrix with bits
	for i in range(m):
		h[i] = [char for char in string[i:m+i]]	
		
	return h
	
# same thing as hankel(), but generates ints instead of strings
def inthankel(string, m):
	h = [[None for _ in range(m)] for _ in range(m)]	# make empty matrix
	
	# fill the matrix with bits
	for i in range(m):
		h[i] = [int(char) for char in string[i:m+i]]	
		
	return h

# prints a hankel matrix
def print_hankel(string, m):
	h = hankel(string, m)

	# print each row of h
	for row in h:
		print(''.join(row))

# makes a string for a pmatrix in LaTeX
def tex_hankel(string, m):
	h = hankel(string, m)
	
	# build the 1&0&1 parts
	rows = []
	for row in h:
		rows.append('&'.join([char for char in row]))
	
	# join each row with slashes
	data = " \\\\ ".join(rows)
	
	string = '\\begin{pmatrix} %s \\end{pmatrix}' % data
	return string

# makes a copy-pasteable hankel matrix for wolframalpha
def wolfram_hankel(string, m):
	h = hankel(string, m)
	
	# make rows like {0,0} 
	rows = []
	for row in h:
		nums = ','.join([char for char in row])	
		rows.append('{%s}' % nums)
		
	data = ",".join(rows) 	# {0,1},{1,0}
	string = "{%s}" % data 	# {{0,1},{1,0}}
	
	return string


string = '10011001001110001100010100011\
1101100111110101010010110110101100001101\
1100101011110000000100010010000'

# find determinants
for i in range(2,50):
	h = np.array(hankel(string, i))
	det = round(np.linalg.det(h)) % 2
	
	print('determinant of H(%i): %f' % (i, det))
	
# calculate coefficients for linear recurrence size 8
############
m = 8

# find H_8
h = inthankel(string, m)
# calculate inverse of hankel
invh = np.linalg.inv(np.array(h))

# make a column vector of m+1 to 2m - 1, right hand side
resultvector = [[int(string[i+1])] for i in range(m-1, 2*m - 1)]
resultvector = np.array(resultvector)
print("Right hand side: ")
print(resultvector)


# multiply H^-1 with the result vector
coeff = np.dot(invh, resultvector)
print("Coeff: ")
print(coeff)

print("Coeff rounded and mod 2:")
print(np.mod(np.around(coeff),2))

# generate next nums
generated = string[0:m] # initial vector
for i in range(m+1, len(string) + 1):
	z = [int(x) for x in string[i-m-1:i-1]]
	multed = np.dot(z,coeff)
	summed = int(np.sum(multed))
	print("z_%i: %i" % (i, summed % 2))
	
	generated += '' + str(summed % 2) # add to our generated string
	
print("\nOriginal String vs Generated ")
print(string)
print(generated)
	