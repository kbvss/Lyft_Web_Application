import requests

url = 'https://lyft-interview-test.glitch.me/test'
myjson = {"string_to_cut": "iamyourlyftdriver"}

r = requests.post(url, json = myjson)

print(r.text)
