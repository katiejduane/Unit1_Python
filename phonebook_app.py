# Electronic Phone Book
# =====================
# 1. Look up an entry
# 2. Set an entry
# 3. Delete an entry
# 4. List all entries
# 5. Quit
# What do you want to do (1-5)?
# If they choose to look up an entry, you will ask them for the person's name, and then look up the person's phone number by the given name and print it to the screen.
# If they choose to set an entry, you will prompt them for the person's name and the person's phone number,
# If they choose to delete an entry, you will prompt them for the person's name and delete the given person's entry.
# If they choose to list all entries, you will go through all entries in the dictionary and print each out to the terminal.
# Search for an entry
# You can limit this to Name, or loop through the entire dictionary
# If they choose to quit, end the program.
# Example session:

# $ python phonebook.py

# Electronic Phone Book
# =====================
# 1. Look up an entry
# 2. Set an entry
# 3. Delete an entry
# 4. List all entries
# 5. Search for an entry
# 6. Quit
# What do you want to do (1-5)? 2
# Name: Melissa
# Phone Number: 584-394-5857
# Entry stored for Melissa.

# Psuedo_Code: What do I need to do to create a basic phonebook app? First, I need to create a phonebook, and for that,
# I'll use a dictionary for storing the data. I'll make only a few entries, and then once the app is complete, actually 
# use it to store additional entries.
# 1. Make a phonebook with 5 entries
# 2.

phonebook = {
    "BRENDAN BRODY": "716-935-9264", #The dashes are casuing numbers to print wrong. How to fix w/o making a string??
    "ELLEN BRODY": "716-982-9404",
    "HANNAH DUANE": "716-597-9296",
    "STEVEN DUANE": "716-432-2939",
    "SHIRLEY DUANE": "716-598-0220"
}

from time import sleep

def welcome():
    user_name = "Katie"
    print "Welcome to your phonebook, %s, what would like to do today?" % user_name
    sleep(1)
    print """
    1. Look up an entry
    2. Set an entry 
    3. Delete an entry
    4. List all entries
    5. Quit
    """
    "                     " # what the hell is a way to create a space/line break? nothing works!

def look_up_entry():
    name = raw_input("Type first and last name: ").upper()
    if name not in phonebook:
        print "Contact not found, try again."
    else:
        print phonebook.get(name)

def add_contact(): #This code throws no errors but: it adds the contact and then it vanishes when the variable changes...
    print "Great, you'd like to add a new contact!"
    contact_name = raw_input("Type the first and last name of your contact: ")
    contact_entry = contact_name.upper()
    contact_num = raw_input("Enter your contact's number xxx-xxx-xxxx ")
    if len(contact_num) == 12:
        phonebook[contact_entry] = contact_num
        print "Contact added!" 
    else:
        print "Error with phone number. Please try again." # Do I need a loop to insert logic to try again?
    
        
def delete_contact():  #same issue; contact is deleted during program, but that deletion is not actually saved, dict returns to previous state.
    contact_to_delete = raw_input("Type the first and last name of the contact you want to remove: ")
    contact_to_delete = contact_to_delete.upper()
    if contact_to_delete in phonebook:
        del phonebook[contact_to_delete]
        print "Contact deleted"
    else:
        print "Contact not found, try again"
#Logic to try again?
        
      
def start_phonebook(): # I need to work on how it reprints the welcome/prompts fter the user hits a number and then finishes entering. Like adding a quit or return to menu prompt or something...
    start = True 
    def quit_prompt(): # This doesn't work right... doesn't print 'exiting' and doesn't actually change the boolean to stop the while loop...
        quit_op = raw_input("Would you like to something else or quit? Enter Q for Quit or C to continue using your phonebook: ")
        quit_op = quit_op.upper
        if quit_op == "Q":
            print "Exiting..."
            start = False
        else:
            pass

    while start:
        welcome()
        user_choice = int(raw_input("Enter a number from the list: "))
        if user_choice == 1:
            look_up_entry()
            quit_prompt()    
        elif user_choice == 2:
            add_contact()
            quit_prompt()
        elif user_choice == 3:
            delete_contact()
            quit_prompt()
        elif user_choice == 4:
            print phonebook
            quit_prompt()
        elif user_choice == 5: # couldn't seem to create this outside the function, as 'start' was not defined
            quit_prompt()
        else:
            print "Option not found. Choose from 1-5"
                

# phonebook["Maria Luna"] = "123-457-7890" ***HMMMMMM. as soon as i comment out this code, these contacts vanish from the dictionary!
# phonebook["Planet Jupiter"] = "098-765-4321"

# sample = "John Smith"
# sample_num = "111-111-1111"
# del phonebook[sample]
# phonebook[sample] = sample_num

# sample = "Lisa Greene"
# sample_num = "111-111-1111"
# phonebook.update({sample:sample_num})

# sample = "Shirley Duane"
# print phonebook.get(sample)

# search = phonebook.get()
# print search

# look_up_entry()
# add_contact()
# delete_contact()
start_phonebook()


# print phonebook




