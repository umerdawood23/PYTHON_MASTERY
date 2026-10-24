import json

Details = '{"Name":"Umer", "Age":24}'
y = json.loads(Details)

print(y)
print(type(y))

for x in y:
    print(x,y[x])