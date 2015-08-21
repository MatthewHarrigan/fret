import unittest
from fretboard import get_index

class GetNumberTest(unittest.TestCase):

    def test_get_index(self):
        # Open E
        self.assertEqual(get_index(6, 'E'), 12)

        self.assertEqual(get_index(6, 'F'), 1)
        self.assertEqual(get_index(6, 'D#/Eb'), 11)

        # Open A
        self.assertEqual(get_index(5, 'A'), 17)

        self.assertEqual(get_index(5, 'F'), 13)
        self.assertEqual(get_index(5, 'F#/Gb'), 14)
        self.assertEqual(get_index(5, 'G'), 15)
        self.assertEqual(get_index(5, 'G#/Ab'), 16)
        self.assertEqual(get_index(5, 'A'), 17)

        # Open D
        self.assertEqual(get_index(4, 'D'), 22)

        self.assertEqual(get_index(4, 'D#/Eb'), 11)
        self.assertEqual(get_index(4, 'E'), 12)

        self.assertEqual(get_index(4, 'F'), 13)
        self.assertEqual(get_index(4, 'F#/Gb'), 14)
        self.assertEqual(get_index(4, 'G'), 15)
        self.assertEqual(get_index(4, 'G#/Ab'), 16)
        self.assertEqual(get_index(4, 'A'), 17)
        self.assertEqual(get_index(4, 'A#/Bb'), 18)
        self.assertEqual(get_index(4, 'B'), 19)
        self.assertEqual(get_index(4, 'C'), 20)
        self.assertEqual(get_index(4, 'C#/Db'), 21)

        # Open G
        self.assertEqual(get_index(3, 'G'), 27)

        self.assertEqual(get_index(3, 'G#/Ab'), 16)
        self.assertEqual(get_index(3, 'A'), 17)
        self.assertEqual(get_index(3, 'A#/Bb'), 18)
        self.assertEqual(get_index(3, 'B'), 19)
        self.assertEqual(get_index(3, 'C'), 20)
        self.assertEqual(get_index(3, 'C#/Db'), 21)
        self.assertEqual(get_index(3, 'D'), 22)
        self.assertEqual(get_index(3, 'D#/Eb'), 23)
        self.assertEqual(get_index(3, 'E'), 24)
        self.assertEqual(get_index(3, 'F'), 25)
        self.assertEqual(get_index(3, 'F#/Gb'), 26)

        # Open B
        self.assertEqual(get_index(2, 'B'), 19)

        self.assertEqual(get_index(2, 'C'), 20)
        self.assertEqual(get_index(2, 'C#/Db'), 21)
        self.assertEqual(get_index(2, 'D'), 22)
        self.assertEqual(get_index(2, 'D#/Eb'), 23)
        self.assertEqual(get_index(2, 'E'), 24)
        self.assertEqual(get_index(2, 'F'), 25)
        self.assertEqual(get_index(2, 'F#/Gb'), 26)
        self.assertEqual(get_index(2, 'G'), 27)
        self.assertEqual(get_index(2, 'G#/Ab'), 28)
        self.assertEqual(get_index(2, 'A'), 29)
        self.assertEqual(get_index(2, 'A#/Bb'), 30)

        # Open E
        self.assertEqual(get_index(1, 'E'), 36)
        self.assertEqual(get_index(1, 'F'), 25)
        self.assertEqual(get_index(1, 'F#/Gb'), 26)
        self.assertEqual(get_index(1, 'G'), 27)
        self.assertEqual(get_index(1, 'G#/Ab'), 28)
        self.assertEqual(get_index(1, 'A'), 29)
        self.assertEqual(get_index(1, 'A#/Bb'), 30)
        self.assertEqual(get_index(1, 'B'), 31)
        self.assertEqual(get_index(1, 'C'), 32)
        self.assertEqual(get_index(1, 'C#/Db'), 33)
        self.assertEqual(get_index(1, 'D'), 34)
        self.assertEqual(get_index(1, 'D#/Eb'), 35)

if __name__ == '__main__':
    unittest.main()
