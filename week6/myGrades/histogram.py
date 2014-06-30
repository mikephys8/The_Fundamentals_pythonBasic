__author__ = 'Administrator'

from count_grades_range import count_grade_ranges

def write_histogram(range_counts, histfile):
    """(list of int, file open for writing) -> NoneType

    Write a histogram of *'s based on the number of grades in each range.

    The output format:

    0-9:   *
    10-19: **
    20-29: ******
      :
    90-99: **
    100:   *
    """

    histfile.write('0-9:   ')
    histfile.write('*' * range_counts[0])
    histfile.write('\n')

    # writes the 2-digits ranges.
    for i in range(1, 10):
        low = i * 10
        high = i * 10 + 9
        histfile.write(str(low) + '-' + str(high) + ': ')
        histfile.write('*' * range_counts[i])
        histfile.write('\n')

    histfile.write('100:   ')
    histfile.write('*' * range_counts[-1])
    histfile.write('\n')

