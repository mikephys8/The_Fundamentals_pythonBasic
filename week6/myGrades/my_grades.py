__author__ = 'Administrator'
# from  someOtherLib import lib as _

def read_grades(gradefile):

    """(file open for reading) -> list of float
    Read and return the list of grade sin file
    Precondition: gradefile starts with a header that contains
    no blank lines, then has a blank line, and then lines
    containing a student number and a grade.
    """

    # skip over the header.
    line = gradefile.readline()
    while line != '\n':
        line = gradefile.readline()
    # Read the grades, accumulating them into a list.

    grades = []

    line = gradefile.readline()
    while line != '':
        # Now we have a string containing the info for a
        # single student.
        # Find the last space and take everything after
        # that space.

        # .rfind() method finds from the right most place
        # of the line the first! index number of the char.
        # that's why we add +1 for passing the space and
        # start from the number till the end of string.

        #this returns str
        grade = line[line.rfind(' ') + 1:]
        #but we want float
        grades.append(float(grade))
        line = gradefile.readline()
    return grades






