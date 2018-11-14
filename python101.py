# print "Hello World"
# print """
# It was a dark and stormy night.
# It was a good second line.
# """

# # Variables: strings, letters, numbers, or any other stuff you can make with a keyboard!
# # Variables do not make the program faster; they make it slower. 
# # Variables make it easier for us (developers) to wrtie programs.

# theBestClass = "our class"
# the_best_class = "our class"

# print theBestClass

# # "\n" = new line!

# # Data Types: Programming languages see different types of variables differently. 
# # - Strings: English stuff
# # - Numbers: integers/floats
# # - Booleans: True or False, on or off, 1 or 0
# # - Lists: list of things in one variable
# # - Dictionaries: variable of variables
# # - Objects: Super Dictionaries!

# # Primitive Data Types; Strings, numbers ,booleans
# # Abstract Data Types: Lists, Dictionaries, Objects

# month = "November"
# print type(month)
# date = 13
# print type(date)
# date1 = 13.0
# print type(date1)
# abool = True
# print type(abool)
# aList = []
# print type(aList)
# aDict = {}
# print type(aDict)

# # Concatenate is programming speak for adding things together!
# first = "Katie "
# last = "Duane"
# print first + last
# fullName = first + last
# print fullName

# # cast = change a variable to a new data type

# # OPERANTS: +, -, /, *, %, **
# print 2 + 2
# print 2 - 2
# print 2 / 2
# print 2 * 2
# print 2 % 2
# # % = modulus. Modulus divides the number and gives you a remainder.
# print 2**3
# print "-" * 20 #(* can be used to duplicate non-numbers)
# Python does not have a simple incrementers: ++ 
# You must increment by += 1
# Input: raw_input
# name = raw_input("What is your name? ")
# print name

# CONDITIONALS:
# a single = means set the left to whatever is on tbe right
# Two == means compare whatever is on the left to what is on the right
# print 2 == 2
# print 2 == 3

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
