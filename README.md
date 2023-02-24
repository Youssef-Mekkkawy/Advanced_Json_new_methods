# Json Advanced Exmaple.

```terminal
> pip install -r requirements.txt
```

Usage:

```python
from Modules.json_advanced_method import Json_Advanced_Method

def Example_1():

    json_method = Json_Advanced_Method()

    yield json_method.Get_Info(Objs= Dict_, key="first-name.0"), json_method.Get_Info(Objs= Dict_, key="last-name.0")

    yield json_method.Get_Info(Objs= Dict_, key="first-name.1"), json_method.Get_Info(Objs= Dict_, key="last-name.1")

    yield json_method.Get_Info(Objs= Dict_, key="first-name.2"), json_method.Get_Info(Objs= Dict_, key="last-name.2")

def Example_2(Method = "value"):
    json_method = Json_Advanced_Method()

    yield json_method.Get_Info(Objs= Dict_, key="Youssef", method = Method)
    yield json_method.Get_Info(Objs= Dict_, key="Mahmoud", method = Method)

    yield json_method.Get_Info(Objs= Dict_, key="Homes", method = Method)
    yield json_method.Get_Info(Objs= Dict_, key="Example", method = Method)

    yield json_method.Get_Info(Objs= Dict_, key=True, method = Method)
    yield json_method.Get_Info(Objs= Dict_, key =1111, method = Method)
    
def Example_3(Method = "path"):
    json_method = Json_Advanced_Method()
    
    yield json_method.Get_Info(Objs= Dict_, key="Info.name", method = Method)
    yield json_method.Get_Info(Objs= Dict_, key="Info.accounts-lists", method = Method)

    yield json_method.Get_Info(Objs= Dict_, key="data.0.MainId", method = Method)
    yield json_method.Get_Info(Objs= Dict_, key="success", method = Method)


if __name__ == "__main__":
    for first_name, last_name in Example_1():
        print(first_name, last_name)
    print("#"*10)


    for key in Example_2():
        print(key)

    print("#"*10)
    for key in Example_3():
        print(key)
```

Input Dict.

```json
{
    "Info": {
        "name":{
            "first-name":"Ahmed",
            "last-name" :"Mohamed"
        },
        "accounts-lists":{
            "facebook-name":"Test",
            "instgram-name":"none"
        }
    },
    "More-Info":{
        "Zero": "0"
    },
    "data": [
        {
            "MainId": 1111,
            "first-name": "Sherlock",
            "last-name": "Homes",
            "categories": [
                {
                    "CategoryID": 1,
                    "CategoryName": "Example"
                }
            ]
        },
        {
            "MainId": 1222,
            "first-name": "James",
            "last-name": "Watson",
            "categories": [
                {
                    "CategoryID": 2,
                    "CategoryName": "Example2"
                }
            ]
        }
    ],
    "messages": [],
    "success": true
}
```

Output Like That

Example (1)



```tex
Ahmed Mohamed
Sherlock Homes
James Watson
```

Output Like That

Example (2)

```tex
Info.name.first-name
Info.name.last-name
data.0.last-name
data.0.categories.0.CategoryName
success
data.0.MainId
```

Output Like That

Example (3)

```tex
{'first-name': 'Ahmed', 'last-name': 'Mohamed'}
{'facebook-name': 'Test', 'instgram-name': None}
1111
Truerue
```


