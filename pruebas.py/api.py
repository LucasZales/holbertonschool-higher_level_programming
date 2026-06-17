#!/usr/bin/python3
import requests

url = "https://www.google.com/"
response = requests.get(url)

print(response)