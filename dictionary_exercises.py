# Given the following dictionary, representing a mapping from names to phone numbers:

# phonebook_dict = {
#   'Alice': '703-493-1834',
#   'Bob': '857-384-1234',
#   'Elizabeth': '484-584-2923'
# }
# # Write code to do the following:
# # Print Elizabeth's phone number.
# print phonebook_dict['Elizabeth']
# # Add a entry to the dictionary: Kareem's number is 938-489-1234.
# phonebook_dict['Kareem'] = '938-489-1234'
# # Delete Alice's phone entry.
# del phonebook_dict['Alice']
# # Change Bob's phone number to '968-345-2345'.
# phonebook_dict['Bob'] = '968-345-2345'
# # Print all the phone entries.
# print phonebook_dict

# # In this exercise, are you using dynamic keys or fixed keys?
# # Exercise 2: Nested Dictionaries
# ramit = {
#   'name': 'Ramit',
#   'email': 'ramit@gmail.com',
#   'interests': ['movies', 'tennis'],
#   'friends': [
#     {
#       'name': 'Jasmine',
#       'email': 'jasmine@yahoo.com',
#       'interests': ['photography', 'tennis']
#     },
#     {
#       'name': 'Jan',
#       'email': 'jan@hotmail.com',
#       'interests': ['movies', 'tv']
#     }
#   ]
# }

# # Write a python expression that gets the email address of Ramit.
# print ramit['email']
# # Write a python expression that gets the first of Ramit's interests.
# print ramit['interests'][0]
# # Write a python expression that gets the email address of Jasmine.
# print ramit['friends'][0]['email']
# # Write a python expression that gets the second of Jan's two interests.
# print ramit['friends'][1]['interests'][1]
# # In this exercise, are you using dynamic keys or fixed keys?
# answer = "I don't know"

# Letter Summary
# Write a letter_histogram function that takes a word as its input, 
# and returns a dictionary containing the tally of how many times each 
# letter in the alphabet was used in the word. For example:

# >>> letter_histogram('banana')
# {'a': 3, 'b': 1, 'n': 2}
# In this exercise, are you using dynamic keys or fixed keys?

# I need to...
# - turn the word into a list 
# - make an empty dictionary
# - count each letter in the list (should the count be saved to a variable? and the letters, too?)
# - create a dictionary with the letters (as keys) and the counts as corresponding values.


def letter_histogram(word):
  count_dict = {}
  # for letter in word:
  #   count_dict[letter] = 0 #see comment below...
  for letter in word:
    if letter not in count_dict:
      count_dict[letter] = 1
    else:
      count_dict[letter] += 1 #I'm a little confused about this part of the loop; the 0 and  += 1...
  return count_dict
 
print letter_histogram("pippi")

# ***=========A BETTER SOLUTION===========***
# def char_frequency(str1):
#     dict = {}
#     for n in str1:
#         keys = dict.keys()
#         if n in keys:
#             dict[n] += 1
#         else:
#             dict[n] = 1
#     return dict
# print(char_frequency('google.com'))

# Word Summary
# Write a word_histogram function that takes a paragraph of text as its input, 
# and returns a dictionary containing the tally of how many times each word 
# was used in the text. For example:

# >>> word_histogram('To be or not to be')
# {'to': 2, 'be': 2, 'or': 1, 'not': 1}
# In this exercise, are you using dynamic keys or fixed keys?

# I need to: break the sentence into a list of words...???

def word_histogram(sentence): # should it include more logic to exclude periods, commas, etc...?
    sentence = sentence.lower()
    sentence_list = sentence.split()
    word_dict = {}
    for word in sentence_list:
        word_dict[word] = 0
    for word in sentence_list:
        word_dict[word] += 1
    return word_dict
    
print word_histogram("The ship is the shoe is the poo")
