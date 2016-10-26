import requests
import json
# url where the request will be sent.
url = "http://challenge.code2040.org/api/register"

token = '<TOKEN>'
#created a json dictionary that contains the token, and the url to my github Code2040 respository
myInfo = json.dumps({'token': token, 'github': 'https://github.com/osnaldy/2040'})

#information about the returned type data
headers = {'Content-type': 'application/json'}

#complete a POST request using python library 'requests'
req = requests.post(url, myInfo, headers=headers)