import circles
import unittest
import math

class TestCircle(unittest.TestCase):
	def setUp(self):
		self.c1 = circles.Circle(0, 0, 10)
		self.c2 = circles.Circle(2, 3, 4)
		self.c3 = circles.Circle(5, 5, 1)

	def test_repr(self):
		self.assertEqual(repr(self.c1), 'Circle(0, 0, 10)')
		self.assertEqual(repr(self.c2), 'Circle(2, 3, 4)')
		self.assertEqual(repr(self.c3), 'Circle(5, 5, 1)')

	def test_eq(self):
		self.assertFalse(self.c1 == self.c2)
		self.assertFalse(self.c2 == self.c3)
		self.assertFalse(self.c3 == self.c1)
		self.assertTrue(self.c1 == self.c1)
		self.assertTrue(self.c2 == self.c2)
		self.assertTrue(self.c3 == self.c3)

	def test_ne(self):
		self.assertTrue(self.c1 != self.c2)
		self.assertTrue(self.c2 != self.c3)
		self.assertTrue(self.c3 != self.c1)
		self.assertFalse(self.c1 != self.c1)
		self.assertFalse(self.c2 != self.c2)
		self.assertFalse(self.c3 != self.c3)

	def test_area(self):
		self.assertEqual(self.c1.area(), math.pi * 10 ** 2)
		self.assertEqual(self.c2.area(), math.pi * 4 ** 2)
		self.assertEqual(self.c3.area(), math.pi * 1 ** 2)

	def test_move(self):
		self.assertEqual(self.c1.move(-self.c1.pt.x, -self.c1.pt.y), circles.Circle(0, 0, 10))
		self.assertEqual(self.c2.move(-self.c2.pt.x, -self.c2.pt.y), circles.Circle(0, 0, 4))
		self.assertEqual(self.c3.move(-self.c3.pt.x, -self.c3.pt.y), circles.Circle(0, 0, 1))

	def test_cover(self):
		self.assertEqual(self.c1.cover(self.c1), self.c1)
		self.assertEqual(self.c2.cover(self.c2), self.c2)
		self.assertEqual(self.c3.cover(self.c3), self.c3)
		self.assertEqual(circles.Circle(0, 0, 100).cover(circles.Circle(1, 1, 1)), circles.Circle(0, 0, 100))
		self.assertEqual(circles.Circle(0, 0, 10).cover(circles.Circle(10, 0, 10)), circles.Circle(5, 0, 15))
		self.assertEqual(circles.Circle(5, 5, 10).cover(circles.Circle(2, 10, 8)), circles.Circle(4.014495755427527, 6.642507074287455, 11.915475947422651))

if __name__ == "__main__":
	unittest.main()
