import unittest
import sys
sys.path.append("./src")
from div.div2 import div1

class TestDivideByThree(unittest.TestCase):

	def test_divide_by_three(self):
		self.assertEqual(div1(12), 4)

unittest.main()