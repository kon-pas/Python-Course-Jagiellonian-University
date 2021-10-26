def print_ruler(length):
	img = '|'
    for e in range(0, length):
    	img += '....|'
	img += '\n'
	for e in range(0, length+1):
		img += f'{e:<5}'
	return img

if __name__ == "__main__":
 	print_ruler(12)
