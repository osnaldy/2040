import requests
import json

# url where the API string will be requested
url_reverse = "http://challenge.code2040.org/api/reverse"
# url where the reversed string will be submitted
url_validate = "http://challenge.code2040.org/api/reverse/validate"

token = '<TOKEN>'
#information about the returned type data
headers = {'Content-type': 'application/json'}

#create a Json dictionary that contains the token
myToken = json.dumps({"token": token})

#complete a POST request using python library 'requests' in order to retrieve the string from the API
req1 = requests.post(url_reverse, myToken, headers=headers)

message = []

#used python built-in function reversed() to reverse the retrieve string
for i in reversed(req1.text):
    message.append(i)
reverse =''.join(message)
print reverse

#made a second http post request to validate the reversed string
req2 = requests.post(url_validate, data={"token": token, "string": reverse})
print req2.content