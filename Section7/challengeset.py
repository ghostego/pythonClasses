
vowels = {"a", "e", "i", "o", "u"}
# vowels = frozenset("aeiou")

while True:
	check_string = set(input("Enter a string "))
	# final_set = set(check_string).difference(vowels)
	check_string.difference_update(vowels)
	# print(final_set)
	# finalList = sorted(final_set)
	print(sorted(check_string))
	# print(finalList)