""" 2.16 Funkcja zwraca zmodyfikowany napis, ktory przyjmuje jako pierwszy
argument. Modyfikacje polegaja na podmianie ciagu znakow, bedacych
drugim argumentem, na ciag znakow okreslonych przez trzeci argument. Bazowo
jest to podmiana 'GvR' na 'Guido van Rossum'. """
def replace_string(_line, _string1="GvR", _string2="Guido van Rossum"):
	return _line.replace(_string1, _string2)

if __name__ == "__main__":
	line = "Lorem GvR ipsum dolor sit amet, consectetur adipiscing elit"
	print(replace_string(line))
