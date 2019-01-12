import json

with open('data.json', 'rt') as file:
    file_contents = json.load(file) # now file is a dictionary 

print(file_contents['friends'][0])

cars = [
    {'make': 'Ford', 'model': 'Fiesta'}, 
    {'make': 'Ford', 'model': 'Focus'}, 
]

# use json.dump
with open('cars_json.txt', 'wt') as new_file:
    json.dump(cars, new_file)

# my_json_string 
my_json_string = '[{"name": "Alfa Romeo", "released": 1950}]'
incorrect_car = json.loads(my_json_string)
print(incorrect_car[0]['name'])

# with json, you can use lists and dictionaries only - NO TUPLES!!
