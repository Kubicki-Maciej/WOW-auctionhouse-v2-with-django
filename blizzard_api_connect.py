import requests
from token_api import CLIENT_SECRET, CLIENT_ID


def get_acces_token(client_id, client_secret):
    url = 'https://oauth.battle.net/token'
    data = {'grant_type': 'client_credentials'}
    auth = (client_id, client_secret)
    response = requests.post(url, data=data, auth=auth)
    access_token = response.json()['access_token']
    return access_token

def get_auction_data(realm_slug, region='eu'):
    access_token = get_acces_token(CLIENT_ID, CLIENT_SECRET)
    # /data/wow/connected-realm/{connectedRealmId}/auctions
    url = f"https://{region}.api.blizzard.com/data/wow/connected-realm/{realm_slug}/auctions"
    params = {'namespace': f'dynamic-{region}', 'locale': 'en_US', 'access_token': access_token}
    response = requests.get(url, params=params)

    if response.status_code == 200:
        auction_data = response.json()
        return auction_data
    else:
        print(f"Error fetching data: {response.status_code}")
        return None
    
def get_auction_commodities_data(region='eu'):
    access_token = get_acces_token(CLIENT_ID, CLIENT_SECRET)
    # /data/wow/connected-realm/{connectedRealmId}/auctions
    url = f"https://{region}.api.blizzard.com/data/wow/auctions/commodities"
    params = {'namespace': f'dynamic-{region}', 'locale': 'en_US', 'access_token': access_token}
    response = requests.get(url, params=params)

    if response.status_code == 200:
        auction_data = response.json()
        return auction_data
    else:
        print(f"Error fetching data: {response.status_code}")
        return None

# Example usage
# auction_data = get_auction_data('1084','eu')

# print('wait')

# [{'numer': 1312268659, 'item': {'id': 1951, 'context': 1, 'bonus_lists': [...], 'modifiers': [...]}, 'buyout': 4440000, 'quantity': 1, 'time_left': 'LONG'},{'numer': 1312268659, 'item': {'id': 1951, 'context': 1, 'bonus_lists': [...], 'modifiers': [...]}, 'buyout': 4440000, 'quantity': 1, 'time_left': 'LONG'},{'numer': 1312268659, 'item': {'id': 1951, 'context': 1, 'bonus_lists': [...], 'modifiers': [...]}, 'buyout': 4440000, 'quantity': 1, 'time_left': 'LONG'}
