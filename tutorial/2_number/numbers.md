# Numbers in Python

/*

* File: numbers.md
* Project: 2_numbers
* File Created: Tuesday, 7th March 2023 10:50:46 am
* Author: Hanlin Gu (hg_fine_codes@163.com)
* -----
* Last Modified: Tuesday, 7th March 2023 6:31:22 pm
* Modified By: Hanlin Gu (hg_fine_codes@163.com>)
 */

<!-- TOC -->

* [Numbers in Python](#numbers-in-python)
  * [1. Integers and Floats](#1-integers-and-floats)
    * [1.1. Arithmetic Operators](#11-arithmetic-operators)
      * [1.1.1. Check even or odd number by `a % 2`](#111-check-even-or-odd-number-by-a--2)
    * [1.2. Operators in `operator`](#12-operators-in-operator)
    * [1.3. Order of operations](#13-order-of-operations)
    * [1.4. Increment a Variable](#14-increment-a-variable)
    * [1.5. Build-in functions to work with numbers](#15-build-in-functions-to-work-with-numbers)
  * [2. Numbers vs. String](#2-numbers-vs-string)

<!-- /TOC -->

<div style="page-break-after:always"></div>

## 1. Integers and Floats

The build in method `type()` gives one the type of the variable.

```python
num = 3

print（type(num)）
```

Output:

```python
<class 'int'>
```

```python
num = 3.0

print(type(num))
```

Output:

```python
<class 'float'>
```

### 1.1. Arithmetic Operators

```python
# Arithmetic Operators
# Addition:         3 + 2
# Subtraction:      3 - 2
# Multiplication:   3 * 2
# Division:         3 / 2
# Floor Division:   3 // 2
# Exponent:         3 ** 2
# Modulus：         3 % 2
```

```python
print(3 + 2)
print(3 - 2)
print(3 * 2)
print(3 / 2)
print(3 // 2)
print(3 ** 2)
print(3 % 2)
```

Output:

```python
5
1
6
1.5
1
9
1
```

Note that in Python 2, `3 / 2` gives `1` which is the floor of `3 / 2`. But in Python 3, `3 / 2` gives the right answer `1.5`.

`floor` of a number `n` means the largest integer that is less than `n`.

`ceil` of a number `n` means the smallest integer that is bigger than `n`.

For negative numbers, the floor division gives the same result. However, the modulo operator `%` gives different answers based on where the negative number is.

```python
print(-5 // 2)
print(5 // -2)
print(5 // 2)
print(-5 // -2)
```

Output:

```python
-3
-3
2
2
```

modulo `a % b` is calculated by $a = b*c + r$, where `c` is an integer and `r` is the modulus. The rule is that `b` and `r` have the same sign, which means that if `b` is negative then `r` is also negative. The sign of `r` has no relationship with `a`.

```python
print(5 % 2)
print(-5 % 2)
print(5 % -2)
print(-5 % -2)
```

Output:

```python
1
1
-1
-1
```

```python
print(5 % 3)
print(-5 % 3)
print(5 % -3)
print(-5 % -3)
```

Output:

```python
2
1
-1
-2
```

> Reference:
>
> [python 模的运算 根本概念](https://www.bilibili.com/read/cv6406588/)
>
> [python中remainder_从C++和Python除法的区别谈谈求模(Modulus)和取余(Remainder)
](https://blog.csdn.net/weixin_39765588/article/details/111449037?ops_request_misc=&request_id=&biz_id=102&utm_term=modulus%20python&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduweb~default-1-111449037.142^v73^wechat,201^v4^add_ask,239^v2^insert_chatgpt&spm=1018.2226.3001.4187)

#### 1.1.1. Check even or odd number by `a % 2`

If `a % 2` equals to `0` then `a` is even. If `a % 2` is `1` means `a` is odd.

```python
print(2 % 2)
print(3 % 2)
print(4 % 2)
print(5 % 2)
print(-5 % 2)
```

Output:

```python
0
1
0
1
1
```

### 1.2. Operators in `operator`

> Reference:
>
> [Python 教程之运算符（9）—— Python 中的运算符函数](https://blog.csdn.net/m0_73720982/article/details/126917992?ops_request_misc=&request_id=&biz_id=102&utm_term=modulus%20python&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduweb~default-3-126917992.142^v73^wechat,201^v4^add_ask,239^v2^insert_chatgpt&spm=1018.2226.3001.4187)

The arithmetic operators can also be written as

```python
import operator as op

print(op.add(3, 2))  # summation 3 + 2
print(op.sub(3, 2))  # subtraction 3 - 2
print(op.mul(3, 2))  # multiplication 3 * 2
print(op.truediv(3, 2))  # true division 3 / 2
print(op.floordiv(3, 2))  # floor division 3 // 2
print(op.pow(3, 2))  # exponent 3 ** 2
print(op.mod(3, 2))  # modulo operator: modulus of 3 / 2
```

Output:

```python
5
1
6
1.5
1
9
1
```

The comparison operators are

```python
import operator as op

print(op.lt(3, 2))  # check if 3 is less than 2
print(op.gt(3, 2))  # check if 3 is greater than 2
print(op.le(3, 2))  # check if 3 is less or equal to 2
print(op.ge(3, 2))  # check if 3 is greater or equal to 2
print(op.eq(3, 2))  # check if 3 is equal to 2
print(op.ne(3, 2))  # check if 3 is not equal to 2
```

Output:

```python
False
True
False
True
False
True
```

### 1.3. Order of operations

The order of operation is the same as arithmetic operations. And brackets have the priority of calculation.

### 1.4. Increment a Variable

```python
num = 1
num = num + 1
print(num)
```

Output:

```python
2
```

```python
num = 1
num += 1
print(num)
```

Output:

```python
2
```

And one can use this syntax to other operators as well.

```python
num = 1
num *=5
print(num)
```

Output:

```python
5
```

### 1.5. Build-in functions to work with numbers

* Absolute value: `abs()`

```python
print(abs(-2))
```

Output:

```python
2
```

* Round the value to the nearest integer: `round()`

```python
print(round(2.49))
print(round(2.50))
print(round(2.51))
```

Output:

```python
2
2
3
```

```python
print(round(-2.49))
print(round(-2.50))
print(round(-2.51))
```

Output:

```python
-2
-2
-3
```

`round()` function can take a second argument to show how many digits one would like to round to.

Round to the first digit after the decimal.

```python
print(round(2.50, 1))
print(round(2.75, 1))
```

Output:

```python
2.5
2.8
```

However, `round(num, 0)` gives the round value of num and returns as float.

```python
print(round(2.50, 0))
print(round(2.51, 0))
```

Output:

```python
2.0
3.0
```

* Comparison operators

Comparison will return `boolean` value which is `true` or `false`.

```python
# Comparison
# Equal:            3 == 2
# Not Equal:        3 != 2
# Greater Than:     3 > 2
# Less Than:        3 < 2
# Greater or Equal: 3 >= 2
# Less or Equal:    3 <= 2
```

```python
num_1 = 3
num_2 = 2

print(num_1 == num_2)
print(num_1 != num_2)
print(num_1 > num_2)
print(num_1 < num_2)
print(num_1 >= num_2)
print(num_1 <= num_2)
```

Output:

```python
False
True
True
False
True
False
```

Notice that single equal `=` is assignment, the double equal `==` means compare whether the two values are equal or not. The exclamation mark equal `!=` means not equal.

<!-- exclamation mark 感叹号 -->

## 2. Numbers vs. String

Some of the variables may look like numbers but indeed are strings.

```python
num_1 = '100'
num_2 = '200'

print(num_1 + num_2)
```

Output:

```python
100200
```

This is essentially two strings concatenated together by `+`, rather than the plus operation for two numbers.

To convert the string to numbers, one can use `casting`.

> Reference
>
> [Type Casting in Python (Implicit and Explicit) with Examples](https://www.geeksforgeeks.org/type-casting-in-python-implicit-and-explicit-with-examples/)

```python
num_1 = '100'
num_2 = '200'

num_1 = int(num_1)
num_2 = int(num_2)

print(num_1 + num_2)
```

Output:

```python
300
```
