import json
import requests

url1 = "http://challenge.code2040.org/api/haystack"
url2 = "http://challenge.code2040.org/api/haystack/validate"

token = "<TOKEN>"

my_info = json.dumps({"token": token})


headers = {'Content-type': 'application/json'}

req = requests.post(url1, my_info, headers=headers)

results = json.loads(req.text)
print results

haystack = results['haystack']

for i in range(0, len(haystack)):

    if haystack[i] == results['needle']:

        index = i

        print index

req1 = requests.post(url2, data={"token": token, "needle": index})

print req1.text
