# 3-8 Seeing the World

bucketlist = ['Mississippi', 'San Francisco', 'Hawaii', 'New York', 'Disney World', 'Anartica', 'Alaska',
              'Africa', 'Italy', 'Bahamas', 'Australia', 'California', 'North Pole', 'Metropolis', 'Utah', 'England']

# Loop for vertical list reversed
# for i in reversed(bucketlist):
#    print(i)

print("\nPrints list alphabetically & shows original list")
print(f"{bucketlist}")
print(f"{sorted(bucketlist)}")
print(f"{bucketlist}\n\n")

print("Prints list in reverse alphabetical order & shows original list")
print(f"{bucketlist}")
print(f"{sorted(bucketlist, reverse=True)}")
print(f"{bucketlist}\n\n")

print("Prints list in reverse order & shows changed list")
print(f"{bucketlist}")
bucketlist.reverse()
print(f"{bucketlist}\n\n")

print("Prints list in reverse order & restores list back to original order")
print(f"{bucketlist}")
bucketlist.reverse()
print(f"{bucketlist}\n\n")

print("Prints list in reverse order & restores original list another way")
print(f"{bucketlist}")
print(list(reversed(bucketlist)))
print(f"{bucketlist}\n\n")

print("Sorts and stores list in alphabetical order")
print(f"{bucketlist}")
bucketlist.sort()
print(f"{bucketlist}")
print(f"{bucketlist}\n\n")

print("Sorts and stores list in reverse alphabetical order")
print(f"{bucketlist}")
bucketlist.sort(reverse=True)
print(f"{bucketlist}")
print(f"{bucketlist}\n\n")
