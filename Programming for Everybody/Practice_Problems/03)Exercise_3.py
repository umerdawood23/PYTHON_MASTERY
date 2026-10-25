import urllib.request
import json, ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
#Using While Loop to make sure that we Loop into the program
while True:
    url = input("Enter the URL: ")
    if len(url) < 1: break

    data = urllib.request.urlopen(url)
    data_1 = data.read().decode()
    data_2 = json.loads(data_1)
    print("Retrieved:", len(data_2), 'characters')
    break

    for num in data:
        print(num["userId"])
        print(num["id"])
        print(num["title"])
        print(num["body"])
