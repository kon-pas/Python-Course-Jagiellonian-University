import unittest
import fracs

class TestFrac(unittest.TestCase):
	"""Klasa testujaca modul fracs.py."""

	def setUp(self):
		self.f1 = fracs.Frac(-1, 2)
		self.f2 = fracs.Frac(12, 4)
		self.f3 = fracs.Frac(3.0)
		self.f4 = fracs.Frac(2.5)
		self.f5 = fracs.Frac(0, 99)

	def test_str(self):
		self.assertEqual(str(self.f1), '-1/2')
		self.assertEqual(str(self.f2), '12/4')
		self.assertEqual(str(self.f3), '3')
		self.assertEqual(str(self.f4), '5/2')
		self.assertEqual(str(self.f5), '0/99')


	def test_repr(self):
		self.assertEqual(repr(self.f1), 'Frac(-1, 2)')
		self.assertEqual(repr(self.f2), 'Frac(12, 4)')
		self.assertEqual(repr(self.f3), 'Frac(3, 1)')
		self.assertEqual(repr(self.f4), 'Frac(5, 2)')
		self.assertEqual(repr(self.f5), 'Frac(0, 99)')

	def test_eq(self):
		self.assertFalse(self.f1 == self.f2)
		self.assertTrue(self.f2 == self.f3)
		self.assertFalse(self.f3 == self.f4)
		self.assertFalse(self.f4 == 2)
		self.assertFalse(4 == self.f1)


	def test_ne(self):
		self.assertTrue(self.f1 != self.f2)
		self.assertFalse(self.f2 != self.f3)
		self.assertTrue(self.f3 != self.f4)
		self.assertTrue(self.f4 != 2)
		self.assertTrue(4 != self.f1)

	def test_lt(self):
		self.assertTrue(self.f1 < self.f2)
		self.assertFalse(self.f2 < self.f3)
		self.assertFalse(self.f3 < self.f4)
		self.assertFalse(self.f4 < 2)
		self.assertFalse(4 < self.f1)

	def test_le(self):
		self.assertTrue(self.f1 <= self.f2)
		self.assertTrue(self.f2 <= self.f3)
		self.assertFalse(self.f3 <= self.f4)
		self.assertFalse(self.f4 <= 2)
		self.assertFalse(4 <= self.f1)

	def test_gt(self):
		self.assertFalse(self.f1 > self.f2)
		self.assertFalse(self.f2 > self.f3)
		self.assertTrue(self.f3 > self.f4)
		self.assertTrue(self.f4 > 2)
		self.assertTrue(4 > self.f1)

	def test_ge(self):
		self.assertFalse(self.f1 >= self.f2)
		self.assertTrue(self.f2 >= self.f3)
		self.assertTrue(self.f3 >= self.f4)
		self.assertTrue(self.f4 >= 2)
		self.assertTrue(4 >= self.f1)

	def test_add(self):
		self.assertEqual(self.f1 + self.f2, fracs.Frac(5, 2))
		self.assertEqual(self.f2 + self.f3, fracs.Frac(6, 1))
		self.assertEqual(self.f3 + self.f4, fracs.Frac(11, 2))
		self.assertEqual(self.f4 + 2, fracs.Frac(9, 2))
		self.assertEqual(4 + self.f1, fracs.Frac(7, 2))

	def test_sub(self):
		self.assertEqual(self.f1 - self.f2, fracs.Frac(-7, 2))
		self.assertEqual(self.f2 - self.f3, fracs.Frac(0, 1))
		self.assertEqual(self.f3 - self.f4, fracs.Frac(1, 2))
		self.assertEqual(self.f4 - 2, fracs.Frac(1, 2))
		self.assertEqual(4 - self.f1, fracs.Frac(9, 2))

	def test_mul(self):
		self.assertEqual(self.f1 * self.f2, fracs.Frac(-3, 2))
		self.assertEqual(self.f2 * self.f3, fracs.Frac(9, 1))
		self.assertEqual(self.f3 * self.f4, fracs.Frac(15, 2))
		self.assertEqual(self.f4 * 2, fracs.Frac(5, 1))
		self.assertEqual(4 * self.f1, fracs.Frac(-2, 1))

	def test_truediv(self):
		self.assertEqual(self.f1 / self.f2, fracs.Frac(-1, 6))
		self.assertEqual(self.f2 / self.f3, fracs.Frac(1, 1))
		self.assertEqual(self.f3 / self.f4, fracs.Frac(6, 5))
		self.assertEqual(self.f4 / 2, fracs.Frac(5, 4))
		self.assertEqual(4 / self.f1, fracs.Frac(-8, 1))

	def test_pos(self):
		self.assertEqual(self.f1, +self.f1)
		self.assertEqual(self.f2, +self.f2)
		self.assertEqual(self.f3, +self.f3)
		self.assertEqual(self.f4, +self.f4)
		self.assertEqual(self.f5, +self.f5)

	def test_neg(self):
		self.assertEqual(-self.f1, fracs.Frac(1, 2))
		self.assertEqual(-self.f2, fracs.Frac(-12, 4))
		self.assertEqual(-self.f3, fracs.Frac(-3, 1))
		self.assertEqual(-self.f4, fracs.Frac(-5, 2))
		self.assertEqual(-self.f5, fracs.Frac(0, 1))

	def test_invert(self):
		self.assertEqual(~self.f1, fracs.Frac(2, -1))
		self.assertEqual(~self.f2, fracs.Frac(4, 12))
		self.assertEqual(~self.f3, fracs.Frac(1, 3))
		self.assertEqual(~self.f4, fracs.Frac(2, 5))

	def test_float(self):
		self.assertEqual(float(self.f1), -0.5)
		self.assertEqual(float(self.f2), 3.0)
		self.assertEqual(float(self.f3), 3.0)
		self.assertEqual(float(self.f4), 2.5)
		self.assertEqual(float(self.f5), 0.0)

	def test_hash(self):
		self.assertEqual(self.f1, fracs.Frac(-1.0, 2.0))
		self.assertEqual(self.f2, fracs.Frac(12.0, 4.0))
		self.assertEqual(self.f3, fracs.Frac(3.0, 1.0))
		self.assertEqual(self.f4, fracs.Frac(2.500000))
		self.assertEqual(self.f5, fracs.Frac(0.00, 99))

if __name__ == '__main__':
	unittest.main()
