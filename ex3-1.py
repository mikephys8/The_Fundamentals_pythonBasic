__author__ = 'Administrator'
import math

# print(dir(math))
# print(help(math.ceil))

print(math.ceil(84.2))
print('-------------------------------------------')

def traffic_report(light):
    if light == 'red':
        return 'stop'
    elif light == 'yellow':
        return 'slow'
    elif light == 'green':
        return 'go'

print(traffic_report('yellow'))
print('-------------------------------------------')

def fruit_color(fruit):
    if fruit == 'apple':
        return 'red'
    elif fruit == 'banana':
        return 'yellow'
    elif fruit == 'pear':
        return 'green'

print(fruit_color('peach'))
print('-------------------------------------------')

def weather_report(temp):
    if temp >= 20:
        return 'warm enough for ice cream'
    elif temp >= 0:
        return 'above freezing'

print(weather_report(20))
print(weather_report(10))
print(weather_report(-5))
print(weather_report(30))
print('-------------------------------------------')