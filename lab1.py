import requests

#print(requests.__version__)
resp = requests.get("https://raw.githubusercontent.com/ShanemelAsuncion/CMPUT404_Lab/master/lab1.py")
print(resp.text)