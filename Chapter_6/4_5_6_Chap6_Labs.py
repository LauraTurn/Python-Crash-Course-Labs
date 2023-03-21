print("\n6-4 Glossary Dictionary Part 2\n")

glossary = {
    'dictionary': 'A collection of key-value pairs',
    'if-elif-else syntax': 'Used to test more than 2 situations',
    'key': 'Number, string, list, or dictionary connected to a value',
    'keys method': 'Returns list of keys & can be used to check a dictionary for specific key',
    'key-value pair': 'A set of values associated with each other',
    'none': 'A special value meaning "No values exist"',
    'range function': 'Used within a list to include all numbers between',
    'set': 'A collection in which each item must be unique (no repetition)',
    'sorted function': 'Used to list keys in a particular order',
    'value': 'The contents of a key'
}

for terms, definitions in glossary.items():
    print(f"{terms.title()}:\n\t{definitions}")

print("\n6-5 Rivers\n")

world_rivers = {
    'nile': 'egypt',
    'amazon': 'south america',
    'yangtze': 'china'
}

for river, location in world_rivers.items():
    print(f" The {river.title()} River flows through {location.title()}.")
print()

for river in world_rivers.keys():
    print(river.title())
print()

for location in world_rivers.values():
    print(location.title())

print("\n6-6 Polling\n")

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'nate': 'c#',
    'ava': 'f#'
    }

people = ['mike', 'jen', 'tina', 'sarah', 'loretta', 'ava']

for pollers in favorite_languages:
    if pollers in people:
        print(f"{pollers.title()}, thank you for taking the poll.")
    else:
        print(f"{pollers.title()}, please remember to take the poll!")
print()
