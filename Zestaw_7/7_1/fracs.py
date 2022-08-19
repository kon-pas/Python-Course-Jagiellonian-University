import errors

class Frac:
	"""Klasa reprezentująca ułamek."""

	def __init__(self, *args):
		if len(args) == 1:
			if type(args[0]) is float:
				(self.x, self.y) = args[0].as_integer_ratio()
			else:
				raise TypeError("To nie jest liczba typu float")
		elif len(args) == 2:
			if args[1] == 0:
				raise ZeroDivisionError
			else:
				self.x = args[0]
				self.y = args[1]
		else:
			raise errors.ArgNumError("Nieprawidlowa liczba argumentow, podaj 1 lub 2 argumenty")

	def __str__(self):
		if self.y == 1:
			return '{}'.format(self.x)
		return '{}/{}'.format(self.x, self.y)

	def __repr__(self):
		return f'Frac({self.x}, {self.y})'

	def __eq__(self, other):
		return bool(float(self) == float(other))

	def __ne__(self, other):
		return bool(float(self) != float(other))

	def __lt__(self, other):
		return bool(float(self) < float(other))

	def __le__(self, other):
		return bool(float(self) <= float(other))

	def __gt__(self, other):
		return bool(float(self) > float(other))

	def __ge__(self, other):
		return bool(float(self) >= float(other))

	def __add__(self, other):
		if type(other) is int:
			return Frac(self.x + self.y * other, self.y)
		return Frac((self.x * other.y + other.x * self.y), (self.y * other.y))

	__radd__ = __add__

	def __sub__(self, other):
		if type(other) is int:
			return Frac(self.x - self.y * other, self.y)
		return Frac((self.x * other.y - other.x * self.y), (self.y * other.y))

	def __rsub__(self, other):
		return Frac(other * self.y - self.x, self.y)

	def __mul__(self, other):
		if type(other) is int:
			return Frac(self.x * other, self.y)
		return Frac((self.x * other.x), (self.y * other.y))

	__rmul__ = __mul__

	def __truediv__(self, other):
		if type(other) is int:
			if other == 0:
				raise ZeroDivisionError("Nie mozna dzielic przez zero")
			return Frac(self.x, self.y * other)
		return Frac(self.x * other.y, self.y * other.x)

	def __rtruediv__(self, other):
		if other == 0:
			raise ZeroDivisionError("Nie mozna dzielic przez zero")
		return Frac(other * self.y, self.x)

	def __pos__(self):
		return self

	def __neg__(self):
		return Frac(-self.x, self.y)

	def __invert__(self):
		if self.x == 0:
			raise ValueError("Licznik nie moze byc rowny zero")
		return Frac(self.y, self.x)

	def __float__(self):
		return float(self.x) / float(self.y)

	def __hash__(self):
		return hash((self.x, self.y))
