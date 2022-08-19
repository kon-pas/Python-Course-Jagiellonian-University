def get_string_numbers_except_mod_3(limit):
	output = ''
	for i in range(limit+1):
		if i % 3 != 0:
			output = output + str(i) + ' '
	return output

if __name__ == "__main__":
	print(get_string_numbers_except_mod_3(30))
