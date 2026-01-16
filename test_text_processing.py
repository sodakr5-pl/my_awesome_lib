import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from text_processing import word_count

import unittest

class TestTextProcessing(unittest.TestCase):

    def test_word_count_simple(self):
        self.assertEqual(word_count("Hello world"), 2)

    def test_word_count_more_words(self):
        self.assertEqual(word_count("Python is very cool"), 4)

    def test_word_count_empty(self):
        self.assertEqual(word_count(""), 0)


if __name__ == "__main__":
    unittest.main()
