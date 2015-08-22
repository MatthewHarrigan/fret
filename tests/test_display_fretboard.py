import unittest
from display_fretboard.display_fretboard import display_fretboard

class DisplayFretboardTest(unittest.TestCase):

    def test_empty_fretboard(self):

        str = ('0 1 2 3 4 5 6 7 8 9 10 11 \n'
            'e | | | | | | | | | | | \n'
            'b | | | | | | | | | | | \n'
            'g | | | | | | | | | | | \n'
            'd | | | | | | | | | | | \n'
            'a | | | | | | | | | | | \n'
            'e | | | | | | | | | | | \n')

        self.assertEqual(display_fretboard(), str)
