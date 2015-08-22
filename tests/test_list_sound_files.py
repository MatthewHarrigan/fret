import unittest
from list_sound_files.list_sound_files import list_files

class ListFilesTest(unittest.TestCase):

    def test_list_files(self):
        self.assertEqual(list_files('./tests/test_sound_files', 'file_e'), ['file_e', 'file_f', 'file_fsharp'])
