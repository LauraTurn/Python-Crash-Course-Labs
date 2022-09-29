print("")
print("4-3 Counting to Twenty")
print("Loop to print numbers 1-20")
for value in range(1, 21):
    print(value)
print("")

# print("Loop to add numbers 1 to one million to list & print")
# print("4-4 One Million")
# million = []
# for value in range(1, 1000000001):
#     million.append(value)
# print(million)
# print("")

# print("4-5 Summing to a Million")
# print("Loop to print simple statistics & add numbers 1 to one million")
# million = []
# for value in range(1, 1000000001):
#     million.append(value)
# print(f"Min number: {min(million)}")
# print(f"Max number: {max(million)}")
# print(f"Sum of all: {sum(million)}")
# print("")

print("4-5 Odd Numbers")
odd_numbers = list(range(1, 21, 2))
print(odd_numbers)
print("")

print("4-5 Threes")
third_numbers = []
for thirds in range(3, 31, 3):
    third_numbers.append(thirds)
print(third_numbers)
print("")

print("4-5 Cubes")
cubes = []
for numeral in range(1, 10):
    cubes.append(numeral**3)
print(cubes)
print("")

print("4-5 Cube Comprehension: Cubes Concisely")
cubes = [cubes**3 for cubes in range(1, 10)]
print(cubes)
print("")
