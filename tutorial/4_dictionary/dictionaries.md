# Dictionaries - Working with Key-Value Pairs

<!-- TOC -->

- [Dictionaries - Working with Key-Value Pairs](#dictionaries---working-with-key-value-pairs)
  - [1. Dictionary definition](#1-dictionary-definition)
  - [2. Add a New Entry to the Dictionary](#2-add-a-new-entry-to-the-dictionary)
    - [2.1. Update Value](#21-update-value)
  - [3. Delete a Specific Key and its Value](#3-delete-a-specific-key-and-its-value)
    - [3.1. `del`](#31-del)
    - [3.2. `.pop()` method](#32-pop-method)
  - [4. Loop through the Keys and values](#4-loop-through-the-keys-and-values)
    - [4.1. Dictionary - Length, Keys, and Values](#41-dictionary---length-keys-and-values)
    - [4.2. Loop the Dictionary](#42-loop-the-dictionary)

<!-- /TOC -->

## 1. Dictionary definition

Each word that one looks up is the `key`, and the definition of that word is the `value`.

In python, a dictionary is represented by curly braces with key and value pairs `{key:value}`.

```python
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

print(student)
print(student['courses'])
```

Output:

```python
{'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
['Math', 'CompSci']
```

The `value` could be `any thing` as strings, numbers, lists, tuples, and sets. And the `key` could be `any immutable` data type.

```python
student = {1: 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

print(student[1])
```

Output:

```python
John
```

If a key doesn't exist, then it will return a `KeyError`.

```python
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

print(student['phone'])
```

Output:

```python
Traceback (most recent call last):
  File "d:\Documents\Code\python\tutorial\5_dictionary.py", line 14, in <module>
    print(student['phone'])
KeyError: 'phone'
```

Sometime, if a searching value is not in the dictionary, one would like to return `None` or a boolean value (`True` or `False`) rather than `KeyError`. The `.get()` method can solve this problem.

```python
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

print(student.get('name'))
print(student.get('phone'))
```

Output:

```python
John
None
```

We can change the output of the key that does not exist in the `.get()` method by assign a second value `.get(key, assign_output)`.

```python
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

print(student.get('phone', 'Not Found'))
```

Output:

```python
Not Found
```

## 2. Add a New Entry to the Dictionary

To add a new entry to the existed dictionary, one can directly set the value to the key of that dictionary `var_dict[key] = value`. If a key already exists, then this will update the value of that key.

```python
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

student['phone'] = '111-222-3333'
student['age'] = 22

print(student.get('phone', 'Not Found'))
print(student)
```

Output:

```python
111-222-3333
{'name': 'John', 'age': 22, 'courses': ['Math', 'CompSci'], 'phone': '111-222-3333'}
```

### 2.1. Update Value

To update multiple values at a time,
`.update()` method will do the work by `var_dict.update({key1:value1, key2:value2})`.

```python
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

student.update({'name': 'Jane', 'age': 26, 'phone': '111-222-3333'})

print(student)
```

Output:

```python
{'name': 'Jane', 'age': 26, 'courses': ['Math', 'CompSci'], 'phone': '111-222-3333'}
```

## 3. Delete a Specific Key and its Value

### 3.1. `del`

```python
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

del student['age']

print(student)
```

Output:

```python
{'name': 'John', 'courses': ['Math', 'CompSci']}
```

### 3.2. `.pop()` method

The pop method allows to remove and grab the removed variable.

```python
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

age = student.pop('age')

print(student)
print(age)
```

Output:

```python
{'name': 'John', 'courses': ['Math', 'CompSci']}
25
```

## 4. Loop through the Keys and values

### 4.1. Dictionary - Length, Keys, and Values

```python
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

print(len(student))
print(student.keys())
print(student.values())
print(student.items())
```

Output:

```python
3
dict_keys(['name', 'age', 'courses'])
dict_values(['John', 25, ['Math', 'CompSci']])
dict_items([('name', 'John'), ('age', 25), ('courses', ['Math', 'CompSci'])])
```

### 4.2. Loop the Dictionary

- Loop only the key

The direct `for` loop will gives only the `key` but not the `value`.

```python
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

for key in student:
    print(key)
```

Output:

```python
name
age
courses
```

- Loop through both key and value

By the `.items()` method, one can loop through both the keys and values of the dictionary.

```python
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

for item in student.items():
    print(item)
```

Output:

```python
('name', 'John')
('age', 25)
('courses', ['Math', 'CompSci'])
```

```python
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

for key, value in student.items():
    print(key, value)
```

Output:

```python
name John
age 25
courses ['Math', 'CompSci']
```
