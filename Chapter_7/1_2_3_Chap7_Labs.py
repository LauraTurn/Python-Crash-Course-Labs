print("\n7-1 Rental Car\n")

car_type = input("What type of car would you like to rent? ")

print(f"Let me see if I can find you a {car_type.title()}!\n")


print("\n7-2 Restaurant Seating\n")

guests = input("Please enter the number of people in your dinner group: ")
guests = int(guests)

if guests >= 8:
    print("I'm sorry, you will have to wait for a table to accomodate your party...\n")
else:
    print("Your table is ready!\n")


print("\n7-3 Multiples of 10\n")

number = input("Enter a number and I will tell you if it's a multiple of 10: ")
number = int(number)

if number % 10 == 0:
    print(f"\nThe number {number} IS a multiple of 10.")
else:
    print(f"\nThe number {number} is NOT a multiple of 10.")
print()
