from main import isOldEnough
import unittest

class TestIsOldEnough(unittest.TestCase):
	def test_isOldEnough(self):
		actual = isOldEnough("2000/01/01","2020/01/01")
		self.assertEqual(actual, True)

if __name__ == '__main__':
	unittest.main()