# 3-4 Create guest list and invite each person with a message

change_list = ['Truman Capote', 'Barack Obama', 'Oprah Winfrey', 'Hugo Reyes']
print(f"\nThe number of people invited to dinner: {len(change_list)}")
print(f"{change_list}")

print(f"{change_list[0]}, I know you are deceased but I would LOVE to have you over to dinner.")
print(f"{change_list[1]}, you are the only president on my dinner party invite list.")
print(f"{change_list[2]}, you are a wonderful role model for a woman like me.  Please come to my house for din-din.")
print(f"{change_list[3]}, because you are the coolest character on 'Lost', I need you at my dinner party!\n")

# 3-5 Start with the same list, print & replace the name of the guest who can't make it
print(f"The number of people invited to dinner: {len(change_list)}")
print(f"{change_list}")
print(f"{change_list[0]}, is terribly sorry he can't make it because he is deceased.\n")
change_list[0] = 'Bill Murray'

# Reprints invitations
print(f"{change_list[0]}, you are alive and funny.  Please come to my dinner party!")
print(f"{change_list[1]}, you are the only president on my dinner party invite list.")
print(f"{change_list[2]}, you are a wonderful role model for a woman like me.  Please come to my house for din-din.")
print(f"{change_list[3]}, because you are the coolest character on 'Lost', I need you at my dinner party!")
print(f"{change_list}\n")

# 3-6 Start with the same list, print table message
print(f"The number of people invited to dinner: {len(change_list)}")
print(f"{change_list}")
print(f"{change_list[0]}, {change_list[1]}, {change_list[2]}, & {change_list[3]}, guess who found a bigger table!")

# Add to beginning of list
change_list.insert(0, 'Kirsten Wiig')

# Add to middle of list
change_list.insert(3, 'Beyonce')

# Add to end of list
change_list.append('Robin Williams')
print(f"{change_list}\n")

# Print invitations for each person
print(f"The number of people invited to dinner: {len(change_list)}")
print(f"{change_list}")
print(f"{change_list[0]}, winner, winner, chicken dinner!")
print(f"{change_list[1]}, you are alive and funny.  Please come to my dinner party!")
print(f"{change_list[2]}, you are the only president on my dinner party invite list.")
print(f"{change_list[3]}, you are alive and funny.  Please come to my dinner party!")
print(f"{change_list[4]}, you are a wonderful role model for a woman like me.  Please come to my house for din-din.")
print(f"{change_list[5]}, because you are the coolest character on 'Lost', I need you at my dinner party!")
print(f"{change_list[6]}, you are SO missed.  Come to dinner.\n")

# 3-7 Shrinking Guest List
# Add a table message
print(f"The number of people invited to dinner: {len(change_list)}")
print(f"{change_list}")
print(f"Sorry everyone, I can only have 2 peeps at my dinner party!")

gotta_go = change_list.pop(3)
print(f"{gotta_go}, sorry, you are first to be UN-invited!")

gotta_go = change_list.pop(0)
print(f"{gotta_go}, sorry, you are UN-invited!")

gotta_go = change_list.pop(0)
print(f"{gotta_go}, sorry, you are UN-invited!")

gotta_go = change_list.pop()
print(f"{gotta_go}, sorry, you are UN-invited.")

gotta_go = change_list.pop(1)
print(f"{gotta_go}, sorry, you are UN-invited.\n")

print(f"The number of people invited to dinner: {len(change_list)}")
print(f"{change_list}")
print(f"{change_list[0]}, I cannot wait to meet you!")
print(f"{change_list[1]}, so excited to see this dinner party play out, brother!\n")

change_list.remove(change_list[0])
change_list.remove(change_list[0])
print(f"The number of people invited to dinner: {len(change_list)}")
print(f"{change_list}\n")
