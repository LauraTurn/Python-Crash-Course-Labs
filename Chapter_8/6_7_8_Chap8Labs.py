print("\n8-6 City Name")
print("Returning a Simple Value\n")

def city_country(city_name, country_name):
    """Return information about a city"""
    location = f"{city_name}, {country_name}"
    return location.title()

place = city_country('paris', 'france')
print(place)

place = city_country('london', 'england')
print(place)

place = city_country('rome', 'italy')
print(place)


print("\n\n8-7 Album")
print("Returning a Dictionary\n")

def make_album(artist_name, album_title, tracks=None):
    album = {'artist': artist_name, 'album': album_title}
    if tracks:
        album['tracks'] = tracks
    return album

music = make_album('prince', 'purple rain')
print(music)

music = make_album('madonna', 'the immaculate collection')
print(music)

music = make_album('cher', 'heart of stone')
print(music)

music = make_album('britney spears', 'britney', tracks=15)
print(music)


print("\n\n8-8 User Albums")
print("Using a Function with a While Loop")

def make_new_album(artist_name, album_title, tracks=None):
    album = {'artist': artist_name, 'album': album_title}
    if tracks:
        album['tracks'] = tracks
    return album

while True:
    print("\nPlease give me some album information.")
    print("Enter 'q' at any time to quit.")
    a_name = input("Artist Name: ")
    if a_name == 'q':
        break
    a_title = input("Album Title: ")
    if a_title == 'q':
        break

    album_info = make_new_album(a_name, a_title)
    print(f"I have never heard {a_title.title()} by {a_name.title()} before!")

print("Thanks for talking music with me. Goodbye!")
print()
