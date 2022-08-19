""" 2.12.1 Funkcja zwraca napis stworzony z pierwszych znakow napisu,
ktory przyjmuje jako argument. """
def first_letters(_string):
	return ''.join(word[0] for word in _string.split())

""" 2.12.2 Funkcja zwraca napis stworzony z pierwszych znakow napisu, 
ktory przyjmuje jako argument. """
def last_letters(_string):
	return ''.join(word[-1] for word in _string.split())

if __name__ == "__main__":
	line = "Lorem ipsum dolor sit amet consectetur adipiscing elit sed do"
	print(first_letters(line))
	print(last_letters(line))
