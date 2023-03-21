print("\n6-1 Person Dictionary\n")

favorite_person = {
    'first_name': 'Harry',
    'last_name': 'Potter',
    'age': '11',
    'city': 'London'
}

fp_fname = favorite_person.get('first_name')
fp_lname = favorite_person.get('last_name')
fp_age = favorite_person.get('age')
fp_city = favorite_person.get('city')

print(fp_fname)
print(fp_lname)
print(fp_age)
print(fp_city)

print("\n6-2 Favorite Numbers Dictionary\n")

favorite_numbers = {
    'loretta': '1',
    'audrey': '55',
    'nate': '11',
    'ava': '77',
    'ryan': '66'
}

print(favorite_numbers)

print("\n6-3 Glossary Dictionary\n")

glossary = {
    'dictionary': 'A collection of key-value pairs',
    'key': 'Number, string, list, or dictionary connected to a value',
    'key-value pair': 'A set of values associated with each other',
    'none': 'A special value meaning "No values exist"',
    'value': 'The contents of a key'
}

print(glossary)

def1 = glossary['dictionary']
def2 = glossary['key']
def3 = glossary['key-value pair']
def4 = glossary['none']
def5 = glossary['value']

print("\nPython Glossary")
print(f"==========")
print(f"Dictionary:\n\t{def1}")
print(f"Key:\n\t{def2}")
print(f"Key-Value Pair:\n\t{def3}")
print(f"None:\n\t{def4}")
print(f"Value:\n\t{def5}\n")
