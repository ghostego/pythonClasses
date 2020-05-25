activity = input("What would you like to do today? ")

# the casefold function converts a string to lowercase
if "cinema" not in activity.casefold():
    print("But I want to go to the cinema")