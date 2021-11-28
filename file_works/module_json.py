import json

"""
load() и loads() для превращения кодированных данных JSON в объекты Python.
dump() и dumps() для превращения объектов Python в JSON

"""
my_json_string = """
{
    "worker": "Jon Smith",
    "skills": ["programming", "design", "engineering"],
    "age": 40,
    "workplaces": [
        {
            "first": "IBM",
            "time": "2010-2014"
        },
        {
            "second": "Apple",
            "time": "2014-2018"
        }
    ],
  "is_working": true,
  "driving_license": null
}
"""

# Сериализация в JSON-строку словаря
my_dict = {"Apple": 150, "Pineaple": 300, "Lemon": 60}
json_str = json.dumps(my_dict)
print(type(json_str))

# Сериализация в JSON-объект словаря
with open("new_json.json", 'w') as file:
    json.dump(my_dict, file)

# Десериализация JSON в словарь
with open("new_json.json") as file:
    data = json.load(file)

# Десериализация JSON-строки в словарь
data = json.loads(my_json_string)



