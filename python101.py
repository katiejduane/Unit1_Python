print "Hello World"
print """
It was a dark and stormy night.
It was a good second line.
"""

# Variables: strings, letters, numbers, or any other stuff you can make with a keyboard!
# Variables do not make the program faster; they make it slower. 
# Variables make it easier for us (developers) to wrtie programs.

theBestClass = "our class"
the_best_class = "our class"

print theBestClass

# "\n" = new line!

# Data Types: Programming languages see different types of variables differently. 
# - Strings: English stuff
# - Numbers: integers/floats
# - Booleans: True or False, on or off, 1 or 0
# - Lists: list of things in one variable
# - Dictionaries: variable of variables
# - Objects: Super Dictionaries!

# Primitive Data Types; Strings, numbers ,booleans
# Abstract Data Types: Lists, Dictionaries, Objects

month = "November"
print type(month)
date = 13
print type(date)
date1 = 13.0
print type(date1)
abool = True
print type(abool)
aList = []
print type(aList)
aDict = {}
print type(aDict)

# Concatenate is programming speak for adding things together!
first = "Katie "
last = "Duane"
print first + last
fullName = first + last
print fullName

# cast = change a variable to a new data type

# OPERANTS: +, -, /, *, %, **
print 2 + 2
print 2 - 2
print 2 / 2
print 2 * 2
print 2 % 2
# % = modulus. Modulus divides the number and gives you a remainder.
print 2**3
print "-" * 20 #(* can be used to duplicate non-numbers)
# Python does not have a simple incrementers: ++ 
# You must increment by += 1
