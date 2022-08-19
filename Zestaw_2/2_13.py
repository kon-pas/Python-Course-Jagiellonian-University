""" 2.13 Funkcja zwraca laczna dlugosc wyrazow z napisu, ktory przyjmuje jako
argument. """
def sum_len_words(_string):
	return sum([len(word) for word in _string.split()])

if __name__ == "__main__":
    line = "Lorem ipsum dolor sit amet consectetur adipiscing elit sed do"
    print(sum_len_words(line))
