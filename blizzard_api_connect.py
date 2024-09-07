import requests
from token_api import CLIENT_SECRET, CLIENT_ID


# Your Blizzard API credentials
client_id = 'your-client-id'
client_secret = 'your-client-secret'

def get_acces_token(client_id, client_server):
    url = 'https://oauth.battle.net/token'
    data = {'grant_type': 'client_credentials'}
    auth = (client_id, client_secret)
    response = requests.post(url, data=data, auth=auth)
    access_token = response.json()['access_token']

def get_auction_data(realm_slug, access_token, region='eu'):
    url = f"https://{region}.api.blizzard.com/data/wow/connected-realm/{realm_slug}/auctions"
    params = {'namespace': f'dynamic-{region}', 'locale': 'en_US', 'access_token': access_token}
    response = requests.get(url, params=params)

    if response.status_code == 200:
        auction_data = response.json()
        return auction_data
    else:
        print(f"Error fetching data: {response.status_code}")
        return None

# Example usage
auction_data = get_auction_data('draenor', access_token)
print(auction_data)