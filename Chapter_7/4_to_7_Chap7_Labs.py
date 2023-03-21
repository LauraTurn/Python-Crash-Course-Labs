print("\n7-4 Pizza Toppings")

prompt = "\nPlease enter a topping you would like on your pizza."
prompt += "\nEnter 'done' when your pizza order is done. Topping to add: "

active = True
while active:
    topping = input(prompt)

    if topping == 'done':
        active = False
    else:
        print(f"\nAdding {topping.title()} to your pizza!")

print("\n\tIf that is all the toppings you would like, we will start making your pizza now!")
print()


print("\n7-5 Movie Tickets\n")

age = input("Thank you for coming to Lapeer Cinema. May I ask how old you are? ")
age = int(age)

while age > 0:
    if age < 4:
        print("\nYour movie ticket is free!")
        break
    elif age < 13:
        print("\nYour movie ticket is $10, please.")
        break
    else:
        print("\nYour movie ticket is $15, please.")
        break

print("\n\tEnjoy the show!")
print()


print("\n7-6 Three Exits\n")

print("This exercise is modifying the 2 above which I have already done.")

print()


print("\n7-7 Infinity\n")

# Write a While Loop that that never ends.  Type Ctl-C to exit.
age = input("Thank you for coming to Lapeer Cinema. May I ask how old you are? ")
age = int(age)

while age > 0:
    if age < 4:
        print("\nYour movie ticket is free!")
    elif age < 13:
        print("\nYour movie ticket is $10, please.")
    else:
        print("\nYour movie ticket is $15, please.")

print("\n\tEnjoy the show!")
print()

print()
