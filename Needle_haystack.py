import json
import requests

# url where the API dictionary will be requested
url1 = "http://challenge.code2040.org/api/haystack"
# url where the needle position found in the haystack array will be submitted
url2 = "http://challenge.code2040.org/api/haystack/validate"

token = "<TOKEN>"

#create a Json dictionary that contains the token
my_info = json.dumps({"token": token})


headers = {'Content-type': 'application/json'}

#complete a POST request using python library 'requests' to retrieve the dictionary
req = requests.post(url1, my_info, headers=headers)

#deserialize the data from the Json document
results = json.loads(req.text)
print results


haystack = results['haystack']

#iterate through the haystack array to look for any needle word
for i in range(0, len(haystack)):
#when the word needle appears, the index will be added to the index variable
    if haystack[i] == results['needle']:

        index = i

        print index
#do a Post request to the second url in order to submit the index in which the needle word was found
req1 = requests.post(url2, data={"token": token, "needle": index})

print req1.text
