__author__ = 'Administrator'

print('sit' in 'tis')
print(len('deed') == 2)
print('bit' in 'habit')
print(len('deed') == 4)
print('----------------------')
print(len(''))
print('----------------------')
dance_style = 'Gangnam'

print(dance_style[-4])
print(dance_style[4])
print(dance_style[-3])
print(dance_style[3])
print('----------------------')
title = 'Queen'
print(title[1])
print('----------------------')
s = 'carrot'
print(s[:3])
print(s[-6:4])
print(s[-6:-3])
print(s[-1:3])
print('----------------------')
vehicle = 'car'
print(vehicle[-1] + vehicle[1] + vehicle[:1] + 'e' + vehicle)
print('----------------------')
print('apple'.upper() == 'APPLE')
print('apple'.upper().isupper())
print('12.34'.isalnum())
print('apple'.upper().islower())

print(help(str.isupper))
print(help(str.isalnum))
print(help(str.islower))
print('---------/-/-/-//-/-------------')
s = 'Apple'
s1 = '12345'
print(s.islower() or s.isupper())#<-True
print(s.lower() or s.upper() or s.isdigit())
print(s.isalpha() or s.isnumeric())#<-True
print(s.isalpha() and s.isnumeric())#<-False

print(help(str.isalpha))
print(help(str.isnumeric))
print(help(str.find))
print('----------------------')
s1 = 'address'
s2 = 's'
c = int(s1.find(s2))
print(s1.find(s2, s1.find(s2)+1))
# print(s1.count(s2))
print('---------------------------------')
digits = '0123456789'
result = 100

for digit in digits:
    result = result - int(digit)

print(result)
print('--------------------------')
digits = '0123456789'
result = 0

for digit in digits:
    result = digit

print(result)
print('----------------------------------')

digits = '0123456789'
result = ''

for digit in digits:
    result = result + digit * 2

print(result)
print('--------------------------')


