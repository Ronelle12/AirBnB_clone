import unittest
import shutil
import os


class TestFileExistence(unittest.TestCase):
    def test_filepath(self):
        directory_path = 'C:/AirBnB_clone/tests'
        # file_path = os.path(directory_path)
        (self.assertTrue(os.path.exists(directory_path)),
         f"Folder {directory_path} does not exist directory")


if __name__ == '__main__':
    unittest.main()
