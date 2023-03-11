# Conditionals and Booleans: If, else, Elif Statements

<!-- TOC -->

- [Conditionals and Booleans: If, else, Elif Statements](#conditionals-and-booleans-if-else-elif-statements)
  - [1. Conditionals](#1-conditionals)
    - [1.1. if statement](#11-if-statement)
    - [1.2. Else statement](#12-else-statement)
    - [1.3. Elif: check multiple statements](#13-elif-check-multiple-statements)
  - [2. Boolean Operations](#2-boolean-operations)
  - [3. Object identity: `is`](#3-object-identity-is)
  - [4. False Values](#4-false-values)

<!-- /TOC -->

/*

- File: conditional-booleans_if-else-elif.md
- Project: 5_conditional-booleans
- File Created: Saturday, 11th March 2023 5:14:43 pm
- Author: Hanlin Gu (hg_fine_codes@163.com)

- -----

- Last Modified: Saturday, 11th March 2023 8:50:51 pm
- Modified By: Hanlin Gu (hg_fine_codes@163.com>)
 */

## 1. Conditionals

### 1.1. if statement

```python
if True:
    print('Conditional was True')
```

Output:

```python
Conditional was True
```

The print is only executed when the statement of `if` is `True`. When the statement is `False`, it will not process the print() function.

```python
if False:
    print('Conditional was True')
```

Output:

```python
```

Conditionals are usually not hard coded as above. One usually write some code that evaluated to `True` or `False` like a `boolean` statement.

```python
language = 'Python'

if language == 'Python':
    print('Conditional was True')
```

Output:

```python
Conditional was True
```

```python
# Comparison:
# Equal:            ==
# Not equal:        !=
# Greater than:     >
# Less than:        <
# Greater or equal: >=
# Less or equal:    <=
# Object identity:  is
```

The object identity `is` checks whether the two variables have the same object in memory.

### 1.2. Else statement

```python
language = 'Python'

if language == 'Python':
    print('Language is Python')
else:
    print('No Match')
```

Output:

```python
Language is Python
```

```python
language = 'Java'

if language == 'Python':
    print('Language is Python')
else:
    print('No Match')
```

Output:

```python
No Match
```

### 1.3. Elif: check multiple statements

`elif` statement could check for multiple statements.

```python
# Check if the language is either Python or Java or JavaScript
# if none of those return 'No Match'

language = 'Java'

if language == 'Python':
    print('Language is Python')
elif language == 'Java':
    print('Language is Java')
elif language == 'JavaScript':
    print('Language is JavaScript')
else:
    print('No Match')
```

Output:

```python
Language is Java
```

Python doesn't have switch case.

## 2. Boolean Operations

`and`, `or`, and `not`

- `and`

`and`: only both of the statements are true returns true.

```python
user = 'Admin'
logged_in = True

if user == 'Admin' and logged_in:
    print('Admin Page')
else:
    print('Bad Creds')
```

Output:

```python
Admin Page
```

```python
user = 'Admin'
logged_in = False

if user == 'Admin' and logged_in:
    print('Admin Page')
else:
    print('Bad Creds')
```

Output:

```python
Bad Creds
```

- `or`

`or`: at least one of the statements is true will return true.

```python
user = 'Admin'
logged_in = False

if user == 'Admin' or logged_in:
    print('Admin Page')
else:
    print('Bad Creds')
```

Output:

```python
Admin Page
```

- `not`

`not`: switch a boolean

```python
user = 'Admin'
logged_in = False

if not logged_in:
    print('Please Log In')
else:
    print('Welcome')
```

Output:

```python
Please Log In
```

## 3. Object identity: `is`

`is` means the two variables are actually the same object in memory. `a is b` is essentially `id(a) == id(b)`

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
print(a is b)
```

Output:

```python
True
False
```

One can find the identity by `id()` function.

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(id(a))
print(id(b))
print(a is b)
```

Output:

```python
2355797972480
2355798349632
False
```

```python
a = [1, 2, 3]
b = a

print(id(a))
print(id(b))
print(a is b)
```

Output:

```python
2168446473728
2168446473728
True
```

## 4. False Values

For the list of `False` values below, the statement is `False`. But for `everything else` it will return as `True`

```python
# False Values:
    # False
    # None
    # Zero of any numeric type
    # Any empty sequency. For example, '', [], ().
    # Any empty mapping (Dictionary). For example, {}.
```

```python
condition = False

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')
```

Output:

```python
Evaluated to False
```

Notice that, if `condition = 0 or 0.0`, it is also a `False` statement.

```python
condition = 0

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')
```

Output:

```python
Evaluated to False
```

```python
condition = ' '

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')
```

Output:

```python
Evaluated to True
```
