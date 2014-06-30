__author__ = 'Administrator'

def count_grade_ranges(grades):

    """(list of float) -> list of int
    Return a list of int where each index indicates
    how many grades were in these ranges:

    0-9:    index 0
    10-19:  1
    20-29:  2
      :
    90-99:  9
    100:    10

    >>> count_grade_ranges([77.5, 37.5, 0.5, 9.5, 72.5, 100.0, 55.0, 70.0, 79.5])
    [2, 0, 0, 1, 0, 1, 0, 4, 0, 0, 1]
    """
    range_counts = [0] * 11 #fills an empty list with 11 zeros in each index number

    for grade in grades:
        which_range = int(grade // 10) #<- floor division
        range_counts[which_range] = range_counts[which_range] + 1
    return range_counts

print(count_grade_ranges([77.5, 37.5, 0.5, 9.5, 72.5, 100.0, 55.0, 70.0, 79.5]))


