import json

class ReadList () :
    """NAME
        ReadList

        FUNCTIONS
            read_json (self, file, action = "r" (optional), rEncoding = "UTF-8" (optional))
                Reads json file
            
            check_list (self, data, number = 5 (optional))
                Returns values from list that are less than number argument
            
        DATA DESCRIPTORS
            None
    """
    def __init__(self) :
        pass

    def read_json (self, file : str, action : str = "r", rEncoding = "UTF-8") -> object :
        with open (file, action, encoding = rEncoding) as f :
            data = json.load(f)
        return data


    def check_list (self, data, number : int = 5) -> list :
        container = []
        for element in data :
            if element < number :
                container.append(element)
        return container

if __name__ == "__main__" :
    x = ReadList()
    container = x.read_json("lista.json")
    print(x.check_list(container))