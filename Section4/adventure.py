available_exits = ["north", "south", "east", " west"]

chosen_exit = ""
while chosen_exit not in available_exits:
    chosen_exit = input("Please choose a direction: ")
    if chosen_exit.casefold() == "quit":
        print("Game over")
        break
else: # else in this case happens when you complete a loop without breaking out of it
    print("Aren't you glad you escaped?")