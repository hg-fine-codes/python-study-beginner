# How to Write String in Python

/*

* File: string_learn.md
* Project: tutorial
* File Created: Friday, 3rd March 2023 12:18:41 pm
* Author: Hanlin Gu (hg_fine_codes@163.com)
* -----
* Last Modified: Friday, 3rd March 2023 4:34:15 pm
* Modified By: Hanlin Gu (hg_fine_codes@163.com>)
 */

<!-- TOC -->

* [1. string](#1-string)
  * [1.1. What is String in Python](#11-what-is-string-in-python)
  * [1.2. Length of String](#12-length-of-string)
  * [1.3. Slicing of String](#13-slicing-of-string)
  * [1.4. String Methods](#14-string-methods)

<!-- /TOC -->

<div style="page-break-after:always"></div>

## 1. string

### 1.1. What is String in Python

To indicate string, one can use single quote `'` or double quote `"` or triple quote `"""`. Depending on what is in the string, if there is single or double quote in the string, it is recommended to use triple quote from the outside.

```python
print('Hello World')
```

Output:

```script
Hello World
```

To make `print()` shorter, one can define a variable like `message` to store the string information. And the print that variable instead `print(message)`.

```python
message = """Tom says it's "Bobby's World"!"""
print(message)
```

Output:

```script
Tom says it's "Bobby's World"!
```

### 1.2. Length of String

To get the length of string is `len()`.

```python
message = 'Hello World'
print(len(message))
```

Output

```script
11
```

### 1.3. Slicing of String

Partition of string is to write the variable followed by brackets with numbers inside `var_name[]`.

In python, the number counting `starts from 0`. One specific number `[n]` means to get that letter at the specific position `n+1`.

`[-n]` means counting from the end, for example `[-1]` is the last letter.

`[start:stop]` means the string that starts from `start` to the `stop`, but include the `start`  and exclude the `stop`.

`[:stop]` give the letters from the beginning to the `stop` which is equivalent to `[0:stop]`.

Similarly, `[start:]` means all the letters from the `start` to the last letter of the string.

```python
message = 'Hello World'
print(message[0])
print(message[-2])
print(message[0:5])
print(message[:5])
print(message[6:])
```

Output

```script
H
l
Hello
Hello
World
```

### 1.4. String Methods

The use of different methods, return a new string with the methods applied.

* all lower case: `var_name.lower()`

* all upper case: `var_name.upper()`

* count certain number of characters: `var_name.count()`

`count()` takes a string as an argument.

* find certain index: `var_name.find()`

`found()` also takes a string argument, and returns where that string `starts`. If a string is not find, then it will return `-1`.

```python
message = 'Hello World'
print(message.lower())
print(message.upper())
print(message.count('Hello'))
print(message.count('l'))
print(message.find('World'))
print(message.find('abc'))
```

Output:

```script
hello world
HELLO WORLD
1
3
6
-1
```

* replace some characters by other characters: `var_name.replace(var1,var2)`

`replace(var1,var2)` takes two variables, the first variable `var1` is the string that one wants to be replaced and the second variable `var2` is the string to replace the original string.

```python
message = 'Hello World'
new_message = message.replace('World','Universe')
print(message)
print(new_message)
```

Output:

```script
Hello World
Hello Universe
```

If one set the replaced string as the old string, then the old string will be changed.

```python
message = 'Hello World'
message = message.replace('World','Universe')
print(message)
```

Output:

```script
Hello Universe
```

* Add multiple strings and concatenate them together

(1) Use `+` to connect two strings

```python
greeting = 'Hello'
name = 'Michael'

message = greeting + name

print(message)
```

Output:

```script
HelloMichael
```

However, there is no space between the two strings and it's very easy to make mistakes like this during concatenation.

```python
greeting = 'Hello'
name = 'Michael'

message = greeting + ', ' + name

print(message)
```

Output:

```script
Hello, Michael
```

(2) formatted string `format()`

But, if the sentience is long, it's hard to keep track of the variables to write in this way.

```python
greeting = 'Hello'
name = 'Michael'

message = greeting + ', ' + name + '. Welcome!'

print(message)
```

Output:

```script
Hello, Michael. Welcome!
```

To write the sentence above, one would use method `format()` by leaving the placeholder `{}` in the string to take the places of the variables and add the variable names in the brackets of `format()` in orders.

```python
greeting = 'Hello'
name = 'Michael'

message = '{}, {}. Welcome!'.format(greeting, name)

print(message)
```

Output:

```script
Hello, Michael. Welcome!
```

This is easier to read.

(3) f strings: for Python 3.6 and above

This f string method is very convenient to use since it can also combine other methods. In the `format()` method, this also works.

```python
greeting = 'Hello'
name = 'Michael'

message1 = f'{greeting}, {name}. Welcome!'
message2 = f'{greeting}, {name.upper()}. Welcome!'

print(message1)
print(message2)
```

Output:

```script
Hello, Michael. Welcome!
Hello, MICHAEL. Welcome!
```

* all methods available for the variable: `dir(vir_name)`

```python
greeting = 'Hello'
name = 'Michael'

print(dir(name))
```

Output:

```script
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
```

* How does the String Methods Work `help(obj_type)`

```python
print(help(str))
```

For certain method, `help(obj_type.method_name)`

```python
print(help(str.rsplit))
```

Output:

```script
rsplit(self, /, sep=None, maxsplit=-1)
    Return a list of the words in the string, using sep as the delimiter string.
    
      sep
        The delimiter according which to split the string.
        None (the default value) means split according to any whitespace,
        and discard empty strings from the result.
      maxsplit
        Maximum number of splits to do.
        -1 (the default value) means no limit.
    
    Splits are done starting at the end of the string and working to the front.

None
```
