#!/usr/bin/python

def main():
	
	degree = 5

	# generate all binary numbers
	bins = [bin(i)[2:].zfill(degree) for i in range(2 ** degree)]

	print("Initialization vectors:")
	for b in bins:
		print(b)

	# generate string length 2x max possible period (2^n-1)
	# z_(m+5) = z_m + z_(m+1)
	print("\nGenerating keystream using z_(m+t) = z_m + z_(m+1)")
	strings = []
	for i in range(len(bins)):
		z = bins[i]
		maxlength = 2*((2 ** degree) - 1) 
		while len(z) < maxlength:
			m = len(z)  - degree
			z += str((int(z[m]) + int(z[m + 1])) % 2)
		strings.append(z)

	for string in strings:
		print(string)

	print('\nFinding repeats...')
	print("string:repeatstring:length")
	for string in strings:
		rep = findrepeat(string)
		count = len(rep)
		print("%s:%s:%i" % (string, rep, count))
	
# finds the longest repeating string up to 1/2 string length
def findrepeat(string):
	# check if the string is a multiple of the first n chars
	for length in range(1, len(string) // 2):
		rep = string[:length]
		multiplier = len(string) // length	# determines how many times the substring is repeated
		if rep * multiplier == string[:length * multiplier]:
			return rep
			
	return string
	
if __name__ == "__main__":
	main()