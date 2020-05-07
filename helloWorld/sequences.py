# A sequence is defined as an ordered set of items
# The string "Hello World" contains 11 items, each is a character
# A list of strings is a sequence.
# A sequence seems like an array.
# Not all sequence types can be concatenated

string1     =   "he's "
string2     =   "probably "
string3     =   "pining "
string4     =   "for the "
string5     =   "fjords"

print(string1 + string2 + string3 + string4 + string5)
print("he's " "probably " "pining " "for the " "fjords")

print("Helo " * 5)

print("Helo " * (5 + 4))
print("Helo " * 5 + "4")

# to check for a substring
today = "friday"
print("day" in today)       # True
print("fri" in today)       # True
print("thur" in today)      # False
print("parrot" in "fjord")  # False