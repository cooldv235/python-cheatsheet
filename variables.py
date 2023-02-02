# A Variable is a container for a value, which can be of various types

'''
This is 
a multiline
or docstring
in python
'''

"""
VARIABLE RULES:
1. Variable names are case-sensitive
2. Must start with a letter or an underscore
3. Can have numbers but can not start with one
"""

# x = 1           # int 
# y = 2.5         # float
# name = 'John'   # string
# is_cool = True  # bool

#multiple assignments
x,y,name,is_cool = (1,2.5,'John',True)

print('Hello')
print(x)
print(x,y,name,is_cool)

# check type of a variable
print(type(x))

# Casting
x = str(x)  # int to str
y = int(y)  # float to int
z = float(y)    # 2.0
