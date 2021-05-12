# Question #4
# What is this code doing?

import requests
import os

from requests.auth import HTTPBasicAuth

user = os.environ['api_user']
password = os.environ['api_password']

response = requests.get('https://kitten-api.com/cat', auth=HTTPBasicAuth(user, password))
