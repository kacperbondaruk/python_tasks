import json
from exercise3 import ReadList
import unittest

class Test_ReadList (unittest.TestCase) :

    def test_read_json (self) :
        expected_data = [element for element in range (10)]
        with open ("test_file.json", "w") as f :
            json.dump(expected_data, f)

        x = ReadList()
        result = x.read_json("test_file.json")
        self.assertEqual(result, expected_data)

if __name__ == "__main__" :
    unittest.main()