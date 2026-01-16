import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from data_utils import is_empty  

import unittest

class TestDataUtils(unittest.TestCase):

    def test_empty_none(self):
        self.assertTrue(is_empty(None))

    def test_empty_string(self):
        self.assertTrue(is_empty(""))

    def test_empty_spaces(self):
        self.assertTrue(is_empty("   "))

    def test_not_empty(self):
        self.assertFalse(is_empty("hello"))

if __name__ == "__main__":
    unittest.main()
