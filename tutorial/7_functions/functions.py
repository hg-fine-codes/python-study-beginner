# define a function

# def hello_func():
#     pass


# print(hello_func)
# print(hello_func())

# DRY
# def hello_func():
#     print('Hello Function.')


# hello_func()
# hello_func()
# hello_func()

# def hello_func():
#     return 'Hello Function.'


# print(hello_func())

# def hello_func():
#     return 'Hello Function.'


# print(hello_func().upper())

# def hello_func(greeting):
#     return '{} Function.'.format(greeting)


# print(hello_func('Hi'))


# def hello_func(greeting, name='You'):
#     return '{}, {}!'.format(greeting, name)


# print(hello_func('Hi'))
# print(hello_func('Hi', 'Corey'))
# print(hello_func('Hi', name='Corey'))
# print(hello_func(name='Corey', greeting='Hi'))

# def student_info(*args, **kwargs):
#     print(args)
#     print(kwargs)


# student_info('Math', 'Art', name='John', age=22)

# def student_info(*args, **kwargs):
#     print(args)
#     print(kwargs)


# courses = ['Math', 'Art']
# info = {'name': 'John', 'age': 22}

# student_info(courses, info)

# student_info(*courses, **info)


# Snippets context

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
