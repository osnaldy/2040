import requests
import json

url_reverse = "http://challenge.code2040.org/api/reverse"
url_validate = "http://challenge.code2040.org/api/reverse/validate"

token = '<TOKEN>'

headers = {'Content-type': 'application/json'}

myToken = json.dumps({"token": token})

req1 = requests.post(url_reverse, myToken, headers=headers)

message = []

for i in reversed(req1.text):
    message.append(i)
reverse =''.join(message)
print reverse

req2 = requests.post(url_validate, data={"token": token, "string": reverse})
print req2.content