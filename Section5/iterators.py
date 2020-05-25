string = "1234567890"

for char in string:
    print(char)

my_iterator = iter(string)

# for loops automatically uses iter(string) syntax behind the scenes
print(my_iterator)
# the next function gets the next iteratotor
print(next(my_iterator))
print(next(my_iterator))