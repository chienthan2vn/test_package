import unittest
import sys
sys.path.append("./src")
from mul.mul import mul

class TestMultiplyByThree(unittest.TestCase):

	def test_multiply_by_three(self):
		self.assertEqual(mul(3), 9)

unittest.main()