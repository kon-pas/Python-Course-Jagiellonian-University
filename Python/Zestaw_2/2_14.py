""" 2.14.1 Funkcja zwraca najdluzszy wyraz z napisu, ktory przyjmuje jako
argument. """
def longest_word(_string):
	return max(_string.split(), key=len)

""" 2.14.2 Funkcja zwraca dlugosc najdluzszego wyrazu z napisu, 
ktory przyjmuje jako argument. """
def longest_word_length(_string):
	return len(max(_string.split(), key=len))

if __name__ == "__main__":
	line = "Lorem ipsum dolor sit amet consectetur adipiscing elit sed do"
	print(longest_word(line))
	print(longest_word_length(line))
