import random
import math

# (a) różne liczby int od 0 do n-1 w kolejności losowej
def random_list(size):
	return random.sample(list(range(0, size)), size)

# (b) różne liczby int od 0 do n-1 prawie posortowane (liczby są blisko swojej prawidłowej pozycji)
def almost_sorted_list(size):
	arr = []
	for y in range(0, size, 3):
		arr += random.sample([x for x in range(y, y+3)], 3)
	return list(filter(lambda x: x < size, arr))

# (c) różne liczby int od 0 do n-1 prawie posortowane w odwrotnej kolejności
def reversed_almost_sorted_list(size):
	arr = almost_sorted_list(size)
	arr.reverse()
	return arr

# (d) n liczb float w kolejności losowej o rozkładzie gaussowskim
def random_gauss_list(size):
	arr = []
	for i in range(size):
		arr += [random.gauss(0.0, 1.0)]
	return arr

# (e) n liczb int w kolejności losowej, o wartościach powtarzających się, należących do zbioru k elementowego (k < n, np. k^2 = n)
def random_list_with_duplicates(size):
	arr = []
	maximum = math.floor(size/3)
	for i in range(size):
		arr += [random.randint(0, maximum)]
	return arr
