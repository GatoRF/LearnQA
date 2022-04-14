import json

#example1
json_text = """{"messages":[{"message":"This is the first message","timestamp":"2021-06-04 16:40:53"},{"message":"And this is a second message","timestamp":"2021-06-04 16:41:01"}]}"""
py_json_text = json.loads(json_text)

print(py_json_text["messages"][1])



#example1
jsonData = """ {
    "ID"       : 210450,
    "login"    : "admin",
    "name"     : "John Smith",
    "password" : "root",
    "phone"    : 5550505,
    "email"    : "smith@mail.com",
    "online"   : true
} """

dictData = json.loads(jsonData)
print(dictData["name"])