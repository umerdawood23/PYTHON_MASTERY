import urllib.request
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter the URL: ")

print("Retreiving:", url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()
print("Reterived:", len(data), 'characters')

# Parse the JSON data (decode bytes to string first)
info = json.loads(data.decode())

# Navigate the JSON structure
counts = info['comments']
print('Count:', len(counts))

total = 0
for item in counts:
    total = total + int(item['count'])

print('Sum:', total)