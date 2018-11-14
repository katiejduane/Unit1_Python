# secret_number = 5

# if (secret_number == 3):
#     print "Secret number is 3"
# else:
#     print "Secret number is not 3."

# WHILE LOOPS:
# game_on = True;
# i = 0
# while(game_on):
#     i += 1
#     if (i == 10):
#         game_on = False;
#     else:
#         print "Game on!"

# Python Exercises: Guess a Number!
# secret_number = 5
# print "I am thinking of a number from 1 to 10."
# user_guess = 0
# while user_guess != secret_number:
#     user_guess = int(raw_input("What is the number? "))
#     if (user_guess == secret_number):
#         print "You win!"
#     else:
#         print "Wrong number"

# secret_number = 5
# print "I am thinking of a number from 1 to 10."
# user_guess = 0
# while user_guess != secret_number:
#     user_guess = int(raw_input("What is the number? "))
#     if (user_guess < secret_number):
#         print "%i is  too low" % user_guess
#     elif (user_guess > secret_number):
#         print "%i is too high" % user_guess
#     else:
#         print "You win!"


# THIS IS THE ONE THAT HAD THE INFINITE LOOPING ISSUE!!!
# import random
# my_random_number = random.randint(1, 10)
# print "I am thinking of a number from 1 to 10. You have 5 guesses left!"
# user_guess = 0
# guesses_taken = 0

# while guesses_taken < 6:
#     print "Take a guess!"
#     user_guess = int(raw_input("What is the number?"))
#     guesses_taken = guesses_taken + 1
#     while user_guess != my_random_number:
#         if (user_guess < my_random_number):
#             print "%i is  too low" % user_guess
#         elif (user_guess > my_random_number):
#             print "%i is too high" % user_guess
#         else:
#             break
#     if (user_guess == my_random_number):
#         print "You guessed it!"
#     else:
#         print "Sorry, you didn't get it!"

import random
my_random_number = random.randint(1, 10)

user_guess = 0
guesses_taken = 0

print "I am thinking of a number from 1 to 10. You have 5 guesses left!"

while guesses_taken < 6:
    user_guess = int(raw_input("What is the number? "))

    guesses_taken = guesses_taken + 1
    guesses_left = 6 - guesses_taken

    if (user_guess < my_random_number):
        print "Your guess is too low. You have %i guesses left" % guesses_left

    if (user_guess > my_random_number):
        print "Your guess is too high. You have %i guesses left" % guesses_left

    if (user_guess == my_random_number):
        break

if (user_guess == my_random_number):
    print "You guessed it!"
else:
    print "Sorry, you didn't get it!"
