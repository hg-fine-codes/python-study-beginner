# Mutable
# list_1 = ['History', 'Math', 'Physics', 'CompSci']
# list_2 = list_1

# print(list_1)
# print(list_2)

# list_1[0] = 'Art'

# print(list_1)
# print(list_2)

# Immutable
# tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
# tuple_2 = tuple_1

# print(tuple_1)
# print(tuple_2)

# tuple_1[0] = 'Art'

# print(tuple_1)
# print(tuple_2)

# tuple examples

tuple_1 = ('Math', 'Art', 'Physics', 'MatSci')

print(sorted(tuple_1))

print(tuple_1.index('Art'))

print(tuple_1[1:])

for index, course in enumerate(tuple_1, start=1):
    print(index, course)


# .sort(), .append(), .insert(), .extend(), .remove(), .pop()
# can not be used to tuples
# print(tuple_1.sort())
# print(tuple_1.append('Education'))

# print(tuple_1.insert('Education'))
# print(tuple_1.extend(['Education', 'Mechanics']))

# print(tuple_1.remove('Art'))
# print(tuple_1.pop())
