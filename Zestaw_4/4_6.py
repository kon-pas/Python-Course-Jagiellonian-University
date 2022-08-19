def sum_seq(sequence):
	result = 0
	for element in sequence:
		if isinstance(element, (list, tuple)):
			result += sum_seq(element)
		else:
			result += element
	return result

if __name__ == '__main__':
	print(sum_seq([0, 1, [[2, [[[3, 4], 5], [6, 7], ]], ], [8], 9]))
