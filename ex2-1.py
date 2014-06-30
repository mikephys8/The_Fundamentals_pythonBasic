__author__ = 'Administrator'

def get_capital(country):
    countries = {'Canada': 'Ottawa', 'Greece': 'Athens', 'France': 'Paris',
                 'Germany': 'Berlin', 'Japan': 'Tokyo', 'Spain': 'Madrid',
                 'Norway': 'Oslo'}
    for item in countries:
        if country == item:
            return countries[item]
print(get_capital('Spain'))

print('------------------//----------------')

def longer(country1, country2):
    if len(country1) > len(country2):
        return country1
    elif len(country1) < len(country2):
        return country2
    else:
        print('They are equal')
print(longer('hello man', 'hello man'))

print('------------------//----------------')

print('The longer string comparing the ' + get_capital('Japan') + ' and ' + get_capital('Greece')+ ' is ' + longer(get_capital('Japan'), get_capital('Greece')))
