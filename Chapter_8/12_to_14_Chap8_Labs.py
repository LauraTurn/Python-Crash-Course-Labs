print("\n8-12 Sandwiches")
print("\nPassing a List")

def make_sandwich(toppings):
    print("\nSandwich Toppings Ordered:")
    for topping in toppings:
        order = f"\t{topping.title()}"
        print(order)

sandwich = ['lettuce', 'tomato', 'turkey', 'ham', 'cheddar cheese']
make_sandwich(sandwich)

sandwich = ['peanut butter', 'strawberry jelly']
make_sandwich(sandwich)

sandwich = ['chalk', 'alligator meat', 'tortise shells', 'hats', 'photographs', 'paper']
make_sandwich(sandwich)


print("\n\n8-13 User Profile")
print("\nReturning a Dictionary\n")

def build_profile(first, last, city, marital_status, employed):
    """Build a dictionary containing everything we know about a user."""
    person = {'first': first, 'last': last, 'location': city, 'married?': marital_status, 'employed?': employed}
    return person

user_profile = build_profile('laura', 'lynn', 'lapeer', 'single', 'yes')
print(user_profile)


print("\n\n8-14 Cars")
print("Using Arbitrary Keyword Arguments")

def build_car(manufacturer, model, **car_info):
    """Build a dictionary containing everything we know about a user."""
    car_info['make'] = manufacturer
    car_info['model'] = model
    return car_info

car_profile = build_car('ford', 'escape',
                        mileage=47000,
                        automatic='yes',
                        color='red')

print(car_profile)
print()
