__author__ = 'Administrator'

import tkinter.filedialog
from my_grades import read_grades
from count_grades_range import count_grade_ranges
from histogram import write_histogram

a1_filename = tkinter.filedialog.askopenfilename()
a1_file = open(a1_filename, 'r')
# what follows is for testing purpose
# for line in a1_file:
#     print(line)
a1_histfilename = tkinter.filedialog.askopenfilename()
a1_histfile = open(a1_histfilename, 'w')

# Read the grades into a list.
print(read_grades(a1_file))

# Count the grades per range.
# print(count_grade_ranges([77.5, 37.5, 0.5, 9.5, 72.5, 100.0, 55.0, 70.0, 79.5]))

print(count_grade_ranges([0.9, 10.5, 20.9, 55.3, 35.9, 54.2, 100.0, 34.2, 58.7, 59.9, 28.7, 89.3, 85.7, 49.1, 59.6, 15.9, 82.4, 48.4, 33.8, 61.8, 23.5, 54.7, 62.5, 45.9, 75.6, 37.5, 64.5, 43.6, 98.5, 73.5, 67.3, 54.7, 99.9, 40.8, 78.3, 77.9, 69.9]))

# Write the histogram into the file.

# write_histogram(count_grade_ranges([77.5, 37.5, 0.5, 9.5, 72.5, 100.0, 55.0, 70.0, 79.5]), a1_histfile)

# too big for one line inside a function!!!
c = [0.9, 10.5, 20.9, 55.3, 35.9, 54.2, 100.0, 34.2, 58.7, 59.9, 28.7, 89.3, 85.7, 49.1, 59.6, 15.9, 82.4, 48.4, 33.8, 61.8, 23.5, 54.7, 62.5, 45.9, 75.6, 37.5, 64.5, 43.6, 98.5, 73.5, 67.3, 54.7, 99.9, 40.8, 78.3, 77.9, 69.9]
write_histogram(count_grade_ranges(c), a1_histfile)

# # den anagnwrizei thn range_counts???
# # write_histogram(range_counts, a1_histfile)
a1_file.close()
a1_histfile.close()
