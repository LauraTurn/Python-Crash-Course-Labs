# 3-10 Write a program to create a list and execute each function in the chapter

# Adds items to an empty list
groceries = []
groceries.append('popcorn')
groceries.append('salt')
groceries.append('toothpaste')
groceries.append('laundry detergent')
groceries.append('tuna')
groceries.append('bread')
groceries.append('butter')
groceries.append('frozen goodies')
groceries.append('dryer sheets')
groceries.append('eggs')
print(f"\nGrocery List: \n{groceries}")
print(f"I can't forget to get {groceries[0]} for Ava.\n")

# Prints pretty list
print("Nice looking grocery list:")
print(f"{groceries[0].title()}")
print(f"{groceries[1].title()}")
print(f"{groceries[2].title()}")
print(f"{groceries[3].title()}")
print(f"{groceries[4].title()}")
print(f"{groceries[5].title()}")
print(f"{groceries[6].title()}")
print(f"{groceries[7].title()}")
print(f"{groceries[8].title()}")
print(f"{groceries[9].title()}\n")

# Replaces last item in list
grocery_list = ['popcorn', 'salt', 'toothpaste', 'laundry detergent', 'tuna', 'bread', 'butter', 'frozen goodies',
                'dryer sheets', 'eggs']
print(f"Original: {grocery_list}")
grocery_list[-1] = 'milk'
print(f"Replace last item: {grocery_list}")
print(f"Total grocery items: {len(grocery_list)}\n")

# Adds to end of list
print(f"Original: {grocery_list}")
grocery_list.append('eggs')
grocery_list.append('cheese')
grocery_list.append('more cheese')
print(f"With added items: {grocery_list}")
print(f"Total grocery items: {len(grocery_list)}\n")

# Inserts item at beginning of list
print(f"Original: {grocery_list}")
grocery_list.insert(0, 'cheese?')
print(f"Added beginning item: {grocery_list}")
print(f"Total grocery items: {len(grocery_list)}\n")

# Deletes first item
print(f"Original: {grocery_list}")
del grocery_list[0]
print(f"Remove first item: {grocery_list}")
print(f"Total grocery items: {len(grocery_list)}\n")

# Deletes third item
print(f"Original: {grocery_list}")
del grocery_list[2]
print(f"Remove 3rd item: {grocery_list}")
print(f"Total grocery items: {len(grocery_list)}\n")

# Popping an item
print(f"Original: {grocery_list}")
last_added = grocery_list.pop()
print(f"You don't need {last_added.title()}, seriously.")
print(f"Popped: {grocery_list}")
print(f"Total grocery items: {len(grocery_list)}\n")

# Popping an item by position from a list
print(f"Original: {grocery_list}")
by_position = grocery_list.pop(3)
print(f"Popped by position: {grocery_list}")
print(f"Total grocery items: {len(grocery_list)}\n")

# Removing an item by value
print(f"Original: {grocery_list}")
enough = 'dryer sheets'
grocery_list.remove(enough)
print(f"You have enough {enough}.  You don't need any more.")
print(f"Popped by value: {grocery_list}")
print(f"Total grocery items: {len(grocery_list)}\n")

print("\nPrints list alphabetically & shows original list")
print(f"{grocery_list}")
print(f"{sorted(grocery_list)}")
print(f"{grocery_list}\n")

print("Prints list in reverse alphabetical order & restores list")
print(f"{grocery_list}")
print(f"{sorted(grocery_list, reverse=True)}")
print(f"{grocery_list}\n")

print("Prints list in reverse order & restores list another way")
print(f"{grocery_list}")
print(list(reversed(grocery_list)))
print(f"{grocery_list}\n")

print("Prints list in reverse order & shows changed list")
print(f"{grocery_list}")
grocery_list.reverse()
print(f"{grocery_list}\n")

print("Prints list in reverse order & restores list")
print(f"{grocery_list}")
grocery_list.reverse()
print(f"{grocery_list}\n")

print("Sorts and stores list in alphabetical order")
print(f"{grocery_list}")
grocery_list.sort()
print(f"{grocery_list}\n")

print("Sorts and stores list in reverse alphabetical order")
print(f"{grocery_list}")
grocery_list.sort(reverse=True)
print(f"{grocery_list}\n")

print("Sorts and restores list in alphabetical order")
print(f"{grocery_list}")
grocery_list.sort()
print(f"{grocery_list}\n")
