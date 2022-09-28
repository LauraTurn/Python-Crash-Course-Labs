print("")
print("4-10 Slices")
my_foods = ['pizza', 'falafel', 'carrot cake', 'cannoli', 'seafood', 'fish tacos']
print("The first three items in the list are:")
print(my_foods[:3])

print("\nThree items from the middle of the list are:")
print(my_foods[2:5])

print("\nThe last three items in the list are:")
print(my_foods[-3:])
print("")
print("")

print("4-11 My Pizzas, Your Pizzas")
pizzas = ['hawaiian', 'extravaganza', 'spinach and feta', 'margherita']
friend_pizzas = pizzas[:]

pizzas.append('pepperoni')
friend_pizzas.append('anchovy')

print(f"My favorite pizzas are:")
for pizza in pizzas:
    print(pizza.title())
print("")
print(f"My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza.title())
print("")
print("")

print("4-12 More Loops")
my_foods = ['pizza', 'falafel', 'carrot cake', 'toast', 'seafood', 'fish tacos']
your_foods = my_foods[:]

my_foods.append('chicken')
your_foods.append('tuna')
your_foods.append('cannoli')
your_foods.append('chips')

print("My favorite foods are:")
for food in my_foods:
    print(food.title())
print("")

print("Your favorite foods are:")
for food in your_foods:
    print(food.title())
print("")
print("")

print("4-13 Buffet")
print("Looping Over a Tuple")
buffet_menu = ('ribs', 'pork chops', 'steak', 'ham', 'pasta')
for food in buffet_menu:
    print(food.title())
print("")

# # Throws error as item cannot be changed within the tuple
# buffet_menu[4] = 'cake'
# for food in buffet_menu:
#     print(food.title())
# print("")

print("Changing Variables & Looping Over Same Tuple")
buffet_menu = ('ribs', 'pork chops', 'steak', 'cakes', 'pies')
for food in buffet_menu:
    print(food.title())
print("")
