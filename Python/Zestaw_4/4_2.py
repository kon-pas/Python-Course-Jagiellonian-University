def make_ruler(n):
	img = '|'
	for e in range(0, n):
		img += '....|'
	img += '\n0'
	for e in range(1, n + 1):
		img += str(e).rjust(5)
	return img

def make_grid(rows, cols):
	img = '+'
	for row in range(rows):
		img += '---+'
	for col in range(cols):
		img += '\n|'
		for row in range(rows):
			img += f'{"|":>4}'
		img += '\n+'
		for row in range(rows):
			img += '---+'
	return img

if __name__ == '__main__':
	print(make_ruler(12))
    print(make_grid(8, 6))

	
