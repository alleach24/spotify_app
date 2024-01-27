import api_token
import requests

f = open("current_token.txt", "r")
access_token = f.readline()
f.close()
headers = {"Authorization": "Bearer " + access_token}


url = "https://api.spotify.com/v1/search"

type_data=["playlist"]
payload = {"type":type_data}

r = requests.get(url, params=payload, headers=headers)

print(r.url)
print(r.status_code)
print(r.text)