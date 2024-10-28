from formatted_name import formatted_name
import unittest


class TestFormattedName(unittest.TestCase):
    def test_full_name_with_middle(self):
        self.assertEqual(formatted_name("john", "doe", "james"), "John James Doe")

    def test_full_name_without_middle(self):
        self.assertEqual(formatted_name("john", "doe"), "John Doe")

    def test_empty_first_name(self):
        self.assertEqual(formatted_name("", "doe"), " Doe")

    def test_empty_last_name(self):
        self.assertEqual(formatted_name("john", ""), "John ")

    def test_empty_middle_name(self):
        self.assertEqual(formatted_name("john", "doe", ""), "John Doe")

    def test_return_type(self):
        result = formatted_name("john", "doe")
        self.assertIsInstance(result, str)
