import requests
import json
import time

url = "https://api.amazon.com/auth/O2/create/codepair"

obj = {
    "response_type":"device_code",
    "client_id":"amzn1.application-oa2-client.9c67ffcb9f9a419d82576fdc04f0ad20",
    "scope":"alexa:all",
    "scope_data":
    {
        "alexa:all": {
            "productID": "Software",
            "productInstanceAttributes": {
                "deviceSerialNumber": "jdfhb"
            }
        }
    }   
}

headers1 = {'Content-Type': 'application/x-www-form-urlencoded'}

x = requests.post(url, data = obj, headers=headers1)

print(x.text)

time.sleep(60)

url2 = 'https://api.amazon.com/auth/o2/token'

headers2 = {
'Host':'api.amazon.com',
'Content-Type': 'application/x-www-form-urlencoded'}

temp = json.loads(x.text)

obj2 = {
    'grant_type':'device_code',
    'device_code':temp['device_code'],
    'user_code':temp['user_code']
}

x2 = requests.post(url2, data = obj2, headers=headers2)

print(x2.text)