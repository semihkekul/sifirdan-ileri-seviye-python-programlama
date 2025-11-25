import json

person_str = '{"name": "Semih", "PL":["C++", "Python"]}'

loaded_str = json.loads(person_str)

print(loaded_str["name"])
# Semih

person_dict = {"name": "Ali", "PL":["Scala, R"]}

print(json.dumps(person_dict, indent=4))
'''
{
    "name": "Ali",
    "PL": [
        "Scala, R"
    ]
}
'''