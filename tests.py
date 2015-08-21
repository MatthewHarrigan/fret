import unittest
from fretboard import get_note_index

class GetNumberTest(unittest.TestCase):

    def test_getting_low_e(self):
        self.assertEqual(get_note_index(6, 'E'), 0)


if __name__ == '__main__':
    unittest.main()
