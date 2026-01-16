import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from math_tools import modulo, multiply  

import unittest

class TestMathTools(unittest.TestCase):

    def test_modulo(self):
        self.assertEqual(modulo(10, 3), 1)

    def test_modulo_zero(self):
        self.assertEqual(modulo(8, 4), 0)

    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)

    def test_multiply_zero(self):
        self.assertEqual(multiply(5, 0), 0)

if __name__ == "__main__":
    unittest.main()
