import json
import requests

#url where the API will provide the dictionary containing
#The first value prefix is a string. The second value array is an array of strings.
url1 = "http://challenge.code2040.org/api/prefix"
#POST a dictionary here:
url2 = "http://challenge.code2040.org/api/prefix/validate"
token = "<TOKEN>"
headers = {'Content-type': 'application/json'}

#create a Json dictionary that contains the token
r = json.dumps({"token": token})
#request to retrieve the dictionary
req1 = requests.post(url1, r, headers=headers)

#deserialize the resulted data from the json document
results = json.loads(req1.text)


array = results['array']
prefix = results['prefix']
result_Array = []

#loop through the length of the array
for i in range(0, len(array)):
    #loop for strings that do not contain prefix and add them to a new array.
    if not(array[i].startswith(prefix)):

        result_Array.append(array[i])
print result_Array

#create another json dictionary that contains the data that will be submitted to the API
final_results = json.dumps({"token": token, "array": result_Array})

#make a final http POST request to send the data collected
req2 = requests.post(url2, final_results, headers=headers)
print req2.text