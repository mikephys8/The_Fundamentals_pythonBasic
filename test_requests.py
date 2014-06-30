__author__ = 'Administrator'

import requests

r = requests.get('https://github.com/timeline.json')
data = r.json()
for item in data :
    print(item['type'])

