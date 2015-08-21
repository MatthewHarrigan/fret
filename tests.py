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

if __name__ == '__main__':
    unittest.main()
