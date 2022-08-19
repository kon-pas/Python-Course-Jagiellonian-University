class Frac:
	"""Klasa reprezentująca ułamek."""

	def __init__(self, x=0, y=1):
		self.x = x
		self.y = y

	def __str__(self):
		if self.y == 1:
			return '{}'.format(self.x)
		return '{}/{}'.format(self.x, self.y)

	def __repr__(self):
		return f'Frac({self.x}, {self.y})'

	def __eq__(self, other):
		return bool(self.x / self.y == other.x / other.y)

	def __ne__(self, other):
		return bool(self.x / self.y != other.x / other.y)

	def __lt__(self, other):
		return bool(self.x / self.y < other.x / other.y)

	def __le__(self, other):
		return bool(self.x / self.y <= other.x / other.y)

	def __gt__(self, other):
		return bool(self.x / self.y > other.x / other.y)

	def __ge__(self, other):
		return bool(self.x / self.y >= other.x / other.y)

	def __add__(self, other):
		return Frac((self.x * other.y + other.x * self.y), (self.y * other.y))

	def __sub__(self, other):
		return Frac((self.x * other.y - other.x * self.y), (self.y * other.y))

	def __mul__(self, other):
		return Frac((self.x * other.x), (self.y * other.y))

	def __truediv__(self, other):
		if other.x == 0:
			return ZeroDivisionError
		return Frac((self.x * other.y), (self.y * other.x))

	def __pos__(self):
		return self

	def __neg__(self):
		return Frac(-self.x, self.y)

	def __invert__(self):
		if self.x == 0:
			return self
		return Frac(self.y, self.x)

	def __float__(self):
		return self.x / self.y

	def __hash__(self):
		return hash(float(self))
