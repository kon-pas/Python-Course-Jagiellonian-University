def counting_sort(arr):
	"""
	Sortowanie przez zliczanie.
	Sortowanie polega na zliczeniu wystąpień w tablicy elementów (kluczy) o tych samych wartościach.
	Algorytm ma swoje zastosowanie dla danych o dużej liczbie duplikatów.
	Algorytm jest ograniczony pod względem typu danych wejściowych. Klucze muszą należeć do skończonego zbioru,
	a implementacja różni się w zależności od sortowanych danych.
	Poniżej przedstawione stabilna implementacja dla liczb całkowitych od 0 do n.
	Złożoność czasowa O(n+m), gdzie n jest wielkością danych wejściowych, m liczbą unikalnych kluczy.
	"""

	# print(arr)
	arr_size = len(arr)
	counting_arr_size = max(arr) - min(arr) + 1
	counting_arr = [0] * counting_arr_size
	answer_arr = [0] * arr_size
	for i in range(arr_size):
		counting_arr[arr[i]] += 1
	for i in range(1, counting_arr_size):
		counting_arr[i] += counting_arr[i-1]
	for i in range(arr_size - 1, -1, -1):
		j = arr[i]
		counting_arr[j] -= 1
		answer_arr[counting_arr[j]] = arr[i]
	return answer_arr
