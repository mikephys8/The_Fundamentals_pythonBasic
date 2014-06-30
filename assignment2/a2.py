def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len(dna)
print(get_length('ATCGAT'))
print(get_length('ATCG'))

def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    if dna1 > dna2:
        return True
    return False
print(is_longer('ATCG', 'AT'))
print(is_longer('ATCG', 'ATCGGA'))


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    i = 0
    if dna != '' and nucleotide != '':
        for char in dna:
            if nucleotide == char:
                i = i + 1
        return i
    else:
        return 'Caution! Put values in dna and nucleotide!!!'
print(count_nucleotides('ATCGGC', 'G'))
print(count_nucleotides('ATCTA', 'G'))


def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    if dna2 in dna1:
        return True
    return False
print(contains_sequence('ATCGGC', 'GG'))
print(contains_sequence('ATCGGC', 'GT'))

print('----------------------------------------')
def is_valid_sequence(dna):
    '''(str) -> bool

    Return True if and only if the DNA sequence
    is valid (that is, it contains no characters
    other than 'A', 'T', 'C' and 'G')

    >>> is_valid_sequence('ATCGAG')
    True
    >>> is_valid_sequence('ATCGKAG')
    False
    >>> is_valid_sequence('atcgac')
    'Caution! Put values in dna or put it in capital letters!!!'
    '''

    i = 0
    nucleotide = ['A', 'T', 'G', 'C']
    if dna != '' and dna[i] not in 'atgc':
        for char in dna:
            if char not in nucleotide:
                i = i + 1
    else:
        return 'Caution! Put values in dna or put it in capital letters!!!'
    if i > 0:
        return False
    return True
print(is_valid_sequence('ATCGAG'))
print(is_valid_sequence('AMTCLGAG'))
print(is_valid_sequence('ATCGKAG'))
print(is_valid_sequence('atcgac'))

print('------------------/-/-/-/------------------------')
def insert_sequence(dna1, dna2, index):
    '''(str, str, int) -> str

    Precondition: You can assume that the index is valid

    >>> insert_sequence('CCGG', 'AT', 2)
    'CCATGG'
    >>> insert_sequence('CCGG', 'AT', 0)
    'ATCCGG'
    >>> insert_sequence('CCGG', 'AT', 3)
    'CCGGAT'
    '''

    i = 0
    if dna1 != '' and dna2 != '':
        for i in range(len(dna1)):
            while i != index:
                i = i + 1
            if i != 0 and i != len(dna1) - 1:
                dna1 = dna1[:i] + dna2 + dna1[i:]
                return dna1
            elif i == 0:
                dna1 = dna2 + dna1
                return dna1
            elif i == len(dna1) - 1:
                dna1 = dna1 + dna2
                return dna1
    else:
        print('Caution! Fill in dna sequences properly')
print(insert_sequence('CCGG', 'AT', 2))
print(insert_sequence('CCGG', 'AT', 0))
print(insert_sequence('CCGG', 'AT', 3))
print(insert_sequence('CTCAGAG', 'AT', 4))

print('-------------/-/-/-/-/-//-///--/-/-/-/-/------------')
def get_complement(nucleotide):
    '''(str) -> str

    Precondition: nucleotide is one of 'A','T','G','C'
    'A' = complement of 'T' and vice versa
    'G' = complement of 'C' and vice versa

    >>> get_complement('A')
    'T'
    >>> get_complement('T')
    'A'
    >>> get_complement('G')
    'C'
    >>> get_complement('C')
    'G'
    '''
    nucleotides = ['A', 'T', 'G', 'C']
    if nucleotide in nucleotides:
        if nucleotide == 'A':
            return 'T'
        elif nucleotide == 'T':
            return 'A'
        elif nucleotide == 'G':
            return 'C'
        else:
            return 'G'
    else:
        print('Give a nucleotide \'A\', \'T\', \'G\' or \'C\'')
print(get_complement('A'))
print(get_complement('T'))
print(get_complement('G'))
print(get_complement('C'))
print(get_complement('K'))

print('----------***************--------------')
def get_complementary_sequence(dna_sequence):
    '''(str) -> str


    >>> get_complementary_sequence('AGTCAGG')
    'TCAGTCC'
    >>> get_complementary_sequence('AT')
    'TA'
    '''
    complementary = ''
    for char in dna_sequence:
        complementary = complementary + get_complement(char)
    return complementary
print(get_complementary_sequence('AGTCAGG'))
print(get_complementary_sequence('AT'))
