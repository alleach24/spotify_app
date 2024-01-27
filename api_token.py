import requests


def get_access_token():

     f1 = open("keys&tokens/client_id.txt", "r")
     client_id_key = f1.readline()
     f1.close()
     f2 = open("keys&tokens/client_secret.txt", "r")
     client_secret_key = f2.readline()
     f2.close()


     url = "https://accounts.spotify.com/api/token"
     #hide client stuff
     payload = dict(grant_type="client_credentials", client_id=client_id_key, client_secret=client_secret_key)
     header = {'Content-Type': 'application/x-www-form-urlencoded'}
     
     r = requests.post(url, data=payload, headers=header)

     access_token = r.json()['access_token']

     f = open("keys&tokens/current_token.txt", "w")
     f.write(access_token)
     f.close()

     return access_token

def check_active_token():
     
     f = open("keys&tokens/current_token.txt", "r")
     access_token = f.readline()
     f.close()

     # make some api call
     url = "https://api.spotify.com/v1/search"
     headers = {"Authorization": "Bearer " + access_token}
     type_data=["playlist"]
     payload = {"type":type_data}
     r = requests.get(url, params=payload, headers=headers)
     
     if r.status_code == 401:
          get_access_token()
          f = open("keys&tokens/current_token.txt", "r")
          access_token = f.readline()
          f.close()
          return access_token
     
     return access_token