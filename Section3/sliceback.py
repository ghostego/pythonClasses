#					 01234567890123456789012345
letters = "abcdefghijklmnopqrstuvwxyz"

backwards = letters[25::-1]
backwards = letters[::-1] # this is an idiom in python, ::-1 
print(backwards)

qpo = letters[16:13:-1]
print(qpo)

edcba = letters[4::-1]
print(edcba)

back8 = letters[:17:-1]
print(back8)

print(letters[-4:]) # wxyz, gets the last 4 items
print(letters[-1:]) # z, gets the last item
print(letters[:1]) # a, gets the first item, doesn't return an error if letters is empty
print(letters[0])