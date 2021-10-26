def get_strings_intersection(string1, string2):
	return ''.join(set(string1).intersection(set(string2)))

def get_strings_union(string1, string2):
	return ''.join(set(string1).union(set(string2)))

if __name__ == "__main__":
	print(get_strings_intersection('abcd', 'defga'))
	print(get_strings_union('abcd', 'defga'))
