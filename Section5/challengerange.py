o = range(0, 100, 4)
print(o)        #printing a range will just return the range ->> "range(0, 100, 4)"
p = o[0:25:5]  #taking slices of the range will result in the line p = o[10:20:2] looking
                # at the steps of the original range, and multiplying each of our new values
                # by it
print(p)
for i in p:
    print(i)