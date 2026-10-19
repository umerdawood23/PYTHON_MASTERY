# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the span tags
tags = soup('span')
total_sum = 0
count = 0

for tag in tags:
    # Extract the text content from the span tag, convert to integer, and add to sum
    try:
        number = int(tag.text)
        total_sum = total_sum + number
        count = count + 1
    except ValueError:
        # Ignore any spans that don't contain valid numbers
        continue

print("Count:", count)
print("Sum:", total_sum)