from fibonacci import Fibonacci
import unittest


class TestFibonacci(unittest.TestCase):
    def setUp(self):
        self.fibonacci = Fibonacci()

    def test_base_cases(self):
        self.assertEqual(self.fibonacci(0), 0)
        self.assertEqual(self.fibonacci(1), 1)

    def test_small_numbers(self):
        self.assertEqual(self.fibonacci(5), 5)
        self.assertEqual(self.fibonacci(10), 55)

    def test_large_numbers(self):
        self.assertEqual(self.fibonacci(10), 55)
        self.assertEqual(self.fibonacci(20), 6765)

    def test_cache(self):
        self.assertEqual(self.fibonacci(15), 610)
        self.assertEqual(self.fibonacci(15), 610)

    def test_negative(self):
        self.assertRaises(ValueError, self.fibonacci, -5)

    def test_not_integer(self):
        self.assertRaises(ValueError, self.fibonacci, "five")
        self.assertRaises(ValueError, self.fibonacci, 5.5)
