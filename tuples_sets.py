# A tuple is a collection which is ordered and unchangeable. Allows duplicate members

# Create a tuple
fruits = ('Apples','Oranges','Grapes')
# fruits2 = tuple(('Apples','Oranges','Grapes'))

# Single value in a tuple needs a trailing comma otherwise python will conside it a string
fruits2 = ('Apples',)

# Get Value
print(fruits[1])

# Can't change value
# fruits[0] = 'Pears'

# Delete tuple
# del fruits2

# A Set is a collection which is unordered and unindexed. No duplicate members

# Create a set
cars = {'Maruti','BMW','Audi'}

# Check if in set
print('BMW' in cars)

# Add to set
cars.add('Renault')

# Remove from set
cars.remove('Renault')

# Clear a set
cars.clear()
