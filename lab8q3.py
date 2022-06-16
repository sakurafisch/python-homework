import json
with open('pets.json') as file:
    pets = json.load(file)
    print(pets)
