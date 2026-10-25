import json

try:
    File = input("Enter the file name: ")
except FileNotFoundError:
    print("File do not found!")

data = json.loads(File)
for num in data['items']:
    del num['in_stock']
new_file = updated_inventory
new_file = json.dump(new_file)
