class NumberProgram () :
    """NAME
        NumberProgram
        
        FUNCTIONS
        number_scanner (self, number : int, check : int (optional))
            Checks if the number is odd or even

        DATA DESCRIPTORS
            __init__ (pass)
    """
    def __init__ (self) :
        pass

    def number_scanner (self, number : int, check : int = 0) -> str:
        if isinstance(number, int) != True and isinstance(check, int) != True:
            raise ValueError("You can input integer values only")
        elif number == 0 :
            raise ValueError("You can't divide by 0")
        elif check != 0 :
            if number % check == 0 :
                return f"{number} was divided evenly by {check} \n"
            else :
                return f"{number} wasn't divided evenly by {check} \n"
        else:
            if number % 4 == 0 :
                return f"{number} is Even and can be divided by 4 \n"
            elif number % 2 == 0 :
                return f"{number} is Even \n"
            else :
                return f"{number} is Odd \n"
    
        

if __name__ == "__main__" :
    x = NumberProgram()
    print(x.number_scanner(2))
    print(x.number_scanner(1))
    print(x.number_scanner(-1))
    print(x.number_scanner(0))