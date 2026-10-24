#Importing the Libraries that are neeeded 
import urllib.request 
import json, ssl

# Saving the service URL into a variable
serviceurl = 'https://py4e-data.dr-chuck.net/opengeo?'

#SSL Certificate Errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input("Enter the adress:")
    if (len(address)) < 1: break

    address = address.strip()
    dict_1 = dict()
    dict_1['A'] = address

    url = serviceurl + urllib.parse.urlencode(dict_1)

    print("Retreiving: ", url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Reterived:', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'features' not in js:
        print("===Donload Error===")
        print(data)
        break
    if len(js['features']) == 0: 
        print("NO values found")
        print(data)
        break

plus_code = js['features'][0]['properties']['plus_code']
print('plus code', plus_code)

