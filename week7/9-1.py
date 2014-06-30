__author__ = 'Administrator'

tup = ('a', 3, -0.2)
print(tup[0])
print(tup[1])
print(tup[2])
print(tup[-1])
print('-------------')
print(tup[:2])
print(tup[1:2])
print(tup[1:3])
print(tup[2:3])
print(tup[2:])
print('-------------')
# tuples arer immutable!!cannot be assigned with other
# value in opposition with list
# tup[0] = 'b'
print('-------------')
# lists have a lot of methods
print(dir(list))
print('\n\n')
# but tuples only have count and index
print(dir(tuple))
print('-------------')

for item in tup:
    print(item)
print('\n')
print('The length of tup is: ' + str(len(tup)))
print('-------------')
for i in range(len(tup)):
    print('The number of i is: ' + str(i))
    print('The tuple in index ' + str(i) +' contains: ' + str(tup[i]))
print('-------------')
# if you want to create a tuple in repl
print((1,2))
# only one element tuple(it just parenthesizes the mathematical expression
print((1))
# to create on element tuple
print((1,))
# empty tuple(do not require comma)
print(())

