import ssl
from urllib.request import urlopen
from bs4 import BeautifulSoup

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Prompt user for URL, count, and position
url = input("Enter URL: ")
count = int(input("Enter count: "))
position = int(input("Enter position: "))

print("Retrieving:", url)

# Repeat the process 'count' times
for i in range(count):
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")

    # Retrieve all of the anchor tags
    tags = soup("a")
    
    # Get the tag at the specified position (position is 1-indexed, Python list is 0-indexed)
    target_tag = tags[position - 1]
    
    # Extract the href attribute (the next URL) and the name inside the tag contents
    url = target_tag.get("href", None)
    name = target_tag.contents[0]
    
    print("Retrieving:", url)

print("The answer to the assignment is:", name)