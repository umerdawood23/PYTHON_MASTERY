dict_1 = dict()
names = ['Umer','Umer','Ali','Bakar','Usama']

for name in names:
    if name not in dict_1:
        dict_1[name] = 1
    else:
        dict_1[name] = dict_1[name] + 1
print(dict_1)

for name in names:
    if name not in dict_1:
        dict_1[name] = dict_1[name].get(name, 0) + 1 
print(dict_1)