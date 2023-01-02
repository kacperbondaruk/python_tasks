
from ctypes import Union


class RpsGame () :
    """NAME
        RpsGame

        DESCRIPTION
            Rock Paper Scissors Game
        
        FUNCTIONS
            choice (self, playerName)
                Asks player what he chooses (Rock / Paper / Scissors)

            question (self, function)
                Asks player if he want to continue game
            
            game (self)
                Main class function to run the game using other class functions
        
        DATA DESCRIPTORS
            self.run - Handles loop in game function when False loop doesn't work anymore
    """
    def __init__ (self) :
        self.run = True

    def choice (self, playerName : str) -> str:
        """Asks player what he chooses (Rock / Paper / Scissors)
        
        Args:
            playerName (str) : Input the name of the player (Player1 , Player2 etc.)
        
        Returns:
            str : Returns player choice
         """
        rps = input(f"""Choose {playerName}:
        1 - Rock
        2 - Paper
        3 - Scissors\n""")
        if rps not in ["1", "2", "3"]:
            print(f"{player} value is not from 1 - 3 range try again\n")
            self.choice(playerName)
        else:
            return rps
    
    def question (self, functionName) -> None :
        """Asks player if he want to play next round
        
        Args:
            functionName (function) : Calls function after given question

        Returns:
            None
            """
        question = input("""Do you want to start new game? 
                1 - yes
                2 - no \n""")
        if question == "1" or question.lower() == "yes" :
            functionName
        elif question == "2" or question.lower() == "no" :
            print("Thank you for the game \n")
            self.run = False
        else :
            print("Choose number from 1 to 2 or write yes or no \n")
            self.question(functionName)
                    

    def game (self) -> None:
        """Main function to run whole game

        Args :
        None

        Returns :
        None
        """
        while self.run :
            player1 = self.choice("Player 1")
            player2 = self.choice("Player 2")
            if player1 == player2 :
                print("Draw! \n")
                self.question(self.game)
            elif (player1 == "1" and player2 == "3") or (player1 == "2" and player2 == "1") or (player1 == "3" and player2 == "2"):
                print("Player 1 Wins \n")
                self.question(self.game)
            else :
                print("Player 2 Wins \n")
                self.question(self.game)
                
            


if __name__ == "__main__" :
    x = RpsGame()
    x.game()