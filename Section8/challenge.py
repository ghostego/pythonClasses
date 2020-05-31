
with open("original.txt", "a") as jabber:
	for i in range(1, 13):
		print("{:2} times 2 is {}".format(i, i*2), file=jabber)


print('-'*40)