import json

file = open('data.json', 'r')
file_contents = json.load(file) # now file is a dictionary 
file.close() 

print(file_contents['friends'][0])

cars = [
        {'make': 'Ford', 'model': 'Fiesta'}, 
        {'make': 'Ford', 'model': 'Focus'}, 
]

# use json.dump
new_file = open('cars_json.txt', 'wt')
json.dump(cars, new_file)
new_file.close() 


# my_json_string 
my_json_string = '[{"name": "Alfa Romeo", "released": 1950}]'
incorrect_car = json.loads(my_json_string)
print(incorrect_car[0]['name'])

# with json, you can use lists and dictionaries only - NO TUPLES!!
