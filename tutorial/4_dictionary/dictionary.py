# Dictionary

student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

# student = {'name': 'John', 'age': 25, 'courses': ('Math', 'CompSci')}

# student = {'name': 'John', 'age': 25, 'courses': {'Math', 'CompSci'}}

# student = {1: 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

# print(student)
# print(student['courses'])

# print(student['phone'])

# print(student.get('name'))
# print(student.get('phone'))

# Add new entry
# student['phone'] = '111-222-3333'
# student['age'] = 22

# print(student.get('phone', 'Not Found'))
# print(student)

# student.update({'name': 'Jane', 'age': 26, 'phone': '111-222-3333'})

# Remove key and value
# del student['age']

# age = student.pop('age')

# print(student)
# print(age)

# Loop keys and values
# print(len(student))
# print(student.keys())
# print(student.values())
# print(student.items())

# for key in student:
#     print(key)

# for item in student.items():
#     print(item)

for key, value in student.items():
    print(key, value)
