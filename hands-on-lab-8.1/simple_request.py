import requests
# Making a GET request
myobj = {
    "username": "",
    "password": "",
}
r = requests.post('http://85.245.94.213:7777/login', json=myobj)

# check status code for response received
# success code - 200
print(r)
# print content of request
print(r.content)