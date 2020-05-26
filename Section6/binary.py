# for i in range(256):
#     print("{0:>2} in binary is {0:>08b} and {0:>02x} in hex".format(i))

# x = 0x20
# y = 0x0a
# print(x)
# print(y)
# print(x * y)

# print(0b00101010) #leading with 0b will print the following value in binary

powers = []
for power in range(15, -1, -1):
    powers.append(2 ** power)

x = int(input("gimme a number "))
printing = False

for power in powers:
    bit = x // power
    if bit != 0:
        printing = True
    if printing:
        print(bit, end='')
    x %= power