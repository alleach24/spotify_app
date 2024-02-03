import requests
import api_token

access_token = api_token.check_active_token()
headers = {"Authorization": "Bearer " + access_token}

url = "https://api.spotify.com/v1/search"

type_query = ["playlist"]
query = "emo"
limit = 50
offset = 250
payload = {'type':type_query, 'q':query, 'limit':limit, 'offset':offset}

r = requests.get(url, params=payload, headers=headers)


playlists_array = r.json()['playlists']['items']


for playlist in playlists_array:
    if playlist['description']:
        if '@gmail.com' in playlist['description']:
            print(playlist['description'])

