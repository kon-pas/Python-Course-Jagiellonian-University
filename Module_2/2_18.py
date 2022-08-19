""" 2.18 Funkcja zwraca liczbe cyfr zero liczby calkowitej, ktora przyjmuje
jako argument. """
def count_zeros(_number):
	return str(_number).count('0')

if __name__ == "__main__":
	big_int = 312421015005030253250053205020502305205020
	print(count_zeros(big_int))
