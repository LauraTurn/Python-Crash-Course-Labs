print("\n8-3 T-Shirt")
print("Passing Arguments\n")

def make_shirt(shirt_size, shirt_text):
    """Display information about a t-shirt"""
    print(f"\nI would like to order a size {shirt_size.title()} shirt.")
    print(f"The message on my shirt should read: \"{shirt_text}\"")

make_shirt('large', 'Boy Mom')
make_shirt(shirt_text='Nope', shirt_size='x-large')


print(f"\n\n8-4 Large Shirts")

def make_shirt(shirt_size='large', shirt_text='I Love Python'):
    """Display information about a t-shirt"""
    print(f"\nI would like to order a size {shirt_size.title()} shirt.")
    print(f"The message on my shirt should read: \"{shirt_text}\"")

make_shirt()
make_shirt('medium')
make_shirt(shirt_text='Nope', shirt_size='x-large')


print(f"\n\n8-5 Cities")

def describe_city(city_name, count_name="canada"):
    """Display information about a city"""
    print(f"\nThe beautiful city of {city_name.title()} is in {count_name.title()}.")

describe_city('toronto')
describe_city('ottawa')
describe_city('moscow', 'germany')
print()
