# Question #1
# What is this code doing?

import requests

data = [
    {
        "breed": "Persian",
        "weight_kg": 3.78,
        "name": "Felix"
    }
]

requests.post('https://kitten-api.com/cat', data=data)
