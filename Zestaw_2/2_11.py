""" 2.11 Funkcja wyswietla napis, ktory przyjmuje jako argument. Wszystkie 
znaki napisu oddzielone sa od siebie znakiem podlogi '_' """
def split_letters(_string):
	return '_'.join(_string[i] for i in range(0, len(_string)))

if __name__ == "__main__":
	print(split_letters("abcd"))
