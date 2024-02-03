import requests
import api_token

access_token = api_token.check_active_token()
headers = {"Authorization": "Bearer " + access_token}


##########################################
#### get_category_id_list
# categories_obj_list = []
url = "https://api.spotify.com/v1/browse/categories"
country_code=["US"]
payload = {"limit":50}

r = requests.get(url, params=payload, headers=headers)
categories_list = r.json()['categories']['items']
f1 = open("info/categories_list.txt", "a")
for category in categories_list:
    f1.write(category['name'] + " - " + category['id'] + "\n")
    print(category['name'] + " - " + category['id'])
    # cat_name = category['name']
    # cat_id = category['id']
    # category_obj = {'category_name': cat_name, 'category_id': cat_id}
    # categories_obj_list.append(category_obj)

# f1 = open("info/categories_list.txt", "w")
# f1.write(str(categories_obj_list))
f1.close()
##########################################