import json

class EvenElements () :
    """NAME
        EvenElements

        DESCRIPTION
            Loads Json file and returns even number using function with List Comprehensions
        
        FUNCTIONS
            read_json(self, file)
                Load list from json file
            
            find_even
                Checks all even numbers in list using List Comprehensions
        
        DATA DESCRIPTORS
            NONE
    """
    def __init__(self) -> None:
        pass

    def read_json (self, file : str) -> list:
        """Loads list from json file

        Args:
            file (str): json file name (string)

        Returns:
            list: return list from json file
        """
        with open (file, "r", encoding = "UTF-8") as f :
            data = json.load(f)
        return data

    def find_even (self, data : list) -> list :
        """Checks all even numbers in list using List Comprehensions

        Args:
            data (list): Takes list from scanned json file

        Returns:
            list: Returns modified list
        """
        container = [element for element in data if element % 2 == 0]
        return container

if __name__ == "__main__" :
    x = EvenElements()
    data = x.read_json("exercise7_data.json")
    print(x.find_even(data))