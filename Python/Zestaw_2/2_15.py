""" 2.15 Funkcja zwraca napis skladajacy sie z cyfr liczb umieszczonych w
tablicy, ktora przyjmuje jako argument. """
def concatenate(_array):
	return ''.join([str(i) for i in _array])

if __name__ == "__main__":
	L = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61]
	print(concatenate(L))
