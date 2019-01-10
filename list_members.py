import pprint
import requests

AUTH_TOKEN = 'xoxb-...'

params = {'token': AUTH_TOKEN}

r = requests.post('https://slack.com/api/users.list', params=params)

for member in r.json()['members']:
    print(member['id'], member['name'])