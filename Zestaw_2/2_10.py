""" 2.10 Funkcja zwraca liczbe wyrazow napisu, ktory przyjmuje jako argument """
def count_words(_string):
	return len(_string.split())

if __name__ == "__main__":
	line = "Lorem ipsum dolor sit amet consectetur adipiscing elit"
	print(count_words(line))
