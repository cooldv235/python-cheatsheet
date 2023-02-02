# Strings in python are surrounded by either single or double quotes quotation marks,
#  Lets look at some examples

name = 'Dushyant'
age = 26

# Concatenate

# Normal
# print('Hello, my name is ' + name + ' and I am ' + str(age))

# Arguments by position
# print('My name is {name} and I am {age}'.format(name=name, age=age))

# F-Strings v3.6+
print(f'Hello my name is {name} and I am {age}')

# String methods
s = 'hello world'

# Capitalize sting
print(s.capitalize())

# Make all letters uppercase
print(s.upper())

# Make all lower
print(s.lower())

# Swap case
print(s.swapcase())

# Get length
print(len(s))

# Replace 
print(s.replace('world','everyone'))

# Count
sub = 'h'
print(s.count(sub))

# Starts with
print(s.startswith('hello'))

# Ends with
print(s.endswith('d'))

# Split into a list
print(s.split())

# Find a position
print(s.find('r'))

# Is all alphanumeric
print(s.isalnum())

# Is all alphabetic
print(s.isalpha())

# Is all numeric
print(s.isnumeric())
