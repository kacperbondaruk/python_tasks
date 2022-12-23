from dataclasses import asdict
from datetime import date
import re

class UserQuestion ():
    """_summary_
    """
    def __init__(self) -> None:
        self.date = date.today()
        self.regex_name = "^[a-zA-Z]"
        self.regex_age = "^([0-9]|[1-9][0-9]|100)$"

    def question_name (self, name = ""):
        name = input("What's your name? \n")
        if not re.match(self.regex_name, name)  :
            raise ValueError("Input have to contain english letters from a - z")
        else:
            return name

    def question_age (self):
        self.age = input("What's your age? \n")
        if not re.match(self.regex_age, self.age) :
            raise ValueError("Input have to contain numbers from 0 - 9 max value = 100 ")      

if __name__ == "__main__" :
    x = UserQuestion()
    x.question_name()
    x.question_age()