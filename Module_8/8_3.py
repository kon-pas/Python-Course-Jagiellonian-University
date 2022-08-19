from random import uniform
from math import pi

def calc_pi(n=100):
	"""Obliczanie liczby pi metodą Monte Carlo.
	n oznacza liczbę losowanych punktów."""

	radius = 1
	num_points_circle = 0

	for x in range(n):
		x, y = uniform(-radius, radius), uniform(-radius, radius)
		if (x ** 2 + y ** 2) ** 0.5 <= radius:
			num_points_circle += 1

	return 4 * num_points_circle / n

if __name__ == "__main__":
	for num_zeros in range(1, 7):
		pi_calculated = calc_pi(10 ** num_zeros)
		print(f'Liczba losowan: {10**num_zeros},\t'.expandtabs(13), end='')
		print(f'Obliczona liczba pi: {pi_calculated},\t'.expandtabs(11), end='')
		print(f'Blad bezwzgledny: {abs(pi_calculated - pi)},')
