import unittest
from amity import Amity

class TestAmity(unittest.TestCase):
	def test_type_of_amity(self):
		self.assertIsInstance(Amity(), object)
			