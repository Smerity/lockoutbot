import requests

AUTH_TOKEN = 'xoxb-...'

channel = '#locked-out'
USER_ID = 'UDAS0J04S'
text = f'<@{USER_ID}>, Smerity locked himself out'

params = {
    'token': AUTH_TOKEN,
    'channel': channel,
    'text': text
}

r = requests.post('https://slack.com/api/chat.postMessage', params=params)
print(r)
print(r.json())