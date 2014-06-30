__author__ = 'Administrator'
#
lst = ['abcdefghijklmnopqrstuvwxyz']
for i in range(len(lst)):
    print(lst[i])
    print('\n\n\n')

# This also gives us flexibility to process only part of a list.
# For example, We can print only the first half of the list:
# lst = ['abcdefghijklmnopqrstuvwxyz']
# for i in range(lst) // 2):
#     print(lst[i])
# #     print('\n\n')
#
# # Or every other element:
lst = ['abcdefghijklmnopqrstuvwxyz']
for i in lst[0].split('m', 1):
    print(i + 'm')
    print('\n')
print('\n\n')

#firstpart, secondpart = string[:len(string)/2], string[len(string)/2:]

lst = ['abcdefghijklmnopqrstuvwxyz']
s = lst[0]
#print(s[:len(s)/ 2])
# for i in s:
print(s[:len(s)//2], s[len(s)//2:])
#koble

def count_adjacent_repeats(s):
    ''' (str) -> int

    Return the number of occurrences of a character and an adjacent character
    being the same.

    >>> count_adjacent_repeats('abccdeffggh')
    3
    '''

    repeats = 0

    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            repeats = repeats + 1

    return repeats

def shift_left(L):
    ''' (list) -> NoneType

    Shift each item in L one position to the left and shift the first item to
    the last position.

    Precondition: len(L) >= 1

    >>> shift_left(['a', 'b', 'c', 'd'])
    '''

    first_item = L[0]

    for i in range(len(L) - 1):
        L[i] = L[i + 1]

    L[-1] = first_item

# for pyhton visualizer
# def shift_left(L):
#     ''' (list) -> NoneType
#
#     Shift each item in L one position to the left and shift the first item to
#     the last position.
#
#     Precondition: len(L) >= 1
#
#     >>> shift_left(['a', 'b', 'c', 'd'])
#     '''
#
#     first_item = L[0]
#
#     for i in range(len(L) - 1):
#         L[i] = L[i + 1]
#
#     L[-1] = first_item
#
# letters = ['a', 'b', 'c', 'd']
# print(shift_left(letters))
# print(letters)
