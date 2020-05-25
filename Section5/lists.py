# # ipAddress = input("Please enter an IP address ")
# # print(ipAddress.count("."))

# parrotList = ["non pinin'", "no more", "a stiff", "bereft of life"]

# parrotList.append("A norwegian blue")
# for state in parrotList:
#     print("This parrot is " + state)

# even = [2, 4, 6, 8]
# odd = [1, 3, 5, 7, 9]

# numbers = even + odd
# # numbers.sort()
# print(sorted(numbers))

# list_1 = []
# list_2 = list()

# print("List 1 is {}".format(list_1))
# print("List 2 is {}".format(list_2))

# if list_1 == list_2:
#     print("The lists are equal")
    
# print(list("The lists are equal"))

# even = [2,4,6,8]
# if you set a variable equal to another list, it will be pointing to the same spot in memory
# any updates you make to the new variable list will effect the original unless you call the 
# new list variable declration like new_list = list(old_list), or new_list = sorted(old_list)
# another_even = list(even)
# another_even.sort(reverse=True)
# print(even)

even = [2,4,6,8]
odd = [1,3,5,7,9]

numbers = [even, odd]

for num in numbers:
    print(num)
    for val in num:
        print(val)