""" 2.19 Funkcja zwraca tablice bedaca zmodyfikowana tablica, ktora przyjmuje
jako argument. Modyfikacje polegaja na wypelnieniu zerami wszystkich 
elementow tablicy tak, aby dlugosc kazdego elementu wynosila co najmniej trzy, 
tj. uprzednie 7 zostaje zamienione na 007. """
def fill_with_zeros(_array):
	return [str(element).zfill(3) for element in _array]

if __name__ == "__main__":
	_array = [1, 2, 24, 14, 240, 10, 7, 155, 120, 1, 2]
	print(fill_with_zeros(_array))
