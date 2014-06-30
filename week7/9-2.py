__author__ = 'Administrator'

# with lists we've seen so far
grades = [['A1', 80], ['A2', 70], ['A3', 90]]
print(grades[0])
print(grades[1])
print(grades[2])
print('-------------')
print(grades[0][0])
print(grades[0][1])
print('--------------------------------------------------')


# The general form of a dictionary is:

# {key1: value1, key2: value2, ..., keyN: valueN}

asn_to_grade = {'A1': 80, 'A2': 90, 'A3': 90}
# in order to print the value, you call the dictionary with argument
# the value's corresponding key!
print(asn_to_grade['A2'])
# for checking if a key exist in a dict, so as to prevent errors
print('A4' in asn_to_grade)
print('A2' in asn_to_grade)
# the previous checking method only searches for keys not for values so:
print(80 in asn_to_grade) #returns False
print('-------------')
print(len(asn_to_grade))
print('-------------')
# dict like lists are muttable so:
asn_to_grade['A4'] = 85
print(len(asn_to_grade))
print(asn_to_grade)
print('-------------')
asn_to_grade['A4'] = 90
print(asn_to_grade)
print('-------------')
# for deleteing akey-value from a dict we use del:
del asn_to_grade['A4']
print(len(asn_to_grade))
print(asn_to_grade)
print('-------------')
# print the keys of a dict
for assignment in asn_to_grade:
    print(assignment)
print('-------------')
# print the values of a dict
for assignment in asn_to_grade:
    print(asn_to_grade[assignment])
print('-------------')
# print the keys and values of a dict
for assignment in asn_to_grade:
    print(assignment, asn_to_grade[assignment])
print('-------------')
# empty dict is declared as:
d = {}
# and its length is 0
print(len(d))
print('-------------')
# the data types of the keys-values of a dict may vary, .
# but the keys must be immutable!!! so cannot be lists, dicts, etc for example!!!
e = {'apple': 2, 5 : 8}
print(e)
# print(e[[1, 2]] = 'banana') #,- gives error!!!
# but instead of using lists as keys, we can use tuples
# which are immutable!!!
e[(1, 2)] = 'banana'
print(e)




