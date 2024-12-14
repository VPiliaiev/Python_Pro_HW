import unittest
from Sum_of_Intervals import sum_of_intervals


class TestSumOfIntervals(unittest.TestCase):
    def test_fixed_cases(self):
        self.assertEqual(sum_of_intervals([(1, 5)]), 4)
        self.assertEqual(sum_of_intervals([(1, 5), (6, 10)]), 8)
        self.assertEqual(sum_of_intervals([(1, 5), (1, 5)]), 4)
        self.assertEqual(sum_of_intervals([(1, 4), (7, 10), (3, 5)]), 7)

    def test_large_numbers(self):
        self.assertEqual(sum_of_intervals([(-1_000_000_000, 1_000_000_000)]), 2_000_000_000)
        self.assertEqual(sum_of_intervals([(0, 20), (-100_000_000, 10), (30, 40)]), 100_000_030)


if __name__ == "__main__":
    unittest.main()
