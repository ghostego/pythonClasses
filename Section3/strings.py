print("Today is a good day to learn python");
print('Python is fun');
print("Python's strings are easy to use");
print("We can even include \"quotes\" in strings");
greeting = "Hello";
name = input("Please enter your name ");

# if we want a space we can add that too
print(greeting + " " + name);

age = 24
print(age)

print(type(age))
print(type(greeting))

age_in_words = "2 years"
# F-strings are like Javascript es6 syntax, using the f in front of the string
print(name+f" is {age} years old")


print(f"Pi is approximately {22/7:12.50f}")