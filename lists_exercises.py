# Playlist:
# animals = ["fox", "bear", "puma"]
# for i in animals:
#     print i

# Sum of numbers:
my_numbers = [1, 2, 3, 4, 5]
print sum(my_numbers) #is it cheating to use the sum() module?

# Largest Number
print max(my_numbers)

# Smallest Number
print min(my_numbers)

# Even Numbers
long_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(len(long_list)):
    if (long_list[i] % 2 == 0):
        print long_list[i],

#Positive Numbers
pos_negs = [-2, -1, 0, 1, 2]
for i in pos_negs:
    if (i > 0):
        print i

# Positive Numbers 2
pos_negs = [-2, -1, 0, 1, 2]
pos_numbers = []
for i in pos_negs:
    if (i > 0):
        pos_numbers.append([i])
print pos_numbers

# Multiply a list
list_to_mult = [1, 2, 3]
factor = 2
multiplied = [x * factor for x in list_to_mult]
print multiplied

# Multiply Vectors:
# [a*b for a,b in zip(lista,listb)
nums_1 = [1, 2, 3]
nums_2 = [3, 2 ,1]
result = [a * b for a, b in zip(nums_1, nums_2)]
print result



