print("\n7-8 Deli")
print("Moving Items from One List to Another\n")
# Removes items from a list and adds it to another list
# Prints a message for each list item as it is moved and then prints the new full list.

sandwich_orders = ['roast beef', 'ham and swiss', 'chicken salad', 'peanut butter and jelly', 'pastrami', 'turkey club', 'grilled cheese']
finished_sandwiches = []

print(f"\t{sandwich_orders}\n")

while sandwich_orders:
    in_the_works = sandwich_orders.pop()

    print(f"I made the {in_the_works} sandwich.")
    finished_sandwiches.append(in_the_works)

print("\nThe following sandwiches have been made:")
for finished_sandwiches in finished_sandwiches:
    print(f"\t{finished_sandwiches.title()}")


print("\n7-9 No Pastrami")
print("Removing All Instances of Specific Values fron a List\n")

print("Welcome to Sam's Sandwichs! I am sorry but we are out of pastrami today.\n")

sandwich_orders = ['pastrami','roast beef', 'pastrami','ham and swiss', 'pastrami','chicken salad',
                   'peanut butter and jelly', 'pastrami', 'turkey club', 'grilled cheese']
finished_sandwiches = []

print(f"\t{sandwich_orders}\n")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    in_the_works = sandwich_orders.pop()

    print(f"I made the {in_the_works} sandwich.")
    finished_sandwiches.append(in_the_works)

print("\nThe following sandwiches have been made:")
for finished_sandwiches in finished_sandwiches:
    print(f"\t{finished_sandwiches.title()}")


print("\n7-10 Dream Vacation")
print("Filling a Dictionary with User Input\n")

replies = {}
polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    reply = input("If you could visit one place in the world, where would you go? ")

    replies[name] = reply
    repeat = input("Would you like to let another person rely? (y/n) ")
    if repeat == 'n':
        polling_active = False

print("\n--- Poll Results ---")
for name, reply in replies.items():
    print(f"{name.title()} would like to visit {reply.title()} one day.")

print()
