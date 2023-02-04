import unittest
import sys
sys.path.append("./src")
from divide.divide_by_three import divide_by_three 

class TestDivideByThree(unittest.TestCase):

	def test_divide_by_three(self):
		self.assertEqual(divide_by_three(12), 4)

unittest.main()