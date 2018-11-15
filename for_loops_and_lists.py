# Basic For Loop Syntax
# for i in range(1, 10):
#     print i

# # The third number is the "step" (how much it increments by)
# for i in range(1, 10, 2):
#     print i

# # Lists!

# student1 = "Brian"
# student2 = "Brandon"
# student3 = "Zac"

# OR:

# students = ["Brian", "Brandon", "Zac"]
# print students[0]
# print students[-1]

# teams = [["Falcons", "Panthers", "Saints", "Bucs"], ["Bills", "Dolphins", "49ers"]]
# print teams
# print teams[0]
# print teams[0][0]

# num_of_students = len(students)
# for i in range(0, num_of_students):
#     print "Welcome to class, %s" % students[i]

atlanta_teams = []
atlanta_teams.append("Falcons") # .append() adds an item to the END of the list.
atlanta_teams.append("Braves")
atlanta_teams.append("Hawks")
atlanta_teams.append("Thrashers")

atlanta_teams.pop() # .pop() will remove last item in a list, .pop(2) (or whatever number, will remove item at that index)
atlanta_teams.pop(2)

atlanta_teams.insert(2, "United") # .insert(index, item) inserts an item in a list at the index declared

atlanta_teams.sort() # .sort() is a mutating method, and changes the order; alphabetical, or whatever. 
# you can also used sorted(list_name) to create a sorted list and store in a new array, but not change the original list.

atlanta_teams.reverse() # sorts in reverse order!

# If you have a string and you want to split it into a list... split! Split expects a "delimiter".
# It's what you want split to look for. Each time it finds it, it will create a new element!
reindeer = "Dasher, Dancer, Prancer, Vixen"
reindeer_as_a_list = reindeer.split(', ')
print reindeer_as_a_list

# If you want part of a list, you use [x:y] This will create a copy of the array. It will not mutate the original.
# It will start copying at the x index, and will stop at the y. You begin with the index you want, and stop one index after.

dancerPrancer = reindeer_as_a_list[1:3]

print dancerPrancer



