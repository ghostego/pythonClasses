shopping_list = ["milk", "pasta", "spam", "eggs", "bread", "rice"]

# for item in shopping_list:
#     if item != "spam":
#         print("Buy " + item)

# When 'continue' appears in a loop, it ignores the rest of the code in the function
for item in shopping_list:
    if item == "spam":
        break   # getting to break in a loop will stop the loop from continuing,
                # using continue will skip the code for this item
    print("Buy " + item) 