import json 

people_string = '''
{
  "people": [
    {
      "name": "John Smith",
      "phone": "615-555-7164",
      "emails": ["johnsmith@bogusemail.com", "john.smith@work-place.com"],
      "has_license": false
    },
    {
      "name": "Jane Doe",
      "phone": "560-555-5153",
      "emails": null,
      "has_license": true
    }
  ]
}
'''

"""data = json.loads(people_string)


for person in data['people']:
    del person['phone']

new_string  = json.dumps(data, indent=2, sort_keys=True)
print(new_string)"""
sum = 0  # For Storing the Sum
count = 0 # The Counter for the Numbers

with open('json.json') as f:
    data = json.load(f)

for stat in data["comments"]:
    print(stat['name'])
    print(stat['count'])
     