name = input("What is your name? ")
age = int(input("How old are you? "))

if 18 <= age < 31:
    print("Welcome {}, you are {} years old which means you can come in!".format(name, age))
else:
    print("{}, I am going to have to ask you to leave. Don't make me call security".format(name))