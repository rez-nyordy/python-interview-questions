# Question #2
# What is this code doing?

import requests

response = requests.get('https://kitten-api.com/cat', params=[('breed', 'Maine Coon')])

cats: list = response.json()

for cat in cats:
    print(cat.name)
