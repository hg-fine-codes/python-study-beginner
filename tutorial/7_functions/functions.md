# Functions

<!-- TOC -->

- [Functions](#functions)
  - [1. Define a function](#1-define-a-function)
    - [1.1. Function `return`](#11-function-return)
  - [2. Pass arguments to a function](#2-pass-arguments-to-a-function)
  - [3. Snippets - number of days per month](#3-snippets---number-of-days-per-month)

<!-- /TOC -->

/*

- File: functions.md
- Project: 7_functions
- File Created: Wednesday, 15th March 2023 5:09:08 pm
- Author: Hanlin Gu (hg_fine_codes@163.com)

- -----

- Last Modified: Wednesday, 15th March 2023 8:44:59 pm
- Modified By: Hanlin Gu (hg_fine_codes@163.com>)
 */

<div style="page-break-after:always"></div>

## 1. Define a function

In the `def fun_name():`, parenthesis are where the parameters are going into when the function is called.

If one would like to leave a function for later, one can use `pass` to avoid error. To execute the function, one need to add the parenthesis, otherwise it equals to the function itself.

```python
def hello_func():
    pass

print(hello_func)
```

Output:

```python
<function hello_func at 0x000001A6CB023E20>
```

```python
def hello_func():
    pass


# print(hello_func)
print(hello_func())
```

Output:

```python
None
```

```python
def hello_func():
    print('Hello Function!')


hello_func()
```

Output:

```python
Hello Function!
```

Function allow one to reuse code without repeating oneself. This is called keeping your code `DRY`.

```python
def hello_func():
    print('Hello Function.')


hello_func()
hello_func()
hello_func()
```

Output:

```python
Hello Function.
Hello Function.
Hello Function.
```

### 1.1. Function `return`

```python
def hello_func():
    return 'Hello Function.'


print(hello_func())
```

Output:

```python
Hello Function.
```

For the first time to look at a function, focus on the `input` and what's `returned` instead of understanding every details of every function does.

As we know the function `hello_func()` returns a string. Then all the methods, functions that work for string can be applied to this function as well.

```python
def hello_func():
    return 'Hello Function.'


print(hello_func().upper())
```

Output:

```python
HELLO FUNCTION.
```

## 2. Pass arguments to a function

If one defined an argument in the function, it's required to input an argument when calling that function otherwise there'll be a `TypeError`.

```python
def hello_func(greeting):
    return '{} Function.'.format(greeting)

print(hello_func())
```

Output:

```python
Traceback (most recent call last):
  File "d:\Documents\Code\python\tutorial\8_functions.py", line 35, in <module>
    print(hello_func())
TypeError: hello_func() missing 1 required positional argument: 'greeting'
```

```python
def hello_func(greeting):
    return '{} Function.'.format(greeting)


print(hello_func('Hi'))
```

Output:

```python
Hi Function.
```

Notice that this `greeting` variable doesn't affect any variable outside the function. It's only local to the function, so that one doesn't need to worry about anything that one doesn't want to affect.

Right now the `greeting` is a required argument, because it doesn't have a default value.

By setting default value for an argument, if the function doesn't have that argument given then it will use the default value instead.

```python
def hello_func(greeting, name='You'):
    return '{}, {}!'.format(greeting, name)


print(hello_func('Hi'))
print(hello_func('Hi', 'Corey'))
print(hello_func('Hi', name='Corey'))
print(hello_func(name='Corey', greeting='Hi'))
```

Output:

```python
Hi, You!
Hi, Corey!
Hi, Corey!
Hi, Corey!
```

**Note** your require `positional arguments` have to come before your `keyword arguments`. If you try to create a function with those out of order, then it will give you an error.

`*args` and `**kwargs` allow us to accept an arbitrary number of positional or keyword arguments. The name does not have to be `args` and `kwargs` but it's good to stay with convention so that it's more readable for others.

```python
def student_info(*args, **kwargs):
    print(args)
    print(kwargs)


student_info('Math', 'Art', name='John', age=22)
```

Output:

```python
('Math', 'Art')
{'name': 'John', 'age': 22}
```

`args` prints a tuple of all the positional arguments, and `kwargs` is a dictionary of all the keyword values.

Some times one might see function call with arguments using `*` or `**`. When it's used in that context, it will actually `unpack` a sequency or dictionary and pass those values into the function individually.

```python
def student_info(*args, **kwargs):
    print(args)
    print(kwargs)


courses = ['Math', 'Art']
info = {'name': 'John', 'age': 22}

student_info(courses, info)
```

Output:

```python
(['Math', 'Art'], {'name': 'John', 'age': 22})
{}
```

```python
def student_info(*args, **kwargs):
    print(args)
    print(kwargs)


courses = ['Math', 'Art']
info = {'name': 'John', 'age': 22}

student_info(*courses, **info)
```

Output:

```python
('Math', 'Art')
{'name': 'John', 'age': 22}
```

## 3. Snippets - number of days per month

The three quotes `"""Documents"""` in the `def` is called `doc string`, and it helps document what a `function` or a `class` supposes to do.

```python
# Number of days per month. First value placeholder for indexing purpose.
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year):
    """Return True for leap years, False for non-leap years."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    """Return number of days in that month in that year."""

    if not 1 <= month <= 12:
        return 'Invalid Month'

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]


print(is_leap(2023))
print(is_leap(2024))
print(days_in_month(2023, 2))
print(days_in_month(2024, 2))
```

Output:

```python
False
True
28
29
```
