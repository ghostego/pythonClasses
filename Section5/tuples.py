t = "a", "b", "c"
print(t)                # prints: ('a', 'b', 'c')

print("a", "b", "c")    # prints: 'a', 'b', 'c'
print(("a", "b", "c"))  #to print a tuple, you need second sets of parenthesis, prints: ('a', 'b', 'c')

welcome = "Welcome to my nightmare", "Alice Cooper", 1975
bad = "Bad Company", "Bad Company", 1974
budgie = "Night Flight", "Budgie", 1981
imelda = "More Mayhem", "Emilda May", 2011, (1, "Pulling the Rug"), (2, "Psycho"),(3, "Mayhem"),(4, "Kentish Town Waltz")

metallica = "Ride the Lightning", "Metallica", 1984
print(imelda)
title, artist, year, track1, track2, track3, track4 = imelda
print(title)
print(artist)
print(year)
print(track1)
print(track2)
print(track3)
print(track4)

# print(imelda)

# print(metallica)
# print(metallica[0])
# print(metallica[1])
# print(metallica[2])

# # metallica[0] = "Master of Puppets" # We cant do this, tuples are immutable

# # you can do this though
# imelda = imelda[0], "Imelda May", imelda[2]
# print(imelda)

# # Lists are mutable objects
# metallica2 = ["Ride the Lightning", "Metallica", 1984]
# print(metallica2)
# # so this syntax works
# metallica2[0] = "Master of Puppets"
# print(metallica2)

# # unpacking the tuple, using the syntax will go in order on the object
# title, artist, year = imelda
# print(title)    # More Mayhem
# print(artist)   # Imelda May
# print(year)     # 2011

# metallica2.append("Rock") 
# title2, artist2, year2 = metallica2     # this will give an error as we added a fourth item to this list but only 3 vars   
# print(title2)
# print(artist2)
# print(year2)