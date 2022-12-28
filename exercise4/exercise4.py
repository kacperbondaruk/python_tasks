import json


class Divisor () :
    """NAME
        Divisor

        DESCRIPTION
            Finds divisors of the given number inside json file
        
        FUNCTIONS
            find_divisor (self, data)
                finds divisors of the given number
            
            scan_json (self, file)
                Read list with int values inside json file
        
        DATA DESCRIPTORS
            NONE

    """
    def __init__ (self) :
        pass

    def find_divisor (self, data : int) -> list:
        """Find divisors for given number

        Args:
            data (int): Number for function

        Returns:
            list: Returns list of divisors of the given number
        """
        numbers = [x for x in range(1, data+1) if data % x == 0 ]
        return numbers
    
    def scan_json (self, file : str) :
        """Load list of numbers inside json file

        Args:
            file (str): Name of json file in string format

        Raises:
            ValueError: Appears if user gave file argument in format different than string

        Returns:
            object : Returns json file in python format
        """
        if type(file) != str :
            raise ValueError("file argument takes only file name in string")
        else:
            with open (file, "r", encoding = "UTF-8") as f :
                data = json.load(f)
                return data

if __name__ == "__main__" :
    x = Divisor()
    data = x.scan_json("exercise4_data.json")
    for index in data :
        print(f"{index} divisors are {x.find_divisor(index)}")