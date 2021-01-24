dict = {'name':'zara','age':7, 'class':'first'}

dict['age'] = 8
dict['school'] = 'Cambrige School'

del dict['name']

print(dict)

dict.clear() # remove all entries in dictionary

print(dict)

del dict

print(dict) #delete entire dictionary