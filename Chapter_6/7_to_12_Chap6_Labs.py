print("\n6-7 People\n")

person_0 = {
    'first_name': 'Harry',
    'last_name': 'Potter',
    'age': '11',
    'city': 'Surrey'
}

person_1 = {
    'first_name': 'Hermione',
    'last_name': 'Granger',
    'age': '11',
    'city': 'London'
}

person_2 = {
    'first_name': 'Ron',
    'last_name': 'Weasley',
    'age': '11',
    'city': 'The Burrow'
}

people = [person_0, person_1, person_2]

for person in people:
    print(person)
print()


print("\n6-8 Pets\n")

pet1 = {
    'name': 'porky',
    'type': 'pig',
    'age': '4',
    'owner_name': 'granny'
}

pet2 = {
    'name': 'bugs',
    'type': 'rabbit',
    'age': '6',
    'owner_name': 'elmer'
}

pet3 = {
    'name': 'taz',
    'type': 'tazmanian devil',
    'age': '5',
    'owner_name': 'witch hazel'
}

pet4 = {
    'name': 'daffy',
    'type': 'duck',
    'age': '3',
    'owner_name': 'sylvester'
}

pets = [pet1, pet2, pet3, pet4]

for pet in pets:
    print(pet)
print()


print("\n6-9 Favorite Places")

favorite_places = {
    'calvin': ['space', 'woods', 'bedroom'],
    'hobbes': ['woods', 'sunshine'],
    'mom': ['living room', 'spa'],
    'dad': ['camping', 'work', 'garage']
}

for name, locations in favorite_places.items():
    print(f"\n{name.title()}'s favorite places are:")
    for location in locations:
        print(f"\t{location.title()}")
print()


print("\n6-10 Favorite Numbers")

favorite_numbers = {
    'loretta': ['0', '1'],
    'audrey': ['3', '44', '55'],
    'nate': ['7','11', '100'],
    'ava': ['6', '33', '49', '77'],
    'ryan': ['8','66', '666', '6666']
}

for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()}'s favorite numbers are:")
    for number in numbers:
        print(f"\t{number}")
print()


print("\n6-11 Cities\n")

cities = {
    'new york': {
        'state': 'new york',
        'population': '8,992,908',
        'nickname': 'the big apple'
        },
    'los angeles': {
        'state': 'california',
        'population': '3,930,586',
        'nickname': 'the city of angels'
        },
    'chicago': {
        'state': 'illinois',
        'population': '2,761,625',
        'nickname': 'the windy city'
    }
}

for city, city_facts in cities.items():
    state_location = city_facts['state']
    pop = city_facts['population']
    second_name = city_facts['nickname']

    print(f"{city.title()}")
    print(f"\tState: {state_location.title()}")
    print(f"\tPopulation: {pop}")
    print(f"\tNickname: {second_name.title()}\n")


print("\n6-12 Extensions\n")



print()