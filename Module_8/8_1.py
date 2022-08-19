def solve1(a, b, c):
	"""Rozwiązywanie równania liniowego a x + b y + c = 0."""

	def real(arg):
		return f'{arg} nalezy do zbioru liczb rzeczywistych'

	print('\tRozwiazanie rownania {} * x + {} * y + {} = 0:'.format(a, b, c))

	if a == 0:
		if b == 0:
			if c == 0:
				print(real('x'))
				print(real('y'))
			elif c != 0:
				print('Rownanie {} * x + {} * y + {} = 0 jest sprzeczne'.format(a, b, c))
		elif b != 0:
			if c == 0:
				print(real('x'))
				print('y = 0')
			elif c != 0:
				print(real('x'))
				print(f'y = {-c/b}')
	elif a != 0:
		if b == 0:
			if c == 0:
				print('x = 0')
				print(real('y'))
			elif c != 0:
				print(f'x = {-c/a}')
				print(real('y'))
		elif b != 0:
			temp = -c/b
			if temp > 0:
				print(real('x'))
				print(f'y = {-a/b} * x + {-c/b}')
			elif temp == 0:
				print(real('x'))
				print(f'y = {-a/b} * x')
			elif temp < 0:
				print(real('x'))
				print(f'y = {-a/b} * x - {c/b}')

if __name__ == "__main__":
	solve1(1, 2, 3)
	solve1(1, 2, -3)
	solve1(1, -2, 3)
	solve1(-1, 2, 3)
	solve1(-1, 2, -3)
	solve1(-1, -2, 3)
	solve1(1, -2, -3)
	solve1(0, 2, 3)
	solve1(0, 2, 3)
	solve1(1, 0, 3)
	solve1(1, 2, 0)
	solve1(0, 0, 3)
	solve1(0, 2, 0)
	solve1(1, 0, 0)
	solve1(0, 0, 0)
