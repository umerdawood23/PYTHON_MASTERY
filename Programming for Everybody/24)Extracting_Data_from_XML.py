import urllib.request
import xml.etree.ElementTree as ET 

url = input("Enter the url: ")
if len(url) < 1:
    url = "https://py4e-data.dr-chuck.net/comments_2479198.xml"

print("Retrieving:", url)                       # Printing the Retrieving URL
uh = urllib.request.urlopen(url)                # Storing the URL in the URL variable and also requesting the URLOPEN
data = uh.read()                                # Reading and storing the data

print("Retrieved:", len(data), "characters")    # Printing the Retrived characters and numbers
tree = ET.fromstring(data)                          

# Use './/count' for the XPath selector
counts = tree.findall('.//count')
nums = list()

for result in counts:
    # Convert text to integer and append to our list
    nums.append(int(result.text))

print('Count:', len(nums))
print('Sum:', sum(nums))