def flatten(sequence):
	flat = []
	for element in sequence:
		if isinstance(element, (list, tuple)):
			flat += flatten(element)
		else:
			flat.append(element)
	return flat

if __name__ == '__main__':
	print(flatten([0, 1, [[2, [[[3, 4], 5], [6, 7], ]], ], [8], 9]))
