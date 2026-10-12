thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

print(thisdict)



rhisdictionary = {
	"lora": "Lahsan",
    "Ma": "La",
    "color": ["A", "D", "a"]
}

print(rhisdictionary)

dict_1 = {'Name':'Umer', 'Age': 24, 'Gender':'Male'}
print(dict_1)

dict_2 = {}
print(dict_2)
dict_1['Name'] = 'Dawood'
print(dict_1)

dict_3 = dict()
names = ['Umer', 'Ali', 'Bakar', 'Umer', 'Umer']
for name in names:
    if name not in dict_3:
        dict_3[name] = 1
    else:
        dict_3[name] = dict_3[name] + 1
print(dict_3)

X = dict_3.get('Umer', 0)
print(X)

