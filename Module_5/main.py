import unittest
import fracs
import gc

class TestFractions(unittest.TestCase):

	def setUp(self):
		self.zero = [0, 1]
		self.f1 = [-1, 2]
		self.f2 = [0, 1]
		self.f3 = [3, 1]
		self.f4 = [6, 2]
		self.f5 = [0, 2]

	def test_reduce_frac(self):
		self.assertEqual(fracs.reduce_frac(self.f1), [-1, 2])
		self.assertEqual(fracs.reduce_frac(self.f2), self.zero)
		self.assertEqual(fracs.reduce_frac(self.f3), [3, 1])
		self.assertEqual(fracs.reduce_frac(self.f4), [3, 1])
		self.assertEqual(fracs.reduce_frac(self.f5), self.zero)
		self.assertEqual(fracs.reduce_frac([1, -1]), [-1, 1])
		self.assertEqual(fracs.reduce_frac([20, -10]), [-2, 1])
		self.assertEqual(fracs.reduce_frac([-5, -15]), [1, 3])
		self.assertEqual(fracs.reduce_frac([1, 0]), ZeroDivisionError)

	def test_add_frac(self):
		self.assertEqual(fracs.add_frac(self.f1, self.f2), [-1, 2])
		self.assertEqual(fracs.add_frac(self.f3, self.f4), [6, 1])
		self.assertEqual(fracs.add_frac(self.f1, self.f4), [5, 2])

	def test_sub_frac(self):
		self.assertEqual(fracs.sub_frac(self.f1, self.f2), [-1, 2])
		self.assertEqual(fracs.sub_frac(self.f5, self.f1), [1, 2])
		self.assertEqual(fracs.sub_frac(self.f4, self.f3), self.zero)

	def test_mul_frac(self):
		self.assertEqual(fracs.mul_frac(self.f1, self.f2), self.zero)
		self.assertEqual(fracs.mul_frac(self.f3, self.f4), [9, 1])
		self.assertEqual(fracs.mul_frac(self.f1, self.f4), [-3, 2])

	def test_div_frac(self):
		self.assertEqual(fracs.div_frac(self.f1, self.f4), [-1, 6])
		self.assertEqual(fracs.div_frac(self.f3, self.f4), [1, 1])
		self.assertEqual(fracs.div_frac(self.f4, self.f5), ZeroDivisionError)

	def test_is_zero(self):
		self.assertFalse(fracs.is_zero(self.f1))
		self.assertTrue(fracs.is_zero(self.f2))
		self.assertFalse(fracs.is_zero(self.f3))
		self.assertFalse(fracs.is_zero(self.f4))
		self.assertTrue(fracs.is_zero(self.f5))

	def test_is_positive(self):
		self.assertFalse(fracs.is_positive(self.f1))
		self.assertFalse(fracs.is_positive(self.f2))
		self.assertTrue(fracs.is_positive(self.f3))
		self.assertTrue(fracs.is_positive(self.f4))
		self.assertFalse(fracs.is_positive(self.f5))

	def test_frac2float(self):
		self.assertEqual(fracs.frac2float(self.f1), -0.5)
		self.assertEqual(fracs.frac2float(self.f2), 0.0)
		self.assertEqual(fracs.frac2float(self.f3), 3.0)
		self.assertEqual(fracs.frac2float(self.f4), 3.0)
		self.assertEqual(fracs.frac2float(self.f5), 0.0)

	def test_cmp_frac(self):
		self.assertEqual(fracs.cmp_frac(self.f1, self.f2), -1)
		self.assertEqual(fracs.cmp_frac(self.f2, self.f3), -1)
		self.assertEqual(fracs.cmp_frac(self.f3, self.f4), 0)
		self.assertEqual(fracs.cmp_frac(self.f4, self.f5), 1)
		self.assertEqual(fracs.cmp_frac(self.f5, self.f1), 1)

	def tearDown(self):
		del self.zero, self.f1, self.f2, self.f3, self.f4, self.f5
		gc.collect()

if __name__ == '__main__':
	unittest.main()
