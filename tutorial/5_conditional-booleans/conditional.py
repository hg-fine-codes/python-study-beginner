# Conditionals
# if True:
#     print('Conditional was True')

# if False:
#     print('Conditional was True')

# language = 'Python'

# if language == 'Python':
#     print('Conditional was True')

# Comparison:
# Equal:            ==
# Not equal:        !=
# Greater than:     >
# Less than:        <
# Greater or equal: >=
# Less or equal:    <=
# Object identity:  is

# language = 'Java'

# if language == 'Python':
#     print('Language is Python')
# else:
#     print('No Match')

# Check if the language is either Python or Java or JavaScript
# if none of those return 'No Match'

# language = 'Java'

# if language == 'Python':
#     print('Language is Python')
# elif language == 'Java':
#     print('Language is Java')
# elif language == 'JavaScript':
#     print('Language is JavaScript')
# else:
#     print('No Match')

# Boolean Operations
# and
# or
# not

# user = 'Admin'
# logged_in = False

# if user == 'Admin' and logged_in:
#     print('Admin Page')
# else:
#     print('Bad Creds')

# user = 'Admin'
# logged_in = False

# if user == 'Admin' or logged_in:
#     print('Admin Page')
# else:
#     print('Bad Creds')

# user = 'Admin'
# logged_in = False

# if not logged_in:
#     print('Please Log In')
# else:
#     print('Welcome')

# a = [1, 2, 3]
# b = [1, 2, 3]

# print(a == b)

# a = [1, 2, 3]
# b = [1, 2, 3]

# print(id(a))
# print(id(b))
# print(a is b)

# a = [1, 2, 3]
# b = a

# print(id(a))
# print(id(b))
# print(a is b)

# False Values:
# False
# None
# Zero of any numeric type
# Any empty sequency. For example, '', [], ().
# Any empty mapping (Dictionary). For example, {}.

condition = 123

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')
