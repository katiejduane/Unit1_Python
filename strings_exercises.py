# String exercises
my_string = "Katie hates to sing"

print my_string.upper()
print my_string.capitalize()
print my_string[::-1]

#LeetSpeak
leet = {"A": "4", "E": "3", "G": "6", "I": "1", "O": "0", "S": "5", "T": "7"}
leet_string = my_string.upper()
final_string = ""

for i in range(0, len(leet_string)):
    current_letter = leet_string[i]
    if current_letter in leet:
        current_letter = leet[current_letter]
    final_string += current_letter
print final_string

# Long Long Vowels
v_string = "Look at me, cheesehead!"
vowels = {"oo": "ooooo", "ee": "eeeee"}
long_string = ""

#Comment out the purpose of each line of the code!
for i in range(0, len(v_string)):
    current_letter = v_string[i]
    if (i != len(v_string)-1):
        current_vowels = v_string[i] + v_string[i + 1]
        if current_vowels in vowels:
            current_letter = vowels[current_vowels]
        long_string += current_letter
print long_string


# Cipher... (how to store the plan/cipher? as strings all smushed together, strings with spaces, as a list, or a dictionary?)
plain = "abcdefghijklmnopqrstuvwxyz"
cipher = "bcdefghijklmnopqrstuvwxyza"

