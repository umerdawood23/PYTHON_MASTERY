import xml.etree.ElementTree as ET

tree = ET.parse('xml_file.xml')
root = tree.getroot()

print(root)
print(len(root))

print(root[0].tag)
print(root[0].text)

for child in root:
    print (child[0].tag)
    print(child[0].text)