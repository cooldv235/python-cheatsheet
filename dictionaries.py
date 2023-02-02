# A dictionary is a collection which is unordered, changeable and indexed. No duplicate members allowed

# Create a dict
person = {
    'firstName' : 'John',
    'lastName'  : 'Doe',
    'age'       : 26
}

# Get value
print(person['firstName'])
print(person.get('lastName'))

# Add key/value
person['phone'] = '9876654345'

# Get dict keys
print(person.keys())

# Get dict items
print(person.items())

# Copy a dict
person2 = person.copy()
person2['city'] = 'Mumbai'

# Remove item
del(person['age'])
person.pop('phone')

# List of dicts
people = [
    {'name':'Raju','age':25},
    {'name': 'Shyam','age':35}
]

print(person)