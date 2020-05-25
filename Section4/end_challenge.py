option_list = ["1. Learn Python", "2. Learn Java", "3. Go swimming", "4. Have dinner"]

while True:
    choice = int(input("Please choose your option from the list below: \n {} \n {} \n {} \n {} ".format(option_list[0],option_list[1], option_list[2], option_list[3])))
    option_length = len(option_list)
    print(option_length)

    if choice == 0:
        print("Goodbye!")
        break
    elif choice > option_length:
        print("{} is not a valid choice".format(choice))
    elif choice:
        index_choice = choice - 1
        print(option_list[index_choice])
