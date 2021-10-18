""" 2.17.1 Funkcja zwraca napis bedacy alfabetycznym posortowaniem napisu,
ktory przyjmuje jako argument. Litery duze maja wyzszy priorytet od liter
malych. """
def sort_by_alphabetical_order(_string):
	return ' '.join(sorted(_string.split(), key=str.lower))

""" 2.17.2 Funkcja zwraca napis bedacy posortowaniem wedlug dlugosci 
wyrazow z napisu, ktory przyjmuje jako argument. """
def sort_by_length(_string):
	return ' '.join(sorted(_string.split(), key=len))

if __name__ == "__main__":
	line = "Lorem GvR ipsum dolor sit amet consectetur adipiscing elit"
	print(sort_by_alphabetical_order(line))
	print(sort_by_length(line))
