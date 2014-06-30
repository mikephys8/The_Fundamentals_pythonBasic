__author__ = 'Administrator'

for i in range(10):
    print(i)
help(range)

# for presenting only odd indices starting at 1, ending at 11-1, with pace 2
for i in range(1, 11, 2):
    print(i)
print('\n\n')
# for presenting only even indices starting at 0, ending at 11-1, with pace 2
for i in range(0, 11, 2):
    print(i)

for i in range(10, 101, 20):
    print(i)
print('--------------------------------')
s = 'computer science'
print(len(s))
print('\n')
for i in range(len(s)):
    print(i)