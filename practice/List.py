names = ['Ayse', 'Aysegul', 'Tugba', 'Husniye']
print(names)
names.append('Ayca')
print(names)
print(names.remove('Ayca'))
print(names)
names.insert(3, 'Leyla')
print(names)

##en sonki ekenemti getirir
names.pop()
print(names)
print(names.index('Ayse'))
print('Husniye' in names)
names.sort()
print(names)
names.reverse()
print(names)
name_list = names.copy()
print(name_list)
names.clear()
print(names)
print(name_list[1:])
print(name_list[1:2])
print(name_list[-2])
print(name_list.count("Ayse"))