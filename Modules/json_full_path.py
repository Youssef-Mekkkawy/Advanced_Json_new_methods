#!/usr/bin/env python3

"""
i Get This traverse Function from Github.
Author:
* Laszlo Szathmary, alias Jabba Laci, 2017--2020, jabba.laci@gmail.com.

Github:- https://github.com/jabbalaci/JSON-path/blob/master/jsonpath.py

Find the path of a key / value in a JSON hierarchy easily.
It was made for JSON files, but it also works with dictionaries,
of course.

Inspired by:
* http://stackoverflow.com/a/34837235/232485 (doesn't treat nested lists)
* http://chris.photobooks.com/json/default.htm (in-browser visualization)


"""

import json
from typing import Any, Dict, List, Union

class Json_full_Path:
    def __init__(self) -> None:
        ...
    def Reader(self, filename:str):
        """
        -----------
        filename : str path of Json File.
        ----------
        """
        with open(filename) as file:
            return json.load(file)
        
    def traverse(self, path: str, obj: Any, Dict___, count:int, method:str) -> None:
        """
        Traverse the object recursively and print every path / value pair.
        """
        if isinstance(obj, list): 
            for i, subnode in enumerate(obj):
                count+=1
                self.traverse(path + f'{i}.', subnode, Dict___, count, method)
        elif isinstance(obj, dict):
            for k, v in obj.items():
                # count+=1
                self.traverse(path + f'{k}.', v, Dict___, count, method)
        else:
        
            method = method.lower()
            # here Get Value of key.
            if method == "key":
                Dict___[path[:-1].split(".")[-1]+"."+str(count)] = path[:-1]
            # Here Get Key of value.
            elif method == "value":
                Dict___[obj] = path[0:][:-1]
               
            else:
                return "Accept Only key/value"

    def process(self, d:dict, method:str):
        """
        Process the given JSON file.
        """
        count = 0
        Dict___ = {}
        d: Dict
        self.traverse("", d, Dict___, count, method = method)
        return Dict___

    ##############################################################################

if __name__ == "__main__":

    full_json_path = Json_full_Path()
    with open("Write_.json", "w", encoding="utf-8") as jsonfile:
        # jsonfile.write(json.dumps(full_json_path.process(full_json_path.Reader("Json/data.json"), method="key"), indent=4))
        jsonfile.write(json.dumps(full_json_path.process(full_json_path.Reader("Json/data.json"), method="value"), indent=4))

