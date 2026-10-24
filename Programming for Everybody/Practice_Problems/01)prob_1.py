import json

employees_json = '''
{
  "company": "TechCorp",
  "employees": [
    {"name": "Alice Johnson", "department": "Engineering", "has_license": true, "email": "alice@tech.com"},
    {"name": "Bob Smith", "department": "Marketing", "has_license": false, "email": "bob@tech.com"},
    {"name": "Charlie Brown", "department": "Engineering", "has_license": true, "email": "charlie@tech.com"}
  ]
}
'''


data = json.loads(employees_json)
for num in data["employees"]:
    if num["has_license"]:  
        print(num['name'])