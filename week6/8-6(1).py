__author__ = 'Administrator'

__author__ = 'Administrator'

import tkinter.filedialog
tkinter.filedialog.askopenfilename()

from_filename = tkinter.filedialog.askopenfilename()
print(from_filename)
to_filename = tkinter.filedialog.asksaveasfilename()
print(to_filename)
from_file = open(from_filename, 'r')
contents = from_file.read()
print(contents)
to_file = open(to_filename, 'w')
# .write() method returns an int of how many char are there in the str
# including the \n as one char AND We have to add the newline ourselves!
to_file.write("Copy\n")
to_file.write(contents)
to_file.close()

to_file = open(to_filename, 'r')
print(to_file.read())
