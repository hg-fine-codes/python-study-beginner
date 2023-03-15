# Loops and Iterations: For - While Loops

<!-- TOC -->

- [Loops and Iterations: For - While Loops](#loops-and-iterations-for---while-loops)
  - [1. `for` loop](#1-for-loop)
    - [1.1. `break`](#11-break)
    - [1.2. `continue`](#12-continue)
    - [1.3. Nested loop: loop within a loop](#13-nested-loop-loop-within-a-loop)
    - [1.4. `range(n)`](#14-rangen)
  - [2. `while` loop](#2-while-loop)
    - [2.1. `break` in `while` loop](#21-break-in-while-loop)
    - [2.2. Infinite loop](#22-infinite-loop)

<!-- /TOC -->

/*

- File: loops and iterations.md
- Project: 6_loops-iterations
- File Created: Sunday, 12th March 2023 9:28:08 pm
- Author: Hanlin Gu (hg_fine_codes@163.com)

- -----

- Last Modified: Wednesday, 15th March 2023 5:03:11 pm
- Modified By: Hanlin Gu (hg_fine_codes@163.com>)
 */

<div style="page-break-after:always"></div>

## 1. `for` loop

`for` loop: print all the elements in a list

```python
nums = [1, 2, 3, 4, 5]

for num in nums:
    print(num)
```

Output:

```python
1
2
3
4
5
```

### 1.1. `break`

`break` statement breaks out of the loop. It will not continue execute the code after `break` in the `for` loop.

```python
nums = [1, 2, 3, 4, 5]

for num in nums:
    if num == 3:
        print('Found!')
        break
    print(num)
```

Output:

```python
1
2
Found!
```

### 1.2. `continue`

If one wants to ignore a value without break out of the loop completely, one can use `continue` statement. `continue` will skip to the next iteration of a loop.

```python
nums = [1, 2, 3, 4, 5]

for num in nums:
    if num == 3:
        print('Found!')
        continue
    print(num)
```

Output:

```python
1
2
Found!
4
5
```

When the program meets `continue`, it goes to the next iteration directly. Without `continue`, it will run through that iteration and then go to the next one.

```python
nums = [1, 2, 3, 4, 5]

for num in nums:
    if num == 3:
        print('Found!')
    print(num)
```

Output:

```python
1
2
Found!
3
4
5
```

### 1.3. Nested loop: loop within a loop

```python
# Nested loop: loop within a loop
nums = [1, 2, 3, 4, 5]

for num in nums:
    for letter in 'abc':
        print(num, letter)
```

Output:

```python
1 a
1 b
1 c
2 a
2 b
2 c
3 a
3 b
3 c
4 a
4 b
4 c
5 a
5 b
5 c
```

### 1.4. `range(n)`

Run through a loop for a certain number of times, one can use the build in function `range()`.

```python
for i in range(10):
    print(i)
```

Output:

```python
0
1
2
3
4
5
6
7
8
9
```

If one wants to start from 1, and goes to 10, then use `range(1, 11)`.

```python
for i in range(1, 11):
    print(i)
```

Output:

```python
1
2
3
4
5
6
7
8
9
10
```

## 2. `while` loop

`while` loop runs until `certain condition` is met or get a `break`.

```python
x = 0

while x < 10:
    print(x)
    x += 1
```

Output:

```python
0
1
2
3
4
5
6
7
8
9
```

### 2.1. `break` in `while` loop

```python
x = 0

while x < 10:
    if x == 5:
        break
    print(x)
    x += 1
```

Output:

```python
0
1
2
3
4
```

### 2.2. Infinite loop

Sometimes, one would like to create an infinite loop that never ends until one gets some input or finds some values. To create an infinite loop, simply to replace the conditional statement of `while` into `True`.

```python
x = 0

while True:
    if x == 5:
        break
    print(x)
    x += 1
```

Output:

```python
0
1
2
3
4
```

If one accidentally get stucked in a infinite loop, in general `ctrl + c` will terminate the process.
