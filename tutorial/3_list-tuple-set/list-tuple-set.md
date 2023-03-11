# Lists, Tuples, and Sets

<!-- TOC -->

- [Lists, Tuples, and Sets](#lists-tuples-and-sets)
  - [1. Lists](#1-lists)
    - [1.1. Locate the Elements in the List with index](#11-locate-the-elements-in-the-list-with-index)
    - [1.2. List Methods and Functions](#12-list-methods-and-functions)
      - [1.2.1. Add an Element](#121-add-an-element)
      - [1.2.2. Remove Items from the List](#122-remove-items-from-the-list)
      - [1.2.3. Sort List](#123-sort-list)
      - [1.2.4. Other List Functions](#124-other-list-functions)
      - [1.2.5. Find the index of certain value](#125-find-the-index-of-certain-value)
      - [1.2.6. Turn List into Strings](#126-turn-list-into-strings)
  - [2. Tuples](#2-tuples)
  - [3. Sets](#3-sets)
    - [3.1. Remove duplicates](#31-remove-duplicates)
    - [3.2. Membership test](#32-membership-test)
    - [3.3. Determine what values are shared or not shared with other set](#33-determine-what-values-are-shared-or-not-shared-with-other-set)
  - [4. Create empty lists, tuples, and Sets](#4-create-empty-lists-tuples-and-sets)

<!-- /TOC -->

/*

- File: list-tuple-set.md
- Project: 3_list-tuple-set
- File Created: Wednesday, 8th March 2023 8:16:17 am
- Author: Hanlin Gu (hg_fine_codes@163.com)

- -----

- Last Modified: Saturday, 11th March 2023 4:31:11 pm
- Modified By: Hanlin Gu (hg_fine_codes@163.com>)
 */

<div style="page-break-after:always"></div>

## 1. Lists

In python, the square brackets `[]` indicates a list, and the values are separated by comma `,`.

```python
courses = ['History', 'Math', 'Physics', 'CompSci']

print(courses)
print(len(courses))
print(type(courses))
```

Output:

```python
['History', 'Math', 'Physics', 'CompSci']
4
<class 'list'>
```

### 1.1. Locate the Elements in the List with index

The index rule is the same as in string, such that `var_name[idx]` gives you the element or part of the list with index as `idx` in the variable `var_name`.

- Python counting from `0`. The negative index `[-num]` means counting from the end. So the last item is `[-1]`.

```python
courses = ['History', 'Math', 'Physics', 'CompSci']

print(courses[0])
print(courses[-1])
```

Output:

```python
History
CompSci
```

It's convenient to use `[-1]` as the last item of a list, since this is always true even with the length of the list is changed i.e. adding new elements into the list.

If an index does not exist, it will return an `IndexError`.

```python
print(courses[4])
```

Output:

```python
Traceback (most recent call last):
  File "d:\Documents\Code\python\tutorial\list-tuple-set.py", line 11, in <module>
    print(courses[4])
IndexError: list index out of range
```

- Slicing

The index `[start:stop]` include index `[start]` but exclude `[stop]`  and return as a list. If the index is `[:stop]`, this will give you all the elements before the index `[stop]`, excluding the stop element. If the index is `[start:]`, this gives you all the elements starting from index `[start]`, including the start element, all the way to the end.

```python
courses = ['History', 'Math', 'Physics', 'CompSci']
print(courses[0:3])
print(courses[:3])
print(courses[2:])
```

Output:

```python
['History', 'Math', 'Physics']
['History', 'Math', 'Physics']
['Physics', 'CompSci']
```

### 1.2. List Methods and Functions

#### 1.2.1. Add an Element

- Add the element to the end: `var_name.append()`

```python
courses = ['History', 'Math', 'Physics', 'CompSci']
courses.append('Art') 
print(courses)
```

Output:

```python
['History', 'Math', 'Physics', 'CompSci', 'Art']
```

- Add the element to specific location in the list: `var_name.insert()`

`.insert()` takes two arguments, the first is the location, and the second is the element, i.e. `var_name.insert(loc,element)`.

```python
courses = ['History', 'Math', 'Physics', 'CompSci']
courses.insert(0, 'Art')
print(courses)
```

Output:

```python
['Art', 'History', 'Math', 'Physics', 'CompSci']
```

- Multiple values to add to the list: `var_name.extend()`

If one still use `.insert()` method,

```python
courses = ['History', 'Math', 'Physics', 'CompSci']
courses_2 = ['Art', 'Education']
courses.insert(0, courses_2)
print(courses)
```

Output:

```python
[['Art', 'Education'], 'History', 'Math', 'Physics', 'CompSci']
```

the new values are added directly as a list in the beginning rather than adding the individual values to the list.

And `.append()` also does the similar operation by putting the whole list at the end.

```python
courses = ['History', 'Math', 'Physics', 'CompSci']
courses_2 = ['Art', 'Education']
courses.append(courses_2)
print(courses)
```

Output:

```python
['History', 'Math', 'Physics', 'CompSci', ['Art', 'Education']]
```

The correct way to add all the values in the list `var_2` to the list `var_1` is to use `var_1.extend(var_2)`.

```python
courses = ['History', 'Math', 'Physics', 'CompSci']
courses_2 = ['Art', 'Education']
courses.extend(courses_2)
print(courses)
```

Output:

```python
['History', 'Math', 'Physics', 'CompSci', 'Art', 'Education']
```

#### 1.2.2. Remove Items from the List

- Direct remove of an element: `var_name.remove()`

```python
courses = ['History', 'Math', 'Physics', 'CompSci']
courses.remove('Math')
print(courses)
```

Output:

```python
['History', 'Physics', 'CompSci']
```

- `.pop()` method

`var_name.pop()` by default will remove the last element of the `var_name`, and it saved the removed value.

```python
courses = ['History', 'Math', 'Physics', 'CompSci']

popped = courses.pop()

print(popped)
print(courses)
```

Output:

```python
CompSci
['History', 'Math', 'Physics']
```

If one has a `stack` or a `queue`, then one can go through and keep popping out values until your list is empty.

#### 1.2.3. Sort List

- Reverse List: `var_name.reverse()`

```python
courses = ['History', 'Math', 'Physics', 'CompSci']
courses.reverse()
print(courses)
```

Output:

```python
['CompSci', 'Physics', 'Math', 'History']
```

- Sorting the list: `var_name.sort()`

Sort the list in alphabetic order by `var_name.sort()`.

If the list contains numbers, it will sort those in ascending order.

```python
courses = ['History', 'Math', 'Physics', 'CompSci']
nums = [1, 53, 5, 244, 72]

courses.sort()
nums.sort()

print(courses)
print(nums)
```

Output:

```python
['CompSci', 'History', 'Math', 'Physics']
[1, 5, 53, 72, 244]
```

If we want to sort the list in descending order, one could set the reverse in sort as true `var_name.sort(reverse=True)`.

```python
courses = ['History', 'Math', 'Physics', 'CompSci']
nums = [1, 53, 5, 244, 72]

courses.sort(reverse=True)
nums.sort(reverse=True)

print(courses)
print(nums)
```

Output:

```python
['Physics', 'Math', 'History', 'CompSci']
[244, 72, 53, 5, 1]
```

- Sorted the list without altering the original list: `sorted()` function

```python
courses = ['History', 'Math', 'Physics', 'CompSci']

sorted_courses = sorted(courses)

print(sorted_courses)
print(courses)
```

Output:

```python
['CompSci', 'History', 'Math', 'Physics']
['History', 'Math', 'Physics', 'CompSci']
```

This is very useful, since a lot of time you don't want to alter your original list.

#### 1.2.4. Other List Functions

- Minimum value: `min()`

- Maximum value: `max()`

- Sum of the sequence: `sum()`

```python
nums = [1, 53, 5, 244, 72]

print(min(nums))
print(max(nums))
print(sum(nums))
```

Output:

```python
1
244
375
```

#### 1.2.5. Find the index of certain value

- To find the index of a certain value one can use `var_name.index()`.

```python
courses = ['History', 'Math', 'Physics', 'CompSci']

print(courses.index('CompSci'))
```

Output:

```python
3
```

If one search a value that is not in the list, there'll be an `ValueError`.

```python
courses = ['History', 'Math', 'Physics', 'CompSci']

print(courses.index('Art'))
```

Output:

```python
Traceback (most recent call last):
  File "d:\Documents\Code\python\tutorial\list-tuple-set.py", line 53, in <module>
    print(courses.index('Art'))
ValueError: 'Art' is not in list
```

- Find if a value is in the list or not by `in` operator

```python
courses = ['History', 'Math', 'Physics', 'CompSci']

print('Art' in courses)
print('Math' in courses)
```

Output:

```python
False
True
```

This is going to be specially useful when go over the topics of `conditionals` and `if-else` statements. This can also be used to `loop` through values of the list by using a `for` loop.

```python
courses = ['History', 'Math', 'Physics', 'CompSci']

for item in courses:
    print(item)
```

Output:

```python
History
Math
Physics
CompSci
```

- Get the index and value simultaneously: `enumerate()` function

The `enumerate()` function returns two values which are the index that we are on and its value.

```python
courses = ['History', 'Math', 'Physics', 'CompSci']

for item in enumerate(courses):
    print(item)
```

Output:

```python
(0, 'History')
(1, 'Math')
(2, 'Physics')
(3, 'CompSci')
```

```python
courses = ['History', 'Math', 'Physics', 'CompSci']

for index, course in enumerate(courses):
    print(index, course)
```

Output:

```python
0 History
1 Math
2 Physics
3 CompSci
```

If one don't want to start the index at 0, one can pass a `start` value for `enumerate` function as `enumerate(var_list, start=)`

```python
courses = ['History', 'Math', 'Physics', 'CompSci']

for index, course in enumerate(courses, start=1):
    print(index, course)
```

Output:

```python
1 History
2 Math
3 Physics
4 CompSci
```

#### 1.2.6. Turn List into Strings

- Turn a list into strings separated by certain values using string method `.join()` and passes the list as argument.

To turn the list of `courses` into a string of comma separated values.

```python
courses = ['History', 'Math', 'Physics', 'CompSci']

course_str = ', '.join(courses)
print(course_str)
```

Output:

```python
History, Math, Physics, CompSci
```

- Turn a string into a list by `.split()` method

```python
courses = ['History', 'Math', 'Physics', 'CompSci']

course_str = ' - '.join(courses)

new_list = course_str.split(' - ')

print(course_str)
print(new_list)
```

Output:

```python
History - Math - Physics - CompSci
['History', 'Math', 'Physics', 'CompSci']
```

## 2. Tuples

Tuples are very similar to list, but with one major difference that we can't modify tuples. In programming, this is called mutable and immutable. Lists are mutable, but tuples are immutable .

<!-- mutable 可变的
immutable 不可变得 -->

If you need to modify your list, then this mutability is what you want.

```python
# Mutable
list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1

print(list_1)
print(list_2)

list_1[0] = 'Art'

print(list_1)
print(list_2)
```

Output:

```python
['History', 'Math', 'Physics', 'CompSci']
['History', 'Math', 'Physics', 'CompSci']
['Art', 'Math', 'Physics', 'CompSci']
['Art', 'Math', 'Physics', 'CompSci']
```

If you want a list of values that you know not to change, then we can use a `tuple`. Tuple uses parentheses `()` instead of square brackets `[]` in `list`.

```python
# Immutable
tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

tuple_1[0] = 'Art'

print(tuple_1)
print(tuple_2)
```

Output:

```python
Traceback (most recent call last):
  File "d:\Documents\Code\python\tutorial\test.py", line 20, in <module>
    tuple_1[0] = 'Art'
TypeError: 'tuple' object does not support item assignment
('History', 'Math', 'Physics', 'CompSci')
('History', 'Math', 'Physics', 'CompSci')
```

Since `tuple` is immutable, it doesn't have nearly as many methods as `list`. One can't add, delete, append values in tuple. But for loop, access values, index and all the other things expect for what mutates the elements works in tuple.

- `.sort()`, `.append()`, `.insert()`, `.extend()`, `.remove()`, `.pop()` can not be used to tuples.

- `sorted()`, `.index()`, `in`, `enumerate()`, and slicing can apply to tuples.

```python
tuple_1 = ('Math', 'Art', 'Physics', 'MatSci')

print(sorted(tuple_1))

print(tuple_1.index('Art'))

print(tuple_1[1:])

for index, course in enumerate(tuple_1, start=1):
    print(index, course)
```

Output:

```python
['Art', 'MatSci', 'Math', 'Physics']
1
('Art', 'Physics', 'MatSci')
1 Math
2 Art
3 Physics
4 MatSci
```

## 3. Sets

Sets are values that are `unordered` and with `no duplicates`. Sets use curly braces `{}`.

<!-- curly braces 大括号 -->

```python
cs_courses = {'History', 'Math', 'Physics', 'CompSci'}

print(cs_courses)
```

Output:

```python
{'Math', 'History', 'CompSci', 'Physics'}
```

However, if one run the above code again, one gets a different result.

```python
{'History', 'Physics', 'Math', 'CompSci'}
```

Unlike `list` and `tuple`, `set` doesn't care about orders. The main uses for a `set` is either to test a value is `part of the set` or to `remove duplicated values` because sets throw away duplicates.

### 3.1. Remove duplicates

Sets automatically throw away the duplicates.

```python
cs_courses = {'History', 'Math', 'Physics', 'CompSci', 'Math'}

print(cs_courses)
```

Output:

```python
{'History', 'CompSci', 'Physics', 'Math'}
```

### 3.2. Membership test

Sets do this test a lot more efficiently than lists and tuples.

```python
cs_courses = {'History', 'Math', 'Physics', 'CompSci', 'Math'}

print('Math' in cs_courses)
```

Output:

```python
True
```

Even `list` and `tuple` also has `in` operation, `set` is optimized to search for the existence of a value.

### 3.3. Determine what values are shared or not shared with other set

Notes that `.intersection()` and `.difference()` of sets return a set.

- The common values of two sets

To find the common values of sets `var_1` and `var_2`, one can use `.intersection()` method as `var_1.intersection(var_2)`.

```python
cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
art_courses = {'History', 'Math', 'Art', 'Design'}

print(cs_courses.intersection(art_courses))
```

Output:

```python
{'Math', 'History'}
```

- Values in set `var_1` but not in set `var_2`

To get the Values in set `var_1` but not in set `var_2`, `.difference()` can be used as `var_1.difference(var_2)`.

```python
cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
art_courses = {'History', 'Math', 'Art', 'Design'}

print(cs_courses.difference(art_courses))
```

Output:

```python
{'CompSci', 'Physics'}
```

- Combine the two sets

To combine the two sets `var_1` and `var_2`, one can use `.union()` method as `var_1.union(var_2)`.

```python
cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
art_courses = {'History', 'Math', 'Art', 'Design'}

print(cs_courses.union(art_courses))
```

Output:

```python
{'Design', 'Math', 'CompSci', 'Physics', 'Art', 'History'}
```

## 4. Create empty lists, tuples, and Sets

```python
# Empty Lists
empty_list = []
empty_list = list()

# Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

# Empty Sets
empty_set = {}  # This isn't right! It's a dictionary
empty_set = set()
```
