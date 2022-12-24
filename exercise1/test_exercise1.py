import unittest
from unittest.mock import PropertyMock, patch
from exercise1 import UserQuestion

class Test_UserQuestion(unittest.TestCase) :

    @patch('builtins.input', return_value='Kacper')
    def test_question_name (self, mock_input) :
        myClass = UserQuestion()
        result = myClass.question_name()
        self.assertEqual(result, 'Kacper')

    @patch('builtins.input', return_value='40')
    def test_question_age(self, mock_input) :
        myClass = UserQuestion()
        result = myClass.question_age()
        self.assertEqual(result, '40')
    
    def test_count_years(self):
        obj = UserQuestion()
        obj.age = 50
        result = obj.count_years()
        self.assertEqual(result, 2072)


if __name__ == "__main__" :
    unittest.main()