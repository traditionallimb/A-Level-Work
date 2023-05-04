inp = [5, 25, 17, 267, 118]


def summing(inp):
	if not inp:
		return None
	else:
		return inp[0] + summing(inp[1:])


summing(inp)
