__author__ = 'Administrator'
myfile = open('test.txt', 'r')

for index, line in enumerate(myfile):
    print ('this is line '+str(index) +',' +line)