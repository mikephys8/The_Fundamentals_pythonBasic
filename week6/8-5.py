__author__ = 'Administrator'
flanders_filename = 'lecture_code_week6_In Flanders Fields.txt'
file = open(flanders_filename, 'r')
# --------------------------------------------
# with open(flanders_filename, 'r') as flanders_file:
#     for line in flanders_file:
#         print(type(line))
#         # print(flanders_file.readline())
# --------------------------------------------
# for line in flanders_file:
    # print(line, end='')
    # print(line.rstrip('\n'))
    # print(line - '\n') <- TypeError

    # This strips all whitespace
    # from the beginning and end of each line, rather
    # than just the newline at the end.
    # print(line.strip())
# --------------------------------------------
print(flanders_file.read())

