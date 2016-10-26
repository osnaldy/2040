import datetime
import json
import requests
#dictionary with the value for datestamp is a string
#formatted as an ISO 8601 datestamp the value for interval is a number of seconds.


url1 = "http://challenge.code2040.org/api/dating"
url2 = "http://challenge.code2040.org/api/dating/validate"
token = "<TOKEN>"

tokenInfo = json.dumps({"token": token})

headers = {"Content-type": "application/json"}

req1 = requests.post(url1, tokenInfo, headers=headers)

extracted = json.loads(req1.text)

#extract the array that contains the datestamp
#and also extract the array that interval integer
datestamp = extracted['datestamp']
interval = extracted['interval']

#used datatime library in order to convert the datatime to a especif format
datestamp_format = datetime.datetime.strptime(datestamp, "%Y-%m-%dT%H:%M:%SZ")
#added the seconds to the alreadt formated string
new_datestamp_format = datestamp_format + datetime.timedelta(seconds=interval)
new_datestamp_format = new_datestamp_format.strftime("%Y-%m-%dT%H:%M:%SZ")

#created a dictionary for the data that will be submitted.
dictionary = {}
dictionary['token'] = token
dictionary['datestamp'] = new_datestamp_format

req2 = requests.post(url2, json = dictionary, headers=headers)

print req2.text