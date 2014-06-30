__author__ = 'Administrator'
# import tkinter.filedialog
# tkinter.filedialog.askopenfilename()

def merge(L):
    merged = []
    for i in range(0, len(L), 3):
        merged.append(L[i] + L[i + 1] + L[i + 2])
    return merged

print(merge([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print('---------- End of question 1 ----------------\n')
def mystery(s):
    """ (str) -> bool
    Return True if and only if s is equal to the reverse of s.
    """
    matches = 0
    for i in range(len(s) // 2):
        if s[i] == s[len(s) - 1 - i]:     # <--- How many times is this line reached?
            matches = matches + 1

    return matches == (len(s) // 2)

print(mystery('pottop'))
print(mystery('civic'))
print(mystery('pottpo'))
print('---------- End of question 3 ----------------\n')
def shift_right(L):
    ''' (list) -> NoneType

    Shift each item in L one position to the right
    and shift the last item to the first position.

    Precondition: len(L) >= 1
    '''

    last_item = L[-1]

    # MISSING CODE GOES HERE
    #Wrong!! out of range, it should be len(L) - 1
    # for i in range(len(L)):
    #     L[i + 1] = L[i]
    # print('----------------')
    #Correct
    for i in range(1, len(L)):
        L[len(L) - i] = L[len(L) - i - 1]
    # print('----------------')
    #Wrong!!! IndexError: list index out of range
    # for i in range(1, len(L)):
    #     L[i] = L[i + 1]
    # print('----------------')
    #Wrong!!!
    # for i in range(len(L) - 1):
    #     L[i] = L[i + 1]
    L[0] = last_item
    print(L)
print(shift_right(['a', 'b', 'c', 'd']))
print('---------- End of question 4 ----------------\n')
def make_pairs(list1, list2):
    ''' (list of str, list of int) -> list of [str, int] list

    Return a new list in which each item is a 2-item list with the string from the
    corresponding position of list1 and the int from the corresponding position of list2.

    Precondition: len(list1) == len(list2)

    >>> make_pairs(['A', 'B', 'C'], [1, 2, 3])
    [['A', 1], ['B', 2], ['C', 3]]
    '''

    pairs = []

    # CODE MISSING HERE
    # Wrong!!! returns the same list(not grouped, just in sequence)
    # in every index of pairs
    # inner_list = []
    # for i in range(len(list1)):
    #     inner_list.append(list1[i])
    #     inner_list.append(list2[i])
    #     pairs.append(inner_list)
    # Wrong!!! returns only the last sublist of the expected pairs list
    # for i in range(len(list1)):
    #     inner_list = []
    #     inner_list.append(list1[i])
    #     inner_list.append(list2[i])
    # pairs.append(inner_list)
    #Correct
    for i in range(len(list1)):
        pairs.append([list1[i], list2[i]])
    #Correct
    for i in range(len(list1)):
        inner_list = []
        inner_list.append(list1[i])
        inner_list.append(list2[i])
        pairs.append(inner_list)
    return pairs
print(make_pairs(['A', 'B', 'C'], [1, 2, 3]))
print('---------- End of question 5 ----------------\n')
def contains(value, lst):
    """ (object, list of list) -> bool

    Return whether value is an element of one of the nested lists in lst.

    >>> contains('moogah', [[70, 'blue'], [1.24, 90, 'moogah'], [80, 100]])
    True
    """

    found = False  # We have not yet found value in the list.

    # CODE MISSING HERE
    #Correct (like in javascript...)
    # for i in range(len(lst)):
    #     for j in range(len(lst[i])):
    #         if lst[i][j] == value:
    #             found = True
    #Correct --But Python ROCKS!!!--
    for sublist in lst:
        if value in sublist:
            found = True
    #Wrong!! the value != whole sublist!!!
    # for item in lst:
    #     if value == item:
    #         value = True
    #Wrong! because without if the condition becomes False and function exits!
    # for i in range(len(lst)):
    #     for j in range(len(lst[i])):
    #         found = (lst[i][j] == value)

    return found
print(contains('moogah', [[70, 'blue'], [1.24, 90, 'moogah'], [80, 100]]))
print('---------- End of question 9 ----------------\n')


file = open('lecture_code_week6_In Flanders Fields.txt', 'r')
def lines_startswith(file, letter):
    """ (file open for reading, str) -> list of str

    Return the list of lines from file that begin with letter. The lines should have the
    newline removed.

    Precondition: len(letter) == 1
    """
    # file = open('lecture_code_week6_In Flanders Fields.txt', 'r')
    matches = []

    # CODE MISSING HERE
    #Correct
    # for line in file:
    #     if letter in line:
    #         matches.append(line.rstrip('\n'))
    # Correct
    for line in file:
        if letter == line[0]:
            matches.append(line.rstrip('\n'))

    #Correct
    # for line in file:
    #     if line.startswith(letter):
    #         matches.append(line.rstrip('\n'))
    #Wrong
    # for line in file:
    #     matches.append(line.startswith(letter).rstrip('\n'))

    return matches
print(lines_startswith(file, 'T'))
print('---------- End of question 12 ----------------\n')

# to_filename = tkinter.filedialog.asksaveasfilename()
# to_file = open(to_filename, 'w')
# def write_to_file(to_file, sentences):
#     """ (file open for writing, list of str) -> NoneType
#
#     Write each sentence from sentences to file, one per line.
#
#     Precondition: the sentences contain no newlines.
#     """
#
#     # CODE MISSING HERE
#     #Wrong! writes everything in one line without spaces
#     # for s in sentences:
#     #     to_file.write(s)
#     # to_file.write('\n')
#     #TypeError: sentences must be str, not list
#     # to_file.write(sentences)
#     #Wrong! writes everything in one line without spaces
#     # for s in sentences:
#     #     to_file.write(s)
#     #Correct!!!!!!!!
#     for s in sentences:
#         to_file.write(s + '\n')
#     #Correct!!!!!!!!
#     # for s in sentences:
#     #     to_file.write(s)
#     #     to_file.write('\n')
# print(write_to_file(to_file, ['We are the Dead. Short days ago',
#                               'We lived, felt dawn, saw sunset glow',
#                               'Loved and were loved, and now we lie',
#                               'In Flanders fields.']))
# to_file.close()
# # print(to_file.read())





