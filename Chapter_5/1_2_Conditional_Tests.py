print("\n5-1 Conditional Tests")

champion = 'Harry Potter'
print("\nIs champion == 'Harry Potter'? I predict True.")
print(champion == 'Harry Potter')
print("Is character == 'Hermione Granger? I predict False.")
print(champion == 'Hermione Granger')

elf = 'Dobby'
print("\nIs elf == 'Dobby'? I predict True.")
print(elf == 'Dobby')
print("Is elf == 'Winky'? I predict False.")
print(elf == 'Winky')

headmaster = 'Dumbledore'
print("\nIs headmaster == 'Dumbledore'? I predict True.")
print(headmaster == 'Dumbledore')
print("Is headmaster == 'Flickwick'? I predict False.")
print(headmaster == 'Flickwick')

professor = 'McGonagall'
print("\nIs professor == 'McGonagall'? I predict True.")
print(professor == 'McGonagall')
print("Is professor == 'Filch'? I predict False.")
print(professor == 'Filch')
print("")

villain = 'Voldemort'
print("\nIs villain = 'Voldemort'? I predict True.")
print(villain == 'Voldemort')
print("Is villain = 'Snape'? I predict False.")
print(villain == 'Snape')

print("\n5-2 More Conditional Tests")
bad_guy = 'Malfoy'
if bad_guy != 'Goyle':
    print("Goyle didn't do it!")

if bad_guy == 'Malfoy':
    print("Malfoy wasn't all bad!\n")

bad_guys = ['Malfoy', 'Crabbe', 'Goyle', 'Riddle']
print("Which one is the worse?")
for bad_guy in bad_guys:
    if bad_guy == 'Riddle':
        print(bad_guy.upper())
    else:
        print(bad_guy.lower())

print("\nNumerical Tests")
age = 40
print("How old are you?")
if age != 21:
    print(age == 21)
    print("21? You ain't that young.  Nice try!")
if age == 40:
    print(age == 40)
    print("40. Now you're being honest.")

print("\nThere are 18 guests.")
guests = 18
print("Are there more than ten guests?")
print(guests > 10)
# True
guests = 40
print("Are there fewer guests than 40?")
print(guests < 25)
# False

print("Are there at least more than 15 guests?")
print(guests >= 15)
# True
print("Are there at least less than 25 guests")
print(guests <= 25)
# True

guests_0 = 50
guests_1 = 100
print("\nThere are 50 guests at the first party and 100 at the next.")
print("Does the first party have at least 50 guest and the second less than 150?")
print(f"{guests_0 >= 50 and guests_1 <= 150}")
# True
print("Does the first party have at less than 50 guest and the second less than 150?")
print(f"{guests_0 < 50 and guests_1 <= 150}")
# False

guests_2 = 10
guests_3 = 20
print("\nThere are 10 guests at the first party and 20 at the next.")
print("Does the first party have 10 guests or more OR the second more than 30?")
print(f"{guests_2 >= 10 or guests_3 > 30}")
# True
print("Does the first party have less than 5 guests OR the second more than 10?")
print(f"{guests_2 <= 5 or guests_3 <= 10}")
# False

print("Check if an item is in a list")
previous_passwords = ['Shinola123', 'Pizza44', 'Monkey11', 'Shark33']
new_password = 'Rocket77'
if new_password not in previous_passwords:
    print(f"\nYour password has been changed to: {new_password}")
new_password = 'Monkey11'
if new_password in previous_passwords:
    print(f"{new_password} has been used in the past. New passwords must be unique.\n")
