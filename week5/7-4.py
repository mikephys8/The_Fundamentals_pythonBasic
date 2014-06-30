__author__ = 'Administrator'

colours = []
prompt = 'Enter another one of your favourite colours (type return to end): '
colour = input(prompt)
# Enter another one of your favourite colours (type return to end): blue
# >>> colour
# 'blue'
# >>> colours
# []
while colour != '':
    colours.append(colour)
	colour = input(prompt)

if 'magenda' in colours:
   colours.remove('magenda')