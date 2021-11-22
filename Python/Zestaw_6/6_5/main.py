import unittest
import fracs
import gc

class TestFrac(unittest.TestCase):

	def setUp(self):
		self.f1 = fracs.Frac(-1, 2)
		self.f2 = fracs.Frac(0, 1)
		self.f3 = fracs.Frac(3, 1)
		self.f4 = fracs.Frac(6, 2)
		self.f5 = fracs.Frac(0, 2)

	def test_str(self):
		self.assertEqual(str(self.f1), '-1/2')
		self.assertEqual(str(self.f2), '0')
		self.assertEqual(str(self.f3), '3')
		self.assertEqual(str(self.f4), '6/2')
		self.assertEqual(str(self.f5), '0/2')

	def test_repr(self):
		self.assertEqual(repr(self.f1), 'Frac(-1, 2)')
		self.assertEqual(repr(self.f2), 'Frac(0, 1)')
		self.assertEqual(repr(self.f3), 'Frac(3, 1)')
		self.assertEqual(repr(self.f4), 'Frac(6, 2)')
		self.assertEqual(repr(self.f5), 'Frac(0, 2)')

	def test_eq(self):
		self.assertFalse(self.f1 == self.f2)
		self.assertTrue(self.f2 == self.f5)
		self.assertTrue(self.f3 == self.f4)
		self.assertFalse(self.f4 == self.f5)
		self.assertTrue(self.f5 == self.f2)

	def test_ne(self):
		self.assertTrue(self.f1 != self.f2)
		self.assertFalse(self.f2 != self.f5)
		self.assertFalse(self.f3 != self.f4)
		self.assertTrue(self.f4 != self.f5)
		self.assertFalse(self.f5 != self.f2)

	def test_lt(self):
		self.assertTrue(self.f1 < self.f2)
		self.assertTrue(self.f2 < self.f3)
		self.assertFalse(self.f3 < self.f4)
		self.assertFalse(self.f4 < self.f5)
		self.assertFalse(self.f5 < self.f1)

	def test_le(self):
		self.assertTrue(self.f1 <= self.f2)
		self.assertTrue(self.f2 <= self.f3)
		self.assertTrue(self.f3 <= self.f4)
		self.assertFalse(self.f4 <= self.f5)
		self.assertFalse(self.f5 <= self.f1)

	def test_gt(self):
		self.assertFalse(self.f1 > self.f2)
		self.assertFalse(self.f2 > self.f3)
		self.assertFalse(self.f3 > self.f4)
		self.assertTrue(self.f4 > self.f5)
		self.assertTrue(self.f5 > self.f1)

	def test_ge(self):
		self.assertFalse(self.f1 >= self.f2)
		self.assertFalse(self.f2 >= self.f3)
		self.assertTrue(self.f3 >= self.f4)
		self.assertTrue(self.f4 >= self.f5)
		self.assertTrue(self.f5 >= self.f1)

	def test_add(self):
		self.assertEqual(self.f1 + self.f2, fracs.Frac(-1, 2))
		self.assertEqual(self.f2 + self.f3, fracs.Frac(3, 1))
		self.assertEqual(self.f3 + self.f4, fracs.Frac(6, 1))
		self.assertEqual(self.f4 + self.f5, fracs.Frac(3, 1))
		self.assertEqual(self.f5 + self.f1, fracs.Frac(-1, 2))

	def test_sub(self):
		self.assertEqual(self.f1 - self.f2, fracs.Frac(-1, 2))
		self.assertEqual(self.f2 - self.f3, fracs.Frac(-3, 1))
		self.assertEqual(self.f3 - self.f4, fracs.Frac(0, 1))
		self.assertEqual(self.f4 - self.f5, fracs.Frac(3, 1))
		self.assertEqual(self.f5 - self.f1, fracs.Frac(1, 2))

	def test_mul(self):
		self.assertEqual(self.f1 * self.f2, fracs.Frac(0, 1))
		self.assertEqual(self.f2 * self.f3, fracs.Frac(0, 1))
		self.assertEqual(self.f3 * self.f4, fracs.Frac(9, 1))
		self.assertEqual(self.f4 * self.f5, fracs.Frac(0, 1))
		self.assertEqual(self.f5 * self.f1, fracs.Frac(0, 2))

	def test_truediv(self):
		self.assertEqual(self.f1 / self.f2, ZeroDivisionError)
		self.assertEqual(self.f2 / self.f3, fracs.Frac(0, 1))
		self.assertEqual(self.f3 / self.f4, fracs.Frac(1, 1))
		self.assertEqual(self.f4 / self.f5, ZeroDivisionError)
		self.assertEqual(self.f5 / self.f1, fracs.Frac(0, 1))

	def test_pos(self):
		self.assertEqual(self.f1, +self.f1)
		self.assertEqual(self.f2, +self.f2)
		self.assertEqual(self.f3, +self.f3)
		self.assertEqual(self.f4, +self.f4)
		self.assertEqual(self.f5, +self.f5)

	def test_neg(self):
		self.assertEqual(-self.f1, fracs.Frac(1, 2))
		self.assertEqual(-self.f2, fracs.Frac(0, 1))
		self.assertEqual(-self.f3, fracs.Frac(-3, 1))
		self.assertEqual(-self.f4, fracs.Frac(-6, 2))
		self.assertEqual(-self.f5, fracs.Frac(0, 2))

	def test_invert(self):
		self.assertEqual(~self.f1, fracs.Frac(2, -1))
		self.assertEqual(~self.f2, fracs.Frac(0, 1))
		self.assertEqual(~self.f3, fracs.Frac(1, 3))
		self.assertEqual(~self.f4, fracs.Frac(2, 6))
		self.assertEqual(~self.f5, fracs.Frac(0, 2))

	def test_float(self):
		self.assertEqual(float(self.f1), -0.5)
		self.assertEqual(float(self.f2), 0.0)
		self.assertEqual(float(self.f3), 3.0)
		self.assertEqual(float(self.f4), 3.0)
		self.assertEqual(float(self.f5), 0.0)

	def test_hash(self):
		self.assertEqual(self.f1, fracs.Frac(-1.0, 2.0))
		self.assertEqual(self.f2, fracs.Frac(0.0, 1.0))
		self.assertEqual(self.f3, fracs.Frac(3.0, 1.0))
		self.assertEqual(self.f4, fracs.Frac(6.0, 2.0))
		self.assertEqual(self.f5, fracs.Frac(0.0, 2.0))

	def tearDown(self):
		del self.f1, self.f2, self.f3, self.f4, self.f5
		gc.collect()

if __name__ == '__main__':
	unittest.main()
