# ex. string = "1001"

def encHam74(string):
	b = [int(bit) for bit in string]

	p1 = str((b[0] + b[1] + b[3]) % 2)
	p2 = str((b[0] + b[2] + b[3]) % 2)
	p3 = str((b[1] + b[2] + b[3]) % 2)

	b = [str(bit) for bit in b]
	encoded = p1 + p2 + b[0] + p3 + b[1] + b[2] + b[3]
	print(p1 + p2 + p3)
	print(encoded)
