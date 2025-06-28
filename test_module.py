# test_module.py
import unittest
from demographic_data_analyzer import calculate_average

class TestAnalyzer(unittest.TestCase):
    def test_average(self):
        self.assertEqual(calculate_average([1, 2, 3]), 2)
        self.assertAlmostEqual(calculate_average([1, 2, 3, 4]), 2.5)

if __name__ == "__main__":
    unittest.main()
