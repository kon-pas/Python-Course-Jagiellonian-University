def heron(a, b, c):
	try:
		if sorted([a, b, c])[0] + sorted([a, b, c])[1] <= sorted([a, b, c])[2]:
			raise ValueError
	except ValueError:
		print(f'Nie mozna utworzyc trojkata z podanych bokow: {a}, {b}, {c}')
	else:
		p = (a + b + c) / 2
		print(f'Pole trojkata o bokach {a}, {b}, {c}:', end=' ')
		print((p * (p - a) * (p - b) * (p - c)) ** 0.5)

if __name__ == "__main__":
	heron(0, 0, 0)
	heron(1, 2, 3)
	heron(2, 2, 3)
	heron(7.5, 8.5, 9)
	heron(10, 10, 10)
	heron(-2, 2, 3)
