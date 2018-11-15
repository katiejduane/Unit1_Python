# LOOPS EXERCISES!

# 1-10
# for i in range(1, 11):
#     print i

# # N to M
# start = int(raw_input("Type a number to start: "))
# end = int(raw_input("Type a number to end: "))
# for i in range(start, end):
#     print i

# Odd Numberz
# for i in range (1, 10, 2):
#     print i

# # Print a square!
# length = 5 * " * "
# for i in range(1, 6):
#     print length

# #Print a box shape!
# dimension = int(raw_input("How many inches wide is the box? "))
# width = dimension * " * "
# for i in range (1, dimension + 1):
#     print width

#Hollow Box
box_width = int(raw_input("What's the box's width? "))
box_height = int(raw_input("What's the box's height? "))
space = " "

for i in range(box_height):
    if (i == 0 or i == box_height - 1):
        print box_width * "*"
    else:
        print '*' + space * (box_width - 2) + "*"

# Triangle 1: this isn't right because it's not "centered"
x = 1
n = 4
while (x <= n):
    print("*" * x)
    x = x + 1
#I know it has to always be 7 "characters" wide, with different numbers of empty spaces and asterisks...



