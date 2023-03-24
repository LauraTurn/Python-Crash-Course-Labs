print("\n8-1 Message")
print("Defining a Function\n")

def display_message():
    print("I am learning about python functions!")

display_message()


print("\n\n8-2 Favorite Book")
print("Passing Information to a Function\n")

def favorite_book(book):
    """Display a simple message."""
    print(f"Your favorite book is {book.title()}???")

favorite_book('harry potter')

print()