# Dictionaries! 

zombie = {

}

zombie['weapon'] = "fist"
zombie['health'] = 100
zombie['speed'] = 10

print zombie
print zombie['weapon']

for key,value in zombie.items():
    print "Zombie has a value of %s" % value

# In our game, Zombie loses his arm, so he loses his weapon! 
# If you want to remove a KEY, you must do:
del zombie['weapon']

is_night_time = True
if(is_night_time):
    zombie['health'] += 50

print zombie

# Put lists and dictionaries together:
zombies = []
zombies.append({
    'name': 'hank',
    'weapon': 'bat',
    'speed': 10
})

zombies.append({
    'name': 'willy',
    'weapon': 'axe',
    'speed': 3,
    'victims': [
        'squirrel',
        'rabbit',
        'racoon'
    ]
})

print zombies
# ^^^ this won't print it in the order it's written, but whatever is most efficient for python...

# If we wanted to know the first zombie's weapon... or the second zombie's second victom

print zombies[0]['weapon']
print zombies[1]['victims'][1]