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

data = json.loads(people_string)


for person in data['people']:
    print("Name:" , person['name'])
    print("Phone:" , person['phone'])
    print("Emails:" , person['emails'])
    print("Has_license:" , person['has_license'])