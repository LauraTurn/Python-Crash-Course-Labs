print("\n5-8 Hello Admin")
username = ['admin', 'jerseykid', 'freaksngeeks', 'pulleyshore', 'krazyate']
for user in username:
    if user == 'admin':
        print(f"Hello {user.title()}, would you like to see a status report?")
    else:
        print(f"Hello {user.title()}, thank you for logging in again.")

print("\n5-9 No Users")
username = []
if user in username:
    for user in username:
        if user == 'admin':
            print(f"Hello {user.title()}, would you like to see a status report?")
        else:
            print(f"Hello {user.title()}, thank you for logging in again.")
else:
    print("We need to find some users!")

print("\n5-10 Checking Usernames")
current_users = ['sk8bored', 'funkychicken', 'cupidshuffle', 'PUGLYFE', 'staylisal']
new_users = ['sk8bored', 'puglyfe', 'pumpitup', 'jumpcity', 'fantasyforest']
current_users_lower = []
new_users_lower = []

for current in current_users:
    current_users_lower.append(current.lower())
print(f"Current Usernames: {current_users_lower}")
for new_user in new_users:
    new_users_lower.append(new_user.lower())
print(f"New Usernames: {new_users_lower}")

for new_user in new_users_lower:
    if new_user not in current_users_lower:
        print(f"Username {new_user} is totally available")
    else:
        print(f"The username {new_user} is already being used.  Please enter a unique username.")

print("\n5-1 Ordinal Numbers")
numerals = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for numeral in numerals:
    if numeral <= 1:
        digit = "1st"
    elif numeral == 2:
        digit = "2nd"
    elif numeral < 3:
        digit = "3rd"
    else:
        digit = f"{numeral}th"
    print(digit)




