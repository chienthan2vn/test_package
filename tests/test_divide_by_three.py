import unittest
import sys
sys.path.append("./src")
from div.div import div 

class TestDivideByThree(unittest.TestCase):

	def test_divide_by_three(self):
		self.assertEqual(div(12), 4)

unittest.main()