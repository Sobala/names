students = [ 
{'first_name':  'Michael', 'last_name' : 'Jordan'},
{'first_name' : 'John', 'last_name' : 'Rosales'},
{'first_name' : 'Mark', 'last_name' : 'Guillen'},
{'first_name' : 'KB', 'last_name' : 'Tonel'}
]
for value in students:
	print value['first_name'], value['last_name']

users = {
'Students': [ 
{'first_name':  'Michael', 'last_name' : 'Jordan'},
{'first_name' : 'John', 'last_name' : 'Rosales'},
{'first_name' : 'Mark', 'last_name' : 'Guillen'},
{'first_name' : 'KB', 'last_name' : 'Tonel'}
],
'Instructors': [
{'first_name' : 'Michael', 'last_name' : 'Choi'},
{'first_name' : 'Martin', 'last_name' : 'Puryear'}
]
}
for key, data in users.items():
	print key
	for index, items in enumerate(data):
		print index, items['first_name'], items['last_name'], len(items['first_name']) + len(items['last_name'])	