import requests
import json

json_Arr = requests.get("https://jsonplaceholder.typicode.com/comments")
json_List = json.loads(json_Arr.text)
store_list = []

for item in json_List:
    store_details = {"email": None}
    store_details['email'] = item['email']
    store_list.append(store_details)
for conteudo in store_list:
    if conteudo["email"].endswith('.org'):
        print(conteudo["email"])
