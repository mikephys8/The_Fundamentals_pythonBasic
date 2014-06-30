__author__ = 'Administrator'

def count_vowels(word):
    j = 0
    for i in word:
        if i in 'AaEeIiOoUu':
            j += 1

    return j

print(count_vowels('hello'))

print('-------------------------')

def count_consonants(word):
    k = 0
    for i in word:
        if i not in 'AaEeIiOoUu':
            k += 1

    return k
print(count_consonants('hello'))

print('-----------////--------------')
def count_letters(word):
    """ (str) -> int

    Return the number of letters in word.
    >>> count_letters('hello')
    5
    >>> count_letters('bonjour')
    7
    """
# Write the one-line function body that belongs here.
    return count_vowels(word) + count_consonants(word)
print(count_letters('hello'))