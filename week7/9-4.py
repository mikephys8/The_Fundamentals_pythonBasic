__author__ = 'Administrator'

gradefile = open('student_grades.txt')
def read_grades(gradefile):

    """(file open for reading) -> list of float
    Read the grades from gradefile and return a dictionary where
    each key is a grade and each value is the list of ids of
    students who earned that grade.

    Precondition: gradefile starts with a header that contains
    no blank lines, then has a blank line, and then lines
    containing a student number and a grade.
    """

    # skip over the header.
    line = gradefile.readline()
    while line != '\n':
        line = gradefile.readline()

    # Read the grades, accumulating them into a dict.
    grade_to_ids = {}
    line = gradefile.readline()
    while line != '':
        # Now we have a string containing the info for a
        # single student.
        student_id = line[:4]
        # the strip() method removes all spaces from the string.
        grade = float(line[4:].strip())

        if grade not in grade_to_ids:
            grade_to_ids[grade] = [student_id]
        else:
            grade_to_ids[grade].append(student_id)
        line = gradefile.readline()
    return grade_to_ids

    #     # Find the last space and take everything after
    #     # that space.
    #
    #     # .rfind() method finds from the right most place
    #     # of the line the first! index number of the char.
    #     # that's why we add +1 for passing the space and
    #     # start from the number till the end of string.
    #
    #     #this returns str
    #     grade = line[line.rfind(' ') + 1:]
    #     #but we want float
    #     grades.append(float(grade))
    #     line = gradefile.readline()
    # return grades
classes = read_grades(gradefile)
print(classes)
print('--------------------------------------- \n')
# for printing a dictionary(classes) vertically!
for key, value in sorted(classes.items()):
    print("{} : {}".format(key, value))
