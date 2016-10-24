import requests
import json

url = "http://challenge.code2040.org/api/register"

token = '<TOKEN>'

myInfo = json.dumps({'token': token, 'github': 'https://github.com/osnaldy/2040'})

headers = {'Content-type': 'application/json'}

req = requests.post(url, myInfo, headers=headers)

