def get_string_grid(rows, cols):
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

if __name__ == "__main__":
	print(get_string_grid(3, 4))
