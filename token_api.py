import json

with open('login.json', 'r') as file:
    data = json.load(file)

CLIENT_ID = data['client_id']
CLIENT_SECRET = data['client_secret']

print(CLIENT_ID, CLIENT_SECRET)