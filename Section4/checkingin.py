parrot = "Norwegian Blue"

letter = input("Enter a character: ")

# in is case sensitive, 'Blue' is contained within Norwegian Blue,
# but 'blue' is not
if letter in parrot:
    print("{} is in {}".format(letter, parrot))
else:
    print("I dont need that letter")

