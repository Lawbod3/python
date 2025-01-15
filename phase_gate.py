import unittest
import methodpalindrome


class TestMethodPalindrome(unittest.TestCase):

	def test_that_palindrome_function_exists(self):
		methodpalindrome.get_palindrome(101)

	def test_that_the_sum_of_number(self):
	   actual = methodpalindrome.get_palindrome(101)
	   result = 2
	   self.assertEqual(actual, result)

class TestMethodMultiply(unittest.TestCase):

	def test_that_multiply_function_exist(self):
		methodpalindrome.get_multiply(2, 4)

	def test_that_the_multiple_of_number(self):
	   actual = methodpalindrome.get_multiply(2, 4)
	   result = 8
	   self.assertEqual(actual, result)	



