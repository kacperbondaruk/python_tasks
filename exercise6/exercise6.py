import json

class Palindrome () :
    """NAME
        Palindrome
        
        DESCRIPTION
            check_palindromes if the string is pallindrome or not
        
        FUNCTIONS
            scan_json(self, data)
                Loads list in json file
            
            check_palindrome(self, data)
                Checks strings in list if they are palindromes or not
        
        DATA DESCRIPTORS
            self.palindromes - Holds palindrome strings
            self.nonPalindromes - Holds non-palindrome strings

    """
    def __init__(self):
        self.palindromes = []
        self.nonPalindromes = []

    def scan_json (self, file : str) -> list :
        """Scan json file

        Args:
            file (str): Json_file_name.json

        Returns:
            list: Returns list from json
        """
        with open (file, "r", encoding = "UTF-8") as f :
            data = json.load(f)
        return data
    
    def check_palindrome (self, data : list) -> list :
        """Checks if strings are palindromes

        Args:
            data (list): Input list with strings that you want to check

        Returns:
            list: Returns 2 lists with and without palindromes
        """
        for element in data :
            if element == element[::-1] :
                self.palindromes.append(element)
            else :
                self.nonPalindromes.append(element)
        return self.palindromes, self.nonPalindromes
            



if __name__ == "__main__" :
    x = Palindrome()
    data = x.scan_json("exercise6_data.json")
    print(x.check_palindrome(data))