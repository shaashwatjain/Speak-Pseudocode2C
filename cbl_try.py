import requests
import json
import time

"""
{
 "deviceInfo": {
  "clientId": "amzn1.application-oa2-client.66e7596a5a524d9d949475f12324b454",
  "productId": "Software"
 }
}
"""

details = dict()
details = {
    "ProductID": "Software", 
    "Client_ID": "amzn1.application-oa2-client.66e7596a5a524d9d949475f12324b454", 
    "Client_Secret": "8b039fdc0f52a9823a37bfcae611cc3b4b3b603c589f10b916d33867a9299141"
    }

scopedata = json.dumps({
            "alexa:all": {
                "productID": details['ProductID'],
                "productInstanceAttributes": {
                    "deviceSerialNumber": "987654321"
                }
            }
        })
payload = {
    "client_id": details['Client_ID'],
    "scope": "alexa:all",
    "scope_data": scopedata,
    "response_type": "device_code"
}
req = requests.post( "https://api.amazon.com/auth/O2/create/codepair", data=payload)
response = json.loads(req.text)
print(response)
#print(response["device_code"])

header = {
"Host": "api.amazon.com",
"Content-Type": "application/x-www-form-urlencoded"
}

params = {
    "grant_type":"device_code",
    "device_code":response["device_code"],
    "user_code":response["user_code"]
}

req2 = None

while not req2:
    req2 = requests.post("https://api.amazon.com/auth/O2/token",headers = header, data=params)
    print(req2)
    time.sleep(2)

print(req2.text)
