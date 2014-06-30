__author__ = 'Administrator'

def calculate_averages(grades):
    ''' (list of list of number) -> list of float

    Return a new list in which each item is the average of the grades
    in the inner list at the corresponding position of grades.

    >>> calculate_averages([[70, 75, 80], [70, 80, 90, 100], [80, 100]])
    [75.0, 85.0, 90.0]
    '''

    averages = []

    # Calculate the average of each sublist and append it to averages.
    for grades_list in grades:

        # Calculate the average of grades_list.
        total = 0
        for mark in grades_list:
            total = total + mark

        averages.append(total / len(grades_list))

    return averages