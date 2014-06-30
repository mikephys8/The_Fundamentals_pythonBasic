__author__ = 'Administrator'

print('3' in [1, 2, 3])
print(int('3') in [len('a'), len('ab'), len('abc')])
print('a' in ['mom', 'dad'])
print(len('mom') in [1, 2, 3])
print('-------------///----------------')
def mystery(s):
    i = 0
    result = ''

    while not s[i].isdigit():
        result = result + s[i]
        i = i + 1

    return result
print(mystery('abc123'))
print(mystery('123'))
print(mystery('123abc'))
# print(mystery('abc'))
print('-----------------------------')
def example(L):
    """ (list) -> list
    """
    i = 0
    result = []
    while i < len(L):
        result.append(L[i])
        i = i + 3
    return result
print(example(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']))
print('-----------------------------')

def compress_list(L):
    """ (list of str) -> list of str

    Return a new list with adjacent pairs of string elements from L
    concatenated together, starting with indices 0 and 1, 2 and 3,
    and so on.

    Precondition: len(L) >= 2 and len(L) % 2 == 0

    >>> compress_list(['a', 'b', 'c', 'd'])
    ['ab', 'cd']
    """
    compressed_list = []
    i = 0

    while i < len(L):
        compressed_list.append(L[i] + L[i + 1])
        # MISSING CODE HERE
        i = i + 2

    return compressed_list
print(compress_list(['a', 'b', 'c', 'd']))
print('-----------------------------')
def sum_of_even_numbers():
    i = 0
    result = 0
    for i in range(524, 10509):
        if i % 2 == 0:
            result = result + i
            i = i + 1
    return result
print(sum_of_even_numbers())
print('-----------------------------')

def while_version(L):
    """ (list of number) -> number
    >>> while_version([1, 3, 5, 7, 9, 2, 15])
    25
    """
    i = 0
    total = 0

    while i < len(L) and L[i] % 2 != 0:
        total = total + L[i]
        i = i + 1

    return total
print(while_version([1, 3, 5, 7, 9, 2, 15]))

print('-------/-/-/-/-/-/-/-/-/---------------')
def while_version_dup(L):
    found_even = False
    total = 0

    for num in L:
        if num % 2 != 0 and not found_even:
            total = total + num
        else:
            found_even = True

    return total
print(while_version_dup([1, 3, 5, 7, 9, 2, 15]))
print('-----------------------------')
def sort_list():
    letters = ['b', 'd', 'a']
    # MISSING CODE HERE
    # letters = sort(letters)
    # sort(letters)
    letters.sort()
    # letters = letters.sort()
    return letters
print(sort_list())
print('-----------------------------')

veggies = ['carrot', 'broccoli', 'potato', 'asparagus']
veggies.insert(veggies.index('broccoli'), 'celery')
print(veggies)
print('-----------------------------')

def cap_song_repetition(playlist, song):
    '''(list of str, str) -> NoneType

    Make sure there are no more than 3 occurrences of song in playlist.
    '''
    # playlist = ['Lola', 'Venus', 'Lola', 'Lola', 'Let It Be',
    #
    #             'Lola', 'ABC', 'Cecilia', 'Lola', 'Lola']
    # Correct
    while playlist.count(song) > 3:
        playlist.pop(playlist.index(song))
     # Correct
    while playlist.count(song) > 3:
        playlist.remove(song)
    # Wrong syntax
    # while playlist.count(song) > 3:
    #     playlist.remove(playlist.index(song))
    # Wrong syntax
    # while playlist.count(song) > 3:
    #     playlist.pop(song)
playlist = ['Lola', 'Venus', 'Lola', 'Lola', 'Let It Be',

                'Lola', 'ABC', 'Cecilia', 'Lola', 'Lola']
print(cap_song_repetition(playlist, 'Lola'))
print(playlist)
print('--------------/-/-/-/-/-///////----------------------')

def ex5_test():
    a = [1, 2, 3]
    b = a
    # print(a, b)
    '''>>> print(a, b)
    [1, 'A', 3] [1, 'A', 3]
    '''
    # print('----------------------')
    # MISSING CODE HERE
    #---Correct
    # a = [1, 'A', 3]
    # b = [1, 'A', 3]
    # print(a, b)
    # print('----------------------')
    #---Correct
    # a[1] = 'A'
    # print(a, b)
    # print('----------------------')
    #---Correct
    # b[1] = 'AB'
    # a[1] = a[1][0]
    # print(a, b)
    #---Correct
    b[-2] = 'A'

    print(a, b)
print(ex5_test())
print('---------Telos ewrhthshs 10-------------\n')
print('------------------****************---------------------')
def ex5_test1():
    a = [1, 2, 3]
    b = [1, 2, 3]
    # MISSING CODE HERE
    #---Wrong
    # a[1] = 'A'
    # print(a, b)
    # print('----------------------')
    #---Wrong
    # b[1] = 'AB'
    # a[1] = a[1][0]
    # print(a, b)
    # print('----------------------')
    #---Correct
    a = [1, 'A', 3]
    b = [1, 'A', 3]
    print(a, b)
    # print('-----------------------')
    #---Wrong
    # b[-2] = 'A'
    # print(a, b)

print(ex5_test1())
print('---------Telos ewrhthshs 11-------------\n')

def increment_items(L, increment):
    i = 0
    while i < len(L):
        L[i] = L[i] + increment
        i = i + 1

values = [1, 2, 3]
print(increment_items(values, 2))
print(values)
print('---------Telos ewrhthshs 12-------------\n')

def print_list():
   values = []
   # Correct
   # for num in range(3, 10, 3):
   #    values.append(num)
   # print(values)
   # print('---------------------------')
   #  Wrong
   # for num in range(3, 9, 3):
   #    values.append(num)
   # print(values)
   #Wrong
   # for num in range(1, 3):
   #    values.append(num * 3)
   # print(values)
   #Correct
   for num in range(1, 4):
      values.append(num * 3)
   print(values)
print(print_list())
print('---------Telos ewrhthshs 13-------------\n')

def print_num():
    # Wrong
    # for num in range(3, 19, 8):
    #    print(num)
    # print('---------------------------')
    # Correct
    for num in range(3, 23, 8):
       print(num)
    print('---------------------------')
    # Wrong
    # for num in range(3, 8, 20):
    #    print(num)
    # print('---------------------------')
    # Correct
    for num in range(3, 20, 8):
       print(num)
print(print_num())














