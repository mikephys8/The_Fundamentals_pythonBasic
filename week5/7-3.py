__author__ = 'Administrator'


grades = [80, 90, 70]

for grade in grades:
    print(grade)


# List Operations
#
# Like strings, lists can be indexed:

# >>> grades[0]
# 80
# >>> grades[1]
# 90
# >>> grades[2]
# 70


# Lists can also be sliced, using the same notation as for strings:
#
# >>> grades[0:2]
# [80, 90]


# The in operator can also be applied to check whether a value is an item in a list.
#
# >>> 90 in grades
# True
# >>> 60 in grades
# False
#

# Several of Python's built-in functions can be applied to lists, including:
#
# len(list): return the length of list.
# min(list): return the smallest element in list.
# max(list): return the largest element in list.
# sum(list): return the sum of elements of list (where list items must be numeric).

subjects = ['bio', 'cs', 'math', 'history']

for item in subjects:
    print(item)

street_address = [10, 'Main Street']

for item in street_address:
    print(item)

dir(list)