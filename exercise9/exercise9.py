import random

class GuessingGame () :
    """NAME
        GuessingGame

        DESCRIPTION
            Guessing Game where user have to guess the correct number
        
        FUNCTIONS
            ask_user (self)
                Asks user to guess number or exit the program
            game (self)
                Checks if user guessed number
        DATA DESCRIPTORS
            self.rNumber - Random generated number that user have to guess
            self.gNumber - Array that counts how many guesses user made
    """
    def __init__(self) -> None:
        self.rNumber = random.randint(1, 9)
        self.gNumber = 0

    def ask_user (self) -> int:
        """Ask user for number and checks if it match rNumber

        Args:
            None

        Returns:
            int : returns number that user guessed or rNumber if user typed exit
        """
        guess = input("Try to Guess the Number or type exit to finish : \n")
        if guess.lower() == "exit" :
            return self.rNumber
        try:
            guess = int(guess)
        except ValueError :
            print(f"{guess} has to be in 1 - 9 number range \n")
            return self.ask_user()
        if guess not in range(1, 10) :
            print(f"{guess} has to be in 1 - 9 number range \n")
            return self.ask_user()
        elif guess > self.rNumber :
            self.gNumber += 1
            print(f"{guess} number is too high \n")
            return guess
        elif guess < self.rNumber :
            self.gNumber += 1
            print(f"{guess} number is too low \n")
            return guess
        elif guess == self.rNumber :
            self.gNumber += 1
            print(f"{guess} is the correct number it took you {self.gNumber} guesses \n")
            return guess
    
    def game (self) -> None :
        """Checks if user matched the random generater number

        Args :
            None

        Returns :
            None
        """
        guess = 0
        while guess != self.rNumber :
            guess = self.ask_user()

if __name__ == "__main__" :
    x = GuessingGame()
    x.game()
    