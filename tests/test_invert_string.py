import unittest
from strings.strings import invert_string_number

class InvertStringNumber(unittest.TestCase):
    def test_invert_string(self):
        self.assertEqual(invert_string_number(0), False);
        self.assertEqual(invert_string_number(7), False);

        self.assertEqual(invert_string_number(1), 6)
        self.assertEqual(invert_string_number(2), 5)
        self.assertEqual(invert_string_number(3), 4)
        self.assertEqual(invert_string_number(4), 3)
        self.assertEqual(invert_string_number(5), 2)
        self.assertEqual(invert_string_number(6), 1)

