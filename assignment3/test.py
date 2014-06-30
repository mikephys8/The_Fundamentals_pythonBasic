# from assignment3.a3 import *

words_file = open('assignment3/wordlist1.txt', 'r')
def read_words(words_file):

    word_list = []
    for line in words_file:
        word_list.append(line.rstrip('\n'))
    return word_list
print(read_words(words_file))