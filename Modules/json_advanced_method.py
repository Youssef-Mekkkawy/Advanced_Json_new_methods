import json
import functools, operator

try:
    from Modules.json_full_path import Json_full_Path
except:
    from json_full_path import Json_full_Path



class Json_Advanced_Method(Json_full_Path):
    def __init__(self) -> None:
        super().__init__()

    def Reader(self, filename:str):
        """
        ----------
        filename : str path of Json File.
        ----------
        """
        with open(filename) as file:
            return json.load(file)
    
    def Check_parameter(self, filename, Objs):
        if filename:
            return self.Reader(filename)
        elif not filename and not Objs:
            return "Please got 0 parameter we need at least 1 paramets" 
        else:
            return Objs

    def get_nested_value(self , obj, path):
        """
        ----------
        This Fucntion Create Path for Dict and get value.
        """

        def _getitem(obj, attr, *args):
            return operator.getitem(obj, int(attr) if attr.isnumeric() else attr, *args)

        return functools.reduce(_getitem, [obj] + path.split("."))
        
    def Get_Info(self, filename:str = None,  Objs:dict= None, key:str = None, method:str = "key"):
        """
        --------------
        filename : str 
        --------------
        key : str any key you want it's value.
        --------------
        method:str = key/value/path
        --------------
 
        """

        Objs = self.Check_parameter(filename, Objs)
       
        try:
            if method == "key":
                try:
                    return self.get_nested_value(Objs, self.process(Objs, method)[key])
                except:
                    return "Can't Find key | or Something Worng"
            elif method == "value":
                try:
                    return self.process(Objs, method)[key]
                except:
                    return "Can't Find value | or Something Worng" 
            elif method == "path":
                try:
                    return self.get_nested_value(Objs, key)
                except:
                    return "Can't Find path | or Something Worng"  
        except:
            return "Something Wrong."

if __name__ == "__main__":

    item = Json_Advanced_Method()
    print(item.Get_Info(filename="Json/data.json", key= "last-name.0"))
    print(item.Get_Info(filename="Json/data.json", key= "lastName.1"))
    print(item.Get_Info(filename="Json/data.json", key= "lastName.2"))

    
