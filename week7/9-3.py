__author__ = 'Administrator'

fruit_to_colour = {
    'watermelon': 'green',
    'pomegranate': 'red',
    'peach': 'orange',
    'cherry': 'red',
    'pear': 'green',
    'banana': 'yellow',
    'plum': 'purple',
    'orange': 'orange'}

# the results are not presented in order!!!
print(fruit_to_colour)
print(fruit_to_colour['orange'])
print('-------------')
print(fruit_to_colour['banana'])
print('-------------')
for fruit in fruit_to_colour:
    print(fruit, fruit_to_colour[fruit])
print('-------------------------------------')
# Invert fruit_to_colour
# 1. Initialize the new dict
colour_to_fruit = {}
# 2. Make the invert
for fruit in fruit_to_colour:
    colour = fruit_to_colour[fruit]
    colour_to_fruit[colour] = fruit
print(colour_to_fruit)
#  ^
#  |_ caution! the invert of the first dict occurs
# to same keys with multiple values! this is forbidden!
# So we must create a new dict with keys(colours) that match
# with a list of fruits of the same colour!
# We repeat the invert with more caution!
print('-------------------------------------')
print('-------------------------------------')
colour_to_fruit = {}
# 3. Make the invert correctly
for fruit in fruit_to_colour:
    colour = fruit_to_colour[fruit]
    # If colour  is not already a key in the accumulator
    # add colour: [fruit] as an entry.
    if not (colour in colour_to_fruit):
        colour_to_fruit[colour] = [fruit]#<-list of fruits

    # Otherwise, append fruit to the existing list.
    else:
        colour_to_fruit[colour].append(fruit)#<-add fruit in list of fruits!

# dict with keys=strings and values=list of strings
print(colour_to_fruit)
print('-------------')
print(colour_to_fruit['orange'])
print(colour_to_fruit['orange'][0])
print(colour_to_fruit['red'])
print(colour_to_fruit['red'][-1])






