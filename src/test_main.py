from main import isOldEnough
import unittest

class TestIsOldEnough(unittest.TestCase):
	def test_isOldEnough(self):
		self.assertEqual(isOldEnough("2000/01/01","2020/01/01"), True)
		self.assertEqual(isOldEnough("2000/01/01","2003/01/01"), False)
		with self.assertRaises(Exception):
			isOldEnough("2000/01/01","1940/01/01")#DateException
		with self.assertRaises(Exception):
			isOldEnough("2000-01-01","2000-01-01")#DateFormatException
