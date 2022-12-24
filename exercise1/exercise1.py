from datetime import date, timedelta
import re
class UserQuestion ():
    """_summary_
    """
    def __init__(self) -> None:
        self.date = date.today()
        self.regex_name = "^[a-zA-Z]+$"
        self.regex_age = "^([0-9]|[1-9][0-9]|100)$"
        self.name = ""
        self.age = ""

    def question_name (self) -> str:
        self.name = input("What's your name? \n")
        if not re.match(self.regex_name, self.name)  :
            raise ValueError("Input have to contain english letters from a - z")
        else:
            return self.name

    def question_age (self) -> str:
        self.age = input("What's your age? \n")
        if not re.match(self.regex_age, self.age) :
            raise ValueError("Input have to contain numbers from 0 - 9 max value = 100 ")     
        else:
            return self.age

    def count_years (self) -> date:
        years = 100 - int(self.age)
        self.date = self.date + timedelta(days=365 * years)
        self.date = self.date.year
        return self.date

    def answer (self) -> str:
        return f"{self.name.lower().capitalize()} you will turn 100 years old at {self.date}"
        



if __name__ == "__main__" :
    x = UserQuestion()
    x.question_name()
    x.question_age()
    x.count_years()
    print(x.answer())