import requests

AUTH_TOKEN = 'xoxb-'

channel = '#locked-out'
USER_ID = 'UDAS0J04S' # A user ID obtained by `list_members.py`
text = f'<@{USER_ID}>, Smerity locked himself out'

params = {
    'token': AUTH_TOKEN,
    'channel': channel,
    'text': text
}

r = requests.post('https://slack.com/api/chat.postMessage', params=params)
# You can print the response to see if it succeeded - expecting a 200
print(r)
# The Slack response itself may actually be an error however
# 'ok' will be true or false depending on whether an error was triggered
print(r.json())