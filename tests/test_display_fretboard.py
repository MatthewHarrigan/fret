import unittest
from display_fretboard.display_fretboard import display_fretboard


class DisplayFretboardTest(unittest.TestCase):

    def test_blank_fretboard(self):
        string = 0
        note = 0

        str = ('0 1 2 3 4 5 6 7 8 9 10 11 12 \n'
               'e | | | | | | | | | | | | \n'
               'b | | | | | | | | | | | | \n'
               'g | | | | | | | | | | | | \n'
               'd | | | | | | | | | | | | \n'
               'a | | | | | | | | | | | | \n'
               'e | | | | | | | | | | | | \n')

        self.assertEqual(display_fretboard(string, note), str)

    def test_six_string_e(self):
        string = 1
        note = 'D#/Eb'

        str = ('0 1 2 3 4 5 6 7 8 9 10 11 12 \n'
               'e | | | | | | | | | | D#/Eb | \n'
               'b | | | | | | | | | | | | \n'
               'g | | | | | | | | | | | | \n'
               'd | | | | | | | | | | | | \n'
               'a | | | | | | | | | | | | \n'
               'e | | | | | | | | | | | | \n')

        self.assertEqual(display_fretboard(string, note), str)

    def test_six_string_f(self):
        string = 1
        note = 'F'

        str = ('0 1 2 3 4 5 6 7 8 9 10 11 12 \n'
               'e F | | | | | | | | | | | \n'
               'b | | | | | | | | | | | | \n'
               'g | | | | | | | | | | | | \n'
               'd | | | | | | | | | | | | \n'
               'a | | | | | | | | | | | | \n'
               'e | | | | | | | | | | | | \n')

        self.assertEqual(display_fretboard(string, note), str)

    def test_fifth_string_c(self):
        string = 1
        note = 'F#/Gb'

        str = ('0 1 2 3 4 5 6 7 8 9 10 11 12 \n'
               'e | F#/Gb | | | | | | | | | | \n'
               'b | | | | | | | | | | | | \n'
               'g | | | | | | | | | | | | \n'
               'd | | | | | | | | | | | | \n'
               'a | | | | | | | | | | | | \n'
               'e | | | | | | | | | | | | \n')

        self.assertEqual(display_fretboard(string, note), str)

    def test_fifth_string_bflat(self):
        string = 2
        note = 'A#/Bb'

        str = ('0 1 2 3 4 5 6 7 8 9 10 11 12 \n'
               'e | | | | | | | | | | | | \n'
               'b | | | | | | | | | | A#/Bb | \n'
               'g | | | | | | | | | | | | \n'
               'd | | | | | | | | | | | | \n'
               'a | | | | | | | | | | | | \n'
               'e | | | | | | | | | | | | \n')

        self.assertEqual(display_fretboard(string, note), str)

    def test_first_string_e(self):
        string = 2
        note = 'B'

        str = ('0 1 2 3 4 5 6 7 8 9 10 11 12 \n'
               'e | | | | | | | | | | | E \n'
               'b | | | | | | | | | | | | \n'
               'g | | | | | | | | | | | | \n'
               'd | | | | | | | | | | | | \n'
               'a | | | | | | | | | | | | \n'
               'e | | | | | | | | | | | | \n')

    def test_second_string_b(self):
        string = 2
        note = 'B'

        str = ('0 1 2 3 4 5 6 7 8 9 10 11 12 \n'
               'e | | | | | | | | | | | | \n'
               'b | | | | | | | | | | | B \n'
               'g | | | | | | | | | | | | \n'
               'd | | | | | | | | | | | | \n'
               'a | | | | | | | | | | | | \n'
               'e | | | | | | | | | | | | \n')

        self.assertEqual(display_fretboard(string, note), str)
