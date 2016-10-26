import datetime
import json
import requests

url1 = "http://challenge.code2040.org/api/dating"
url2 = "http://challenge.code2040.org/api/dating/validate"
token = "<TOKEN>"

tokenInfo = json.dumps({"token": token})

headers = {"Content-type": "application/json"}

req1 = requests.post(url1, tokenInfo, headers=headers)

extracted = json.loads(req1.text)

datestamp = extracted['datestamp']
interval = extracted['interval']


datestamp_format = datetime.datetime.strptime(datestamp, "%Y-%m-%dT%H:%M:%SZ")
new_datestamp_format = datestamp_format + datetime.timedelta(seconds=interval)
new_datestamp_format = new_datestamp_format.strftime("%Y-%m-%dT%H:%M:%SZ")

dictionary = {}
dictionary['token'] = token
dictionary['datestamp'] = new_datestamp_format

req2 = requests.post(url2, json = dictionary, headers=headers)

print req2.text


