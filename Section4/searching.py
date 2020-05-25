shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

item_to_find = "albatross"
found_at = None #roughly equivalent to null

# for index in range(6):
for index in range(len(shopping_list)):
    if shopping_list[index] == item_to_find:
        found_at = index
        break

# The actual way to do it
if item_to_find in shopping_list:
    fount_at = shopping_list.index(item_to_find)

if found_at is not None:
    print("Item found at position {}".format(found_at))
else:
    print("{} not found".format(item_to_find))
