import json
import requests

url1 = "http://challenge.code2040.org/api/prefix"
url2 = "http://challenge.code2040.org/api/prefix/validate"
token = "c77d77461928cfefd86f1485d2c54108"
headers = {'Content-type': 'application/json'}

r = json.dumps({"token": token})

req1 = requests.post(url1, r, headers=headers)

results = json.loads(req1.text)

array = results['array']
prefix = results['prefix']
result_Array = []

for i in range(0, len(array)):

    if not(array[i].startswith(prefix)):

        result_Array.append(array[i])
print result_Array

final_results = json.dumps({"token": token, "array": result_Array})

req2 = requests.post(url2, final_results, headers=headers)
print req2.text