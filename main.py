from Modules.json_advanced_method import Json_Advanced_Method
Dict_ = {
    "Info": {
        "name":{
            "first-name":"Ahmed",
            "last-name" :"Mohamed"
        },
        "accounts-lists":{
            "facebook-name":"Test",
            "instgram-name":None
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
    "success": True
}

def Example_1():

    json_method = Json_Advanced_Method()

    yield json_method.Get_Info(Objs= Dict_, key="first-name.0"), json_method.Get_Info(Objs= Dict_, key="last-name.0")

    yield json_method.Get_Info(Objs= Dict_, key="first-name.1"), json_method.Get_Info(Objs= Dict_, key="last-name.1")

    yield json_method.Get_Info(Objs= Dict_, key="first-name.2"), json_method.Get_Info(Objs= Dict_, key="last-name.2")

    
def Example_2(Method = "value"):
    json_method = Json_Advanced_Method()

    yield json_method.Get_Info(Objs= Dict_, key="Ahmed", method = Method)
    yield json_method.Get_Info(Objs= Dict_, key="Mohamed", method = Method)

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
    ...














