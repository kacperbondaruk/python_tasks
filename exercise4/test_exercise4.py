from exercise4 import Divisor
import unittest

class Test_Divisor (unittest.TestCase) :
    """Tests Divisor class methods"""

    def setUp(self):
        self.divisor = Divisor()
    
    def test_find_divisor(self):
        self.assertEqual(self.divisor.find_divisor(10), [1, 2, 5, 10])
        self.assertEqual(self.divisor.find_divisor(15), [1, 3, 5, 15])
        self.assertEqual(self.divisor.find_divisor(20), [1, 2, 4, 5, 10, 20])
    
    def test_scan_json(self):
        self.assertEqual(self.divisor.scan_json("exercise4_data.json"), [1, 3, 4, 5, 8, 123, 152, 5235])
        self.assertRaises(ValueError, self.divisor.scan_json, 123)


if __name__ == "__main__" :
    unittest.main()