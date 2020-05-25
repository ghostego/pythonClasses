import random

highest = 10
answer = random.randint(1, highest)

print("Please guess a number between 1 and {}: ".format(highest))
guess = int(input())

while guess:
    if guess == answer:
        print("Wow, you got it!")
        break
    if guess < answer:
        print("Please guess higher")
    else:
        print("Please guess lower")

    guess = int(input())

    

# else:
#     if guess < answer:
#         print("Please guess higher")
#     else:
#         print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print('Well done, you guessed it')
#     else:
#         print("Sorry, you have not guessed correctly")

# if guess < answer:
#     print("Please guess higher")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it!")
#     else:
#         print("Oof, you beaned it")
# elif guess > answer:
#     print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it!")
#     else:
#         print("Oof, you beaned it")
# else:
#     print("Wow you did it")