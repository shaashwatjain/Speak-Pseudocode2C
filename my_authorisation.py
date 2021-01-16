import requests
import json

details = dict()
details = {
    "ProductID": "Software", 
    "Client_ID": "amzn1.application-oa2-client.9c67ffcb9f9a419d82576fdc04f0ad20", 
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
    "response_type": "code"
}
req = requests.get( "https://www.amazon.com/ap/oa", params=payload)
print(req.json)

payload = {
    "client_id": details['Client_ID'],
    "client_secret": details['Client_Secret'],
    "code": code,
    "grant_type": "authorization_code",
    "redirect_uri": callback
}
url = "https://api.amazon.com/auth/o2/token"
r = requests.post(url, data=payload)
resp = r.json()