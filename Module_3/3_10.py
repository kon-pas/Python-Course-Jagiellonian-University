def get_num_roman_to_arabic(roman):
	D = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90,
	     'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}
	arabic = 0
	while roman != '':
		for e in D:
			if e == roman[0:len(e)]:
				roman = roman[len(e):]
				arabic += D.get(e)
	return arabic

if __name__ == "__main__":
	print(get_num_roman_to_arabic("CXCIX")) # 199
	print(get_num_roman_to_arabic("CCCLXXXV")) # 385
	print(get_num_roman_to_arabic("DXXXVII")) # 537
	print(get_num_roman_to_arabic("DCCCXLVIII")) # 848
	print(get_num_roman_to_arabic("CMXCVI")) # 996
