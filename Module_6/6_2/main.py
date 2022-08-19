import unittest
import points
import gc

class TestPoint(unittest.TestCase):
	def setUp(self):
		self.p1 = points.Point(-1, 2)
		self.p2 = points.Point(0, 1)
		self.p3 = points.Point(3, 1)
		self.p4 = points.Point(6, 2)
		self.p5 = points.Point(0, 2)

	def test_str(self):
		self.assertEqual(str(self.p1), '(-1, 2)')
		self.assertEqual(str(self.p2), '(0, 1)')
		self.assertEqual(str(self.p3), '(3, 1)')
		self.assertEqual(str(self.p4), '(6, 2)')
		self.assertEqual(str(self.p5), '(0, 2)')

	def test_repr(self):
		self.assertEqual(repr(self.p1), 'Point(-1, 2)')
		self.assertEqual(repr(self.p2), 'Point(0, 1)')
		self.assertEqual(repr(self.p3), 'Point(3, 1)')
		self.assertEqual(repr(self.p4), 'Point(6, 2)')
		self.assertEqual(repr(self.p5), 'Point(0, 2)')

	def test_eq(self):
		self.assertTrue(self.p1 == points.Point(-1, 2))
		self.assertTrue(self.p2 == points.Point(0, 1))
		self.assertTrue(self.p3 == points.Point(3, 1))
		self.assertTrue(self.p4 == points.Point(6, 2))
		self.assertTrue(self.p5 == points.Point(0, 2))

	def test_ne(self):
		self.assertTrue(self.p1 != self.p2)
		self.assertTrue(self.p2 != self.p5)
		self.assertTrue(self.p3 != self.p4)
		self.assertTrue(self.p4 != self.p5)
		self.assertTrue(self.p5 != self.p2)

	def test_add(self):
		self.assertEqual(self.p1 + self.p2, points.Point(-1, 3))
		self.assertEqual(self.p2 + self.p3, points.Point(3, 2))
		self.assertEqual(self.p3 + self.p4, points.Point(9, 3))
		self.assertEqual(self.p4 + self.p5, points.Point(6, 4))
		self.assertEqual(self.p5 + self.p1, points.Point(-1, 4))

	def test_sub(self):
		self.assertEqual(self.p1 - self.p2, points.Point(-1, 1))
		self.assertEqual(self.p2 - self.p3, points.Point(-3, 0))
		self.assertEqual(self.p3 - self.p4, points.Point(-3, -1))
		self.assertEqual(self.p4 - self.p5, points.Point(6, 0))
		self.assertEqual(self.p5 - self.p1, points.Point(1, 0))

	def test_mul(self):
		self.assertEqual(self.p1 * self.p2, 2)
		self.assertEqual(self.p2 * self.p3, 1)
		self.assertEqual(self.p3 * self.p4, 20)
		self.assertEqual(self.p4 * self.p5, 4)
		self.assertEqual(self.p5 * self.p1, 4)

	def test_cross(self):
		self.assertEqual(self.p1.cross(self.p2), -1)
		self.assertEqual(self.p2.cross(self.p3), -3)
		self.assertEqual(self.p3.cross(self.p4), 0)
		self.assertEqual(self.p4.cross(self.p5), 12)
		self.assertEqual(self.p5.cross(self.p1), 2)

	def test_length(self):
		self.assertEqual(self.p1.length(), 5 ** 0.5)
		self.assertEqual(self.p2.length(), 1)
		self.assertEqual(self.p3.length(), 10 ** 0.5)
		self.assertEqual(self.p4.length(), 40 ** 0.5)
		self.assertEqual(self.p5.length(), 2)

	def test_hash(self):
		self.assertEqual(self.p1, points.Point(-1.0, 2.0))
		self.assertEqual(self.p2, points.Point(0.0, 1.0))
		self.assertEqual(self.p3, points.Point(3.0, 1.0))
		self.assertEqual(self.p4, points.Point(6.0, 2.0))
		self.assertEqual(self.p5, points.Point(0.0, 2.0))

	def tearDown(self):
		del self.p1, self.p2, self.p3, self.p4, self.p5
		gc.collect()

if __name__ == '__main__':
	unittest.main()
