print("\n5-3 Alien Colors #1")
alien_color = 'green'
print(f"The alien you shot is {alien_color}")
if alien_color == 'green':
    print("The alien is green.  Score: +5 points\n")

alien_color = 'red'
print(f"The alien you shot is {alien_color}")
if alien_color == 'green':
    print("\nThe alien is green.  Score: +5 points")
# No output

print("\n5-4 Alien Colors #2")
alien_color = 'yellow'
print(f"The alien you shot is {alien_color}")
if alien_color == 'green':
    print("The alien is green.  Score: +5 points")
else:
    print("The alien is not green.  Score: +10 points")

print("\n5-5 Alien Colors #3")
alien_color = 'green'
if alien_color == 'green':
    score = 5
elif alien_color == 'yellow':
    score = 10
else:
    score = 15
print(f"The alien you shot is {alien_color}")
print(f"Score: +{score} points.\n")

alien_color = 'yellow'
if alien_color == 'green':
    score = 5
elif alien_color == 'yellow':
    score = 10
else:
    score = 15
print(f"The alien you shot is {alien_color}")
print(f"Score: +{score} points.\n")

alien_color = 'red'
if alien_color == 'green':
    score = 5
elif alien_color == 'yellow':
    score = 10
else:
    score = 15

print(f"The alien you shot is {alien_color}")
print(f"Score: +{score} points.\n")
