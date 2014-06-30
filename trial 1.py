__author__ = 'Administrator'


# a=5
#
# b=8
#
# if a>b:
#     print ("True")
# elif:
#     print ("False")

def square_return(num):
    return num ** 2


def square_print(num):
    print("The square of num is", num ** 2)


def area(base, height):
    '''(number, number) -> number

    Return the area of a triangle with dimensiosn
    base and height.
    '''

    return base * height / 2


def convert_to_celsius(fahrenheit):
    ''' (number) -> float

    Returns the number of Celsius degrees equivalent to fahrenheit degrees.
    '''
    return (fahrenheit - 32) * 5 / 9


def convert_to_minutes(num_hours):
    ''' (int) -> int
    Return the number of minutes there are in num_hours hours!
    >>> convert_to_minutes(2)
    120
    '''
    result = num_hours * 60
    return result


def convert_to_seconds(num_hours):
    ''' (int) -> int
    Return the number of seconds there are in num_hours hours!
    >>> convert_to_seconds(2)
    7200
    '''
    minutes = convert_to_minutes(num_hours)
    seconds = minutes * 60
    return seconds


seconds = convert_to_seconds(2)

dir(math)



