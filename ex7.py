__author__ = 'Administrator'


d = {'a': 1, 'b': 2}
# CODE MISSING HERE
# d.update({'c':3})
d['c'] = 3
print(d)
# {'a': 1, 'c': 3, 'b': 2}
print('-----------------End of q1--------------------------------')
d = {'a': 1, 'b': 2}
# CODE MISSING HERE
d.update({'b':3})
# d['c'] = 3
print(d)
# {'a': 1, 'b': 3}
print('-----------------End of q2--------------------------------')
d = {'a': [1, 3], 'b': [5, 7]}
# CODE MISSING HERE

# Wrong!! - KeyError 'A'
# d['A'].insert(1, 2)

# Wrong - appends object to end
# d['a'].append(2)

#.insert(index, object)-> puts object before index!!!
# Correct
d['a'].insert(1, 2)
print('-----------different method-------------')
# Correct
# d['a'].append(2)
# d['a'].sort()
print(d)
# {'a': [1, 2, 3], 'b': [5, 7]}
print('-----------------End of q3--------------------------------')
# >>> d = {'a': 1, 'c': 3, 'b': 2}
# >>> 'B' in d
# False
# >>> 2 in d
# False
# >>> not ('e' in d)
# True
# >>> 'b' in d
# True
print('-----------------End of q4--------------------------------')
d = {'a': [1, 3], 'b': [5, 7, 9], 'c': [11]}

# Select the expression(s) that evaluate to 3.
# Wrong -> 2
# print(len(d['a']))
print(len(d))
print(len(d['a']) + len(d['c']))
# Wrong -> 'ac'
# print(len(d['a' + 'c']))
print('-----------------End of q5--------------------------------')
tup = (1, 2, 3)

# Select the expression(s) and statement(s) below that result in an error.
subtup = tup[0:2]
print(subtup)
print(tup.count(3))
# Wrong -> TypeError: 'tuple' object does not support item assignment
# tup[-2] = 4
# Wrong -> AttributeError: 'tuple' object has no attribute 'append'
# tup.append(4)
print('-----------------End of q6--------------------------------')
# >>> d = {['a', 'b']:1}
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# TypeError: unhashable type: 'list'
# >>> d = {(1, 'fred', 2.0):1}
# >>> d
# {(1, 'fred', 2.0): 1}
# >>> d = {{1: 2, 3: 4}:1}
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# TypeError: unhashable type: 'dict'
# >>> d = {('single',):1}
# >>> d
# {('single',): 1}
print('-----------------End of q7--------------------------------')
d = {1: ['a', 'b', 'c'], 2: ['d', 'e'], 3: []}

# Select the code fragment(s) that set variable total
# to the number of items in all the lists that occur
# as values in d.

# Correct -> 5

L = []
for k in d:
    L.extend(d[k])

total = len(L)
print(total)
print('-----------different method-------------')
# Correct -> 5

# total = 0
# for k in d:
#     total = total + len(d[k])
# print(total)
print('-----------different method-------------')
# Wrong -> 3

# L = []
# for k in d:
#     L.append(k)
#
# total = len(L)
# print(total)
print('-----------different method-------------')
# Wrong -> 6

# total = 0
# for k in d:
#     total = total + k
# print(total)
print('-----------------End of q8--------------------------------')
# It only keeps the last entry with the same key...
# >>> {1: 10, 1: 20, 1: 30}
# {1: 30}
print('-----------------End of q9--------------------------------')

# opulates dictionary d where each key is the first item
# of each inner list of L and each value is the second item
# of that inner list.
L = [['apple', 3], ['pear', 2], ['banana', 3]]
d = {}
for item in L:
    d[item[0]] = item[1]
print(d)
print(L)
print('-----------------End of q10--------------------------------')
def eat(d):
    '''(dict of {str: int}) -> bool

    Each key in d is a fruit and each value is the quantity of that fruit.

    REST OF DESCRIPTION MISSING HERE

    >>> eat({'apple': 2, 'banana': 3, 'pear': 3, 'peach': 1})
    True
    >>> eat({'apple': 0, 'banana': 0})
    False
    '''
    ate = False
    for fruit in d:
        if d[fruit] > 0:
            d[fruit] = d[fruit] - 1
            ate = True

    return ate
print('-----------------End of q11--------------------------------')

def contains(v, d):
    ''' (object, dict of {object: list}) -> bool

    Return whether v is an element of one of the list values in d.

    >>> contains('moogah', {1: [70, 'blue'], 2: [1.24, 'moogah', 90], 3.14: [80, 100]})
    True
    >>> contains('moogah', {'moogah': [1.24, 'frooble', 90], 3.14: [80, 100]})
    False
    '''

    found = False  # Whether we have found v in a list in d.

    # CODE MISSING HERE

    # Correct
    # for k in d:
    #     if v in d[k]:
    #         found = True
    # Correct
    # for k in d:
    #     for i in range(len(d[k])):
    #         if d[k][i] == v:
    #             found = True
    # Wrong!!!
    # for k in d:
    #     if v == k:
    #         found = True
    #Wrong(doesn't have if, so it it stops in 1st iteration)
    # for k in d:
    #     for i in range(len(d[k])):
    #         found = (d[k][i] == v)

    return found


