# Import Modules and Exploring the Standard Library
<!-- TOC -->

- [Import Modules and Exploring the Standard Library](#import-modules-and-exploring-the-standard-library)
  - [1. Import](#1-import)
    - [1.1. my\_module.py](#11-my_modulepy)
    - [1.2. `import module_name`](#12-import-module_name)
    - [1.3. Shorter module name](#13-shorter-module-name)
    - [1.4. Import the Function Itself](#14-import-the-function-itself)
    - [1.5. Locations that `import` searches](#15-locations-that-import-searches)
    - [1.6. Add Python Path](#16-add-python-path)
      - [1.6.1. Direct Method: `sys.path.append('folder_address')`](#161-direct-method-syspathappendfolder_address)
      - [1.6.2. Add the Folder to Python Environment](#162-add-the-folder-to-python-environment)
        - [Mac](#mac)
        - [Windows](#windows)
  - [2. Exploring the Standard Library](#2-exploring-the-standard-library)
    - [2.1. `random` module](#21-random-module)
    - [2.2. `math` module](#22-math-module)
    - [2.3. `datetime` and `calendar` modules](#23-datetime-and-calendar-modules)
    - [2.4. `os` module](#24-os-module)
      - [2.4.1. Find the Location of a Module](#241-find-the-location-of-a-module)

<!-- /TOC -->

/*

- File: import modules-standard library.md
- Project: 8_import
- File Created: Thursday, 16th March 2023 10:18:07 pm
- Author: Hanlin Gu (hg_fine_codes@163.com)

- -----

- Last Modified: Saturday, 18th March 2023 4:27:33 pm
- Modified By: Hanlin Gu (hg_fine_codes@163.com>)
 */

<div style="page-break-after:always"></div>

## 1. Import

### 1.1. my_module.py

```python
print('Imported my_module...')

test = 'Test String'


def find_index(to_search, target):
    """Find the index of a target value in a sequence"""
    for i, value in enumerate(to_search):
        if value == target:
            return i

    return -1
```

### 1.2. `import module_name`

Put the module in the same folder as the current python file. And use `import module_name` to import the `module_name.py` file.

```python
import my_module

courses = ['History', 'Math', 'Physics', 'CompSci']

index = my_module.find_index(courses, 'Math')

print(index)
```

Output:

```script
Imported my_module...
1
```

### 1.3. Shorter module name

To make the module name shorter, one can define a shorter name by `import module_name as module_shorter`. When call the module, one can use `module_shorter` instead.

```python
import my_module as mm

courses = ['History', 'Math', 'Physics', 'CompSci']

index = mm.find_index(courses, 'Math')

print(index)
```

Output:

```script
Imported my_module...
1
```

### 1.4. Import the Function Itself

```python
from my_module import find_index

courses = ['History', 'Math', 'Physics', 'CompSci']

index = find_index(courses, 'Math')

print(index)
```

Output:

```script
Imported my_module...
1
```

One thing to **note about** this approach, it only gives access to the `find_index()` function not everything else in the module.

`as` still works to make a shortcut for a function by `from module_name import func_name as func_shorter`. But this will reduce the readability of the code, so it's not recommended to do very often.

```python
from my_module import find_index as fi, test

courses = ['History', 'Math', 'Physics', 'CompSci']

index = fi(courses, 'Math')

print(index)
print(test)
```

Output:

```script
Imported my_module...
1
Test String
```

To import every thing, one can use `from module_name import *`. This is not used very often, because it's hard to track the original `module` of a `function`.

### 1.5. Locations that `import` searches

When `import` a module or the standard library, the system is gonna check a multiple locations. And the locations that are checked, is within a list called `sys.path`.

```python
import sys
print(sys.path)
```

Output:

```script
['d:\\Documents\\Code\\python\\tutorial\\9_import modules-library', 'D:\\Program Files\\Python\\Python310\\python310.zip', 'D:\\Program Files\\Python\\Python310\\DLLs', 'D:\\Program Files\\Python\\Python310\\lib', 'D:\\Program Files\\Python\\Python310', 'D:\\Program Files\\Python\\Python310\\Lib\\site-packages', 'D:\\Program Files\\Python\\Python310\\Lib\\site-packages\\win32', 'D:\\Program Files\\Python\\Python310\\Lib\\site-packages\\win32\\lib', 'D:\\Program Files\\Python\\Python310\\Lib\\site-packages\\Pythonwin']
```

It contains the `current directory` of the script that is running, Python `path environment variable`, standard `library` directory, `site-packages` directory for 3rd party packages.

If the imported module is not in the folder, there's a `ModuleNotFoundError` appears.

```python
from my_module import find_index, test

courses = ['History', 'Math', 'Physics', 'CompSci']

index = find_index(courses, 'Math')

print(index)
print(test)
```

Output:

```script
Traceback (most recent call last):
  File "d:\Documents\Code\python\tutorial\9_import modules-library\9_import modules-standard library.py", line 40, in <module>
    from my_module import find_index, test
ModuleNotFoundError: No module named 'my_module'
```

### 1.6. Add Python Path

#### 1.6.1. Direct Method: `sys.path.append('folder_address')`

```python
# Append Path
import sys
sys.path.append('D:\Documents\Code\python\HG_modules')

from my_module import find_index

courses = ['History', 'Math', 'Physics', 'CompSci']
index = find_index(courses, 'Math')

print("The index of 'Math' in courses is {}".format(index))
# print(f"The index of 'Math' in courses is {index}")
print(sys.path)
```

Output:

```script
Imported my_module...
The index of 'Math' in courses is 1
['d:\\Documents\\Code\\python\\tutorial\\9_import modules-library', 'D:\\Program Files\\Python\\Python310\\python310.zip', 'D:\\Program Files\\Python\\Python310\\DLLs', 'D:\\Program Files\\Python\\Python310\\lib', 'D:\\Program Files\\Python\\Python310', 'D:\\Program Files\\Python\\Python310\\Lib\\site-packages', 'D:\\Program Files\\Python\\Python310\\Lib\\site-packages\\win32', 'D:\\Program Files\\Python\\Python310\\Lib\\site-packages\\win32\\lib', 'D:\\Program Files\\Python\\Python310\\Lib\\site-packages\\Pythonwin', 'D:\\Documents\\Code\\python\\HG_modules']
```

#### 1.6.2. Add the Folder to Python Environment

The above is not the best way to add the address to python, because it `append` before other `import`. It is better to change the environment variable, and doesn't need to add the `sys.path.append()` at each time modules from certain location is called.

##### Mac

In the terminal, use `nano` to change the `.bash_profile` file. `~/` means working in the `home directory`.

```shell
nano ~/.dash_profile
```

Scroll to the end of the file and set the python path.

```shell
export PYTHONPATH="/Users/your_user_name/file_location"
```

Here, `your_user_name` is your logged in user name, and `file_location` is where the module is located. **Note that**, no space in between the equal and the path.

Hit `ctrl + x`, then `y` to save the change, and `enter` to keep the same file name. Finally, to restart the terminal.

##### Windows

Right click `Computer 此电脑` $\rightarrow$ `Properties 属性` $\rightarrow$ `Advanced system settings 高级系统设置` $\rightarrow$ `Environment Variable 环境变量`

- In the `User variables 用户变量`, click `New 新建`, set `Variable name 变量名` as `PYTHONPATH`, and `Variable value` as the folder address of the self-defined modules. Finally click `ok` to save the change.

```python
import sys
print(sys.path)
```

Output:

```script
['d:\\Documents\\Code\\python\\tutorial\\9_import modules-library', 'D:\\Documents\\Code\\python\\HG_modules', 'D:\\Program Files\\Python\\Python310\\python310.zip', 'D:\\Program Files\\Python\\Python310\\DLLs', 'D:\\Program Files\\Python\\Python310\\lib', 'D:\\Program Files\\Python\\Python310', 'D:\\Program Files\\Python\\Python310\\Lib\\site-packages', 'D:\\Program Files\\Python\\Python310\\Lib\\site-packages\\win32', 'D:\\Program Files\\Python\\Python310\\Lib\\site-packages\\win32\\lib', 'D:\\Program Files\\Python\\Python310\\Lib\\site-packages\\Pythonwin']
```

The 1st address is the current working directory. It's clear that the 2nd folder is added to the python environment successfully.

## 2. Exploring the Standard Library

### 2.1. `random` module

- The `random.choice()` picks up a random element in a sequence.

```python
import random

courses = ['History', 'Math', 'Physics', 'CompSci']

random_course = random.choice(courses)

print(random_course)
```

Output:

```script
Math
```

### 2.2. `math` module

`math` is for common mathematical operations.

- Convert 90 degree to radians:

```python
import math

rads = math.radians(90)

print(rads)
print(math.sin(rads))
```

Output:

```script
1.5707963267948966
1.0
```

### 2.3. `datetime` and `calendar` modules

```python
import datetime
import calendar

today = datetime.date.today()
print(today)

print(calendar.isleap(2023))
```

Output:

```script
2023-03-17
False
```

### 2.4. `os` module

`os` gives access to the underlying operating system.

- print current working directory

```python
import os

print(os.getcwd())
```

Output:

```script
d:\Documents\Code\python\tutorial\9_import modules-library
```

`os` module has tons of other functionalities. It gives the ability to `scan` the file system, and `create` files, `delete` files.

#### 2.4.1. Find the Location of a Module

The standard library modules are simply python files. To view the location of a module, just print out its `os.__file__`.

```python
import os
import numpy as np

print(os.__file__)
print(np.__file__)
```

Output:

```script
D:\Program Files\Python\Python310\lib\os.py
D:\Program Files\Python\Python310\Lib\site-packages\numpy\__init__.py
```

And `D:\Program Files\Python\Python310\lib` is the standard library directory and it's all the standard modules that are located.
