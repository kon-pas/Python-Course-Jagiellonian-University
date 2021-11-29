from points import Point
import math

class Circle:
	"Klasa reprezentujaca okregi na plaszczyznie"

	def __init__(self, x, y, radius):
		if radius < 0:
			raise ValueError("Promien ujemny")
		self.pt = Point(x, y)
		self.radius = radius

	def __repr__(self):
		return f'Circle({self.pt.x}, {self.pt.y}, {self.radius})'

	def __eq__(self, other):
		return self.pt == other.pt and self.radius == other.radius

	def __ne__(self, other):
		return not self == other

	def area(self):
		return math.pi * self.radius ** 2

	def move(self, x, y):
		return Circle(self.pt.x + x, self.pt.y + y, self.radius)

	def cover(self, other):
		dist_x = other.pt.x - self.pt.x
		dist_y = other.pt.y - self.pt.y
		dist = (dist_x ** 2 + dist_y ** 2 ) ** 0.5
		if dist == 0:
			return self
		elif dist + other.radius < self.radius:
			return self
		elif dist + self.radius < other.radius:
			return other
		else:
			outer_other = other.pt.x + (dist_x * other.radius / dist), other.pt.y + (dist_y * other.radius / dist)
			outer_self = self.pt.x - (dist_x * self.radius / dist), self.pt.y - (dist_y * self.radius / dist)
			vector = (outer_self[0] - outer_other[0]) / 2, (outer_self[1] - outer_other[1]) / 2
			return Circle(outer_other[0] + vector[0], outer_other[1] + vector[1], (vector[0] ** 2 + vector[1] ** 2) ** 0.5)
