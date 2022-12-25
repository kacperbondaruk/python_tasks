import unittest
from exercise2 import NumberProgram

class Test_NumberProgram(unittest.TestCase) :

    def test_number_scanner (self) :
        myClass = NumberProgram()
        result = myClass.number_scanner(2)
        self.assertEqual(result, f"{2} is Even \n")

        result = myClass.number_scanner(1)
        self.assertEqual(result, f"{1} is Odd \n")

        result = myClass.number_scanner(8)
        self.assertEqual(result, f"{8} is Even and can be divided by 4 \n")

        result = myClass.number_scanner(-1)
        self.assertEqual(result, f"{-1} is Odd \n")

        result = myClass.number_scanner(4, -4)
        self.assertEqual(result, f"{4} was divided evenly by {-4} \n")

        result = myClass.number_scanner(4, -3)
        self.assertEqual(result, f"{4} wasn't divided evenly by {-3} \n")



    def test_value_error (self) :
        myClass = NumberProgram()
        self.assertRaises(ValueError, myClass.number_scanner, "xyz", "abc")
        self.assertRaises(ValueError, myClass.number_scanner, 0)

        

if __name__ == "__main__" :
    unittest.main()